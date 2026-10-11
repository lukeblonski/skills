# Eval protocol (from iteration 4)

Replaces the single-agent simulation used up to iteration 3, where one agent played both the user and the assistant and the separation between them was only an instruction.

## Who plays what

| Role | Model | What it gets | What it cannot do |
|---|---|---|---|
| Assistant (tested) | newest Opus (`opus` alias) | the user's messages; with the skill, a copy of `skills/before-you-build/` without `evals/`, `README.md` and the ZIP in an otherwise empty temp folder | read anything outside that folder (refused by Claude Code's permission check); use any MCP server, user settings or installed skills. Without the skill it has no tools at all |
| Simulated user | newest Opus (`opus` alias) | the user-role rules and `user_script.md`, in its own process | see the skill; use any tool |
| Judge (grading and blind A/B) | newest Fable (`fable` alias) | transcripts with the configuration name removed, the assertions / expectations | use any tool; see which run had the skill |

Each role is a separate `claude -p` process. The script exists only in the user process's prompt. The assistant process never receives it and is not told where it is.

Every assistant tool call is logged in `run_meta.json`. A run is marked invalid if the assistant touched a path outside its folder, used a tool other than Read/Glob/Grep, or had any read refused. Invalid runs must be re-run, not graded.

The aliases resolve to the newest model in each family at run time. The resolved model IDs are written into `run_meta.json`, `grading.json`, `comparison.json` and `results.md`.

## Conversation rules

- The opening message is taken verbatim from `## Opening message` in `user_script.md`.
- The user answers only what was asked, from the script; "I don't know" for anything not covered; one to three sentences.
- The conversation ends when the user process judges that the assistant gave its final recommendation and asked nothing that needs an answer (it replies `[END]`).
- Hard cap: 12 exchanges. The harness does **not** tell the assistant it is on its last turn; a run that hits the cap is flagged `hit_cap: true`, and that counts against it.
- `card.md` is the last assistant message.

## Commands

Requires the `claude` CLI on PATH, logged in. Run from the repository root.

```
H=skills/before-you-build/evals/harness/run_evals.py
python3 $H prepare --source skills/before-you-build/evals/cases --dest before-you-build-workspace/iteration-4
python3 $H run     --skill skills/before-you-build --iteration before-you-build-workspace/iteration-4 [--evals 1,4] [--runs 3]
python3 $H grade   --iteration before-you-build-workspace/iteration-4
python3 $H compare --iteration before-you-build-workspace/iteration-4
python3 $H report  --iteration before-you-build-workspace/iteration-4
```

`before-you-build-workspace/` is where results go. It is git-ignored; any folder name works.

`prepare` copies `user_script.md`, `eval_metadata.json` and (when it exists) `task.json` from `skills/before-you-build/evals/cases/` or from an earlier iteration (where `task.json` sits in `blind/<eval>/`). `compare` uses run 1 of each configuration; `grade` grades every run.

## Output per run

```
eval-N-name/<config>/[run-K/]outputs/transcript.md
                                    /card.md
                                    /run_meta.json   models, exchanges, cap, tool calls, isolation check, tokens, cost
eval-N-name/<config>/[run-K/]timing.json
eval-N-name/<config>/[run-K/]grading.json             per-assertion pass/fail with evidence, judge model
blind/<eval>/A|B/, task.json, comparison.json, decoded.json
blind/KEY.json
results.md
```

## Known limits that remain

- The judge is a different model family from the actors, but all three come from the same company.
- The user process decides when the conversation is over; a lenient user can end a run early. Check `exchanges` against the transcript when a result looks odd.
- Without the skill the assistant has no tools; with the skill it has read-only tools. This difference is part of what is being compared.
