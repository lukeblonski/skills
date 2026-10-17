# Tests for to-the-point

These scenarios check whether the assistant helps clarify a product concept while preserving the user's intent and keeping the conversation proportionate.

The six cases are in [`cases.md`](cases.md). Evaluate meaning and decisions rather than exact phrases, a fixed number of turns, or a particular set of headings.

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

The scenarios are evaluation specifications. No independent model runs or pass-rate measurements are included in this addition.
