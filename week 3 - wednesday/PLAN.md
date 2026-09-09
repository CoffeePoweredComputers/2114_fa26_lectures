# Week 3 · Wednesday — the make-up deck

Built 2026-09-08. The Monday/Wednesday section lost Monday to Labor Day, so this one
hour carries the peer-instruction questions of both Week 3 days and nothing else: no
Project 1 chapter, no Test 1 slide, no coding exercise.

## Manifest

| file | from | role |
|---|---|---|
| 01-title | day 2 | kicker WEEK 3 · WEDNESDAY |
| 02-course-info | day 2 | the Week 3/4 clock, now column on Wednesday |
| 03-today | new | the routine ring with the silent first answer struck out and an orange shortcut from "open the question" to "discuss with your group"; plant: five questions, W03D1 then W03D2 |
| 04-open-w03d1 | new | divider · PART 1 OF 2 · open Peer Instruction W03D1 (three questions) |
| 06 / 06b | day 1 | VOTE 1 — the array search |
| 07 / 07b | day 1 | VOTE 2 — contains, C misspelled |
| 08 / 08b | day 1 | VOTE 3 — contains, C fixed |
| 09a-open-w03d2 | new | divider · PART 2 OF 2 · open Peer Instruction W03D2 (two questions) |
| 09 / 09b | day 2 (was 06/06b) | VOTE 4 — the gap; codewalk answer |
| 10 / 10b | new (10-vote-linear, 10b-walk-linear) | VOTE 5 — which ArrayBag operation still takes linear time (answer B, contains); the vote quotes the stem with O(n) in text over the vote 4 bag; the answer is a verdict board dealt D → C → A → B, each verdict lighting what it touches, B's sweep in maroon. Replaced 2026-09-08 after the live Runestone text showed W03D2 Q2 is this, not the F25 remove() question; 10-vote-remove/10b-walk-remove stay on disk, out of the manifest |
| 17-next-class | day 2 | the clock again, static |
| 99-closing | day 2 | dusk |

Day 2's four vote files were renamed (09/09b/10/10b) and their section ids, sids and
vote numbers changed with them, so their slide-local styles cannot collide with day 1's
06/06b/07/07b. The day 1 files were byte-for-byte copies; since then every vote slide gained a 5:00
discussion timer as its one step (js/timer.js and the `.timer` block in deck.css, this deck
only; `data-timer` is seconds, per slide), and on votes 2 and 3 the source's parentheses were
restored (`while ( !found && (i < numberOfEntries))`, `while ((i <= numberOfEntries))`) and
vote 3's heading aligned to Q2's "could not be used" — both edits made in day 1 as well.

## Open
- How the skipped first round is handled in Runestone's Peer+ console is the instructor's
  call; 03's notes say to tell the room before question 1.
- Timing: five questions in one hour is about eight minutes each including the answer; the
  timers are a uniform 5:00, which alone is 25 minutes — vote 1 is a straight trace, votes 2
  and 5 are where groups argue, so the per-slide `data-timer` values may want to differ.
- 17's notes say Test 1 is "Thursday September 24, in class"; this section meets Monday and
  Wednesday.
- Vote 5: "linear" is Week 5 vocabulary, glossed in two lines under the drawing; Runestone sets
  the O(n) as math — check it renders. Activity id unverified.
