# Tests for before-you-build

These tests check one thing: does the skill reach the right verdict, for the right reason, without wasting the user's time?

There are ten test cases. Each one is a made-up person with a made-up idea. Some ideas should be stopped. Some should be waved through quickly. Some are traps. A skill that stops every idea is as useless as one that lets every idea through, so about half the cases expect a quick "go ahead".

## Keep the tests away from the assistant you test

This `evals/` folder sits inside the skill folder, so it is copied when someone installs the skill. The skill never tells the AI to open it. But when you run a test, the assistant being tested must not be able to read this folder. Otherwise it could read the expected answers. The author's script removes the folder from the assistant's copy for you.

## The ten cases

| # | The situation | What a good answer looks like |
|---|---|---|
| 1 | "Let's add dark mode." No real problem behind it. | Not ready yet: name what is missing. |
| 2 | A founder wants a six-month rebuild because "it's the future". | Test first: belief is not proof on a big bet. |
| 3 | "15 friends said they love it." | Test first: compliments are weak evidence. |
| 4 | A one-day button the support team asked for. | Ship it and measure, in a short conversation. |
| 5 | A well-prepared idea with real customer data and a pilot plan. | Agree with the pilot. Don't nag. |
| 6 | The numbers can't work: the market is too small for the goal. | Stop or rethink, and show the arithmetic. |
| 7 | A test failed and the user wants to drop the idea. | First check whether the test was fair. |
| 8 | An AI feature that fixes a weakness today's AI models may soon lose. | Test first, and raise the timing risk. |
| 9 | The user pastes a finished product spec. | Skip what the spec already answers. Ask only about the gaps. |
| 10 | One big customer is asking for a feature. | Test first: ask what the other customers need. |

Full descriptions are in [`cases.md`](cases.md).

## What is in this folder

- `cases.md`: the ten cases written for people. Each one has the opening message, the answers the made-up user gives if asked, the expected verdict, what the skill must notice, and what it must not do.
- `cases/eval-N-.../user_script.md`: the same made-up user, written so another AI can play them.
- `cases/eval-N-.../eval_metadata.json`: the checklist a reviewer uses to mark the conversation pass or fail.
- `cases/eval-N-.../task.json` (some cases only): the checklist for a side-by-side comparison of "with the skill" and "without the skill".
- `evals.json`: just the opening messages, for tools that want them in one file.
- `PROTOCOL.md` and `harness/`: how the author runs the tests (see below).

## How to run a test yourself

The skill works as a conversation, so one question and one answer is not a test. You need three roles:

1. **The assistant** being tested, with the skill installed but without this `evals/` folder.
2. **A pretend user.** It answers only what the assistant asks, using the answers in the case. Anything not in the case gets "I don't know".
3. **A reviewer.** It reads the finished conversation and ticks off the checklist. It is best if the reviewer does not know whether the skill was used.

Run each case twice: once with the skill, once without it. The skill is worth having only if the "with" conversations do better.

You can do this however suits you:

- **By hand.** Open a chat with the skill, play the user yourself from `cases.md`, then check the result against the list. Repeat in a chat without the skill.
- **In your own testing tool.** The files in `cases/` hold everything a tool needs.
- **With the author's script** (next section).

## The author's script

The author uses `harness/run_evals.py`. It runs the three roles as three separate AI sessions, so the assistant cannot peek at the user's answers. It needs a terminal, Python 3 and the Claude Code command-line tool (`claude`), logged in. Each run uses AI credits, so it costs money.

From the top folder of this repository:

```bash
H=skills/before-you-build/evals/harness/run_evals.py
python3 $H prepare --source skills/before-you-build/evals/cases --dest runs/iteration-1
python3 $H run     --skill skills/before-you-build --iteration runs/iteration-1
python3 $H grade   --iteration runs/iteration-1
python3 $H compare --iteration runs/iteration-1
python3 $H report  --iteration runs/iteration-1
```

What each step does: `prepare` copies the cases into a results folder. `run` holds the conversations. `grade` ticks off the checklists. `compare` puts "with" and "without" side by side, with the labels hidden. `report` writes a summary table to `results.md`.

The full rules (which AI plays which role, when a conversation ends, when a run doesn't count) are in [`PROTOCOL.md`](PROTOCOL.md).
