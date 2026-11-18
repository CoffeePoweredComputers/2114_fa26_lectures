# Week 10 · Day 1 — plan

Planned 2026-10-24 for Monday Oct 26 (MW, NCB 320) and Tuesday Oct 27 (TR, Squires): one
deck, both sections. The next class for each section is Test 2. Shared css/js/assets/tools
were cloned from `week 9 - day 2`; the manifest is empty until Builder A fills it.
Sources: the shared brief (`w10d1-brief.md`); the Runestone paste "Peer Instruction W10D1"
(three questions, quoted in the brief); `DECK-PROMPT.md`; the PL repo
(`~/Projects/pl-vt-cs2114`: the 10.1 info page, `practiceExams/test2/infoAssessment.json`
with its 19 slots, the slot stems under `questions/practiceExams/test2/pNN_*`, the twins
`u11q08_iterator_efficiency_a` and `u12q07_insertnode_b`, `homeworks/10_sorting_iterators`);
`~/Downloads/cs2114-deadline-schedule.csv` (Week 11 homework row). Never
`canvas-banks/*`.

## Through-line

**"Test 2 asks about the array and linked-chain implementations the room has already
drawn; today's three votes count what a walk down a chain costs when it is repeated, when
it has to stop one node early, and when a loop sits inside a loop."**

| part | title (divider and tab) | slides |
|---|---|---|
| 1 | What Test 2 asks | 04 test map · 05 practice pointer |
| 2 | Three votes about what a loop costs | 06b peer-plus · 07/07b · 08/08b · 09/09b |
| 3 | Test 2 is next class | 11 rules · 12 your questions |

Q1 and Q3 both end on the sum 1 + 2 + … + n; 09b names that link. Q2 is the walk that
stops on the node before, which W9D2 08b used for remove(p).

## Manifest

| file | owner | role |
|---|---|---|
| 01-title | A | title card; kicker `CS 2114 · FALL 2026 · WEEK 10 · DAY 1` (copy W9D2 01) |
| 01b-today | A | three tabs (W9D2 01b grammar): a 3 × 2 board of small cards · a chain with a ring and a tally · the laptop with a ring; captions = the three divider titles |
| 02-course-info | A | the Week 10/11 clock; Test 2 band on THIS week's Wed–Thu as step 1; Redo band on Week 11; → "next class is the test" |
| 02c-bridge-lists | A | FROM WEEK 9 TO WEEK 10: last week's getNodeAt walk beside what today does with it; → the question for Vote 1, unanswered |
| 03-chapter-1 | A | PART 1 OF 3 · What Test 2 asks |
| 04-test-map | A | "~19 questions, six topics": six rows, one per press, 19 cards with one test-term pill each; → "Test 1's topics can come back" |
| 05-practice-pointer | A | signpost PrairieLearn › Assessments › Test #2 Practice, four facts; → "the number on each card is the slot in the practice" |
| 06-chapter-2 | A | PART 2 OF 3 · Three votes about what a loop costs |
| 06b-peer-plus | B | the routine ring, `Peer Instruction W10D1`; plant: "The three questions are about what a loop over a chain or an array costs." |
| 07-vote-getloop | B | VOTE 1, static, clocks: the stem verbatim, a four-node chain with firstNode on the left, options A–D |
| 07b-walk-getloop | B | VOTE 1 · THE ANSWER: get(i) under the PC bar, one ring per call walking from A, a tally 1 + 2 + 3 + 4 and a hop counter to 10; → verdict D |
| 08-vote-sortedinsert | B | VOTE 2, static, clocks: the stem verbatim without "Q-1: ", a sorted chain 3 → 7 → 12 → 20 with a loose node 10, options A–D (`--long`) |
| 08b-walk-sortedinsert | B | VOTE 2 · THE ANSWER: the runner walk (p, c) inserts 10; then the look-ahead lines; then foreach and reverse traversal fail on the drawing; → verdict B and C |
| 09-vote-pairs | B | VOTE 3, static, clocks: "Consider the following program:" + the five lines in an editor, options A–D |
| 09b-walk-pairs | B | VOTE 3 · THE ANSWER: W5D1 04c's grid with the diagonal included, 4 + 3 + 2 + 1 = 10, grown to 8 × 8 = 36; → verdict D, "the same sum as Vote 1" |
| 10-chapter-3 | A | PART 3 OF 3 · Test 2 is next class |
| 11-test-day | A | the rules checklist + DO / DON'T cards (W5D1 15 with Test 2's facts), Redo line |
| 12-questions | A | the six map topics as chips + "anything else"; Piazza line (W4D2 15) |
| 17-next-class | A | the same clock, static; caption: next class is Test 2 |
| 99-closing | A | dusk (copy) |

File numbers are sort keys; the manifest order is the order on screen. No SSD slide (both
RegisterBlast deadlines have passed; 11's notes carry the after-class line).

## Slide by slide

- **01b.** Three columns that GrowFromCenter one per step. Drawing 1: six small rounded
  cards in a 3 × 2 board, one card orange-edged. Drawing 2: four Link boxes with a blue ring
  on the third and three tally strokes above. Drawing 3: W5D1 01b's laptop with the ring.
  Captions are the divider titles above. Notes: "Part 1 is the map and where the practice
  is. Part 2 is three votes. Part 3 is the rules, then questions."
- **02 / 17.** W9D2's clock moved one week: `now` band Mon–Tue (x 128–366, `wk__cta` at
  247). Step 1 the Test 2 band on THIS week's Wed–Thu (x 366–603), drawn before the bars,
  labels `Test 2` / `in lecture` / `Wed MW` / `Thu TR` (three micro lines as W9D2). Step 2
  the Canvas bracket: `Week 10 · this week`, `Week 11 · next week`, `Week 12 →`. Step 3 the
  Week 10 homework "Week 10: Sorting & Iterators" (blue) and "CE 10 · DLL" (maroon) to the
  Friday pole (Oct 30). Step 4 Project 3 · Deliverable 1 in P3 blue (`wk__ink--p3`, as
  W9D2 drew it), solid Monday and fading Tue–Fri over "your lab day"; the label says
  `Project 3 · Deliverable 1`, the caption says it is the scope. Step 5 "11.2 + 11.3
  modules · due Sunday evening" (blue) to the Sunday pole at the boundary (Nov 1). Step 6
  Week 11 on the same rows: homework "Week 11: Sorted Lists" to the Friday pole (Nov 6;
  the CSV has this row); CE 11 `[TBD: research]`; a project row `[TBD: research]`; a
  modules bar `[TBD: research; the CSV lists nothing due Sun Nov 8]`; and the Redo band
  on Week 11's Wed–Thu (x 1317–1554) drawn like W5D1's: `Test 2` / `Redo` (`.wk__redo`) /
  `in lecture` / `Wed MW` / `Thu TR`. Step 7 the two tiles. Captions: one sentence each,
  measured in Liberation Serif at 36 px, under 1,568 px. 17 is the same SVG static with
  the caption "Next class is Test 2: charged laptop, student ID, LockDown Browser." Notes
  say "same clock as 02". Poles must be `<path d="M722 790 V568">` with `pathLength`, not
  `<line>` (cross-browser rule); W9D2's file uses `<line>`, so convert every pole and range.
- **02c.** One SVG 1664 × 260 in W9D2 08b's grammar. Left: a five-node chain A–E with
  firstNode and lastNode; a ring labelled `curr` moves A → D on press 1 (three pitches,
  translateX 498). Caption 1: "Last week, remove(p) walked from firstNode to the node
  before position p. getNodeAt(3) visited four nodes." Press 2: on the right, a stone
  card with the two lines `get(i)` and `getNodeAt(i)` in mono and the caption "get(i) is
  the same walk, and Test 2 asks what that walk costs." Press 3, in display maroon: "A loop
  calls get(0), get(1), … on this chain. What does the whole loop cost?" The question is
  Vote 1's; nothing on the slide answers it.
- **04 (the test map).** `h2` "~19 questions, six topics", no kicker, no points (the
  instructor deleted them from W4D2's map). Layout: six rows, each a region. Row = the
  region name (display, `--t-small`, maroon, 284 px column) + a 4-column card grid (cards
  325 px, gap 16; short rows leave columns empty). Card = two mono lines at `--t-micro`
  (28): line 1 the slot number in `--fg-1` then the label in `--fg-0`; line 2 ONE pill: the
  test term in mono `--t-micro`, `--accent-2` text on
  `color-mix(in srgb, var(--accent-2) 14%, var(--bg-0))`, padding 0 12 px, radius `--r-3`.
  Card padding 8 × 8, height 92 (2 × 38 + 16). Budget: 6 × 92 + 5 × 8 gaps = 592; +24; a
  two-line caption 98 → 714 of the 752 under a bare h2; slack 38 (≥ 24). Card text: label
  with its number ≤ 18 mono characters (302 px of a 309 inner); a pill ≤ 16 characters
  (269 + 24 padding); two pills in one card only when both texts total ≤ 12 characters.
  Steps: 1–6 one row per press (the row GrowsFromCenter; its pills fade in after it on a
  `--i` stagger of .12 s); the caption fades in with step 6. Caption: "Test 1's topics can
  come back. Generics 2 and UML class diagrams are on the 10.1 list and have no practice
  question." Notes list the formats (multiple choice, checkbox, card select) and say the
  numbers are the practice's slot numbers.

  The regions, their cards and the pill terms (every term marked **to verify in
  research**: a researcher reads all alternatives of the slot and confirms the word is in
  the stem or replaces it). Second terms are the fallback if the first fails:

  | row | region (10.1 topics) | slot · label (≤ 18 chars) | pill (fallback) |
  |---|---|---|---|
  | 1 | Bags on arrays (Bags; arrays) | 19 bag array | `new Object[]` (`capacity`) |
  | | | 12 bag contains | `getIndexOf` (`numberOfEntries`) |
  | | | 13 bag remove | `removeEntry` (`contents`) |
  | | | 6 bag cost | `O(n)` (`worst case`) |
  | 2 | Stacks (Stacks) | 10 stack trace | `pop()` (`push`) |
  | | | 15 stack toString | `size() - 1` (`index 0`) |
  | | | 7 stack cost | `top at index 0` (`O(1)`) |
  | 3 | Recursion (Recursion) | 3 count the calls | `calls itself` (`base case`) |
  | | | 9 print a chain | `after the call` (`reverse order`) |
  | 4 | Queues and deques (Queues; Deques) | 2 queue indices | `frontIndex` (`% length`) |
  | | | 11 deque trace | `addToFront` (`removeBack`) |
  | | | 17 deque add | `lastNode` (`size`) |
  | | | 16 deque remove | `getPreviousNode` (`one mistake`) |
  | 5 | Linked chains and lists (Lists; linked chains) | 4 chain loop | `curr.next` (`!= null`) |
  | | | 5 chain surgery | `new Node(d, n)` (`unreachable`) |
  | | | 14 remove a node | `firstNode` (`node before`) |
  | | | 18 list bug | `which line` (`size`) |
  | 6 | ADTs and tests (UML hierarchy; code coverage) | 1 which ADT | `Deque` (`Bag`) |
  | | | 8 a covering test | `assertEquals` (`every branch`) |

  Slot numbers are the practice assessment's (1–19; its folders are p01–p20 with p08 and
  p11 missing, and slot 8 reuses `practiceExams/test1/p16`). Row 6's name is the one
  place the 10.1 list and the practice differ: the practice has no generics or UML slot,
  so the row is named for what it holds and the caption says the rest.
- **05.** W4D2 11's signpost card (`PrairieLearn › Assessments › Test #2 Practice`) at the
  top; under it four lines at `--t-small`: open now until Dec 31 · 45-minute limit, like
  the test · a fresh set of 19 questions each attempt · not for credit. Plant in maroon:
  "Run it tonight. The number on each card of the map is the question's slot in the
  practice." Static. Notes: no in-class run; the practice is the same shape as the test,
  not the test.
- **06b.** W9D2 06 with `Week 10` / `Peer Instruction W10D1` and the plant above. Notes:
  three questions; Q2 is choose-all-that-apply.
- **07 (Vote 1).** `.vote` layout (deck.css): paraphrase h2 "What does a loop of get(i)
  calls cost on a linked list?", the stem verbatim as `.vote__stem` (keep "get(0), get(1),
  …, get(n)"), left panel one SVG 870 × 260: a four-node chain A–D with firstNode and the
  stone line `get(0)  get(1)  get(2)  get(3)` under the nodes (points at the list, not at
  an option); right: options A–D in mono at `--t-body` with 56 px discs as W9D2 08. Two
  clocks (`timer--vote` 90 s, `timer--discuss` 150 s, as the model). Notes open
  "Answer: D — O(n²) [key from the PL twin u11q08_iterator_efficiency_a; confirm in
  Runestone's results view]".
- **07b.** `grid--code code-mid`: editor 665 px (longest line 31 characters) with
  `for (int i = 0; i < n; i++)` / `    x = list.get(i);` / blank / `T get(int i) {` /
  `    Node c = firstNode;` / `    for (int k = 0; k < i; k++)` / `        c = c.getNext();`
  / `    return c.getData();` / `}`. The PC bar sits on the two walking lines (6–7),
  `data-step="1" data-hold="4"`; the client line is static and the caption names the call.
  Right (951 px): one SVG, the chain A–D (130 × 76 boxes, 166 pitch, firstNode pill); four
  rings `ring--1`…`ring--4`, each a `<g>` at A that is invisible until its step, then
  visible and translated (k − 1) × 166 px (a real move; the previous ring fades on the
  next step; back-steps reverse because every state is a
  `:has(.cap--k:not(.is-pending))` rule). Under the SVG a tally line in mono at
  `--t-small`: `1`, `+ 2`, `+ 3`, `+ 4` appear one per press, `= 10` on press 5. Beside it
  the `.moves` counter labelled "nodes visited": 1 → 3 → 6 → 10 (a tally; the roll is
  allowed). Steps: 1 get(0): ring on A, 1; 2 get(1): A → B, 3; 3 get(2): A → C, 6; 4
  get(3): A → D, 10; 5 "= 10" and the caption "Each call starts at firstNode again. Four
  calls visit 1 + 2 + 3 + 4 = 10 nodes."; 6 caption "For n nodes that is n(n + 1)/2 visits,
  which grows like n²." and the `.verdict` under the editor (A, B, C struck; D "n calls,
  each a walk of up to n nodes"). Notes: the stem's get(n) is one past the last index on
  a 0-based list; the walk uses get(0) to get(n − 1); the cost is the same.
- **08 (Vote 2).** `.vote` layout, `--long` options (the longest, "The reverse transversal
  technique", is 33 characters). h2 "Which techniques insert into a sorted chain in O(n)?".
  Stem verbatim without the "Q-1: " prefix (Runestone's numbering; noted here). Left SVG:
  the chain 3 → 7 → 12 → 20 with firstNode, and a loose node `10` with an empty next
  drawn under the gap between 7 and 12, no arrow. Notes: "Answer: B and C [twin
  u12q07_insertnode_b; confirm in Runestone]"; "transversal" is the source's spelling.
- **08b.** Editor 880 px (longest line 42 characters: the look-ahead `while`), line-height
  1.4, `code-mid`. Lines: the runner version `Node p = null;` / `Node c = firstNode;` /
  `while (c != null && c.data < x) {` / `    p = c;` / `    c = c.next;` / `}` /
  `Node n = new Node(x, c);` / `p.next = n;`; then `walkline--new` lines for the
  look-ahead `while (c.next != null && c.next.data < x)` / `    c = c.next;` /
  `c.next = new Node(x, c.next);`; then one `walkline--new` line `for (int d : list)`.
  Right (736 px): the vote's chain (130 × 76 boxes on a 166 pitch), two rings: `c` blue,
  `p` orange (orange = the reference the work is done through, W9D2 04's rule), the new
  node under the gap. Steps: 1 p is null (a stone `null` label), c on 3; 2 `3 < 10`: p → 3,
  c → 7 (both rings move one pitch); 3 `7 < 10`: p → 7, c → 12; 4 `12 < 10` is false, the
  loop stops; caption "c is the first node that is not smaller. p is the node before it.";
  5 the new node's next arrow draws on to 12 (Create: shaft then head); 6 p.next swings from
  12 to 10 (CSS `d` + `data-swing`, same paths); caption "Two references, one walk: the
  runner technique."; 7 the look-ahead lines appear, the p ring fades; caption "Look-ahead
  compares c.next.data and stops on the node before by itself. One reference, one walk.";
  8 the foreach line appears; a `d` pill sits on the value 7 with no box around it;
  caption "d is 3, then 7, then 12, then 20. The loop never gives you a node, so there is
  no next to set."; 9 a dashed stone arrow from 20 back to 12 draws on and takes a maroon
  cross; caption "A singly linked node has no reference to the node before it. From 20
  there is no way back to 12."; 10 `.verdict` (A and D struck, B and C right). The front
  case (p == null → firstNode = n) is left out of the code; the notes say so and name
  the homework's x709 "Find Node Before" as the same walk.
- **09 (Vote 3).** Code question: `grid grid--code` with the five lines verbatim in an
  `.editor` (bar "the program"; `arr.length`, i, j kept), the sentence "Consider the
  following program:" as the lede above and "What is its time complexity, in terms of the
  length of the array?" under the editor; right: `.opts` A–D. Two clocks. Notes: "Answer:
  D — O(n²) [no PL twin; n + (n − 1) + … + 1 = n(n + 1)/2 prints; confirm in Runestone]".
- **09b.** W5D1 04c copied and changed: the editor holds the vote's five lines
  re-indented at 2 spaces (bar says so; 40 characters → 838 px), the inner loop
  `for (int j = i; …)` so the grid includes the diagonal. 4 × 4 grid: steps 1–4 light rows
  0–3 (4, 3, 2, 1 cells; counter "prints" 4 → 7 → 9 → 10); step 5 the grid grows in place
  to 8 × 8 (04c's track animation) and the counter resets by a `data-roll="off"` pair;
  step 6 row 0 (8); step 7 rows 1–7 (28 more, 36); step 8 the plant "4 entries print 10
  lines and 8 print 36. That is n(n + 1)/2, the sum from Vote 1, and it grows like n²."
  and the `.verdict` under the editor (D right). Notes: the difference from W5D1's
  hasDuplicate is j = i, not j = i + 1, so the diagonal counts.
- **11.** W5D1 15 with Test 2's facts, all confirmed (no placeholder): "Test 2: Wednesday
  (MW) · Thursday (TR)"; checklist: next class, in lecture · on Canvas, inside LockDown
  Browser · 45 minutes · one attempt · ~19 questions · closed book: no notes, IDE, web or
  talking · laptop only; phone away; do the Canvas 2-factor sign-in before you start · pen
  and paper allowed · student ID on the desk. DO (step 1): charge your laptop · bring your
  student ID · LockDown Browser installed and tested · run Test #2 Practice once more
  tonight. DON'T (step 2): open Eclipse or any other program · use your phone · discuss the
  test until both sections have taken it · leave before the end. Redo line (step 2):
  "Test 2 Redo: Wednesday November 4 (MW) · Thursday November 5 (TR), in lecture." Notes:
  the accommodation-letter line; the 10.1 page's rule that an unexcused absence reported
  the same day may get a make-up with a 10-point deduction.
- **12.** W4D2 15 with the six region names as chips plus "anything else"; "Later
  questions: Piazza. Turn on notifications for instructor posts."

## What both builders must agree on

- Chain grammar (02c, 07, 07b, 08, 08b): W9D2 08b's. Link boxes 130 × 76 (`value 56 |
  next 74`), 166 px pitch, `--bg-1` fill with a `--fg-1` 4 px stroke; values mono
  `--t-small`, `null` mono `--t-micro` in stone; reference pills 176 × 44 blue with
  `--t-micro` mono text; ring = rect 142 × 92, radius 14, stroke 5, label under it;
  blue arrows stroke 4 with `marker-end`; markers 12 × 12, fill inline
  (`style="fill: var(--accent-2)"`). Orange = the reference doing the work (p in 08b).
- Marker and gradient ids `w10d1-NN-…` (`w10d1-02c-head`, `w10d1-07b-head`, …).
- Vote layouts: text questions (07, 08) use deck.css `.vote` (stem lede, 870 px left
  panel, `.vote__opts`, `--long` on 08); the code question (09) uses `grid--code` with an
  `.editor` and `.opts`. Clocks on every vote: 90 s vote + 150 s discuss, W9D2 08's block.
- Answer walks end on `.verdict`; `.moves` counters sit inside a `.codewalk`; every CSS
  `d: path()` swing carries the same paths in `data-swing`.
- Pills: the test map's pill style (mono micro, blue 14% wash) is slide-local to 04;
  nobody else draws a pill that could be read as a test term.
- Builder A owns `index.html` and writes the full manifest above at the start, so Builder
  B's files load in Studio as they land.

## Translated, dropped, unverified

- Keys assumed from the PL twins and arithmetic: Q1 D, Q2 B + C, Q3 D. Confirm in
  Runestone's results view before class.
- Quoted quirks kept: Q1's "get(0), get(1), …, get(n)"; Q2's "transversal". Dropped from
  Q2: the "Q-1: " prefix (Runestone numbering, not question text).
- The 10.1 page's "20–30 minutes" (W9D2's notes) is superseded by 45 minutes (instructor,
  2026-10-24, matching the page's "Quizzes will be 45 minutes long"). Delivery: a Canvas
  quiz inside LockDown Browser (brief). "CodeWorkout" on the page is never drawn or named.
- No point values on the map; no SSD slide; no in-class practice run; no 10.2/10.3 content.
- Week 11 clock rows are open (below). The Week 11 homework row is from the CSV.
- Vote timers follow W9D2 08 (90/150), not §7's 150/240; three votes plus a map in 50
  minutes need the shorter rings.

## Open questions for research (PL repo and ~/Downloads only; never canvas-banks/)

1. Week 11 clock rows: CE 11's name and date; Project 3's Week 11 deliverable; any module
   due Sun Nov 8 (the CSV lists 11.2/11.3 on Nov 1, then 13.1/13.2 on Nov 15, nothing
   between). Sources: `cs2114-schedule-fall2026.html`, the deadline imscc exports.
2. Every pill term in the 04 table: read all alternatives of each slot
   (`questions/practiceExams/test2/pNN_*/*/question.html`, slot 8 under `test1/p16`) and
   confirm the term appears in the stems, or pick the fallback, or propose another word.
3. Slot 8: which assertion names its four alternatives use (`assertEquals`,
   `assertThrows`, `assertNull`, …), so the pill is a word the student will see.
4. Do any practice alternatives test Generics 2 or UML (grep the p* folders for
   `extends Comparable`, `<T>`, `UML`, `superclass`)? If yes, the caption on 04 changes.
5. Homework x709 "Find Node Before" (`questions/codeworkout/x709_…`): its method name
   and whether it uses prev/curr runners or look-ahead, so 08b's notes quote it exactly.
6. The 10.2 module slide PDFs (`clientFilesCourse/slides/`, image-only, view the pages): is
   there a sorted-chain insertion drawing or `getNodeBefore` code to follow for 08b's names?
7. The 9.1 `getNodeAt` code (ListIntro24 / ArrayListImplementation24 pages): confirm the
   loop form so 07b's `get` matches what the room saw last week.
8. CE 10 "DLL": is Fri Oct 30 confirmed anywhere (schedule HTML, Canvas export)? The clock
   draws it on the Friday rule either way.
9. Project 3 Deliverable 1: its exact name ("Scope"?) and the teams note, from the Canvas
   project export in ~/Downloads, for 02's caption and notes.
10. Test #2 Practice: confirm `allowAccess` is live on the server copy (startDate
    2026-10-23T16:44, timeLimitMin 45) and that the assessment is tracked and pushed, before
    05 points at it.

For the instructor (not research): the three keys in Runestone; whether Generics 2 and UML
appear on Test 2 at all, given no practice slot covers them.

## Cross-browser

- Swings (08b: p.next 12 → 10): CSS `d: path()` under `:has(.cap--6:not(.is-pending))`
  plus `data-swing='[[6,"…"]]'` with the identical path, so Safari (deck.js fallback) and
  Chrome/Firefox draw the same.
- Ring moves (02c, 07b, 08b): `transform: translateX()` on an SVG `<g>` with
  `transform-box: fill-box`; no `offset-path`.
- Draw-ons (02's poles and ranges, 08b's new-node arrow and the reverse arrow):
  `pathLength="100"` on `<path>` elements only; W9D2's clock `<line>` poles are converted
  to `<path>` with `V`/`H` commands. Arrow heads that draw on are separate paths that
  fade after the shaft (§8); static arrows keep `marker-end`.
- 09b's grid growth animates `grid-template-columns/rows` (Chromium interpolates; Firefox
  too; where a browser does not, the tracks jump to the end state, which is still
  correct). Acceptable; nothing else depends on it.
- `:has()`, `color-mix()`, `transform-box` are allowed; no `@property`, nesting, container
  queries, `foreignObject`, `context-stroke`, `backdrop-filter`.
- Text slides (04, 05, 11, 12) keep ≥ 24 px bottom slack in the sweep; deck.css's
  `text-wrap: pretty` on `--long` options is ignored by Firefox, so 08's options must fit
  without it (33 characters at `--t-small` is 627 px of 746).
- Fonts: only the bundled Liberation Sans/Serif and JetBrains Mono stacks in tokens.css.
- Verification: `python3 tools/add_sids.py slides/*.html` (new files), `lint.py` clean,
  `timeout -k 5 150 tools/measure/run.sh "$PWD"`, then `run3.sh` once step 2b lands.

## Research answers (2026-10-24)

Full detail and per-slot evidence in the researcher's scratchpad report
(`w10d1-research.md`, same session). Never opened `canvas-banks/*`.

1. **Week 11 clock rows.** Homework "Week 11: Sorted Lists" due Fri Nov 6
   (`~/Downloads/cs2114-deadline-schedule.csv`). **There is no CE 11** — the schedule HTML
   lists Challenge Exercises 01–06, 08–10, 13–14 only; Week 11's homework column has no CE
   (`~/Downloads/cs2114-schedule-fall2026.html`, Week 11 row). Project 3 Week 11 deliverable
   = **"Deliverable 2 — Specification"** ("Spec"), due at the start of the Week 11 lab
   (`~/Downloads/CS2114_Projects_Fall2026.imscc` → `assignment_9`,
   `wiki_content/project-3-overview.html`). No module is due Sun Nov 8 — the CSV jumps from
   11.2/11.3 (Nov 1) straight to 13.1/13.2 (Nov 15) (`~/Downloads/cs2114-deadline-schedule.csv`).
2. **Pill-term audit, all 19 slots**: 5 of 19 replaced — slot 1 `Deque`→`ADT`, slot 4
   `curr.next`→`!= null`, slot 7 `top at index 0`→`O(1)`, slot 9 `after the call`→`recursive`,
   slot 18 `which line`→`size`. The other 14 keep the plan's primary term (slots 3, 6, 12, 13,
   19 verified at "most"/tied rather than "all"). Full table with evidence paths in
   `w10d1-research.md` §1.
3. **Slot 8 assertion names** (`questions/practiceExams/test1/p16_covering_test_method/*/server.py`):
   `assertTrue`, `assertFalse`, `assertEquals`, `assertNull`, `assertNotNull` — no
   `assertThrows`. `assertEquals` appears in 3 of 4 (missing from `covering_test_null_on_name`).
4. **Generics 2 / UML in the practice?** No. `grep -rl "extends Comparable\|UML\|superclass\|
   subclass\|<T extends\|? extends\|? super" questions/practiceExams/test2/` → no hits. The
   planned 04 caption is correct as written.
5. **Homework x709 "Find Node Before"**
   (`questions/codeworkout/x709_linkedlistinsertionsortfindnodebefore/`): method stub is
   `public Node<T> findNodeBefore(T value)`, no body given (student writes the walk); the
   class uses `firstNode` and a cursor named `current` elsewhere. Companion
   `x734_linked_chain_find_node_before_value` explicitly offers "look-ahead or runner
   technique," matching the vote's wording.
6. **Course code for sorted insertion** (rendered via `pdftoppm`, read as images):
   `InsertionSortLinked.pdf` slide 4 and `LinkedImplementationofSortedList.pdf` slides 6–7
   both implement the runner technique with **full-word names**: `currentNode`/`previousNode`
   (insertion sort) and `currentNode`/`nodeBefore` (the actual `getNodeBefore` method, same
   name as the homework). Loop: `while ((currentNode != null) &&
   (item.compareTo(currentNode.getData()) > 0)) { previousNode = currentNode; currentNode =
   currentNode.getNext(); }`. **Flag for Builder B**: PLAN's 08b spec uses single-letter `p`/`c`
   in the editor code; every written course source (both PDFs, and the PL twin
   `u12q07_insertnode_b`'s own option text "references, such as `previous` and `current`")
   uses full words, never single letters — `p`/`c` only appears as informal handwritten
   annotation on the diagrams. Consider renaming 08b's code to `previous`/`current`.
7. **9.1 `getNodeAt`** (`clientFilesCourse/slides/LinkedListRemove.pdf` slide 4, "getNodeAt
   Implementation" — this, not ListIntro24, is where the code actually lives):
   ```
   private Node getNodeAt(int givenPosition) {
       Node currentNode = firstNode;
       for (int counter = 0; counter < givenPosition; counter++)
           currentNode = currentNode.getNext();
       return currentNode;
   }
   ```
   0-based (`0 <= givenPosition <= numberOfEntries - 1`), names `currentNode`/`counter`/
   `givenPosition`. The public method is `getEntry(givenPosition)`, not `get(i)`
   (`ListEfficiency.pdf`). 07b and 02c should match these names, not `cur`/`i`.
8. **CE 10 "DLL" date**: not confirmed anywhere. It sits in the Week 10 (Oct 26–30) row's
   homework column with no day-level date, in the schedule HTML and in both Canvas imscc
   exports checked. (The large `cs2114-softw-des-and-data-structures-export.imscc` is a
   **stale/legacy export** — wrong dates, wrong project names — do not use it for anything.)
   The clock's Friday-rule placement (Oct 30) remains the only available answer.
9. **Project 3 Deliverable 1 exact name**: Canvas title **"Project 3 - Deliverable 1 - Scope"**;
   on-page heading "Deliverable 1 — Scope · Week 10 (Oct 26–30) · due at the start of your lab
   session." Teams note: "Teams re-form one last time — you are assigned a group of 3. Check
   Canvas to confirm." (`~/Downloads/CS2114_Projects_Fall2026.imscc` → `assignment_8`).
10. **Test #2 Practice access**: confirmed live —
    `allowAccess: [{startDate: "2026-10-23T16:44:00", endDate: "2026-12-31T23:59:59", credit:
    100, timeLimitMin: 45}]` in `courseInstances/Fall2026/assessments/practiceExams/test2/
    infoAssessment.json`; `git log` shows it committed 2026-10-23 16:53 (`f6fb164`), and local
    `main` is even with `origin/main` (pushed). Server-side sync to the live PL instance
    cannot be verified from the filesystem.

**Vote-text cross-check (item 5 of the research brief):** no wording to fix. The Q1 twin
(`u11q08_iterator_efficiency_a`) and Q2 twin (`u12q07_insertnode_b`) are differently-worded
practice questions that only confirm the keys (D; B+C), not verbatim matches to the Runestone
paste — the brief already treats them that way. Q2's twin option text itself says "`previous`
and `current`" (see item 6 above). Q3 has no twin, as the brief states.

## Builder A: test-map terms (2026-10-24)

Rule applied: a pill names the idea a student should recognise in the question, taken
from words shared by the slot's alternatives; no generic tokens (`!= null`, `size`,
`recursive`, `ADT`). Labels and slot numbers as on 04 (cards sorted by slot in each row).

| slot · label | pill | why |
|---|---|---|
| 6 bag efficiency | `worst case` | "in the worst case" is in 2 of 3 stems and is the idea; `O(n)` is an answer value, not a concept |
| 12 bag contains | `getIndexOf` | kept: the helper the contains code calls, 3 of 4 |
| 13 bag remove | `removeEntry` | kept: the private helper, 3 of 4 |
| 19 bag constructor | `new Object[]` | kept: the generic-array idiom the constructors use; label changed from "bag array" |
| 7 stack efficiency | `where the top is` | all 4 alternatives explain the cost by "where the top lives" (W5D1's chapter idea); `O(1)` is an answer value |
| 10 stack trace | `pop()` | kept, 4 of 4 |
| 15 stack toString | `size() - 1` | kept: the top entry's index, stated in all 4 stems |
| 3 count the calls | `calls itself` | kept, 3 of 4 |
| 9 print a chain | `print order` | 3 of 4 ask in what order a recursive helper prints the chain; replaces `recursive` |
| 2 queue indices | `frontIndex` | kept, 4 of 4 |
| 11 deque trace | `addToFront` | kept, generated in all 4 |
| 16 deque remove | `getPreviousNode` | kept, 4 of 4 |
| 17 deque add ends | `lastNode` | kept, 4 of 4 |
| 4 chain loop | `loop condition` | the slot tests where a walk stops (`curr` vs `curr.next`); the stems say "while the condition holds"; replaces `!= null` |
| 5 chain surgery | `new Node(d, n)` | kept, generated in all 4 |
| 14 remove a node | `node before` | the idea of the slot (in the stems or generated options of 3 of 4) and the link to Vote 2; `firstNode` is literal in 4 of 4 but is a field name, not the idea |
| 18 list bug | `find the defect` | "defect" is in all 4 stems; replaces `size` |
| 1 which ADT | `ADT by behavior` | the four alternatives match an ADT to behaviour, signatures or a scenario (`behavior_to_adt` etc.); replaces `ADT` |
| 8 a covering test | `every case` | "covers every case" is in all 4 stems (test1/p16); better than `assertEquals` (3 of 4, a tool name) |

Builder A notes: the manifest has 20 files (the plan's table), not 19. 11's DO/DON'T items
are at `--t-small` (W5D1 had micro, under the Week 8 floor), so its columns are 760 / 856.
02/17 convert every `<line>` to a `<path>`; the axis and the Canvas bracket stop 6 px
inside the body (Firefox counts round caps into the box). The Redo band's five label lines
end at y 432 and "Week 11 · next week" sits at x 1170 so the two do not touch.

## Review (Fable, 2026-10-24)

Reviewed every slide in manifest order against the brief, DECK-PROMPT §8/§11/§13/§14, the
Research answers and the public practice pools (`questions/practiceExams/test2/`, `test1/p16`;
never `canvas-banks/*`). Vote text checked verbatim against the brief's paste (Q2 without
"Q-1: ", "transversal" kept). Clock checked against §11 and Research answer 1: Test 2 band on
Wed–Thu x 366–603 as step 1, Redo on x 1317–1554, HW blue / CE maroon / P3 accent-2 with the
lab range, no CE 11, no module Nov 8. Lint clean; `run3.sh` run before and after.

Changes:
- **04-test-map.** The pill is the instructor's highlight, so it is now **bold** on a 20% blue
  wash (was regular, 14%); JetBrains Mono's advance is the same at every weight (measured
  252.02 px both ways), so no width changed. Seven pills re-worded to vocabulary a student
  meets in the question, from the stems: 19 `new Object[]` → `capacity` (every p20 stem says
  "room for exactly N entries"); 7 `where the top is` → `top at index 0` (the p07 layouts
  are named by where the top is pinned); 3 `calls itself` → `recursive call`; 4 `loop
  condition` → `cursor != null` and label `traversal loop` (the p04 stems test
  `cur != null` against `cur.next`); 18 `find the defect` → `one defect`, label `a list
  method` (p19: "contains one defect", "which line contains the defect"); 1 `ADT by
  behavior` → `its operations` (p01 matches an ADT to its operations, signatures or where a
  client reaches the entries); 8 `every case` → `code coverage` with label `pick the test`
  (the 10.1 topic name; p16 stems say "passes and covers every case"). Desc and notes
  follow. Longest pill 15 characters (279 px with padding of 309), longest label 18 (306
  px in WebKit's rounding); slack 32 in all three engines.
- **07b.** Cut the notes sentence about iterators making the loop O(n) (10.3 is out of scope).
- **08b.** Step 7 no longer slides the blue ring backwards from 12 to 7: a singly linked
  chain has no way back, which step 9 then says. The look-ahead loop is a second walk from
  firstNode, so a second blue ring (`ring--c2`) appears on 3 and travels to 7 while the
  first fades on 12 (07b's idiom; back-steps reverse). Desc, comment and notes say so.
- **09b.** The line above the grid ("arr.length = 4 · row i, column j") is read as text, so
  it is at `--t-small` (was micro); re-ordered so the value leads. Slack 88 → 77.
- **02.** Caption 6 "P3 D2" → "Deliverable 2" (no abbreviations in prose; 1,468 px of 1,664).
- **03.** Notes: "the idea each question tests" → "the term each question tests".

Final `run3.sh` (Chromium 156 / Firefox 158 / WebKitGTK 605.1.15): no BOTTOM, RIGHT, LEFT or
CLIPPED flags on any slide at any step; the cross-engine diff is empty (no slide differs by
more than 8 px). Smallest slacks: 06b 26–27 (the W9D2 ring, inherited), 04 32, 02/17 35–36.
WebKit reports `CSS d supported: False`, so 08b's swing takes the `data-swing` path; its one
`d: path()` (the `.lnk--7` swing at step 6) carries the identical path in `data-swing`. The
"over" lines on 07/08/09 are the vote timers at the top right, which sit above the body by
design (as in every deck since W5D1).

WebKit font finding (a probe page inside the deck frame, after `document.fonts.ready`):
WebKitGTK loads the bundled faces — `JetBrains Mono` (woff2, variable), `Liberation Sans`
and `Liberation Serif` (woff) all report `status: loaded`, and `document.fonts.check()` is
true for each. The @font-face `src`/`format()` declarations in tokens.css are correct and
need no change. The engines differ only in glyph-advance rounding: WebKit rounds the mono
advance to whole pixels (17 px at 28 px and 19 px at 32 px, where Chromium/Firefox use
16.8 / 19.2), so mono text is about 1% wider in WebKit at micro and small sizes and 1%
narrower at `--t-code`. On older decks that sized an editor to the exact 0.6 em budget at
36 px (21.6 → 22 px in WebKit, +1.9%) the harness would report CLIPPED in WebKit only;
that is the likely cause there. In this deck every editor is at `--t-code` and its
narrowest line keeps 48–53 px (Chromium) / 56–62 px (WebKit) of slack, so nothing to fix.

For the instructor:
- The three keys (Q1 D, Q2 B + C, Q3 D) are from PL twins and arithmetic; confirm in
  Runestone's results view before class.
- Generics 2 and UML class diagrams are on the 10.1 list with no practice slot; 04's caption
  says so. Decide whether they are on Test 2 and tell the room.
- CE 10 "DLL" has no day-level date in any source; the clock draws it on the Friday rule
  (02's notes carry the `[NOT IN ANY SOURCE]` marker).
- The seven re-worded pills on 04 are a judgement call on what a student recognises as the
  question's vocabulary; the Builder A table above records the previous wording.
- 06b's plant sits 26 px above the body edge in Firefox (the W9D2 ring geometry, unchanged).

## Instructor change (2026-10-24)
"for the 19 questions, just mention the topic. dont be that detailed": 04 is now six topic
tiles (3 × 2), each topic name as the highlighted term (bold, blue wash); the 19 per-question
cards, slot numbers and pill terms above are cut. 05 and 12 now point at topics, not cards.
Lint clean; run3 (Chromium, Firefox, WebKit) no flags, 04 slack 112 in all three.
Follow-up the same day ("some topics and the number of questions in each topic", no question
text, no answers): each tile now has its count under the name: bags 4, stacks 3, recursion 2,
queues and deques 4, linked chains and lists 4, ADTs and tests 2 (= 19, from the practice
slots). run3 clean, slack 112 in all three engines.

## MVC coda (2026-10-25)
Instructor: "add a mention of this to the end to show off what an MVC is with respect to
project 3 ... a shortish overview", with six files in ~/Downloads (Counter, Observer,
ConsoleView, WindowView, CounterController, Runner). Two slides between 12 and 17:
- `16-mvc-parts`: a UML class diagram of the six files, model in the middle, built per step
  (model → views → controller → arrows); blue arrows = the calls (increment, update),
  the orange arrow = the click; plant = Project 3 D2 "model/view separation".
- `16b-mvc-click`: one click walked under the PC bar (the controller and the model as
  written, braces of the for dropped; the view's listener is the editor bar) beside the
  three objects it reaches: the model card (data 0 → 1 by crossfade), two windows, the
  console. Plant: the model never names a window or a console.
Notes on 01b, 10, 12 point at the coda. The 6.2 module pages are video-only, so the
vocabulary is the files' own names. Both drawings are inset at the edges for Firefox's
stroke boxes. Lint clean; run3 clean in all three engines (16 slack 48, 16b 76).
