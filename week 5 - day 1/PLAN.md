# Week 5 · Day 1 — plan

Built 2026-09-20 for Monday Sep 21 (MW, NCB 320) and Tuesday Sep 22 (TR, Squires) —
one deck, both sections. Sources: the instructor's paste of Runestone "Peer Instruction
W05D1" (four questions; Q3's options came as a screenshot: O(1), O(n), O(log n), O(n²)) and
their instruction of 2026-09-20 to introduce complexity with step-by-step pseudocode
walkthroughs and to answer every vote the same way;
`~/Downloads/S26 Week 5 Day 1.pdf` (an F25 deck by its metadata, 16 pages: Course Info,
Class Review, Upcoming, one Efficiency line, four Peer+ screenshots — Q1's carries the
instructor's callout "Be careful here that we are referring to the case where the array
needs to be expanded" — the Stack and Bag cost tables, "CW – Week 5" X686, Upcoming);
the PrairieLearn repo (`homeworks/05_efficiency_stacks` = "Week 5: Efficiency & Stacks —
Coding Practice", x685/x686/x687, 10 pts each; `cpPractice/05_efficiency_stacks` whose
`u08q08_efficiency_arraybag_c` is Q1 verbatim with the key O(n), `u08q10_efficiency_
arraystack_c/_d` are Q2/Q3's twins with keys O(n)/O(1); the LinkedStack starter with
`topNode` + `numberOfEntries`; `clientFilesCourse/slides/BagsEfficiency.pdf` = the F25
bag table); `cs2114-schedule-fall2026.html` + `cs2114-deadline-schedule.csv`; the Week 4
decks for the clock, the two-clock vote slides, the DO/DON'T card and the ring. Shared
css/js/assets cloned from `week 4 - day 1` (its `code-walk.js`, `timer.js` and the
ligature fix in `deck.css` are the newest copies), `tools/` from `week 4 - day 2`.

## Through-line

**"Big-O counts the moves an operation makes as the data grows — and where you put the
top of a stack decides whether pop is one move or n."**

- Part 1 · Counting moves — the two shapes the room has already drawn (one write at any
  count; a sweep that grows with the count) get their names; then Vote 1: what does add
  cost when the array is not a fixed length? The answer walk grows the array: n copies,
  then the write.
- Part 2 · Where the top is — three ways to build a stack, then Votes 2, 3, 4: pop with
  the top at index 0 (shift everything: O(n)), pop with the top at the last occupied
  index (one move: O(1)), which pop is least efficient and why (index 0). The costs land
  in one table; the Week 5 homework is three LinkedStack walks.
- Part 3 · Next class is Test 1 — the rules once more, DO / DON'T, the same clock.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `WEEK 5 · DAY 1` |
| 01b-today | three chapter tabs: tally marks over an array row · a stack of boxes with an arrow at the top · the laptop with the ring → the captions are the divider titles |
| 02-course-info | the Week 5/6 clock: now band on Mon+Tue; **Test 1 band on Wed–Thu of this week, step 1**; Fri homework + CE 05; P1 D3 at your lab; 6.x modules Sunday; Week 6 rows (HW, CE 06, P2 D1 in the P2 mix, 7.x modules, Test 1 Redo band) → "next class is the test" |
| 03-chapter-1 | PART 1 OF 3 · Counting moves |
| 04-count-contains | COUNTING MOVES · A LOOP: Week 3's contains (option A) under the PC bar, gnu not in a bag of four; the loop body holds for four presses while one cell per press takes the maroon edge and a counter rolls 0 → 4; return false; then a bag of eight with 8 → "the moves grow with n: linear" |
| 04b-count-add | COUNTING MOVES · NO LOOP: the fixed-size add, three moves (compare, write, count) with the counter in blue; then a bag of nine with the same 3 → "n never enters it: constant" |
| 04c-count-pairs | COUNTING MOVES · A LOOP INSIDE A LOOP: a hasDuplicate with two loops; a 4×4 pair grid lights row by row (3 + 2 + 1), counter to 6; then the 8×8 grid with 28 → "more than four times: quadratic" |
| 04d-big-o | COUNTING MOVES · THE NAMES: the three counts on one graph of moves against n with dashed guides at n = 4 and n = 8 — flat (add, 3 · O(1)), straight rise (contains, n · O(n)), the curve that leaves the picture (hasDuplicate, ~n²/2 · O(n²)); last, the rule: keep the shape, drop the constants, name the worst case → "Vote 1: add, when the array is not a fixed length" |
| 05-peer-plus | the routine ring, W05D1 wording → straight into Vote 1 |
| 06-vote-grow | VOTE 1, static: the stem, a full ArrayBag drawn (length 6, count 6), a two-line gloss ("not a fixed length: the array can grow when it is full"), options A–D verbatim; two clocks |
| 06b-walk-grow | VOTE 1 · THE ANSWER: add + doubleCapacity walked under the PC bar (nine presses): the full check, a new array twice the length, the copy loop held for two presses while the six values travel down, `contents` swings to the new array and the old goes to garbage, the write, the count; a moves counter reaches 11; verdict → "with room, 3 moves; full, n copies first — Big-O names the worst case" |
| 07-chapter-2 | PART 2 OF 3 · Where the top is |
| 08-stack-tops | three columns, one per press: linked chain with topNode at the first node · array with the top at the last occupied index · array with the top at index 0 — all after push(A), push(B), push(C); no costs → "Votes 2, 3, 4: how many moves each pop takes" |
| 09-vote-top0 | VOTE 2, static: the stem, the array with the top at index 0, options verbatim; two clocks |
| 09b-walk-top0 | VOTE 2 · THE ANSWER: pop with a shift loop walked under the PC bar (eight presses): read stack[0], the loop held for four presses while D C B A each slide one cell left (real moves, the counter rolls), the count, the cleared slot; verdict → "seven moves, four of them the shift, and the shift is n − 1: O(n); push shifts too" |
| 10-vote-toplast | VOTE 3, static: the stem, the array with topIndex at the last occupied slot, options as Runestone sets them (math); two clocks |
| 10b-walk-toplast | VOTE 3 · THE ANSWER: Carrano's ArrayStack.pop walked (five presses): the empty check, the read, the cleared slot, topIndex's marker slides one cell left and crossfades 4 → 3; counter 4; verdict → "four moves at any n: O(1); push is the mirror" |
| 11-vote-least | VOTE 4, static: the stem, the three implementations as three small rows, options verbatim; two clocks |
| 11b-walk-least | VOTE 4 · THE ANSWER: the homework's LinkedStack.pop walked (peek reads C, the topNode arrow swings to B and C goes stone, the count), then a board of the three pops (A 3 moves, B 4, C n + 3, D no) and the verdict on C → "why: every other entry has to move up one; the shift is what grows" |
| 12-cost-table | the two F25 tables, rebuilt: Stack (push/pop/peek × array-top-last / linked) and Bag (add, contains, getFrequencyOf, remove(), remove(anEntry), toArray × fixed array / linked); footnote: the two O(n) exceptions the votes found |
| 13-hw-linkedstack | the Week 5 homework: the chain C→B→A under topNode and the class's fields, then three cards one per press — toString → "CBA", toArray → {C, B, A}, getBaseOfStack → A — signpost + "all three are one walk from topNode" |
| 14-chapter-3 | PART 3 OF 3 · Next class is Test 1 |
| 15-test-day | the rules as a checklist + DO / DON'T cards (W4D2's 13, trimmed: no SSD line, "tested last week"), Test 1 Redo Oct 1 |
| 17-next-class | the same clock, static; caption: next class is Test 1 — charged laptop, student ID, LockDown Browser |
| 99-closing | dusk |

## Slide by slide

- **02 / 17** — W4D1's clock one week on: the `now` band on Mon+Tue (x 128–366), and the
  Test 1 band now over **this** week's Wed–Thu (x 366–603), drawn as **step 1** so the room
  hears "next class" before the deadlines. Week 6 adds Project 2 · Deliverable 1 in the
  P2 accent (`color-mix(accent-1 50%, accent-3)`, W1D1's project coding) over "your Week 6
  lab", and a second dashed band over Wed–Thu of Week 6 for Test 1 Redo, labelled like the
  Test 1 band (instructor, 2026-09-20: the redo is the second class of Week 6 for each
  section, MW Wed Sep 30, TR Thu Oct 1). 5.x modules were due last night — notes.
- **04 / 04b / 04c / 04d** — the instructor asked (2026-09-20) for "a few slides introducing
  complexity with nice animations and pseudocode walkthroughs, step by step". Part 1 is
  therefore three counts and a picture: the same grammar on each — real code under the
  program-counter bar on the left, on the right the array the code touches, a display-size
  **moves counter that rolls** (the one place the deck allows a digit roll: a tally truly
  counts), and one caption per press — then the doubling test (a bag of 4, a bag of 8) at
  the end of each. 04 is Week 3's own contains (option A) with gnu not in the bag, so the
  count reaches n; 04b is the Week 3 fixed-size add, three moves in blue; 04c is a
  two-loop duplicate check drawn as the upper triangle of a pair grid (the deck's own
  method — Week 3 had no nested loop); 04d puts the three counts on one graph with dashed
  guides at n = 4 and n = 8 and names them. "Worst case" is said on 04 (not-there is the
  case shown) and again on 04d, because Votes 1 and 2 turn on it. 04c is marked
  skippable in its notes.
- **The loop walks** need a line to stay under the bar for several presses, which the
  step engine could not do (a frag is current on exactly one step). `js/deck.js` in this
  deck adds **`data-hold="M"`**: a `.frag[data-step=k][data-hold=M]` is `is-current` for
  steps k…M (and `reindex` counts holds toward maxStep). `code-walk.js` then keeps the PC
  bar on the held block. Used by 04 (four iterations), 04c (three), 06b (two), 09b (four).
- **The moves counter** is a shared component, `.moves` in `css/deck.css`: one
  `.heap-obj__field` old/new pair per increment, stacked in one grid cell, only the
  latest non-pending pair visible; `code-walk.js` rolls each pair's digits (manim's
  ChangeDecimalToValue). Blue (`.moves--ok`) for the counts that stay small, maroon for
  the ones that grow. It must sit inside a `.codewalk`.
- **06 / 06b** — Q1 is `u08q08_efficiency_arraybag_c` in the PL bank, key O(n); the F25
  callout ("the case where the array needs to be expanded") is the deck's gloss line, in
  the room's words, and the drawing shows the array full. 06b walks add AND the helper it
  calls (two methods in one editor at the tag size; `doubleCapacity` written with an
  explicit copy loop rather than Carrano's `Arrays.copyOf`, so the n is on screen); the
  two arrays are one SVG so the copy travel is exact (160 px straight down —
  TransformFromCopy), `contents` is one arrow that swings (`d: path()`), the old array
  goes to garbage. Week 3's vote called add one write "with the most efficient
  implementation"; the coda and notes reconcile the two: with room it is three moves, full
  it is n copies first, and Big-O names the worst case (amortized analysis is named in the
  notes as a later course's business).
- **08** — the module's three designs, all holding the same three pushes so the pictures
  are comparable; the course's own field names (`topNode` from the x685–x687 starter,
  `topIndex` as Carrano's ArrayStack, which `u08q11_arraystack_locations` describes as
  "top at the last occupied location"). No costs on the slide: they are the votes.
- **09 / 09b / 10 / 10b** — Q2 and Q3 are a pair (twins of `u08q10_efficiency_arraystack_c`
  and `_d`, keys O(n) and O(1)). Both answers are code under the bar with the counter:
  09b's pop is the deck's own (module 5.2 draws the top-at-0 design but ships no code) and
  its shift loop holds for four presses while D C B A slide one cell left, one per press
  (each value is an opaque box inside its cell so it covers what it overwrites); 10b is
  Carrano's ArrayStack.pop, and the only thing that moves is the `topIndex` marker (one
  pitch left, 4 → 3 crossfaded — a replaced value, no roll). Both end on a `.verdict`.
- **11 / 11b** — Q4 has no PL twin; C follows from Q2 and Q3. 11's drawing is 08's three
  designs small, in the options' order. 11b walks the one pop not yet walked — the
  homework's own `LinkedStack.pop` (`topNode`, `numberOfEntries`) — with the topNode arrow
  swinging (`d: path()`) and the popped node going stone; then a board of the three counts
  (3 · 4 · n + 3) and the verdict on C, with the "why" the question asks for as the coda.
- **12** — F25's tables with `contains(anEntry)` added (Week 3's vote) and column heads
  that say where the top is; O(1) blue, O(n) maroon, the two O(n) exceptions in a footnote.
- **13** — the homework is three problems, not nineteen, so cards instead of a trail; the
  results are for the drawn stack (C on top) so the room can check them by eye.
- **15** — W4D2's 13 with the instructor's post-build wording ("On Canvas, inside LockDown
  Browser"); the SSD line is dropped (both RegisterBlast deadlines have passed by the time
  each section sees this — a note for after class instead); "~15 questions" from the
  instructor's edit of W4D2 04; `[45 minutes]` stays a placeholder.
- Timers: every vote runs W4D1's two rings (vote 2:30 on press 1, discussion 4:00 on
  press 2). Four votes at that pace is ~26 minutes and Part 1 is now four walks, so the
  hour is full: Votes 2 and 3 are a pair (the notes say the third can be pressed through
  early), and 04c, 08 and 12 are marked skippable in their notes.

## Translated, dropped, unverified

- Translated: "Lab 05 is due this week / Post Lab 05 – Drawing UML Diagram" → gone (no lab
  deliverables in F26; CE 05 Ice Cream Stack is Friday); "Start Working on Project 2 (Due
  next week)" → Project 2 Deliverable 1 at your Week 6 lab, teams re-form; "Class Review
  Till Now / TRIAL QUIZ" → dropped (the review was W4D2; the trial quiz ran there);
  "Upcoming (Week 5, Week 6): Stacks – Lab 05, Lab 06; Ethics; Design – PostLab 05" →
  the clock's Week 6 row; "CW – Week 5 X686" → the Week 5 homework (x685, x686, x687 on
  PrairieLearn); "Next Class – Test 1" → kept, with the section days; "submit Lab 5 to
  webCAT using Eclipse", "interview activity in Lab", "no lab week 7, weeks 11 & 12
  required attendance" → dropped (not F26, or unverified).
- Question text: Q1 `vtcs2_efficiency_dynamicArrays`, Q2 `vtcs2_efficiency_stacks_2`,
  Q3 `vtcs2_efficiency_stacks_3_202507`, Q4 `vtcs2_efficiency_stacks_4_202507`, quoted
  from the paste; Q1/Q2 spell O(n^2) with a caret, Q3 sets its options as math (O(n²)),
  Q4 sets `pop()` in code — kept as each shows it. Q2's stem has no comma before "what".
- Answers: Q1 = B (PL key); Q2 = B (PL twin `_c`); Q3 = A (PL twin `_d`); Q4 = C.
- **Test 1 delivery**: the instructor's post-build edits to W4D2 (13, 14) replaced
  "PrairieLearn" with "Canvas" — "On Canvas, inside LockDown Browser", "Canvas › Trial
  quiz … access code TrialDuringClass", "Inside it: Canvas › Test #1 Practice". This deck
  follows those edits. DECK-PROMPT §11 and the memory still say PrairieLearn behind
  Canvas — to be reconciled by the instructor.
- **Unverified / placeholders** (orange in Studio): `[45 minutes]` on 15 (the 4.1 page's
  figure);
  `topIndex` as the course ArrayStack's field name (the module's slides are images; Carrano's
  name); lab weekdays are in no source, so projects keep the "your lab day" range.

## Status — 2026-09-20, before the instructor's review

- 25 slides written; `add_sids.py` run; `lint.py` clean on all 25.
- **The Chromium layout sweep did not run**: `chromium --headless=new --dump-dom` returned
  no DOM at all and timed out (5 min), and further chromium runs were declined. The budget
  was checked by arithmetic instead (PIL advances: JetBrains Mono 16.8 px/char at 28 px,
  12.6 at 21 px; the editor's chrome is 70 px; body 685 px under kicker + h2, 752 under a
  bare h2; captions at 36 px wrap at ≈ 19 px/char). Fixes made from that: editors widened
  to clear their longest line (04 → 880, 04c → 800, 06b → 800, 09b → 960 with 92 px cells,
  10b → 780), 11b's separate `.verdict` strip dropped (its board is the verdict; the strip
  ran the left column 40 px over), 13's signpost moved under the left column, two plant
  captions trimmed to three lines. Treat every slack figure as **unmeasured** — open the
  deck in Studio and look at 06b, 11b, 13 and 15 first.
- `js/deck.js` (`data-hold`) and `css/deck.css` (`.moves`) differ from every earlier deck;
  DECK-PROMPT §0 now says to clone this deck's copies.
- Test 1 platform: the slides say Canvas + LockDown Browser, following the instructor's
  W4D2 edits; `[45 minutes]` is an orange placeholder.

## Review round 1 — 2026-09-20 (instructor, by on-screen position)

- 01b + dividers: chapter titles made plain ("Big-O: count the moves, then watch them
  grow" · "Stacks: where the top is decides what pop costs" · "Test 1 is next class").
- 04, 04b, 04c: variable names shortened (a, n, x) so the code sits at the small size;
  the array (04, 04b) and the pair grid (04c) now GROW IN PLACE instead of a second copy
  appearing, and the walkthrough runs a second time on the same lines. That needed
  `data-also="…"` in `js/deck.js` (a frag is current again at the listed steps) next
  to `data-hold`; the moves counter resets by a `data-roll="off"` pair (crossfade) and
  rolls again. 04: 9 steps; 04b: 11; 04c: 8 (the 8×8 grid is one CSS grid whose extra
  tracks animate from 0).
- 04d: plot widened to x 240–1440, axis label end-anchored so it no longer shares a
  baseline with the n = 8 guide label; line labels carry the count as a second line.
- 06, 09, 10, 11 (the vote slides): rebuilt on one shared layout, `deck.css .vote`,
  consolidated from three agent design passes — A "the stem is the headline" (three
  lines of maroon display type; bottom cards wrap Vote 4's options to four lines),
  B "two panels" (paraphrase h2, stem as a muted lede, drawing left, options as
  lettered rows with maroon discs; a tall empty plate), C "poster" (stem as the
  heading, 140 px cells, chips strip; needs a 2×2 fallback for long options). Kept:
  B's structure and option rows, A/C's larger cells (128) and single stroke, no plate;
  gloss lines cut into the notes. Specs and drafts are in the session scratchpad
  (`vote-design-{A,B,C}.{md,html}`).
- 09b: the sliding value no longer carries an opaque box; the overwritten value fades
  as the mover arrives.
- 11b: the board fits the 700 px column (short design names, one badge per row).
- 12 ("slide 12" read as the file prefix; position 12 is a divider): costs as badges,
  short column heads with a sub-line, exceptions as two badge-led lines.
