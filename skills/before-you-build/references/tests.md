# Cheap tests, thresholds, and what to do with the result

## Four rules for choosing a test

1. Go cheap and fast early. The first test should take hours or a couple of days, two weeks at most. If it takes longer, shrink it.
2. Pick the test that gives the strongest evidence you can afford. A deposit beats a sign-up; a sign-up beats a survey.
3. Change one thing at a time, so the result has one explanation.
4. Reduce uncertainty as much as possible before building. Building is usually the most expensive way to learn — unless the thing is small (see "Measured release").

Three more that practitioners insist on:

- **Keep what is attractive.** A test that strips the idea down to something nobody would want gives a false "no". A badge system tested as a plain counter is not a test of badges.
- **Observe, don't ask.** Simulate the experience and watch what people do.
- **Make the action cost them something.** Time, money or reputation. A free click measures curiosity.

## Which test for which unknown

| Unknown | Tests, cheapest first |
|---|---|
| Do they want it? | existing data (support tickets, searches, analytics); "coming soon" door; one-question survey about past behaviour; product video with sign-up; landing page with deposit; offer before building |
| Will they pay / does it pay? | offer before building with a price; pre-order; letter of intent; deposit page; hand-run service for three customers at the real price; quick arithmetic on paper |
| Can we build it? | a short throwaway technical try by engineers (a "spike"); a conversation with the teams you depend on; for AI, a test on real data with the error rate measured |
| Can they use it? | a clickable mockup with five people doing a real task; a non-working model carried around for a week |
| Does it harm anyone? | the embarrassment test: would we be comfortable if the internal discussion were public; who is excluded; what data is used |

Tests with hidden manual work (a person behind the curtain doing what the software would do) test demand, not buildability. Say so when proposing one.

## Catalogue

| Test | How it works | Cost | Evidence level | Trap |
|---|---|---|---|---|
| Existing data | look at support tickets, sales notes, search logs, analytics for the problem's footprint | hours | depends on data; behaviour if it is usage data | tells you about current users only |
| One-question survey | one question about past or current behaviour, inside the product | hours | 1–2 | ask about the past, not the future |
| "Coming soon" door | a button, link or menu item for something that does not exist; count clicks; tell people the truth right after, with a small thank-you | hours | 3 | measures first curiosity only; always disclose |
| Landing page with email | a page describing the product and a sign-up field | a day | 3 (weak) | does not tell you why people did not sign up |
| Landing page with deposit | same, with a payment | a day | 4 | — |
| Product video | a short film showing the product as if it existed, with sign-up or deposit | days | 3–4 | — |
| Offer before building | show a mockup, state a price and a next step, in person, to ten or more people within two weeks | days | 4 | needs some selling skill; the best version because you hear why people say no |
| Letter of intent | a signed statement of intent to buy, based on mockups | days | 4 | some will not sign; signers may dispute terms later |
| Hidden manual service | people behind the scenes do what the software would do; the user does not know | low tech cost, high labour | 4–5 for demand, 0 for buildability | — |
| Open manual service | the service delivered by hand, openly, to a few customers at the real price | low | 4 | does not scale; that is the point |
| One-off delivery | deliver the service once, by hand, without any infrastructure (three bookings, not a booking platform) | low | 5, once | — |
| Non-working model | a mock object or screen carried and "used" for a week to see if the habit forms | very low | 2 | imagination fills in the gaps |
| Clickable mockup | five people try to complete a real task on screens that do nothing | a day | usability only | does not test demand |
| Technical try | engineers build something to throw away, to see if the hard part is possible | days | buildability only | PM guessing buildability without engineers is a common failure |
| Measured release | ship a small real version to a limited group behind a switch, with the prediction written first | real build cost, small | 5 | only for small, reversible, ignorable changes |

The strength of evidence column is a judgement; the authors of these tests do not grade them on one scale.

## Measured release (for small bets)

When the change is cheap, reversible and ignorable, building a small real version is the cheapest honest test. Keep the discipline:

- Limited group, behind a switch, fixed window (two weeks is typical).
- One primary measure close to the goal (time saved, orders created, money paid), not a proxy (clicks, opens, views).
- One or two guardrails: numbers that must not get worse (error rate, response time, existing users' core task).
- Prediction and decision rule written before shipping, like any other test.
- Ship one new thing at a time, not several. Several at once make the result unreadable.
- The team uses it themselves first, for days or weeks. Low enthusiasm inside the company is a warning sign, especially for anything social. (Own use finds problems; it does not tell you which problems matter to others.)
- If the user arrives with their own criteria, keep them exactly as written. Do not add a count on top of a percentage, do not add a criterion, do not ask for a guess they have already committed to. The only thing worth adding is a missing decision rule or a missing guardrail, and only if it is missing.
- For a tiny change (a button, a link), the honest measure may be a use count, which is a proxy. Say so in one line and move on; a one-day change does not deserve a value study.

## Writing the prediction

Template (fill every bracket; vague words like "some", "many", "interested" are not allowed):

> We believe that [specific group] will [specific action, ideally with a price].
> To check, we will [test] with [N people] over [D days].
> We will count [the action].
> We are right if at least [K of N] do it.
> If right → [next step]. If wrong → [stop / change X]. If in between → [one more test / treat as wrong].

Example before: "Some residents of polluted cities would be interested in an affordable air sensor."
Example after: "At least 10 of 100 residents of cities with air quality index above 100 will pay 120 for a portable sensor from the landing page within two weeks."

### Where the number comes from

Four sources, in order of preference. None of the authors derive it from the cost of being wrong; use judgement.

1. **From the goal, backwards.** The minimum success three years out → customers needed → people to reach → what share of a test group must act for that to be plausible.
2. **From the user's own guess**, written down before the test. Ask each person on the team to guess separately, then compare; this stops the most senior guess from winning.
3. **From comparison.** Typical conversions in the user's field, if they know them.
4. **Relative, not absolute.** When comparing several ideas, ask which did best, not whether one was good enough.

### Sample size and time

- Small, fast tests: "3 of 5", "7 of 10". Run in one or two days. Scale up only if the signal is promising.
- When expecting around 10 actions: sample ≈ 1000 ÷ expected %. At 10% expected, 100 people; at 1%, 1000. A rule of thumb, not statistics.
- Business software with a small market: around half the target firms.
- Two to five small tests beat one big one.

### A test that cannot change the decision

If the user would do the same thing whether the result is good, bad or flat, do not run the test. Say so. Either the decision is already made (then make it, and label it as conviction) or the test is measuring the wrong thing.

## After the test

### Was the test fair?

Before reading a bad result as a verdict on the idea, check:

- Did the test keep the attractive part of the idea?
- Did it reach the right people, in enough numbers?
- Was the execution good enough that failure says something about the idea rather than the build? A clumsy first version gives a false "no".
- Were other things changing at the same time?
- Did the team try the test on themselves first?
- Is the data right? A surprising result is checked for a data error before it is believed.

If the test was unfair, fix it and run it again. If it was fair, the belief was not confirmed.

### Resisting the excuses

When the threshold was 10 of 100 and the result is 5, the team will say "people need time to learn", "the design was weak", "5 is still good". These are the reasons the decision rule was written first. If the rule said "below threshold means wrong", it means wrong. Changing the idea so the failed belief is no longer needed is allowed; pretending the belief passed is not.

### A good result

- Was the measure close to real value, or a click? Curiosity is not need.
- If the product needs repeat use, measure interest over time, not just first interest.
- Repeat the test in a different place or group before trusting it.
- For a product used repeatedly: are people still using it after 30, 60, 90 days?
- A survey asking how disappointed users would be if the product disappeared: look at the "very disappointed" group and what they have in common; ignore "somewhat". A high score in one segment matters more than an average across all.

### Then re-rank

After every test, go back to the list of what must be true. Something moved. Decide the next test or the next step. Do not make the final decision on one test. When a kill assumption fails and the test was fair: stop, or redesign the idea so that assumption is no longer required.

## Ethics of testing

- A "coming soon" door tells people the truth as soon as they click, and thanks them.
- No test puts your product into someone else's channel without their consent.
- A test that could harm or mislead the people in it is not cheap, whatever it costs.
