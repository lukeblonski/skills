# Tests for to-the-point

These scenarios check whether the assistant helps clarify a product concept while preserving the user's intent and keeping the conversation proportionate.

The eight cases are in [`cases.md`](cases.md). Evaluate meaning and decisions rather than exact phrases, a fixed number of turns, or a particular set of headings.

## Keep expected behavior away from the assistant

Copy the skill into an isolated test environment without this `evals/` folder. The assistant being tested should see the skill, the user's request, and the raw source material it needs. It should not see the evaluation criteria or suggested answers.

The upload ZIP includes only runtime files and omits the evaluation scenarios.

## Run a case

1. Give the opening request and relevant material to the assistant.
2. Play the user, using the follow-up information in the case. For unspecified facts, say that you do not know rather than inventing supporting evidence.
3. Where the case calls for it, ask for a complete update after the clarifications.
4. Give the finished conversation and output to a separate reviewer with the case's criteria.

Record what happened, which criteria were met, and the evidence for any failure. An incomplete or interrupted conversation may be inconclusive rather than a pass or fail.

For a useful comparison, run the same case in a fresh conversation without the skill and have the reviewer compare the outputs without knowing which one used it. Do not infer an improvement merely from valid package structure.

## Current status

A local run on 2026-10-17 covered the six original scenarios and two additional cases. The [report](results/2026-10-17/report.md) records the procedure, outcomes, limitations, and links to the actual prompts and responses. Evaluated assistants received the runtime skill without this folder; a separate reviewer received the criteria and completed transcripts.

These are single-run observations, not a pass-rate measurement or evidence that the skill improves on an unassisted baseline. Routing was checked using the skill descriptions; it did not execute the implementation or investment-assessment tasks. No external services were changed.
