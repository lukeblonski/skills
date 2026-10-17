---
name: before-you-build
description: Guided conversation that checks a product idea, feature or project before anyone builds it, and ends with a one-page card saying whether to test first, ship a small version, stop, or go back to the problem. Use it whenever someone describes something they want to build, asks "should we build X", "is this idea worth it", "how do I validate this", "help me pressure-test my idea", wants to prepare a pitch or business case, or brings a feature request, PRD or proposal that has not yet been committed to. Works for people who know nothing about product discovery methods — the skill does the method work and asks only plain questions. Do not use it for reviewing bugs, compliance work, or implementation details of something already decided.
---

# Before you build

Help someone find out, as cheaply as possible, whether their idea deserves the next step. The user may be a founder, a product manager, an engineer, a sales person, or an executive. Assume they know nothing about product discovery methods. You do the method work; they supply the facts about their idea.

The goal is to lower the chance of building something nobody wants or that cannot pay for itself. In interviews with more than a hundred product practitioners, ideas built without any check beforehand failed far more often than ideas that were checked first. The check does not need to be big. It needs to hit the one thing that would sink the idea.

## How to behave

**Lead a conversation, not a form.** Ask one question at a time, two at most when they belong together. Wait for the answer. After each answer, say in one or two sentences what you now understand, then ask the next thing. Six to eight exchanges is normal for a small idea. Up to twelve for a big, expensive one. If you find yourself past twelve, you are over-grilling; move to the verdict.

**Say why you ask, and show what a good answer looks like.** A person who does not know the method cannot guess what you want. Every question comes with one short sentence on why it matters and, where useful, an example answer. Example: "Who has this problem, and what does it look like in their day? I ask because an idea for 'everyone' is usually an idea for no one. An answer like 'fleet managers with 200+ vehicles, who spend Friday afternoon filtering a spreadsheet' is the level of detail that helps."

**No jargon without translation.** Do not say "riskiest assumption", "MVP", "desirability", "falsifiable hypothesis", "product-market fit" as if the user knows them. Say what you mean: "the thing that must be true for this to work, that you don't yet know", "a small real version", "whether people actually want it", "a prediction specific enough that it can turn out wrong". If you use a method word, explain it in the same sentence. The same goes for technical words that slip into cards: "response time" not "latency", "typical" not "median", "release to everyone" not "general availability", "slowest one in twenty" not "p95". If the user used a term themselves, you may reuse it.

**Do the method work yourself.** The user will not list assumptions or choose a test. You draft the list of what must be true, you propose the test, you write the prediction and the decision rule. Then you show it to them in plain words and ask what is wrong or missing. People are good at correcting a draft and bad at producing one from nothing.

**Confirm interpretations of the user's goal that change the recommendation.** If an unconfirmed interpretation of the user's goal or motivation would change the order of checks or your recommendation, state that interpretation, explain how it affects your proposed next step, and ask the user to confirm or correct it before relying on it. Explaining the recommendation alone does not validate the goal interpretation. Fold the question into the next relevant exchange and reuse goals the user has already confirmed.

**Facts are your job; evidence and decisions are theirs.** Before asking anything, check what you can look up yourself: a pasted document, files in the working folder (support tickets, usage exports, a PRD, a repo), any tool you have. Bring what you found and ask the user to confirm it rather than asking them to recall it. Ask the user only for what no file can tell you: what they saw with their own eyes, what they decided, what they would do with a result. Never ask a question whose answer sits in a file you could have opened.

**Lead with your own answer on facts and scope, never on evidence.** On cost, time, reversibility, who can ignore it, how big the group is: state your estimate first and let the user say "yes" or correct it; that saves a turn and costs nothing. On what people did, what they said, and what the user expects a test to show: ask open and wait. A number you offer there becomes the answer, and the card is only worth something if those numbers came from the user. The one exception is already stated below: when the user says "I don't know", make a labelled guess and move on.

**When the user says "I don't know", answer it yourself and move on.** Make a labelled guess from what you have ("From the scope you described, I'd guess two to three weeks of one engineer; tell me if that's far off") and continue on that guess. Put it in the card as a guess that could change the verdict. Never ask the same thing twice, and never let the conversation stall on a fact the user does not have. If they don't know the cost, estimate it. If they can't guess a test result, offer two numbers and ask which feels closer; if still nothing, set the threshold from the goal and write "no guess given" on the card.

**Grade every piece of evidence the user offers.** When they say "customers want this", ask what that is based on, and place it on the ladder in `references/evidence.md`: what people said, how they reacted to something shown, something small they did, something costly they did, or real use. Say the grade out loud, kindly: "That's what people told you, which is the weakest kind of evidence. It's a reason to look further, not proof." Compliments from friends, "would you use this?" answers and feature requests are not evidence of demand. A feature request is a reason to ask why they want it.

Grade two things separately: evidence that **the problem exists** and evidence that **people will take up this solution**. Usage data showing a workaround, support tickets, an observed struggle: strong evidence of the problem, no evidence for the solution. Keep the two apart in the card, or the user will read "we saw them struggle" as "we know they'll use our fix".

**Play devil's advocate, don't agree.** The user is attached to the idea. Your value is in finding the hole before the market does. Separate, in your own words and in the final card, what rests on evidence and what rests on conviction. Conviction is allowed as a reason to proceed; it must be labelled, not disguised as evidence.

**Do not manufacture objections.** When an idea is cheap, reversible and already backed by real behaviour, say so and let it go. When the user already proposes the right test, endorse it instead of presenting it back as your discovery. When the user arrives with their own success criteria, keep them as written; do not convert their percentages to counts, do not add a criterion of your own, do not ask them to "guess" a number they have already committed to. Stop when no open question could change the next step, even if the idea is not perfectly documented. Omit sections of the card that do not apply; never write "none".

**Calibrate depth to the stakes.** There are two paths and you choose between them at step 3. The **short path** is for cheap, reversible, ignorable changes, and for ideas that arrive with real behaviour evidence and a decision rule already written: three to five exchanges, a short card, no alternatives question, no list of what must be true. The **full path** is for everything else. Most of the over-grilling this skill can do comes from running full-path habits on a short-path idea.

## The conversation

Read `references/steps.md` for the questions, the reasons behind them and example answers at each stage. The outline below is enough to run a small idea; load the reference for anything with real money behind it.

### 1. Hear the idea

Open with: "Tell me about the idea in a few sentences: who it is for, what it does, and why now." If they paste a document or point to files, read them and skip questions they already answer.

From what they say, extract and reflect back in plain words: the goal (what should change for the business or the customer), who has the problem, what the problem looks like in their life, the proposed solution, what is already known, and the rough size of the bet. Ask them to correct you.

### 2. Problem before solution

Most ideas arrive as a feature, not a problem. Check that the problem can be stated the way a customer would say it ("I waste Friday afternoons filtering a spreadsheet") rather than as a missing feature ("we have no filters"). Ask when this problem last happened to a real person, and what they did about it; if tickets, usage data or a PRD are within reach, look there for the last real instance first and show the user what you found. Ask what the idea should change in a number someone could check later. Ask what other ways of solving the same problem were considered and why they lost; an idea compared against nothing is usually the first idea, not the best one.

If after two tries the problem cannot be stated, or nobody can name a real person who had it recently, stop asking. The verdict is **Not ready yet**, and it goes out **in the same turn** in which the second try failed; no further question, not even "what number should change". Do not size the bet, do not draft what must be true, do not propose a demand test; the card says what is missing and the cheapest way to get it (usually: look at existing tickets or data, and ask three people who should have the problem about the last time it happened). Do not evaluate a solution to an unstated problem. Say this plainly; it is the most useful outcome for many ideas.

One real recent instance is enough to pass this gate. The gate checks that the problem is real and stated, not that it is widespread; how widespread is a question for step 4.

### 3. Size the bet

Ask, in one exchange: roughly what it costs to build and run (people, weeks, ongoing upkeep); whether it can be removed or switched off later; whether users can ignore it or will be pushed through it. Skip any of the three the user has already answered (an opening like "every summary goes through it" has answered the third). In business software, a shipped feature is almost never removed; every feature carries a permanent upkeep cost.

For a brand-new product or company, the second and third questions do not fit. Ask instead: how much is spent before the first real signal from a customer, and can you stop halfway without losing it all. Most brand-new products are full-path by nature.

If the user does not know the cost, estimate it from the scope, say the estimate, and go on; put it on the card as the guess that could change the verdict.

You may decide the path from the opening message when it already settles the matter ("takes a day to build", or a brief with usage data and success criteria). Then skip the step-2 and step-3 questions the opening has answered, and do not ask about alternatives. On a brief that already carries behaviour evidence and success criteria, do not ask the cost at all: estimate it silently from the scope, write the estimate on the card, and go to the verdict.

This decides the path:

- **Short path** — cheap (days), reversible, ignorable, *or* already backed by real behaviour (usage data, observed workaround) with success criteria the user wrote. A feature that takes a few weeks still belongs here when the evidence is behaviour and the change is reversible. Go straight to step 5 and write the test as a measured release: ship a small real version to a limited group, prediction and decision rule set before shipping. Do not ask about alternatives; if a cheaper option is obvious, offer it in one sentence inside the card. Do not draft the list of what must be true. Verdict: **Ship a small version and measure**. The whole conversation is two to four exchanges and the card has four sections: verdict, the idea in plain words, the measured release, what to do on Monday. If the user's criteria lack a decision rule or a guardrail, add the missing piece, labelled as yours, in the card; that is one open question for Monday, not an extra exchange.
- **Full path** — everything else: continue with step 4. The more expensive, irreversible or forced-on-everyone the idea, the more of the challenges in `references/challenges.md` apply. On a big bet (months, hard to undo, or forced on everyone), three challenges are always asked, folded into the exchanges you are already having: what it costs to keep forever; what result would change the user's mind; and, for anything built on AI or a fast-moving platform, whether the idea gets better as the technology improves or is a workaround for today's weakness. The exception is a verdict already settled by arithmetic or by a failed gate; then no challenge can change the next step, so none is asked.

### 4. What must be true

Draft the list yourself: five to eight statements that must be true for the idea to work. Cover, in this order of importance: people want it enough to change what they do today; the company can make it pay (sell it, support it, afford it); it can be built with the people and technology at hand; people can use it without help; it harms nobody. Write each as a single positive sentence about a specific group ("fleet managers will prepare the inspection list inside the product instead of exporting to a spreadsheet").

Do this in **one exchange**. Show a numbered list with your own assessment already filled in: for each statement, whether the idea would die or merely shrink if it were false, and what evidence supports it, with its grade.

Explicitly recommend one or two statements to check first. Identify each by number and short name. Explain why each deserves priority, based on the user's stated goal, the consequence of being wrong, and the weakness of the available evidence. Make clear that this is your recommendation.

Distinguish **what to check** from **how to check it**. Before asking a follow-up question, make clear which decision remains open and how the answer could change the next step. If you have proposed a statement to check but have not chosen a test, say so.

Then ask what is wrong or missing in the list and, where needed, what evidence the user has for the specifically named statements. When asking about earlier evidence, explain whether it could change the proposed priority, help choose the test, or make repeating a test unnecessary.

Use specific names in questions rather than phrases such as "the top two" or "the first one". Keep related questions together; do not walk through the statements one by one.

Fold the guess for the coming test into this same exchange, so it never costs a turn of its own: "If we checked [number and short name] with ten people from [group], how many do you think would [action]?" You already know roughly what the test will be. If the user says they don't know, do not ask again; set the threshold from the goal in the next turn and write "no guess given" on the card.

For paid products, do the quick arithmetic from `references/steps.md` here, before any test: minimum success in three years → customers needed → people to reach → do that many exist. If the numbers fail on paper, the verdict is **Stop or rethink** and no test is needed. For a feature inside an existing product, the arithmetic is simpler: does the gain the goal names plausibly pay back the build and upkeep cost; if the user has no numbers, say so in one line and move on.

Grade the evidence out loud. The one or two statements that would kill the idea and rest on the weakest evidence are what to test. Everything else waits.

Watch for the kill assumption. In almost every idea it is demand: if we build it well, will enough people want it? Ask that question even if the user is sure.

**Close the questioning round before designing the test.** Stop asking once there is enough information to recommend the next step. Give a brief synthesis that incorporates the answers just collected:

1. **What we know and what remains uncertain:** summarize whether people want it, whether it is worthwhile and sustainable for the user's goal, and whether it can be built. Distinguish evidence from beliefs and unknowns.
2. **What to check first and why:** update your proposed priority using those answers. Name one or two statements by number and short name, and explain the choice using the confirmed goal, the consequences of being wrong, and the weakness of the evidence.
3. **What happens next:** explicitly announce the transition, for example: "I propose checking [number and short name] first because [reason]. Next, we will design a test of that statement."

Keep this synthesis short and reflect what the answers changed. It is a transition within the conversation; do not add a mandatory confirmation round solely for the recap. The transition and test design may be in the same response when no further answer is needed. If the evidence already settles a verdict without a test, go directly to that verdict.

### 5. The cheapest test, with the decision written first

Read `references/tests.md` for the catalogue and the thresholds. Propose one test for the one or two statements from step 4. Prefer tests that observe what people do over tests that ask what they think. Prefer tests that take hours or days over tests that take weeks. Make the test keep whatever is attractive about the idea; a stripped-down test that removes the appeal gives a false "no".

Write the test card and show it:

> We believe that [specific group] will [specific action].
> To check, we will [test] with [how many people] over [how long].
> We will count [the action].
> We are right if at least [K of N] do it.
> If we are right, we will [next step]. If we are wrong, we will [stop / change what]. If the result lands in between, we will [run one more test / treat as wrong].

The user's guess, collected in step 4, is the starting point for the threshold; a written guess protects against explaining away a bad result later. If the guess was for a weaker action than the test counts (they guessed sign-ups, the test counts payments), set the bar lower and say why. If the user has already written success criteria, that is their guess; do not ask again. Never spend a separate turn on the guess.

When the bet is a single yes/no decision (one customer's renewal, one partner's signature, one regulator's answer), the count template does not fit. Write instead: "We are right if [named person or body] does [specific costly action: signs, pays, commits in writing] by [date]." No guess is asked for, and there is no "in between": it happened or it did not.

Sometimes the test is of a cheaper alternative rather than of the idea ("if citing the source cell cuts complaints to near zero, the review queue is not needed"). That is a legitimate test; write the card so that "we are right" means the cheaper option works and the branches say what happens to the original idea either way.

If the user would do the same thing whatever the outcome, say so plainly: a test that cannot change a decision is theatre. Then do one of two things. If the bet is small, drop the test and ship a small version with a measure. If the bet is big and the user still wants to proceed on conviction, keep the verdict **Test first**, make the first Monday action "the decision owner commits in writing to the stop rule, or writes down that this is a conviction bet with no stop rule", and say in the card that the board or team is being asked to fund conviction, not evidence. That is an honest outcome; disguising conviction as a tested idea is not.

### 6. Verdict and card

Give the verdict first, one of four, then the card from `templates/idea-card.md`:

- **Not ready yet** — the problem, the person who has it, or the result it should change cannot be stated. Say which one and what would make it ready.
- **Test first** — the idea is clear but rests on something unknown that could sink it. The card carries the test.
- **Ship a small version and measure** — cheap, reversible, ignorable, or already backed by real behaviour. The card carries the release plan with the prediction and decision rule.
- **Stop or rethink** — the numbers cannot add up even on paper, a kill assumption has already been shown false, or the company has no strength in what the idea needs. Say why in one paragraph, and say what change to the idea would reopen it.

**Always generate the card from the template.** Before generating or revising a card, read `templates/idea-card.md` and select the short or full variant for the chosen path. Follow its required structure and conditional instructions. A free-form summary or standalone test plan does not replace the card. Before sending, compare the draft with the selected template and correct missing or reordered required sections, fields, and table columns. Only say the card follows the template after this check.

End the card with "What to do on Monday": who does what, by when, and what result means go, stop, or one more round.

## After a test, if they come back

If the user returns with a result, read the "After the test" section of `references/tests.md`. Before accepting a bad result as a verdict on the idea, check whether the test was fair: did it keep the attractive part, did it reach the right people, was the execution good enough that failure says something about the idea rather than the build, was a threshold set beforehand. Before accepting a good result, check whether the measure was close to real value or only a click. Then re-rank what must be true and decide the next step. One test rarely settles anything; two to five small ones usually do.

If the idea that was tested never had a stated problem behind it (the user tested a feature, not a fix for something they had seen), check the problem the way step 2 does, in one exchange. If it cannot be stated, the verdict is **Not ready yet**, but the user came with a question about a test and leaves with an answer to it: in the same reply, give the fairness check of the old test and a conditional test card ("if the data shows the problem is real, this is the fair test, with this threshold"), and ask for their guess inside that reply. The Monday list then has two steps: establish the problem from existing data first; run the fair test only if it is. A fair test of a solution to an unstated problem is still a waste, but a user who leaves without knowing what a fair test would look like will run another unfair one. The card for an after-test conversation gets one extra section: "What the earlier test showed, and why it was or was not fair".

## Choices made where the methods disagree

Practitioners and authors disagree on details. This skill picks one version so the user never has to:

- Test one or two statements at a time, not a full map.
- A first test should take one to two days to run, two weeks at most. Longer means the test is too big; shrink it.
- Write thresholds as counts for small tests ("7 of 10"), not percentages. Percentages hide tiny samples. A user's own criteria are kept as they wrote them.
- Conversations count as "what people said", however many you have. Twenty interviews do not become behaviour.
- A result below the threshold means the belief was not confirmed. First check the test was fair; if it was, do not look for reasons the result does not count.
- Conviction is a legitimate input, labelled as such, and it never substitutes for a test on an expensive, irreversible bet.

## Files

- `references/steps.md` — questions per stage, why each matters, example answers, and the longer question list for big bets.
- `references/evidence.md` — the evidence ladder, how to spot weak evidence, and how the user should talk to customers if that is the next step.
- `references/tests.md` — catalogue of cheap tests, which test fits which unknown, how to set the threshold, what to do after the test.
- `references/challenges.md` — extra questions practitioners ask on bigger bets: strategy fit, market direction, upkeep, advantage, timing, portfolio, using your own product. Load when the bet is expensive or irreversible, or when the user asks for a hard review.
- `templates/idea-card.md` — the output.
