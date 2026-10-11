# Challenges for bigger bets

Questions practitioners add on top of the basic check. Each group has a trigger: ask it only when the trigger applies. On a small, reversible change most of these are noise. On a six-month build they are the difference between a good decision and an expensive story.

Frequencies come from an analysis of 145 practitioner interviews: the share of interviews in which the practice came up. They say which concerns are common, not which are right.

## Customer signals (45%)

Trigger: the idea came from customer requests, sales, or a loud segment.

- "Why does the customer want this? And why do they have that problem at all?" The request often points at a different problem than the one it names.
- "Have you talked to people who did not buy, or who left?" Current happy users are the easiest to reach and the least informative.
- "Is this for the 80% or for the loud 20%?"
- "How urgent is it for them? Something they think about daily, or once a year?" Urgency predicts adoption better than enthusiasm.
- "What is solving this worth to them in money?" A careful "maybe" at a large number is a better signal than an enthusiastic "yes" at none.
- For business customers: "Do you understand their business the way their operations director does?"
- "Most requests from sales never matter. What makes this one different?"

## Upkeep, side effects, reversibility (43%)

Trigger: always on medium and big bets; also on small "obviously fine" features.

- "What will this cost to maintain forever? In business software it will not be removed."
- "What is the blast radius? What else changes because this exists?"
- "Is this a new option people can ignore, or a change everyone must live with?" These are different bets.
- "What does the current user expect to keep? What breaks for them?"
- "If a test comes out neutral, will you remove it?" Neutral features get removed; if the answer is no, ask why it is being built.
- "Small and flashy?" Such features sail through because nobody questions them. They add complexity like any other.
- "Is this reversible? If yes, why are we not just trying it?"

## Strategy and vision fit (40%)

Trigger: a new product line, a new segment, anything a company's leadership would need to bless.

- "If this succeeds, does it have a place in the company? Where?" Fit with the company comes before fit with the market.
- "Write the chain of reasons from the company's goal to this idea. Where does it break?"
- "What does the company explicitly not do, and why? Does this cross that line?"
- "When customer interest and business interest conflict here, which wins? Decided in advance?"
- "Could the company's product philosophy be a reason not to build this, even if competitors have it?"

## Real small version instead of a test (39%)

Trigger: the team has been discussing for weeks; the thing is small; or the user says "we'll test it when it's built".

- "Would a real, embarrassing, small version teach more than a test? What would it cost to be embarrassed, compared with not knowing?"
- "Instead of discussing for another month, what concrete thing could you make this week: a mockup, a prototype, a one-off delivery?"
- "If you ship, ship one new thing at a time."
- "Prefer small fast bets over half-year projects. Can this be cut into one?"

Balance with the basic rule: a small real version is the cheapest test only when the thing is small, reversible and ignorable. Otherwise test first.

## Conviction and taste (32%), and its critics (13%)

Trigger: the user says "I just know", "we have a strong feeling", "the founder wants it".

Conviction is a legitimate input. Many practitioners build on it for big, contested changes, and intuition is a good source of hypotheses. But:

- "Explain why the idea is good, not that you feel it is." A feeling that cannot be explained is a weak feeling.
- The "murder board": a two-page plan taken apart by three or four people outside the project. Offer to play this role now.
- "If I took away half your resources, what would you build? If the answer is vague, the conviction is weak."
- "Give the document to an engineer to tear apart."
- When a test comes out neutral, it is acceptable to pick the version you would choose starting from scratch — labelled as taste.

In the card, conviction appears under "what rests on conviction", never under evidence.

## Signals on the first real version (28%)

Trigger: a version exists or a pilot is planned.

- Ask users how disappointed they would be if it disappeared. Look at the "very disappointed" group: who are they, what do they have in common. Ignore "somewhat". A 40% average can hide a 70% segment.
- Friends' use is weak evidence. Daily use after 30, 60, 90 days is the measure.
- Do not scale a small problem. First a small group that loves it, then growth.
- Go deeper where it already works before going wider.

## Sales and business model (27%)

Trigger: anything the company will charge for.

- "What is the gross margin? Start from 60% and explain why it would not hold."
- "Who sells it, how, for how much?"
- "Set the trial length by when customers buy, not by when you need revenue."
- "Assign every cost to one transaction and price from there."
- "Draw the loop by which it spreads. Who tells whom?"
- "Does the early price decision lock in the future?"

## Advantage and the right to win (25%)

Trigger: a new market, a competitor comparison, a feature "everyone else has".

- "Why can't someone else do this? Will that still be true in two or three years?"
- "Does the company have a real strength here, or would it have to build a missing capability from zero?" Companies have failed at adjacent businesses because the operations were not theirs.
- "Does the current leader's business model prevent them from building this?"
- "Does this strengthen an existing network or asset (same drivers, same data, same customers), or start a new one?"

## Other people's experience (23%)

Trigger: anything that has been tried before, by anyone.

- "Who has already done something like this, and what did they learn?" Find the person.
- "Who are the sceptics of this trend, and what do they say?" Read them before following.
- "What did other teams' successful tests show that applies here?"
- "How do projects like this usually end?" The outside view corrects the habit of underestimating time and cost.

## Market size and direction (23%)

Trigger: new product, new segment, or a founder pitching.

- "How big is this, and which way is it moving?" Judge a market by its currents more than its size. A small market is fine if it is not a dead end.
- "Big enough to matter, small enough not to attract the giants?"
- "Is this an adjacent segment (same customer, new use; or same use, new customer) or a leap into the unknown?"
- "Could the idea be bigger? Set ambition from potential, not from today's numbers."

## Portfolio of bets (22%)

Trigger: the user manages several ideas, or this is one of many.

- "Is this a small bet or a big one? How many like it can you afford to lose?" New products are a portfolio; roughly half are expected to fail.
- "If more than 30–40% of your tests succeed, your bets are too small."
- "For cheap ideas, plant many and do not pick the winner in advance."
- "Send the biggest bets to discovery first, not the safe small ones."

## Timing and technology (19%)

Trigger: "why now", anything built on AI or a fast-moving platform.

- "What changed that makes this possible now, and was not true two years ago?"
- For AI features: "If the model gets twice as good, does this feature get twice as good? If not, it may not be worth shipping."
- "Are you building around today's weaknesses of the models? That work disappears."
- "AI pays where the current human process is weak: from 10–20% success to 50–80% is a clear win. From 95% to 97% is not."
- "Was this idea abandoned before? What was missing then, and is it now present?"

## Using your own product (19%)

Trigger: the team could use the product themselves.

- "Has the team used it for weeks before customers see it?"
- "Is the team using it intensely, or politely?" Low internal enthusiasm is a warning, especially for anything social.
- "Be your own first customer, then force real use at one real customer within three months."
- "Use it as the next type of user: a fresh account, a different role."
- Limit: own use finds problems; it does not tell you which problems matter to others.

## Idea or execution: was the test fair? (17%)

Trigger: a test has failed, or the user wants to kill an idea.

- "What failed: the idea, the strategy, or the execution?"
- "Was the first version good enough that the failure says something about the idea?"
- "Did the test remove the variables that could confuse the result?" One team launched to a whole school at once so the result would show whether the product worked, not whether the rollout did.
- "Did you try the test on yourselves first?"
- "A result that contradicts intuition is checked for a data error first."

## Check your intuition (13%)

Trigger: the decision rests on conviction and the bet is big.

- "What would have to be true for you to be wrong?"
- "Which single result would change your mind?" If none, say so in the card.

## Founder fit (10%)

Trigger: the user is a founder or will personally carry the project.

- "How much risk can you carry? Do you have the energy to start over if this fails?"
- "Is this your own problem, or one you have been told about?"
