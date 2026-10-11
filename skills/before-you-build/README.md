# before-you-build

`before-you-build` checks a product idea, feature or project **before** your team spends time building it.

It is a guided conversation. You describe your idea in your own words. The assistant asks a few plain questions, one at a time, and says why it asks each one. At the end you get a one-page card with a verdict and a concrete next step.

You do not need to know any product methods. The skill does that part. You only supply the facts about your idea.

## Who it is for

Anyone who has an idea and wants to know if it is worth building: founders, product managers, engineers, designers, sales people, managers.

## What you get

One of four verdicts:

- **Not ready yet.** The problem, the person who has it, or the result you want cannot be stated yet. The card says what is missing and how to find it.
- **Test first.** The idea depends on something you don't know yet, and that unknown could sink it. The card suggests the cheapest way to find out and what result would mean "go".
- **Ship a small version and measure.** The idea is cheap, easy to undo, or already backed by what customers actually do. The card says what to watch after launch.
- **Stop or rethink.** The numbers cannot add up, or a test has already shown the key belief is wrong. The card shows why and what you could change.

Small, cheap ideas get a short conversation and a short card. Big, expensive bets get more questions. The skill tries not to slow down ideas that don't need it.

## An example

> **You:** We want to add dark mode to our invoicing app. Can you help me check if it's a good idea?
>
> **Assistant:** Who would use it, and what goes wrong for them today without it?
>
> **You:** All our users. People like dark mode.
>
> *(a few more questions)*
>
> **Verdict: Not ready yet.** There is no problem a customer would describe yet, and no number that should change. Cheapest next step: search your support tickets for "dark" and ask five users when the screen last bothered them.

## Install

### In the Claude app (no terminal needed)

Works on Pro, Max, Team and Enterprise plans.

1. Download [`before-you-build.zip`](https://github.com/lukeblonski/skills/raw/main/skills/before-you-build/before-you-build.zip).
2. In Claude, open **Settings → Capabilities**. Make sure code execution is turned on.
3. In the **Skills** section, click **Upload skill** and choose the ZIP file.

More help: [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### In Claude Code and other coding assistants

Install with [skills.sh](https://skills.sh). You need [Node.js](https://nodejs.org) on your computer. Open a terminal and paste:

```bash
npx skills@latest add lukeblonski/skills --skill before-you-build
```

Add `--global` at the end to make the skill available in all your projects.

Start a new session after installing, so the assistant can find the skill.

### By hand

Copy this folder (`skills/before-you-build/`) into your assistant's skills folder. For Claude Code that is `~/.claude/skills/`.

## Use

Just describe your idea. For example:

- "I have an idea for X. Help me check it before we build it."
- "Should we build this?" (and paste the proposal)
- "Is this idea worth it?"

The skill answers in the language you write in.

You can also paste a finished document, such as a product spec. The skill skips what the document already answers and asks only about the gaps.

## Where it comes from

The skill is based on two pieces of research by the author, done in October 2026.

1. **Published methods.** A review of how the best-known product thinkers say ideas should be checked (Cagan, Torres, Bland and Osterwalder, Maurya, Fitzpatrick, Savoia, Gilad, Moesta, Olsen, Gothelf and Seiden, Ries). Where scientific research on the same question exists, the methods were checked against it.
2. **Practitioner interviews.** An analysis of 159 interviews with product people (Lenny's Podcast). In stories with a known ending, ideas built without any check failed 16 times out of 33. Ideas checked first failed 9 times out of 131. These are stories told afterwards, so they are not proof. But they point the same way as controlled experiments with entrepreneurs.

What the research supports well:

- What people say they will do overstates what they actually do. This is well established.
- Teaching entrepreneurs to test their ideas makes them drop weak ideas sooner. The evidence is moderate: a few experiments, mostly from one research group.
- Writing down the "go" threshold before the test makes it harder to read the result the way you hoped. The reasoning is strong, but there is little direct evidence.

The specific numbers in the methods (for example "60% conversion" or "7 out of 10") come from the authors' experience. They are not research findings.

The skill contains no quotes from the interviews. Everything is in the skill's own words.

Where the methods disagree (how many beliefs to test at once, how long a test should run, how much interviews are worth), the skill picks one answer so you don't have to. The list is in [`SKILL.md`](SKILL.md), under "Choices made where the methods disagree".

## Limits

- It works as a conversation. It does not yet review a finished document in one go.
- It cannot check your numbers. It judges how strong they are, not whether they are true.
- The verdict is a recommendation. The decision, and responsibility for it, stay with you.

## Tests

The skill comes with ten test cases in the [`evals/`](evals/) folder. Each one is a made-up person with a made-up idea, and the verdict a good answer should reach. Some ideas should be stopped, some should go ahead quickly, and some are traps.

The skill never opens these files during a normal conversation. They are for checking the skill after a change.

You can run the tests in whatever way suits you: by hand in two chat windows, in your own testing tool, or with the author's script. The [tests README](evals/README.md) explains all three in plain words.

## What is in this folder

```text
skills/before-you-build/
  SKILL.md                 how the conversation runs, the verdicts, the rules
  references/              question lists, evidence guide, test catalogue, extra questions for big bets
  templates/idea-card.md   the one-page card you get at the end
  evals/                   the ten test cases and how to run them
  before-you-build.zip     the skill packed for upload in the Claude app
  README.md                this page
```

## License

MIT. You can use, change and share it freely. See [LICENSE](../../LICENSE).
