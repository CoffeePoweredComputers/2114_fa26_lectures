# Week 7 · Day 2 — plan

Built 2026-10-04 for Wednesday Oct 7 (MW, NCB 320) and Thursday Oct 8 (TR, Squires): one
deck, both sections. Friday Oct 9 is Fall Break; the next class is Week 8 Day 1 (Queues).
Shared css/js/assets/tools cloned from `week 6 - day 1` (the newest copies). The Week 7
Day 1 deck (built in parallel) introduced recursion with `fact(3)`: frames on the call
stack, the caller waiting on its call line, returns popping frames, StackOverflowError
without a base case, and one vote (`countDown`). This deck does not repeat any of that.

Sources: `~/Projects/pl-vt-cs2114` — `questions/dataStructures/recursion/u09q03_recursion_linkedchain_{a,b,c,d}`
(twins of Vote 3), `questions/contentPages/07_03_recursion/section_04` (a Panopto video
with `clientFilesCourse/slides/DisplayBagsRecursively.pdf`: `displayChain(Node<T> curr)`,
`firstNode`, `curr.getData()`, `curr.getNext()`, the forward and backward versions),
`questions/codingPractice/recursive_*` (the five homework problems),
`courseInstances/Fall2026/assessments/homeworks/07_recursion/infoAssessment.json`;
`~/Downloads/cs2114-deadline-schedule.csv`. Vote text: the Runestone paste in the build
brief (2026-10-04).

## Through-line

**"A line above the recursive call runs on the way in; a line below it runs on the way
back. That one fact answers all three of today's questions."**

- Part 1 · Before the call and after it: when does each line run? — `count(3)` walked
  twice, the print above the call and then below it; then Votes 1 and 2.
- Part 2 · Recursion on a linked chain: this node, then the rest — `show(curr)` walked
  on a three-node chain; then Vote 3 (`displayChain`, print below the call).
- Part 3 · Writing one: when to stop, how to get smaller — three questions write
  `count(Node curr)` one line each, then it runs; then the homework.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `CS 2114 · FALL 2026 · WEEK 7 · DAY 2` |
| 01b-today | three chapter tabs: a stack of frames with an arrow down on one side and up on the other · a chain with its first node orange and the rest bracketed · three code lines led by orange discs → the captions are the divider titles |
| 02-course-info | (manifest entry only; the reviewer derives it from the Day 1 deck's clock) |
| 03-chapter-1 | PART 1 OF 3 · Before the call and after it: when does each line run? |
| 04-walk-before | concept intro: `count(n)` with `print(n);` above the call, `count(3)` walked: four frames grow, output `3 2 1`, the frames come off with nothing left to do → "a line above the call runs on the way in" |
| 04b-walk-after | the same editor; `print(n);` moves below the call (the two lines swap places) and the same walk runs again: four frames grow with nothing printed, the prints happen as frames come off, output `1 2 3` → "above the call = on the way in; below the call = on the way back" |
| 05-peer-plus | the routine ring, assignment `Peer Instruction W07D2`; takeaway "Three questions: two print orders, then a chain printed by recursion." |
| 06-vote-entry | VOTE 1, static: `example(int x)`, Entry above the call, Exit below it; four print orders; two clocks |
| 06b-walk-entry | VOTE 1 · THE ANSWER: one press per printed line; three frames grow (Entry 3, 2, 1), at x = 1 the `if` is false and Exit 1 prints, then each frame below resumes after the call and prints its Exit; captions name what C, B and D assume; `.verdict` A → "Entry lines on the way in, Exit lines on the way back" |
| 07-vote-mirror | VOTE 2, static: `mirror(int n)`, a print on both sides of the call, step n − 2; two clocks |
| 07b-walk-mirror | VOTE 2 · THE ANSWER: frames mirror(4), mirror(2), mirror(0); the output plate fills `4 2 0 2 4` one token per press, the base case printing the middle 0; captions dismiss B, C, D; `.verdict` A → "the same number twice: once on the way in, once on the way back" |
| 08-chapter-2 | PART 2 OF 3 · Recursion on a linked chain: this node, then the rest |
| 09-walk-chain | concept intro: `show(Node curr)` prints then recurses on `curr.getNext()`, walked on A → B → C → null; a blue ring marks the running frame's node and moves down the chain; output `A B C` → "a chain is one node plus a shorter chain; `null` is the empty chain, so `curr == null` is the base case" |
| 10-vote-chain | VOTE 3, static: the fields and `displayChain` verbatim in two editors; In order / In reverse order / Neither; two clocks |
| 10b-walk-chain | VOTE 3 · THE ANSWER: the same chain and frames; calls go down to `curr == null` (nothing to do), the prints happen on the way back: C, B, A; `.verdict` B → "the line you saw on 09, moved below the call" |
| 11-chapter-3 | PART 3 OF 3 · Writing one: when to stop, how to get smaller |
| 12-write-count | the three questions, one per press, each adding its line to `int count(Node curr)` (`walkline--new`); then `count(A)` runs on the chain and the answers come back up as blue pills: 0, 1, 2, 3 → "ask the three questions in order and the method writes itself" |
| 13-hw-recursion | WEEK 7 HOMEWORK: the three questions as a reference card, then five cards (title, signature, which question is the hard one), one per press; the signpost → "best three of five count, due Friday" |
| 17-next-class | (manifest entry only; the reviewer derives it from the Day 1 deck's clock) |
| 99-closing | dusk |

## Slide by slide

- **The call-stack grammar (04, 04b, 06b, 07b, 09, 10b, 12; the Day 1 deck uses the
  same one).** One SVG in canvas px on the right. A frame is a 440 × 88 rounded rect at a
  96 px pitch, top-up: the call in mono on the left, its local on the right (`n = 3`,
  or `curr` with a blue arrow to a small box naming its node), a stone note `waiting on
  line k` under the call while it waits. The running frame (the top) is an orange 18%
  tint with an orange stroke; waiting frames are `--bg-1` with an `--fg-1` stroke. A new
  frame grows from centre; a frame that returns fades out. State changes are keyed to
  the caption frags with `:has(.cap--k:not(.is-pending))`, rules in step order so the
  latest wins and a back-step reverses them. The first call's frame grows with the PC on
  its first line; every later frame grows on the press where the PC sits on the
  caller's call line. Printed output is a `--paper` plate labelled `output`, one token
  per press (plain fade). Returned values (12 only) are blue pills that appear in the
  frame that returns and travel 96 px down into the frame below (a real move), then fade
  when that frame returns in turn. No maroon: nothing fails today.
- **04 / 04b (split).** One slide would have been 21 presses, so the walk is two slides
  as the brief allowed. 04: ten presses (the call, then print / call pairs, the base
  case, the three frames finishing with nothing left to do, the rule). 04b: eleven
  presses: step 1 swaps lines 3 and 4 in place (the two code spans translate one line
  height, 48 px, in opposite directions; the gutter numbers stay), then the same walk
  with the prints on the way back. The PC uses `data-also` for every revisit of a line.
  `print(n);` is pseudocode, as in the brief; the notes say it stands for
  `System.out.print`.
- **05.** W6D1's ring; only the week, the assignment name, the desc and the takeaway changed.
- **06 / 07 / 10 (votes).** W6D1 05b's layout: the stem's first sentence as the muted
  lede, the code in an editor on the left at the dense size, the question sentence above
  the options on the right (the Runestone order: lead-in, code, question), options with
  maroon key discs. The two clocks are copied from 05b (1:30 vote, 2:30 discuss). On 10
  the stem's "Given fields:" and "And the following code:" are the two editor bars, so
  the stem is quoted in reading order without two extra lines.
- **06b / 07b.** The method under the PC bar at `code-mid`, frames on the right with the
  output plate beside them, one caption per press under the drawing, the verdict across
  the full width (Vote 1's options are about 55 characters, wider than the left column).
- **09 / 10b.** The chain drawn as three Node boxes (`data | next`, 150 × 80, W4D1
  grammar) and `null` in stone, above the frames; frame locals read `curr` with a blue
  arrow to a small box naming the node (`A`, `B`, `C`) or the word `null`. A blue ring
  around the running frame's node travels along the chain (a real move) as calls go in
  and come back. 09's method is named `show` so Vote 3 is not answered in advance; the
  two differ only in where the print sits. Field names follow the 7.3 module's video
  slides (`curr`, `getData()`, `getNext()`, `firstNode`).
- **12.** Example chosen so it is none of the five homework problems: count the nodes of
  a chain. The answer line is split (`int rest = count(curr.getNext());` then
  `return 1 + rest;`) so question 2 and question 3 each add one line. The run uses the
  same chain; the final pill (3) drops below the stack to a `returned` slot.
- **13.** The W5D1 homework-card grammar adapted to five problems: a 3 × 2 grid of
  tiles; the first tile is the three questions (on from the start), then one problem per
  press in the order of the assessment (power, countdownList, reverse, arrayToString,
  sumFrom). Each card: the PL title, the signature without `public static`, and an
  orange question number with the part to think hardest about, phrased from the problem
  statement itself (no solution code).

## Translated, dropped, unverified

- **Runestone keys are ASSUMED (by tracing) for all three votes**: Vote 1 A (Entry 3,
  Entry 2, Entry 1, Exit 1, Exit 2, Exit 3), Vote 2 A (4 2 0 2 4), Vote 3 B (in reverse
  order). Confirm in Runestone's results view before class. For Vote 3 the PL twins only
  partly confirm: `u09q03_recursion_linkedchain_c` (print above the call) is keyed "In
  order", which agrees; `_a` is keyed "In reverse order" but its code as written (`if
  (curr != null) displayChain(...); else System.out.println(curr.getData());`) prints
  nothing useful and would throw on `null`, so its key looks like it belongs to the
  braced version on the slide; `_d`'s key ("In reverse order") also looks wrong for its
  code (it prints only the last node). Flag to the instructor; not changed here.
- The assignment name `Peer Instruction W07D2`, the question order (1 = example, 2 =
  mirror, 3 = displayChain) and the Runestone activity ids are from the brief, not seen
  in Runestone.
- Homework "Week 7: Recursion — Coding Practice" is due Fri Oct 9 11:59 PM by the
  deadline CSV and the assessment's `allowAccess` (end 2026-10-09T23:59:59). That date is
  Fall Break; stated as written, not corrected. Five problems at 10 points each, best
  three count (`bestQuestions: 3`). A credit-0 window stays open to Dec 31 (practice
  after the deadline); not on the slide.
- 02 and 17 are not written here: the reviewer derives them from the Day 1 deck's clock.
  Project 2 is "Project 2 · Linked Chains + Generics" on Canvas; D2 (Spec · declare the
  generic type) is due at the Week 7 lab (schedule page).
- `print(n)` on 04/04b and `print(curr.getData())` on 09 are pseudocode for
  `System.out.print`, kept short so the code reads from the back row.

## Status — 2026-10-04, first build

- Slides written for every manifest entry except 02 and 17 (18 files). `add_sids.py` run
  on the new ones; `lint.py` clean on all 18. Sweep (`timeout -k 5 150 tools/measure/run.sh`,
  run with a temporary manifest that left out 02 and 17, then restored): slack 01b 110 ·
  04 84 · 04b 84 · 05 13 (inherited from W6D1's ring, same figure there) · 06 104 · 06b 53
  · 07 104 · 07b 85 · 09 128 · 10 154 · 10b 104 · 12 86 · 13 0 (the card rows are `1fr`
  and fill the frame by design); no overflow. The vote slides' clocks are reported as
  "over" because they sit in the head band, as on every W6D1 vote slide.
- Sizing changes after the first sweep: 06's options at the micro size, one line each
  (were two lines at the small size; 6 px of slack); 06b's "call stack" label moved beside
  the base line and the step-9 caption cut to two lines (the four-row verdict ran 29 px
  over); 12's "returned" label shortened (ran 31 px past the right edge); 13's signpost
  lost "the best 3 of 5 count" (it is in the heading) and the cards their extra padding
  (81 px over).
- File names differ from the brief: `04-walk-before` + `04b-walk-after` (the walk was split,
  as allowed), `12-write-count` (the example counts nodes; array sum is a homework problem).
- Not committed (`git add "week 7 - day 2"` when asked; never `-A`).

## Review — 2026-10-04 (second pass, after the build)

- `02-course-info` and `17-next-class` written: copies of the Day 1 deck's with the `now`
  band on Wed–Thu (x 366–603, label at 485), the notes for the last class before Fall
  Break, and 17's caption "Next class is after Fall Break: queues. The 8.1 module is due
  Sunday." Edit Day 1's clock first, then re-derive.
- `09`, `10b`, `12`: the word `null` is centred at x 705 so the blue ring sits evenly
  around it (it was 22 px left of the ring's centre).
- Notes on `01b`, `04`, `05` said "Monday's"; they now say "last class's" (the TR section
  had Day 1 on Tuesday).
- Sweep after the review, all 20 slides: no overflow; 02 and 17 slack 36, the rest as in
  the Status block.
