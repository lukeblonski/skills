# Test cases

Use these to check the skill behaves. Each case has an opening message from a user, the answers they would give if asked, the expected verdict, what the skill must notice, and what it must not do. Half the cases should pass without nagging; a skill that stops every idea is as useless as one that waves every idea through.

Wording does not need to match. Verdict, pivotal reasoning and next move do.

## Coverage

| Case | Tests | Expected verdict |
|---|---|---|
| C-01 | Feature with no problem behind it | Not ready yet |
| C-02 | Big bet on conviction only | Test first, with challenges |
| C-03 | "Friends said it's great" as evidence | Test first; evidence regraded |
| C-04 | Cheap, reversible, ignorable feature | Ship a small version and measure; short conversation |
| C-05 | Well-prepared idea with behaviour evidence and a pilot plan | Ship a small version and measure (endorse the pilot); no nagging |
| C-06 | Numbers fail on paper | Stop or rethink |
| C-07 | Failed test, user wants to kill the idea | Check the test was fair before accepting |
| C-08 | AI feature built around today's model weakness | Test first; timing challenge raised |
| C-09 | User pastes a PRD | Skip answered questions; ask only about gaps |
| C-10 | Sales request from one big customer | Test first; customer-signal challenge; ask about the 80% |

## C-01 — feature with no problem

**Opening:** "We want to add dark mode to our invoicing app. Can you help me check if it's a good idea?"

**Answers if asked:** Who: "all our users." Problem: "people like dark mode." Last time it happened: "I don't know, it's just standard now." Number that changes: "satisfaction, I guess." Alternatives: none.

**Expected:** Not ready yet. The problem cannot be stated as something a customer would say; no real recent instance; no number. The card names what is missing (a real person, a moment, a measurable change) and the cheapest way to get it (look at support tickets and feature requests for the word "dark"; ask five users about the last time the screen bothered them).

**Must notice:** "people like it" is level 0–1; "standard now" is not a goal.
**Must not:** proceed to a test for a feature whose problem is unstated; lecture about methodology; ask more than two questions to establish that the problem is missing.

## C-02 — big bet on conviction

**Opening:** "I'm the founder. We're going to rebuild our onboarding from scratch as a guided AI assistant. Six months, four engineers. I know this is the future. Help me prepare the case for the board."

**Answers if asked:** Who: "every new customer." Problem: "onboarding takes too long." Last time: "a customer told me at a conference." Number: "activation, currently about 30%, no target." Cost: six months, four people, hard to undo, everyone goes through it. Evidence: "my gut, and the conference conversation." Alternatives: "we thought about fixing the current flow but it's a dead end."

**Expected:** Test first. Big, irreversible, forced on everyone, resting on conviction plus one anecdote. The skill labels conviction as conviction, raises upkeep/reversibility and the "ignorable vs forced" distinction, asks what would change the founder's mind, proposes a cheap test of the kill assumption (e.g. a hidden-manual-work version of the assistant with ten new customers for two weeks, measuring activation against the 30% baseline), and writes the decision rule. It also asks why the current flow is a dead end, since "fix the current flow" is the obvious alternative.

**Must notice:** the test must keep the attractive part (a real guided experience), not a chatbot stub. The AI timing question applies: does the feature improve as models improve.
**Must not:** tell the founder the idea is bad; accept "I know this is the future" as evidence; skip the alternatives question; run past twelve exchanges.

## C-03 — friends as evidence

**Opening:** "I've got an idea for a meal-planning app for people with food allergies. I've shown it to about 15 people and everyone loves it. What's the next step?"

**Answers if asked:** Who shown: "friends, family, two colleagues." Did any of them use anything: "I showed them mockups." Problem last happened: "my sister spends an hour a week checking labels." Number: "time spent planning, from an hour to 15 minutes." Cost: three months of evenings. Alternatives: "there are apps but none for allergies specifically."

**Expected:** Test first. The skill regrades "15 people love it" as level 2 at best (reaction to a mockup), from people who are not the customer, and says so kindly. The sister's story is a real instance. It proposes a behaviour test: a landing page with a deposit or a hand-run service (the founder plans meals by hand for five allergy sufferers found outside the family for two weeks), with a count threshold. It asks the user for their guess before proposing a number.

**Must notice:** the sister is one real person; "none for allergies" needs checking before it counts as an advantage.
**Must not:** treat the 15 compliments as demand; propose another round of showing mockups; skip the "what does it cost now" question.

## C-04 — cheap, reversible, ignorable

**Opening:** "Our support team asked for a 'copy ticket link' button in the ticket header. Takes a day to build. Should we just do it?"

**Answers if asked:** Who: "support agents, about 40." Problem: "they copy the URL from the address bar and paste it into Slack maybe 20 times a day; the URL has tracking junk on it." Cost: a day, trivially removable, nobody has to use it. Known: "I watched two agents do it yesterday."

**Expected:** Ship a small version and measure. The conversation is short (three to five exchanges). The skill notes the evidence is real observed behaviour, the bet is tiny and reversible, and the right move is to ship it to the 40 agents with one measure (e.g. button used by at least 20 of 40 agents in week one) and a removal rule if not.

**Must notice:** the upkeep question still applies, in one line.
**Must not:** run the full path; ask about market size, strategy fit or business model; produce more than a short card.

## C-05 — well-prepared idea

**Opening:** A pasted brief: fleet managers with 200+ vehicles spend Friday afternoons exporting the vehicle list to a spreadsheet to find vehicles due for inspection; 168 of 420 such managers exported to CSV within five minutes of opening the view in the last 30 days; median time from opening the list to creating a service order is 4 min 20 s in a 60-session sample; 11 of 15 interviewed managers described the manual filtering; reducing service-planning time is a quarterly goal. Proposal: combinable filters, behind a flag, to 20 managers for two weeks. Success: median time under 2 minutes; CSV export share from 40% to under 25%; correct identification not below 98%; response time not worse by more than 200 ms. If both primary criteria met, expand; if not, go back to session evidence.

**Expected:** Ship a small version and measure, endorsing the pilot as proposed. The skill recognises behaviour evidence (level 5 usage data), a real goal, a baseline, a decision rule and guardrails already present. The conversation is one or two exchanges. The card restates the pilot and adds at most one open question (e.g. what the 252 managers who did not export do instead).

**Must notice:** the pilot is the test; the CSV rate is supporting behaviour, the time to create an order is the value measure.
**Must not:** demand more discovery; present the pilot back as its own recommendation; add generic challenges; claim the brief's numbers were verified.

## C-06 — numbers fail on paper

**Opening:** "SaaS tool for independent bookstores to manage author events. $50 a month. I want this to be a real company, say $5M a year in three years. Is it worth building?"

**Answers if asked:** Who: "independent bookstores in the US and UK." Problem: "events are organised in email threads and spreadsheets; my friend who owns a store spends a day a week on it." Number of independent bookstores: "a few thousand in the US, maybe 2,500? UK fewer." Cost: a year of two people.

**Expected:** Stop or rethink. $5M ÷ $600 per customer per year ≈ 8,300 customers, more than the number of bookstores that exist; at a plausible 1 in 100 conversion, 830,000 bookstores would need to be reached. The skill does the arithmetic out loud, in plain words, and says the goal and the market cannot both be true. It offers the reopening options: a different price, a wider customer (all independent retailers running events), or a different goal (a $200k business).

**Must notice:** the friend's day-a-week is a real problem; the issue is the goal, not the need.
**Must not:** propose a demand test before the arithmetic; dismiss the idea as bad; invent market numbers without saying they are rough.

## C-07 — failed test, user wants to kill

**Opening:** "We tested the badges idea with a 'coming soon' button and only 2% clicked. So badges are dead, right?"

**Answers if asked:** What the button said: "'Earn badges — coming soon'." Where: "bottom of the settings page." Who saw it: "everyone who opened settings, about 400 people." Threshold set before: "we didn't set one." Did the team try it: "no."

**Expected:** Not a verdict on badges yet. The skill checks the test was fair: a plain button in settings strips out everything attractive about badges and reaches people in the wrong moment; no threshold was set, so 2% cannot be judged. It proposes a fairer test (show a mockup of a real badge at the moment it would be earned, with the attractive part intact) with a threshold set first, and asks the user to guess the number.

**Must notice:** a stripped-down test gives a false no; "no threshold" means the result cannot be read.
**Must not:** agree badges are dead; agree 2% is fine; propose building badges.

## C-08 — AI feature around today's weakness

**Opening:** "Our users complain the AI summaries hallucinate numbers. We want to build a manual review queue where a human checks every summary before it's shown. Two months of work."

**Answers if asked:** Who: "finance analysts using the summaries." Problem: "last week one pasted a wrong figure into a board deck." Number: "complaints about wrong numbers, 12 last month." Cost: two months, plus permanent reviewer time; removable but the reviewers become a team. Alternatives: "better prompts, showing sources next to numbers, making the model cite the cell."

**Expected:** Test first, and the timing challenge is raised: a review queue is built around a weakness that models are closing; the work may be obsolete before it ships; and the permanent reviewer cost is the real bet. The skill asks whether the alternatives (cite the source cell, show the number with its origin) were tested, and proposes the cheapest test (e.g. two weeks of a human reviewing summaries by hand for the ten analysts who complained, measuring whether wrong-number complaints drop and how many summaries need correction).

**Must notice:** the real problem (wrong numbers in board decks) is serious and real; the proposed solution is the thing in question, not the problem.
**Must not:** dismiss the problem; skip the upkeep question; ignore the alternatives the user listed.

## C-09 — pasted PRD

**Opening:** A one-page PRD with: user, problem, success metric with baseline, scope, and a rollout plan, but no mention of evidence for the problem and no decision rule for the rollout.

**Expected:** The skill does not ask what the PRD already answers. It asks two things: what the problem claim rests on (and grades it), and what result after rollout would make the team keep, change or remove the feature. Verdict depends on the answers; the card reuses the PRD's content.

**Must not:** re-ask the user, problem or metric; produce a card that ignores the PRD's numbers.

## C-10 — one big customer's request

**Opening:** "Our biggest customer wants a custom approval workflow with five levels. Sales says we'll lose the renewal if we don't build it. Three months."

**Answers if asked:** Who else: "nobody else has asked." Why five levels: "that's how their procurement works." What the customer does today: "they do approvals in email, then enter the result." Renewal value: "about 15% of revenue." Removable: "no, once they use it it's forever."

**Expected:** Test first, with the customer-signal and upkeep challenges. The skill separates the renewal risk (real, 15% of revenue) from the product question (a five-level workflow nobody else wants, permanent upkeep). It asks why the customer wants five levels and what problem is behind it; asks whether a two-level version or a manual workaround would keep the renewal; proposes an offer-before-building test with this customer (a mockup, a price or a renewal commitment in writing, a next step) and a check with five other customers of whether approvals are a problem for them.

**Must notice:** "we'll lose the renewal" is a claim from sales, level 1, worth checking with the customer directly.
**Must not:** tell them to refuse the customer; tell them to build it because of the renewal; skip the "who else" question.
