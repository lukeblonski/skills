# The conversation, stage by stage

Questions to ask, why each one matters, and what a good answer looks like. Use the "why" line when you ask; it is written to be said to the user. Do not ask everything. Ask what the previous answer left open.

## Stage 1. Hear the idea

**Opening:** "Tell me about the idea in a few sentences: who it is for, what it does, and why now."

If they paste a document, read it first and only ask about what it leaves out.

From the answer, extract and reflect back:

| What | Plain question if missing | Why it matters |
|---|---|---|
| Goal | "What should be different for the business or the customer if this works?" | An idea without a goal cannot be judged, only admired. |
| Who | "Who exactly has this problem?" | "Everyone" usually means nobody specific has been talked to. |
| Problem | "What does the problem look like in their day?" | People answer "what problem" with a feature list. The problem is what happens to a person, not what the product lacks. |
| Solution | "What do you want to build?" | Usually the only part that arrives fully formed. |
| Known | "What do you already know, and how?" | Sets up evidence grading later. |
| Size | "Roughly how big a bet is this: days, weeks, months?" | Decides how deep the conversation goes. |

Reflect it back: "Here is what I understood: [goal], for [who], because [problem]. You want to build [solution]. You know [known] because [how]. Rough size: [size]. What did I get wrong?"

## Stage 2. Problem before solution

**Question:** "When did this problem last happen to a real person you know of, and what did they do about it?"
Why: an idea whose problem nobody can place in a real person's recent life is usually a solution looking for a problem. A good answer names a person or role, a moment, and what they did instead (exported to a spreadsheet, called support, gave up).

**Question:** "If this works, what number changes, and from what to what?"
Why: without a number nobody can tell later whether it worked. Good answers: "time from opening the list to creating an order, from 4 minutes to under 2", "share of trials that convert, from 8% to 12%". A weak answer is "engagement" or "customer satisfaction" with no baseline.

**Question:** "What other ways of solving this problem did you consider, and why did they lose?"
Why: decisions that weighed more than one option succeed more often. An idea compared against nothing is the first idea, not the best one. If they considered nothing, spend one exchange generating two alternatives together, including "do nothing" and "the cheapest manual version".

**Question (if the problem is still a feature):** "Imagine the customer describing this problem to a colleague. What would they say?"
Why: the problem should sound like something a customer would say. "I can't find vehicles due for inspection without exporting everything" is a problem. "We lack filters" is a feature.

**Gate:** if after two attempts the problem cannot be stated as something a customer would say, or no real recent instance exists, stop here. Verdict: Not ready yet. Say exactly what is missing and the cheapest way to get it (usually: talk to three people who should have the problem, ask about the last time it happened).

## Stage 3. Size the bet

Three questions, together:

1. "What does it cost to build and then keep running? People, weeks, and the ongoing upkeep." Why: every shipped feature costs something forever; in business software it is almost never removed.
2. "Can it be removed or switched off later without pain?" Why: reversible decisions deserve speed; irreversible ones deserve a test.
3. "Can users ignore it, or will everyone be pushed through it?" Why: a new option nobody has to use is a different kind of bet from a rebuild everyone must endure.

Classify:

- **Small bet**: days to build, can be switched off, users can ignore it. Path: ship a small version to a limited group with a prediction written first. Go to the test card in `tests.md`, section "Measured release".
- **Medium bet**: weeks, removable with some pain, or affects existing users' habits. Full path, stages 4 to 6.
- **Big bet**: months, hard to undo, forced on everyone, or a new product line. Full path plus the challenges in `challenges.md`.

Be alert to the small, flashy feature that sails through because nobody questions it. Small things add complexity too. The question "would we remove it if the test came out neutral?" catches these.

## Stage 4. What must be true

Draft five to eight statements. Write each as one positive sentence about a specific group doing a specific thing. Order by the kind of unknown:

1. **Want it.** "[Group] will [change what they do today] because [reason]." Also: "[Group] will do [the steps needed to get the value]." Wanting the result is not the same as being willing to do the work to get it.
2. **Pays.** "[Buyer] will pay [price] for it." "The cost to deliver is below what they pay." "It moves [the business number the goal names]."
3. **Buildable.** "We can build it with [team] in [time] using [technology]." For AI features: "The error rate [X] is acceptable to the user." "The data we have is good enough."
4. **Usable.** "[Group] will understand what to do without help."
5. **Harmless.** "Nobody is worse off: no group is excluded, no data is used in a way they would object to, nothing would embarrass us if the internal discussion were public."

Not every idea needs all five. A small internal tool needs one and three. A paid product needs one and two before anything else.

For each statement, draft your assessment before asking the user anything:

- **Consequence if false:** would the idea die, or just get smaller? Why: only the ones that kill the idea are worth testing now.
- **Existing evidence:** what supports the statement, and how was it obtained? Grade it on the ladder in `evidence.md` and say the grade.

Follow the numbered-list and explicit-priority procedure in [step 4 of the main instructions](../SKILL.md#4-what-must-be-true). Present the assessment in one exchange, invite corrections, and ask only about missing evidence for the statements you identify by number and short name. Explain why you recommend checking them first in relation to the user's goal. Make clear whether the answer could change that recommendation or help choose how to test it. Everything else waits for a later round.

**The kill assumption.** In nearly every idea it is demand: if you build it right, will enough people want it? Ask this even when the user is sure, and especially when the user is the one who will build it. People who are good at building are fooled by the buildable part; it feels like progress.

**Quick arithmetic for paid products.** Before any test, check the numbers on paper. Ask what minimum yearly revenue in three years would still count as success. Divide by what one customer pays per year: that is how many customers are needed. Assume roughly one in a hundred people reached becomes a customer: that is how many people must be reached. Ask whether that many exist. An idea that fails on paper does not need a test; it needs a different price, a different market, or a different goal.

The "one in a hundred" rule is for large markets. When the whole market is a few thousand firms, ask instead what share of them could plausibly be won in three years: a tenth is ambitious, a third is exceptional. Use that to check the goal. For a feature inside an existing product, ask only whether the gain named in the goal plausibly pays back the build and upkeep cost.

## Stage 5. The cheapest test

See `tests.md`. Before proposing, ask the user: "What do you think the result will be?" and get a number. Their guess, written down, is the start of the threshold and protects against moving the goalposts.

## Stage 6. Verdict

Lead with the verdict. One sentence of reason. Then the card. Do not restate the whole conversation. The card is for someone who was not in the room.

## Longer question list for big bets

When the bet is big, these ten questions, used by product leaders for decades, cover the ground. Use the ones the conversation has not already answered:

1. Exactly what problem will this solve?
2. For whom do we solve it?
3. How big is the opportunity?
4. What alternatives are out there?
5. Why are we best suited to pursue this?
6. Why now?
7. How will we get it to market?
8. How will we measure success or make money from it?
9. What factors are critical to success?
10. Given the above, what is the recommendation?

Question 1 is the hardest. Most people answer it with a list of features. Push for the problem.

Then load `challenges.md` for the questions practitioners add on top.
