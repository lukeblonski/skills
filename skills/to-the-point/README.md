# to-the-point

`to-the-point` helps you turn a vague product idea, scattered notes, and things you discover in conversation into a coherent product concept.

Bring what you have: a few sentences, a long stream of thoughts, screenshots, links, an old proposal, or notes that contradict each other. The assistant reads the material, offers a first synthesis, and asks a few questions about choices that would meaningfully change the concept. As you clarify your thinking, it keeps the agreed decisions and updates the whole picture.

## Who it is for

Anyone who knows roughly what they want to create and wants help making it clear: founders, product managers, independent creators, designers, engineers, and people without a technical background.

## What you get

A reusable product concept that explains, as relevant to your idea:

- The problem, intended user, and expected value.
- What using the product would feel like, from starting point to result.
- What the product takes responsibility for.
- A small first version and the longer-term direction.
- Important decisions already made and consequential questions still open.

The structure follows your idea. You do not have to fill out a template or know product methods. The assistant answers in the language you use.

## An example

> **You:** I want to help people coordinate care for an older relative. Today everything is scattered across messages. I have a lot of notes, but I cannot explain the product clearly yet.
>
> **Assistant:** The central idea seems to be helping a family know what needs doing and who is taking care of it. Here is a first synthesis from your notes. One choice would change the product: does the family organize care itself, or does the service also arrange outside help?
>
> **You:** The family does it. Some relatives live nearby, others help remotely. They are the same kind of user in different situations.
>
> **Assistant:** Then we can describe one user with different ways of helping. I will keep that distinction in the concept.
>
> **You:** Update the full synthesis, and keep the first version simple.

The result is a complete revised concept, with the decisions reconciled across the document.

## Install

### In the Claude app

Download [`to-the-point.zip`](https://github.com/lukeblonski/skills/raw/main/skills/to-the-point/to-the-point.zip) and upload it using the [instructions for skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### In Claude Code and other coding assistants

Use the repository's [skills.sh](https://skills.sh) installer:

```bash
npx skills@latest add lukeblonski/skills --skill to-the-point
```

Add `--global` to install it for all your projects.

### By hand

Copy this folder (`skills/to-the-point/`) into your assistant's skills folder. Codex uses `~/.codex/skills/`; Claude Code uses `~/.claude/skills/`.

## Use

Describe your idea and ask for help making it coherent. For example:

- "Help me turn these notes into a clear product concept."
- "I have a vague idea. Work through it with me and synthesize what we decide."
- "Update the whole concept with our latest decisions, keeping the first version simple."

In Codex, you can invoke it explicitly with `$to-the-point` followed by your idea or notes.

## How it works

The assistant gives you something useful to react to early. It separates what you decided from its own suggestions and what remains unknown. It asks about choices that affect the concept, preserves your corrections, and simplifies the first version by narrowing its scope while keeping the essential idea.

The skill was developed from a conversation that began with loose product notes and ended with a coherent concept after several clarifications. The instructions generalize that process; they do not require your product to use AI, agents, or software automation.

If your next question is whether to invest in the idea, [before-you-build](../before-you-build/) supports that separate decision. `to-the-point` focuses on understanding and expressing the concept.

## Limits

- A coherent concept is a working definition, not proof of demand or technical feasibility.
- Recommendations about the first version are proposals until you adopt them.
- The skill does not edit your project, build the product, or publish the concept unless you request those actions.

## Tests

Six behavioral evaluation scenarios are provided in [`evals/cases.md`](evals/cases.md). They cover vague ideas, one persona in several situations, cumulative revisions, source handling, conditional learning and maintenance, and routing boundaries.

The scenarios are prepared for evaluation. No model pass rate is claimed. Structural validation checks the package format; it does not establish the quality of future conversations. See the [evaluation instructions](evals/README.md).

## What is in this folder

```text
skills/to-the-point/
  SKILL.md             conversation and synthesis instructions
  agents/openai.yaml   Codex display name and suggested starting prompt
  evals/               six behavioral scenarios and evaluation instructions
  to-the-point.zip     runtime files packed for upload in the Claude app
  README.md            this page
```

## License

MIT. See [LICENSE](../../LICENSE).
