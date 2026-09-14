# Week 4 · Day 1 — plan

Built 2026-09-12 for Monday Sep 14 (MW, NCB 320) and Tuesday Sep 15 (TR, Squires) —
one deck, both sections. Sources: the instructor's verbatim paste of Runestone
"Peer Instruction W04D1" (two questions), `~/Downloads/S26 Week 4 Day 1.pdf` (an F25 deck
by its metadata: ten pages, no linked-bag code, one array-like drawing of the chain),
`cs2114-schedule-fall2026.html` + `cs2114-deadline-schedule.csv`, and the PrairieLearn
course repo (`homeworks/04_linked_chains`, `contentPages/04_03_linked_bags`). Shared
css/js/assets/tools cloned from `week 3 - wednesday` and `week 3 - day 2/tools`.

## Through-line

**"A linked chain is objects pointing at objects — every operation is a rewiring you can
draw, and every bug is an arrow into the wrong box."**

- Part 1 · Rewiring a chain — what a `Link` is, then Vote 1: three `setNext` calls and
  one raw-field walk. The answer walk swings the arrows and leaves node 5 unreachable.
- Part 2 · Walking a chain — Vote 2: four loops that double every other value. The answer
  walk runs all four on a three-node chain; only A survives an odd length.
- Part 3 · A bag on a chain — `LinkedBag.add` puts the new node at the front in constant
  time; the Week 4 coding practice is nineteen more walks.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `WEEK 4 · DAY 1` |
| 01b-today | three chapter tabs: an arrow redirected · a figure stepping box to box · a bag with a chain inside → the captions are the divider titles |
| 02-course-info | the Week 4/5 clock: now band on Mon+Tue; Fri homework + CE 04; P1 D2 at your lab; 5.x modules Sunday; Week 5 rows; **Test 1 band Wed–Thu**; Canvas tiles → "Wednesday/Thursday we rehearse the exam browser" |
| 02b-ssd | SSD accommodations on Test 1: the letter in AIM, the seat in RegisterBlast by Fri Sep 18 (MW) / Mon Sep 21 (TR); SSD contact line |
| 03-chapter-1 | PART 1 OF 3 · Rewiring a chain |
| 04-node-anatomy | the first Link renders, then a walk down `class Link` member by member: the two fields washed in the box, the constructor makes a second Link (ringed, not linked), `setNext` links it (orange wash, null goes, arrow), `getNext` rings the compartment then the Link it refers to, `getData` reads, `setData` replaces the value; step 9 completes the chain 20→30→10→5 → "this is the chain in Vote 1" |
| 05-peer-plus | the routine ring, W04D1 wording → straight into Vote 1 |
| 07-vote-trace | VOTE 1, static: the stem, the chain it describes drawn as a row of Link boxes (the deck's addition; the question has no picture), the 8-line snippet, options A–E; two clocks — 2:30 vote on press 1, 4:00 discussion on press 2 |
| 07b-walk-trace | VOTE 1 · THE ANSWER: `p q r` pills, three swings, node 5 fades to stone, the `p.next.next` hop, verdict → "every setNext is one arrow moving" |
| 08-chapter-2 | PART 2 OF 3 · Walking a chain |
| 09-vote-double | VOTE 2, static: stem + four numbered code cards in a 2×2 grid; the same two clocks |
| 09b-walk-double | VOTE 2 · THE ANSWER: four lanes on `1→2→3`; B skips node 0, C leaves 3 alone, D throws; verdict → "any arbitrary chain = test the odd one" |
| 10-chapter-3 | PART 3 OF 3 · A bag on a chain |
| 11-linkedbag-add | `add` walked line by line: new node grows, its arrow draws to the old first, `firstNode` swings, the count strikes 3→4 → "so where does the cost move? (Week 5)" |
| 13-hw-reads | the homework as pointer moves, part 1: walk to the end · look one ahead · match by value · two pointers — one picture per press, the rule in the caption, problem numbers on the index |
| 13b-hw-writes | part 2: add after · remove · splice a chain in · rotate/reverse · the LinkedBag four — moved arrows orange, replaced arrows dashed, unreachable nodes stone → "pick five: one from each move you find hard" |
| 16-project-d3 | Project 1 Deliverable 3 (Week 5 lab) as a room scene: your group's presenter at a screen, the other groups at tables; the screen plays the four parts of the 10-minute talk and part 4 (GenAI) radiates to the room → "one thing the other groups do not know yet"; the brief is in the notes |
| 17-next-class | the same clock, static; caption: charged laptop + LockDown Browser installed for Wed/Thu |
| 99-closing | dusk |

## Slide by slide

- **02** — the W3D2 clock shifted one week. New idioms, both recorded in DECK-PROMPT §11:
  the `now` column is a **two-track band** (x 128–366, Mon+Tue) because this deck serves two
  lecture days; **Test 1** is a maroon-outlined band over Wed–Thu of Week 5 (x 1317–1554)
  labelled `Test 1 · in your lecture · Wed MW · Thu TR`, its own step (6), tiles moved to 7.
  4.x modules were due last night and are off the left edge — said in the notes.
- **04** — a walk through the Link class, not a static picture (instructor, 2026-09-12):
  the editor lists the members the questions use, one per line (signature and body on a
  line; the class in Runestone is Allman-style and 38 lines), the PC bar moves down them,
  and the drawing above shows what each member is or does — fields washed blue, reads
  ringed/washed blue, writes washed orange, via `:has(.cap--k.is-current)`. The first Link
  is on screen before the walk; n2 is made with data 3 so `setData(30)` has something to
  do and the chain still ends as Vote 1's. No textbook aliases (there is no textbook).
- **07** — stem verbatim as a `--t-small` paragraph across both columns (wednesday's
  `.lb__stem`), `.code-dense` editor left, `.opts` right. Static. Notes open "Answer: B".
- **07b** — the eight lines as `walkline`s under the PC bar; right, a 2×2 node scene
  (20 30 / 10 5, the chain wrapping like text) so the three rewired arrows have room:
  20→10 goes down, 30→null goes right, 10→30 goes up. Arrows are single cubic paths and
  **swing** via a CSS `d: path()` transition selected with `:has(.cap--k:not(.is-pending))`
  (the shipped idiom); node 5 turns stone at step 6; step 7 rings 20, 10, 30 in turn; the
  verdict strip closes.
- **09** — one-line h2 + the stem verbatim at `--t-small`; the four options as `.opts--code`
  cards in a 2×2 grid at `.code-tag` with gutter numbers, matching Runestone's numbered
  display. Header padding clears the timer.
- **09b** — four lanes (2×2), each a `1→2→3` chain with a `curr` pill that moves by node
  pitch on `:not(.is-pending)` states; values crossfade (no roll); D ends in a maroon cross.
  Steps are synchronised by loop iteration: start · first doubling · second move · third
  move · verdict + coda ("on Q1's four nodes C and D would have passed").
- **11** — `add` as Carrano/OpenDSA write it (`Node newNode = new Node(newEntry);
  newNode.next = firstNode; firstNode = newNode; numberOfEntries++; return true;`), the
  form module 4.3's video teaches; the page itself carries no code, so this is not quoted
  material. Skip live if peer instruction runs long — the notes say so.
- **13 / 13b** — the nineteen problems read from the PL repo (2026-09-13) and grouped by
  the pointer move each needs; captions carry the guard/edge case each spec names (the
  Plan review caught: look-ahead guard, null node/value in addAfterNode, firstNode removal,
  empty chains in splices, the wrap no-op when newHead is already first, 787's split node
  at (n-1)/2 hops). The class is `Node`/`firstNode` (the homework's), not `Link`/`head`.
  Both slides come from one generator script (the picture grammar) — the reads slide has
  4 steps, the writes 5; the index lists all nine on both.
- **02b** — SSD facts from ssd.vt.edu (2026-09-13); dates are exam − 3 business days per
  SSD's own table. The instructor's RegisterBlast deadlines are in the notes only.

## Translated, dropped, unverified

- Translated: "Project 1 is due on Tuesday" → P1 Deliverable 2 (Spec) at your Week 4 lab;
  "Lab 03 released" / "Project 2 gets released" → dropped (P2 starts Week 6); "Test 1 is
  next week" → kept, now with the section days (MW Wed Sep 23 / TR Thu Sep 24, instructor
  2026-09-12); the legacy "Class Business" and "Problem Solving Reflection" → not drawn.
- Dropped: the Peer+ pre-survey, the sample optional MCQ (moved to Day 2's chain recall
  with new values), "Work on assignments and we will walk around".
- Question text: Q1 (`vtcs2_linkedchains_tracing_09142025`) and Q2
  (`vtcs2_linkedchains_tracing_5_202507`) quoted from the instructor's paste. Q1's `Link`
  spells its parameters `dataIn/nextIn`, Q2's `data/next`; 04's code calls the constructor
  and `setNext` only, so neither spelling appears.
  Q2's options carry line numbers in Runestone; the cards keep the gutter numbers.
- Answers: Q1 = B (30; node 5 unreachable). Q2 = A (B starts at position 1; C skips the
  last node of an odd chain; D throws on it — both C and D pass on Q1's four nodes).
- Reported, not fixed (PL repo): x785's test file calls `partialReverse`, which its class
  lacks, so every submission fails to compile; raw `Node getNext()` in x735/x781–x788;
  `getfirstNode()`; x787's parenthetical; x681's `""` for an empty bag.
- Unverified: the PrairieLearn "Test #1 Practice" (PE1) open window — the assessment is
  untracked in the PL repo with `allowAccess: []` as of 2026-09-12; the Canvas assignment
  that launches it in LockDown Browser; whether Test 1 is 45 minutes (the 4.1 page says so
  for "quizzes"). Lab weekdays are in no source, so the project keeps the "your lab day"
  range.
