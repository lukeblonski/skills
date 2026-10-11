#!/usr/bin/env python3
"""Eval harness for the before-you-build skill.

Three separate model processes, each started with `claude -p`:

  ASSISTANT  model: newest Opus  (alias "opus")
             Runs in an empty temporary folder. With the skill, the folder holds
             only a copy of the skill (no evals/). Tools: Read, Glob, Grep with the
             skill, none without it. No MCP servers, no user settings, no skills.
             It never receives the user script: the script exists only in the
             USER process prompt, and any file read outside its folder is refused
             by Claude Code's permission check. Every tool call is logged and
             audited; a run with a call outside the folder is marked invalid.
  USER       model: newest Opus  (alias "opus")
             No tools. Its system prompt holds the user-role rules and the script.
             It sees only the assistant's messages.
  JUDGE      model: newest Fable (alias "fable")
             No tools. Grades each run against the assertions without knowing the
             configuration, and compares with/without pairs blind (A/B random).

Aliases resolve to the newest model in each family at run time; the resolved
model IDs are recorded in run_meta.json, grading.json and comparison.json.

Subcommands:
  prepare  --source evals/cases|ITER_DIR --dest ITER_DIR
  run      --skill SKILL_DIR --iteration ITER_DIR [--evals 1,4] [--configs with_skill,without_skill] [--runs 1] [--parallel 4]
  grade    --iteration ITER_DIR [--evals ...] [--parallel 4]
  compare  --iteration ITER_DIR [--evals ...] [--parallel 4]
  report   --iteration ITER_DIR

Requires the `claude` CLI on PATH, logged in.
"""
import argparse
import concurrent.futures as cf
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ACTOR_MODEL = "opus"   # assistant and simulated user: newest Opus
JUDGE_MODEL = "fable"  # grader and blind comparator: newest Fable
MAX_EXCHANGES = 12
TURN_TIMEOUT = 900
END_TOKEN = "[END]"

ASSISTANT_SYSTEM_BASE = (
    "You are Claude, an AI assistant made by Anthropic, talking with a user in a chat. "
    "Help them with what they ask. You may ask questions; when you do, stop and wait for the answer."
)
ASSISTANT_SKILL_NOTE = (
    "\n\nA skill is installed for you in the folder ./before-you-build/. "
    "Skill description: {description}\n"
    "When the user's request matches that description, read ./before-you-build/SKILL.md first and follow it, "
    "reading the files it points to inside ./before-you-build/ when it tells you to. "
    "Files you write are not shown to the user: everything the user should see goes in your chat reply."
)

USER_SYSTEM = """You are playing a USER in a chat with an AI assistant. You know nothing about product-discovery methods.

Rules:
- Your opening message has already been sent. From now on you receive the assistant's messages.
- Reply ONLY to what the assistant actually asked, using the matching line from "Answers if asked" in your script. Do not volunteer anything that was not asked.
- If the assistant asks something the script does not cover, answer "I don't know" or "we haven't thought about that". Do not invent facts.
- Keep each reply to one to three sentences. Never push back, never ask for method advice; you just answer.
- If the assistant asks several questions at once, answer each briefly from the script.
- If the assistant proposes a draft, list or plan and asks what is wrong with it, say "Nothing jumps out" unless the script says otherwise.
- If the assistant's message gives its final recommendation and asks you nothing that needs an answer (an offer of further help does not count), reply with exactly """ + END_TOKEN + """ and nothing else.
- Write only the user's reply text. No labels, no stage directions, no commentary.

Your script:

{script}
"""

GRADER_PROMPT = """You are grading one conversation between a user and an AI assistant against a list of expectations.
Judge only what is in the transcript. Be strict: an expectation passes only if the transcript clearly meets it.

Expectations:
{expectations}

Transcript:
<transcript>
{transcript}
</transcript>

Return ONLY a JSON object, no prose before or after, in exactly this shape:
{{"expectations": [{{"text": "<expectation text verbatim>", "passed": true, "evidence": "<short quote or pointer to the exchange>"}}]}}
One entry per expectation, in the same order."""

COMPARE_PROMPT = """You are comparing two conversations, A and B, in which an AI assistant helps the same user with the same request.
The user knows nothing about product-discovery methods and answered from the same script in both.
You do not know how A and B were produced. Judge only what is in the transcripts.

Opening request: {prompt}

Expectations for a good conversation:
{expectations}

<conversation_A>
{a}
</conversation_A>

<conversation_B>
{b}
</conversation_B>

Score each conversation 1-5 on:
- content: decision_correctness, reasoning_and_evidence_handling, completeness_of_recommendation
- structure: question_economy, plain_language, actionability
content_score = mean of the content items, structure_score = mean of the structure items (one decimal), overall_score = content_score + structure_score.
Also check each expectation for A and for B.

Return ONLY a JSON object, no prose before or after, in exactly this shape:
{{"winner": "A" or "B",
 "reasoning": "<one paragraph>",
 "rubric": {{"A": {{"content": {{"decision_correctness": n, "reasoning_and_evidence_handling": n, "completeness_of_recommendation": n}}, "structure": {{"question_economy": n, "plain_language": n, "actionability": n}}, "content_score": x, "structure_score": x, "overall_score": x}}, "B": {{...same...}}}},
 "output_quality": {{"A": {{"score": n, "strengths": ["..."], "weaknesses": ["..."]}}, "B": {{...}}}},
 "expectation_results": {{"A": {{"passed": n, "total": n, "pass_rate": x, "details": [{{"text": "...", "passed": true, "note": "..."}}]}}, "B": {{...}}}}}}"""


# ---------------------------------------------------------------- claude CLI

def isolation_flags():
    return [
        "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
        "--setting-sources", "",
        "--disable-slash-commands",
        "--permission-mode", "default",
    ]


def claude_call(prompt, model, system_prompt, cwd, tools="", resume=None):
    """One `claude -p` call. Returns dict: text, session_id, tool_uses, denials, usage, models, ms."""
    cmd = ["claude", "-p", prompt, "--model", model, "--tools", tools,
           "--system-prompt", system_prompt,
           "--output-format", "stream-json", "--verbose"] + isolation_flags()
    if resume:
        cmd += ["--resume", resume]
    t0 = time.time()
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=TURN_TIMEOUT)
    ms = int((time.time() - t0) * 1000)
    tool_uses, final = [], None
    for line in proc.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            for c in ev.get("message", {}).get("content", []):
                if c.get("type") == "tool_use":
                    tool_uses.append({"name": c.get("name"), "input": c.get("input")})
        elif ev.get("type") == "result":
            final = ev
    if final is None or final.get("is_error"):
        raise RuntimeError(f"claude call failed (rc={proc.returncode}): {proc.stderr[-2000:]} {str(final)[:1000]}")
    models = {k: v for k, v in (final.get("modelUsage") or {}).items()}
    return {
        "text": (final.get("result") or "").strip(),
        "session_id": final.get("session_id"),
        "tool_uses": tool_uses,
        "denials": final.get("permission_denials") or [],
        "usage": final.get("usage") or {},
        "models": models,
        "cost_usd": final.get("total_cost_usd") or 0,
        "ms": ms,
    }


def main_model(models, family):
    ids = [m for m in models if family in m]
    return ids[0] if ids else ",".join(models)


def total_tokens(usage):
    return sum(usage.get(k, 0) or 0 for k in
               ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))


def parse_json(text):
    s, e = text.find("{"), text.rfind("}")
    if s < 0 or e < 0:
        raise ValueError("no JSON object in judge output: " + text[:500])
    return json.loads(text[s:e + 1])


# ---------------------------------------------------------------- helpers

def eval_dirs(iteration, only=None):
    out = []
    for d in sorted(Path(iteration).glob("eval-*")):
        m = re.match(r"eval-(\d+)-", d.name)
        if d.is_dir() and m and (not only or int(m.group(1)) in only):
            out.append(d)
    return sorted(out, key=lambda d: int(re.match(r"eval-(\d+)-", d.name).group(1)))


def opening_message(script):
    m = re.search(r"^## Opening message\s*\n(.*?)(?=^## |\Z)", script, re.S | re.M)
    if not m:
        raise ValueError("user_script.md has no '## Opening message' section")
    return m.group(1).strip()


def skill_description(skill_dir):
    text = (Path(skill_dir) / "SKILL.md").read_text()
    m = re.search(r"^description:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def make_sandbox(skill_dir):
    """Empty temp folder; with a skill, a copy of it without evals/ and backups."""
    sb = Path(tempfile.mkdtemp(prefix="byb-assistant-"))
    if skill_dir:
        shutil.copytree(skill_dir, sb / "before-you-build",
                        ignore=shutil.ignore_patterns("evals", "README.md", "*.zip", "*.bak*", ".DS_Store", "__pycache__"))
    return sb


def outside(path_value, sandbox):
    if not isinstance(path_value, str) or not path_value:
        return False
    p = Path(path_value)
    p = (sandbox / p) if not p.is_absolute() else p
    try:
        p.resolve().relative_to(sandbox.resolve())
        return False
    except ValueError:
        return True


def audit(tool_uses, sandbox):
    bad = []
    for t in tool_uses:
        inp = t.get("input") or {}
        for key in ("file_path", "path", "notebook_path"):
            if outside(inp.get(key), sandbox):
                bad.append(t)
        if t.get("name") not in ("Read", "Glob", "Grep"):
            bad.append(t)
    return bad


def render_transcript(exchanges, header=None):
    lines = [header, ""] if header else []
    for i, (u, a) in enumerate(exchanges, 1):
        lines += [f"## Exchange {i}", f"**User:** {u}", "", f"**Assistant:** {a}", ""]
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------- prepare

def cmd_prepare(args):
    src, dst = Path(args.source), Path(args.dest)
    dst.mkdir(parents=True, exist_ok=True)
    for d in eval_dirs(src):
        out = dst / d.name
        out.mkdir(exist_ok=True)
        for f in ("eval_metadata.json", "user_script.md"):
            shutil.copy2(d / f, out / f)
        task = d / "task.json"
        if not task.exists():
            task = src / "blind" / d.name / "task.json"
        if task.exists():
            shutil.copy2(task, out / "task.json")
        print("prepared", out)


# ---------------------------------------------------------------- run

def run_one(skill_dir, eval_dir, config, run_idx):
    script = (eval_dir / "user_script.md").read_text()
    opening = opening_message(script)
    out = eval_dir / config / (f"run-{run_idx}" if run_idx > 1 else "") / "outputs"
    out.mkdir(parents=True, exist_ok=True)

    with_skill = config == "with_skill"
    sandbox = make_sandbox(skill_dir if with_skill else None)
    user_cwd = Path(tempfile.mkdtemp(prefix="byb-user-"))
    a_system = ASSISTANT_SYSTEM_BASE + (ASSISTANT_SKILL_NOTE.format(description=skill_description(skill_dir)) if with_skill else "")
    a_tools = "Read,Glob,Grep" if with_skill else ""
    u_system = USER_SYSTEM.format(script=script)

    exchanges, all_tools, denials = [], [], []
    a_session = u_session = None
    a_tokens = u_tokens = 0
    a_models, u_models = {}, {}
    cost = 0.0
    t0 = time.time()
    user_msg, hit_cap = opening, False

    for n in range(1, MAX_EXCHANGES + 1):
        r = claude_call(user_msg, ACTOR_MODEL, a_system, sandbox, a_tools, resume=a_session)
        a_session = r["session_id"]
        all_tools += r["tool_uses"]; denials += r["denials"]
        a_tokens += total_tokens(r["usage"]); a_models.update(r["models"]); cost += r["cost_usd"]
        exchanges.append((user_msg, r["text"]))
        if n == MAX_EXCHANGES:
            hit_cap = True
            break
        prompt = r["text"] if u_session else f"The assistant replied to your opening message:\n\n{r['text']}"
        ur = claude_call(prompt, ACTOR_MODEL, u_system, user_cwd, "", resume=u_session)
        u_session = ur["session_id"]
        u_tokens += total_tokens(ur["usage"]); u_models.update(ur["models"]); cost += ur["cost_usd"]
        reply = ur["text"].strip()
        if reply == END_TOKEN or reply.endswith(END_TOKEN):
            break
        user_msg = reply

    seconds = round(time.time() - t0, 1)
    violations = audit(all_tools, sandbox)
    (out / "transcript.md").write_text(render_transcript(exchanges, f"# Transcript — {eval_dir.name}, {config}"))
    (out / "card.md").write_text(exchanges[-1][1].strip() + "\n")
    meta = {
        "eval": eval_dir.name, "config": config, "run": run_idx,
        "assistant_model": main_model(a_models, "opus"), "user_model": main_model(u_models, "opus"),
        "exchanges": len(exchanges), "hit_cap": hit_cap,
        "assistant_tool_calls": all_tools, "permission_denials": denials,
        "isolation_violations": violations, "valid": not violations and not denials,
        "assistant_tokens": a_tokens, "user_tokens": u_tokens, "cost_usd": round(cost, 4),
    }
    (out / "run_meta.json").write_text(json.dumps(meta, indent=2))
    (out.parent / "timing.json").write_text(json.dumps(
        {"total_tokens": a_tokens, "duration_ms": int(seconds * 1000), "total_duration_seconds": seconds}, indent=2))
    shutil.rmtree(sandbox, ignore_errors=True); shutil.rmtree(user_cwd, ignore_errors=True)
    flag = "" if meta["valid"] else "  INVALID: assistant touched files outside its folder"
    return f"{eval_dir.name} {config} run{run_idx}: {len(exchanges)} exchanges, {seconds}s{' (cap)' if hit_cap else ''}{flag}"


def cmd_run(args):
    only = [int(x) for x in args.evals.split(",")] if args.evals else None
    jobs = [(d, c, r) for d in eval_dirs(args.iteration, only)
            for c in args.configs.split(",") for r in range(1, args.runs + 1)]
    with cf.ThreadPoolExecutor(args.parallel) as ex:
        futs = {ex.submit(run_one, Path(args.skill), d, c, r): (d.name, c, r) for d, c, r in jobs}
        for f in cf.as_completed(futs):
            try:
                print(f.result(), flush=True)
            except Exception as e:
                print("FAILED", futs[f], e, flush=True)


# ---------------------------------------------------------------- grade

def judge(prompt):
    jdir = Path(tempfile.mkdtemp(prefix="byb-judge-"))
    try:
        r = claude_call(prompt, JUDGE_MODEL, "You are a careful, impartial evaluator. You answer with JSON only.", jdir, "")
    finally:
        shutil.rmtree(jdir, ignore_errors=True)
    return parse_json(r["text"]), main_model(r["models"], "fable")


def run_outputs(eval_dir):
    for cfg in ("with_skill", "without_skill"):
        base = eval_dir / cfg
        for out in sorted(base.glob("**/outputs")):
            yield cfg, out


def grade_one(eval_dir, out):
    meta = json.loads((eval_dir / "eval_metadata.json").read_text())
    transcript = (out / "transcript.md").read_text().split("\n", 1)[1]  # drop header naming the config
    exps = "\n".join(f"{i}. {e}" for i, e in enumerate(meta["assertions"], 1))
    data, model = judge(GRADER_PROMPT.format(expectations=exps, transcript=transcript))
    passed = sum(1 for e in data["expectations"] if e.get("passed"))
    total = len(data["expectations"])
    data["summary"] = {"passed": passed, "failed": total - passed, "total": total,
                       "pass_rate": round(passed / total, 2) if total else 0}
    data["judge_model"] = model
    (out.parent / "grading.json").write_text(json.dumps(data, indent=2))
    return f"{eval_dir.name} {out.parent.relative_to(eval_dir)}: {passed}/{total} (judge {model})"


def cmd_grade(args):
    only = [int(x) for x in args.evals.split(",")] if args.evals else None
    jobs = [(d, o) for d in eval_dirs(args.iteration, only) for _, o in run_outputs(d)]
    with cf.ThreadPoolExecutor(args.parallel) as ex:
        for f in cf.as_completed([ex.submit(grade_one, d, o) for d, o in jobs]):
            try:
                print(f.result(), flush=True)
            except Exception as e:
                print("FAILED", e, flush=True)


# ---------------------------------------------------------------- compare

def compare_one(iteration, eval_dir, rng_seed):
    rng = random.Random(rng_seed)
    w = eval_dir / "with_skill" / "outputs"
    wo = eval_dir / "without_skill" / "outputs"
    if not (w.exists() and wo.exists()):
        return f"{eval_dir.name}: skipped (needs run 1 of both configs)"
    labels = {"A": "with_skill", "B": "without_skill"}
    if rng.random() < 0.5:
        labels = {"A": "without_skill", "B": "with_skill"}
    src = {"with_skill": w, "without_skill": wo}
    bdir = Path(iteration) / "blind" / eval_dir.name
    bdir.mkdir(parents=True, exist_ok=True)
    for lab, cfg in labels.items():
        (bdir / lab).mkdir(exist_ok=True)
        body = (src[cfg] / "transcript.md").read_text().split("\n", 1)[1]
        (bdir / lab / "transcript.md").write_text(f"# Transcript {lab}\n" + body)
        shutil.copy2(src[cfg] / "card.md", bdir / lab / "card.md")
    meta = json.loads((eval_dir / "eval_metadata.json").read_text())
    task_file = eval_dir / "task.json"
    task = json.loads(task_file.read_text()) if task_file.exists() else {"prompt": meta["prompt"], "expectations": meta["assertions"]}
    (bdir / "task.json").write_text(json.dumps(task, indent=2))
    exps = "\n".join(f"{i}. {e}" for i, e in enumerate(task["expectations"], 1))
    data, model = judge(COMPARE_PROMPT.format(
        prompt=task["prompt"], expectations=exps,
        a=(bdir / "A" / "transcript.md").read_text().split("\n", 1)[1],
        b=(bdir / "B" / "transcript.md").read_text().split("\n", 1)[1]))
    data["judge_model"] = model
    (bdir / "comparison.json").write_text(json.dumps(data, indent=2))
    er = data.get("expectation_results", {})
    decoded = {
        "eval": eval_dir.name, "label_key": labels,
        "winner_label": data["winner"], "winner_config": labels[data["winner"]],
        "scores": {labels[l]: data["rubric"][l]["overall_score"] for l in ("A", "B")},
        "expectations": {labels[l]: f"{er.get(l, {}).get('passed')}/{er.get(l, {}).get('total')}" for l in ("A", "B")},
        "reasoning": data["reasoning"], "judge_model": model,
    }
    (bdir / "decoded.json").write_text(json.dumps(decoded, indent=2))
    return eval_dir.name, labels, f"{eval_dir.name}: winner {decoded['winner_config']} {decoded['scores']} (judge {model})"


def cmd_compare(args):
    only = [int(x) for x in args.evals.split(",")] if args.evals else None
    dirs = eval_dirs(args.iteration, only)
    key_path = Path(args.iteration) / "blind" / "KEY.json"
    key = json.loads(key_path.read_text()) if key_path.exists() else {}
    seed = random.SystemRandom().random()
    with cf.ThreadPoolExecutor(args.parallel) as ex:
        futs = [ex.submit(compare_one, args.iteration, d, f"{seed}-{d.name}") for d in dirs]
        for f in cf.as_completed(futs):
            try:
                res = f.result()
            except Exception as e:
                print("FAILED", e, flush=True); continue
            if isinstance(res, str):
                print(res); continue
            name, labels, msg = res
            key[name] = labels
            print(msg, flush=True)
    key_path.parent.mkdir(parents=True, exist_ok=True)
    key_path.write_text(json.dumps(key, indent=2))


# ---------------------------------------------------------------- report

def cmd_report(args):
    it = Path(args.iteration)
    rows, models = [], set()
    for d in eval_dirs(it):
        dec_p = it / "blind" / d.name / "decoded.json"
        row = {"eval": d.name}
        for cfg in ("with_skill", "without_skill"):
            g = d / cfg / "grading.json"
            m = d / cfg / "outputs" / "run_meta.json"
            if g.exists():
                gd = json.loads(g.read_text()); s = gd["summary"]
                row[cfg + "_exp"] = f"{s['passed']}/{s['total']}"; models.add("judge " + gd.get("judge_model", "?"))
            if m.exists():
                md = json.loads(m.read_text())
                row[cfg + "_ex"] = md["exchanges"]; row[cfg + "_tok"] = md["assistant_tokens"]
                row[cfg + "_valid"] = md["valid"]
                models.add("assistant " + md["assistant_model"]); models.add("user " + md["user_model"])
        if dec_p.exists():
            dec = json.loads(dec_p.read_text())
            row["winner"] = dec["winner_config"]; row["scores"] = dec["scores"]
            models.add("judge " + dec.get("judge_model", "?"))
        if len(row) > 1:
            rows.append(row)
    lines = ["# Results — " + it.name, "", "Models: " + ", ".join(sorted(models)), "",
             "| Eval | Blind winner | Score with / without | Expectations with / without | Exchanges with / without | Tokens with / without | Isolation OK |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        sc = r.get("scores", {})
        lines.append("| {e} | {w} | {s1} / {s2} | {x1} / {x2} | {n1} / {n2} | {t1} / {t2} | {v} |".format(
            e=r["eval"], w=r.get("winner", "–"), s1=sc.get("with_skill", "–"), s2=sc.get("without_skill", "–"),
            x1=r.get("with_skill_exp", "–"), x2=r.get("without_skill_exp", "–"),
            n1=r.get("with_skill_ex", "–"), n2=r.get("without_skill_ex", "–"),
            t1=r.get("with_skill_tok", "–"), t2=r.get("without_skill_tok", "–"),
            v="yes" if r.get("with_skill_valid", True) and r.get("without_skill_valid", True) else "NO"))
    (it / "results.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("prepare"); s.add_argument("--source", required=True); s.add_argument("--dest", required=True)
    s = sub.add_parser("run"); s.add_argument("--skill", required=True); s.add_argument("--iteration", required=True)
    s.add_argument("--evals"); s.add_argument("--configs", default="with_skill,without_skill")
    s.add_argument("--runs", type=int, default=1); s.add_argument("--parallel", type=int, default=4)
    for name in ("grade", "compare"):
        s = sub.add_parser(name); s.add_argument("--iteration", required=True)
        s.add_argument("--evals"); s.add_argument("--parallel", type=int, default=4)
    s = sub.add_parser("report"); s.add_argument("--iteration", required=True)
    a = p.parse_args()
    {"prepare": cmd_prepare, "run": cmd_run, "grade": cmd_grade, "compare": cmd_compare, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    main()
