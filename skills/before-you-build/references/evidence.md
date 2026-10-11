# Evidence: what counts, what doesn't

Grade every claim the user makes about customers. Say the grade out loud, in plain words, without making the user feel foolish. The point is not to dismiss what they have; it is to show where it sits so the test can move it up.

## The ladder

| Level | Plain name | Examples | What it is worth |
|---|---|---|---|
| 0 | Not evidence | business plans, spreadsheets, market reports, our own reasoning | Useful for thinking. Says nothing about whether anyone wants it. |
| 1 | What people said | interviews, surveys, "customers keep asking for this", sales requests | A reason to look further. People's stated intentions explain only a fraction of what they later do, and stated willingness to pay runs roughly a fifth above real willingness (meta-analyses). |
| 2 | How people reacted to something shown | reaction to a mockup, a brochure, a product page, a demo | Better than talk. Still talk. |
| 3 | Something small they did | clicked a "coming soon" button, left an email, booked a call | Behaviour, low cost to them. Shows curiosity, not need. |
| 4 | Something costly they did | paid a deposit, signed a letter of intent, spent a day in a workshop, gave you their data, introduced you to their boss | Behaviour with a stake. Strong. |
| 5 | Real use | used the product repeatedly without knowing it was a test; still using it after 30, 60, 90 days | The only evidence that fully counts. |

Levels 0–2 are "they say". Levels 3–5 are "they do". **Quantity does not raise the level.** A thousand interviews are still level 1. Thirty signed deposits are level 4.

**Two different claims, graded separately.** "The problem exists" and "people will take up this solution" are different claims and usually have different evidence. Analytics showing a workaround, support tickets, a recruiter rebuilding the same filters in a usability session: level 4–5 evidence that the problem is real, and level 0 evidence that the proposed fix will be used. Say which claim a piece of evidence supports. A usability session can be strong evidence of a problem even though it is weak evidence of demand for a solution.

How much evidence is enough depends on the bet. A cheap, reversible change can ship on level 1. A large, forced-on-everyone change should not ship below level 4 for its kill assumption, and ideally has a level 5 pilot behind it.

## Things that look like evidence and are not

- **Compliments.** "Great idea", "I'd definitely use that", "love it". Fool's gold. Deflect and return to facts: "How do you handle this today?"
- **Friends, family, colleagues.** They are being kind, and they are not the customer. What counts is whether they use it daily after a month.
- **Hypotheticals.** "Would you buy a product that did X?" Any answer to a question about the future is a guess filtered through how the person wants to see themselves.
- **Generalities.** "Usually", "always", "never", "everyone". Pin each one to a specific event: "When did that last happen?"
- **Promises.** "I'll buy it", "we'd roll it out". The most dangerous sentence is "I would definitely buy that". A promise is level 1; a deposit is level 4.
- **Feature requests.** A request names a solution, not a need. Ask: "Why do you want that? What would it let you do? How do you cope without it?" The request for a logout button turns out to be a need for privacy on a shared computer. Most requests from sales never matter; the ones that do point to a problem behind them.
- **The team's own enthusiasm.** Including the user's. Conviction is allowed, labelled as conviction.
- **A beautiful prototype that ten people liked.** Shows they can use it, maybe. Does not show they want it.
- **A usability test.** Shows whether people can use it. Does not show whether they will.
- **The loud 20%.** A handful of vocal customers are not the 80%. Ask who the quiet majority is and what they do.

## When the next step is talking to customers

If the user needs to go and talk to people, give them these rules. They fit on a card.

**Three rules**

1. Talk about their life, not your idea. Do not pitch. Do not show the idea in the first half of the conversation; once they see it, they become polite.
2. Ask about specific things that happened in the past, not opinions or the future.
3. Talk less, listen more.

**Questions that work**

| Instead of | Ask |
|---|---|
| "Do you think it's a good idea?" | "How are you dealing with this today?" / "Walk me through the last time that happened." |
| "Would you buy a product that did X?" | "What else have you tried?" / "Why do you bother?" |
| "How much would you pay?" | "What does it cost you now, in time or money?" |
| "How often do you do X?" | "How many times did you do X last week?" |
| "Why did you buy it?" | "When did you first start thinking about this? What was going on at the time?" |

Open with "Tell me about the last time you…". When the story is thin, help them remember: "What happened first? What happened next? What happened before that?"

End with "Who else should I talk to?"

**Who to talk to**

- People who should have the problem, not people who are easy to reach.
- People who recently switched to a competitor or a workaround (last 30–90 days; after that the details fade).
- People who almost switched, and people who left.
- Not only the loud ones. Include the quiet majority and the ones who never bought.

**How many**

Five to eight before patterns appear. Around ten, stop and assess. If ten people say ten different things, the group is too broad; narrow it. Conversations give high confidence for known problems in business software and low confidence for truly new things; in that case, combine them with a behaviour test.

**The one sure signal in a conversation**

Ask for a commitment at the end, decided before the meeting: their time (a next meeting, a trial, feedback on a mockup), their reputation (an introduction to their boss or a colleague), or their money (a deposit, a pre-order, a letter of intent). A conversation that ends with a compliment and "let me know when you launch" was a no.

**Ask at least one question whose answer could kill the idea.** If every question is safe, the conversation was reassurance, not research.

## Reading a result

- **A surprising result** is checked for a data error before it is believed.
- **A neutral result** on a feature usually means the feature gets removed, not kept.
- **A bad result** says something about the idea only if the test was fair. See "After the test" in `tests.md`.
- **A good result** on a click or a sign-up says people were curious. Real value needs a measure closer to the goal: time saved, money paid, repeat use.
