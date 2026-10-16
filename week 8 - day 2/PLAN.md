# Week 8 · Day 2 — plan

Built 2026-10-11 for Wednesday Oct 14 (MW, NCB 320) and Thursday Oct 15 (TR, Squires): one
deck, both sections. Shared css/js/assets/tools cloned from `week 7 - day 2` (the newest
copies). Last class (Monday for MW, Tuesday for TR) covered queues and deques on linked
chains (`firstNode`/`lastNode`, `DLNode`, the removeBack and isEmpty votes); this deck does
not repeat it. `02-course-info` and `17-next-class` (the Week 8/9 clock) are written by
another agent into this folder; they are in the manifest only.

Sources: the 8.1 module's video slides in `~/Projects/pl-vt-cs2114/clientFilesCourse/slides/`
(`ArrayQueueIntro.pdf` 8 pages, `ArrayQueueRemove.pdf` 4, `ArrayQueueEnsureCapacity.pdf` 3,
`ArrayQueueWrapUp.pdf` 3, read page by page); the homework problems
`questions/codeworkout/x704`–`x707` (question.html and the `ArrayQueue.java` each one hands
out); the assessment `courseInstances/Fall2026/assessments/homeworks/08_queues/infoAssessment.json`;
the PrairieLearn twins of the two votes `questions/dataStructures/queues/u10q08_circulararrayqueue_{a,b,c,d}`
and `u10q09_circulararrayqueue_{a,b,c,d}`. Vote text: the Runestone paste in the build brief.

## Through-line

**"In an array queue, dequeue increases frontIndex instead of shifting the entries. Both
indices go from the last slot to slot 0 through %, and one slot stays unused so that the
full test and the empty test differ."**

- Part 1 · A queue on an array, where frontIndex moves and both indices wrap around. Four
  walks: dequeue by shifting, dequeue by moving `frontIndex`, the wrap with `%`, the unused
  slot.
- Part 2 · Which slots are in the queue? The routine ring, then two votes. Each vote is
  answered by counting the occupied slots on the strip.
- Part 3 · This week's work: the four ArrayQueue homework problems.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `CS 2114 · FALL 2026 · WEEK 8 · DAY 2` |
| 01b-today | three chapter tabs: a row of cells with an arrow from the last cell back to the first · a row with orange cells past the end and two markers · three code lines led by orange discs; the captions are the divider titles |
| 02-course-info | (manifest entry only; written by the clock agent) |
| 02b-bridge-linked | FROM DAY 1 TO DAY 2 (bridge, 2026-10-11): Day 1's linked queue with firstNode/lastNode, the five operations, a ten-slot strip with frontIndex/backIndex; the bag/stack/queue pattern; the question for Part 1 |
| 03-chapter-1 | PART 1 OF 3 · A queue on an array, where frontIndex moves and both indices wrap around |
| 04-walk-shift | concept intro: a naive `dequeue` that returns `contents[0]` and copies every entry one slot left; the moves counter rolls to 5 for five entries; plant "Removing one entry from n entries costs n moves: one read and n − 1 copies." |
| 04b-walk-front | dequeue by moving `frontIndex` (no `%` yet): one move; then enqueues set `backIndex` to 9 while slots 0–3 are empty; the next `backIndex + 1` is 10; plant "Slots 0 to 3 are empty, but the next backIndex + 1 is 10, and there is no slot 10." |
| 04c-walk-wrap | `backIndex = (backIndex + 1) % contents.length`: the video's table for length 10 one row per press, then enqueue(K) changes `backIndex` from 9 to 0, then dequeues change `frontIndex` from 9 to 0; plant "After slot 9, the next index is 0, for both frontIndex and backIndex." |
| 04d-walk-unused | a new queue (front 0, back 9) is empty; after ten enqueues it is full with the same two index values; with slot 9 unused the full test differs; the three tests appear one per press as code lines; plant "One unused slot makes full and empty different, so a queue of capacity 9 uses an array of 10." |
| 04e-chapter-2 | PART 2 OF 3 · Which slots are in the queue? |
| 05-peer-plus | the routine ring, assignment `Peer Instruction W08D2`; takeaway "Each answer comes from counting the entries between the two indices." |
| 06-vote-indexing | VOTE 1, static: the stem verbatim, a blank 11-cell strip left, five options right; two clocks |
| 06b-walk-indexing | VOTE 1 · THE ANSWER: per option the pills move and the occupied slots wash orange, with a tally row; a caption on why A–C are tempting; `.verdict` D; plant "The size is the number of slots from front to rear, inclusive, in an array of 11." |
| 07-vote-full | VOTE 2, static: the stem verbatim, a blank 6-cell strip left, seven options at `--t-small` right; two clocks |
| 07b-walk-full | VOTE 2 · THE ANSWER: the pills move to 3 and 1; slots 3, 4, 5, 0, 1 wash one per press while the count rolls to 5; slot 2 hatched unused; the full test evaluated; D, F, G ruled out; `.verdict` E; plant "The count runs from frontIndex up to slot 5, then from slot 0 to backIndex." |
| 10-chapter-3 | PART 3 OF 3 · This week's work |
| 11-hw-arrayqueue | WEEK 8 HOMEWORK: a full circular array queue drawn left with the class card, four problem cards right (x704–x707), the signpost "best 4 of 8 count · due Friday" |
| 16-next-week | NEXT WEEK (bridge, 2026-10-11): stack/queue/deque/list by where each adds and removes and where it is in the course; the list row grows in |
| 17-next-class | (manifest entry only; written by the clock agent) |
| 99-closing | dusk |

File numbers are sort keys: `04e` and `10` were chosen so the dividers sort before their
chapters; the manifest order is the order on screen.

## Slide by slide

- **The strip grammar (04–04d).** One SVG per slide at 1:1, ten cells (the video's
  "Cases when queue.length is 10"), indices 0–9. Cells are **96 px on a 108 px pitch**,
  not the 128/144 of the brief: the walks put the editor above and the strip below, and
  the captions (04b, 04d) or the table (04c) need the 530 px to the right of the strip.
  The index sits under each cell in mono at the micro size; an entry is a mono letter at
  the small size; an empty cell is blank. The pills are 176 × 40 with their labels at
  `--t-micro` (revision of 2026-10-11). `frontIndex` is a blue pill ABOVE the strip and
  `backIndex` a blue pill BELOW it (the brief put both above): the two are equal for a
  one-entry queue and adjacent for an empty one, so one row would stack them; the module's
  own drawings put them on either side too (ArrayQueueRemove p. 1). A pill that changes
  value moves (a CSS translate in steps of 108 px); a wrap is a real move from slot 9
  back to slot 0. A cell being read takes a blue edge; a counted cell the orange 18% wash
  with an orange stroke; the unused slot a stone hatch. Every state change is a
  `:has(.cap--k:not(.is-pending))` rule in step order.
- **04 · shift.** The deck's own naive version (the module only asks "what if dequeue 4
  times?" on ArrayQueueIntro p. 1, it shows no shifting code): fields `contents` and `n`,
  seven lines at `--t-code` (the `for` has no braces and `n--; contents[n] = null;` share
  one line, held under the PC for steps 6–7; at eight lines the slack was 12 px).
  Five entries A–E. Step 1 reads `contents[0]` (moves 1); steps 2–5 hold the loop under the
  PC while B, C, D, E are each copied one pitch left, and the value each copy overwrites
  fades (the original stays in its cell until the next copy overwrites it, so after the
  loop E is in both 3 and 4); step 6 `n--` strikes 5 → 4; step 7 clears slot
  4; step 8 the plant. The counter counts entry moves (the read and the copies), so it
  reaches 5 = n; `n--` and the null are left out of the count and the notes say so.
- **04b · front.** Two editors side by side: the video's `dequeue` with
  `frontIndex = frontIndex + 1;` in place of the `%` line (the `%` arrives on 04c) and a
  plain `enqueue`. One read, the slot cleared, the front pill moves 0 → 1: one move,
  counter 1 (blue, `moves--ok`). Then enqueue(F) and enqueue(G–J) move the back pill to 9,
  three more dequeues move the front pill to 4, and the last press puts the PC on
  `backIndex = backIndex + 1;` once more. There is no slot 10.
- **04c · wrap.** One editor: the video's `enqueue` (`ensureCapacity()` left out; it is
  introduced on 04d's plant line and in the notes) plus the `frontIndex` line of the
  video's `dequeue` under a `// in dequeue():` comment, so both `%` lines fit six lines.
  Steps 1–5 build the video's table one row per press (9 → 0 in orange); 6 enqueue(K)
  changes `backIndex` from 9 to 0; 7 enqueue(L); 8 five dequeues change `frontIndex` from
  4 to 9; 9 one more changes it from 9 to 0; 10 the plant. Since the revision the table
  sits beside the editor (mono at `--t-small`) and the captions sit beside the strip.
- **04d · unused.** No method under the PC: the "editor" is the three tests from the
  wrap-up video (ArrayQueueWrapUp p. 2), each line hidden until reached
  (`walkline--new`), the PC on the test being evaluated. A new queue (front 0, back 9:
  the constructor's `contents.length - 1`) passes the empty test; A moves backIndex to 0;
  B–I and J fill all ten slots and the same test still passes; with one slot unused the
  queue is full at nine (J fades, slot 9 hatched, back 8) and the full test passes while
  the empty one fails; eight dequeues leave one entry with front == back. Since the
  revision the tests are at the editor's default `--t-small` (no density class). A count of
  entries (`.moves`) rolls 0 → 1 → 9 → 10 → 9 → 1.
- **05.** W7D2's ring; only the week, the assignment, the desc and the takeaway changed.
- **06 / 07 (votes).** The `.vote` layout: a short paraphrase h2, the stem verbatim as
  the muted lede, the blank strip on the left, the options on the right; the two clocks
  copied from W6D1 06 (1:30 vote, 2:30 discuss). Vote 1's strip is eleven
  `.vote__cell`s narrowed to 70 px on a 78 px pitch so they fit the 870 px panel; Vote 2's
  six cells are the deck's 128 px `.vote__cell`s. Vote 1 options in mono at the small
  size with 8 px rows; Vote 2's seven options at the small size with 6 px rows and 48 px
  key discs (W6D1 06's treatment, smaller discs because seven rows of 80 px discs do not
  fit; 56 px discs left 6 px of slack). The cell indices are at `--t-micro`.
- **06b.** The 11-cell strip at the brief's 128 px cells on a 144 px pitch (11 cells =
  1568 px, full width); per option one press: the pills move, the occupied slots wash in a
  stagger from front to rear, and a tally row (`A · front 0 · rear 5 · 6 entries`) is
  added under the strip, in mono at `--t-small`. The tally is a list rather than a rolling
  numeral because each option restarts the count. Then a caption on why A–C are tempting,
  then the verdict at `--t-small`.
- **07b.** The 6-cell strip (128/144), the count as a `.moves` numeral that rolls 0 → 5,
  one slot per press in the order 3, 4, 5, 0, 1; slot 2 hatched; the full test as a code
  line evaluated in the caption; D, F, G ruled out; the verdict at `--t-small`.
- **11.** W5D1 13's grammar, rearranged because four stacked cards ran 120 px over: top
  row, a full queue of capacity 5 (`contents.length` 6, front 4, back 2, slot 3 unused)
  beside the card naming what the handed-out class already has; then the four problem
  cards in a 2 × 2 grid, one per press, in assessment order: the PL title, the signature
  without `public`, and one sentence at `--t-small` on the hardest part, phrased from
  the problem statement (no solution code); the signpost along the bottom.
- **04c editor width.** 1080 px, not the computed 1050: at 1050 the sweep flagged the
  `frontIndex` line as clipped.

## Translated, dropped, unverified

- **The vote keys come from the PrairieLearn twins**, not from Runestone: Vote 1 D
  (`u10q08_circulararrayqueue_b`, verbatim, marks front 9 / rear 2), Vote 2 E
  (`u10q09_circulararrayqueue_d`, verbatim, marks five elements). Both agree with counting
  on an array of capacity + 1 slots with inclusive indices; the sister variants agree too
  (q08: 5/9, 7/0, 10/3; q09: 5/1 → three, 3/0 → four, 2/0 → five). **Confirm both keys in
  Runestone's results view before class.** The assignment name `Peer Instruction W08D2`
  and the activity ids `vtcs2_circularArray_indexing` / `vtcs2_circularArray_full` are
  from the brief's paste, not seen in Runestone.
- **The array's field is `contents`, not `queue`.** The brief said the intro slides use
  `queue` and the wrap-up `contents`; the PDFs show the opposite pattern: the class code
  (ArrayQueueIntro p. 5–6), `dequeue`/`getFront` (Remove p. 3), `ensureCapacity`
  (EnsureCapacity p. 2) and both wrap-up slides all say `contents`; `queue.length` appears
  only on the "Wrapping Around" table slide (Intro p. 8). The deck uses `contents`
  everywhere, including the table's caption.
- The video's constructor sets `backIndex = contents.length -1;` (the brief wrote
  `backIndex = initialCapacity`; the same value). Its `dequeue` gets the front through
  `getFront()` (which throws `EmptyQueueException` when empty); 04b reads
  `contents[frontIndex]` directly, as the brief's sketch and the homework's `dequeue` do.
- The homework's `ArrayQueue` (x704–x707) is fixed-size: it has `checkCapacity()`, which
  throws `IllegalStateException` when full, not `ensureCapacity()`; `isEmpty`, `getFront`,
  `dequeue`, `clear` are written; x704/x705 have no `enqueue` (that is the method to fix);
  x706/x707 are non-generic (`String`, `Integer`). The class card says `checkCapacity()`.
- The wrap-up slide's "size field" alternative and `ensureCapacity`'s unwrapping copy are
  in the notes of 04d only; neither is walked.
- The naive shifting `dequeue` on 04 is the deck's own code, not the module's.
- Homework: "Week 8: Queues — Coding Practice", 8 problems at 10 points, `bestQuestions:
  4`, credit 100 until 2026-10-16 23:59:59 (three students to Oct 17), then a credit-0
  practice window to Dec 31 (not on the slide).
- CE 08 "Carrano Deque" (Friday), Project 2 D3 (prototype + tests on 2+ element types, at
  your lab), the 9.1/9.2 modules (Sunday Oct 18): from the brief and DECK-PROMPT §11; in
  11's notes only.

## Status — 2026-10-11, first build

- Written: 16 slides (every manifest entry except `02-course-info` and `17-next-class`,
  which the clock agent wrote into this folder while this deck was built; not touched
  here). `add_sids.py` run on the 16 new slides only; `lint.py` clean on all 18 files.
- Sweep (`timeout -k 5 150 tools/measure/run.sh "$PWD"`, all 18 slides, 02 and 17 present),
  slack at the last step: 01 319 · 01b 110 · 02 36 · 03 322 · 04 36 · 04b 68 · 04c 50 ·
  04d 68 · 04e 366 · 05 13 (inherited from W6D1/W7D2's ring, the same figure there) ·
  06 34 · 06b 156 · 07 90 · 07b 157 · 10 366 · 11 55 · 17 14 (the clock agent's) · 99
  389. No overflow and no clipped code at any step. The vote slides' clocks are reported
  as "over" because they sit in the head band, as on every vote slide since W6D1.
- Sizing changes after the first sweep: 04 merged `n--;` and the null onto one line and
  shortened the call line (slack 12 → 36); 04c's editor 1050 → 1080 px (clipped line);
  07's key discs 56 → 48 px and rows 8 → 6 px (6 → 90); 11 re-laid out as above, its
  class-card label shortened and set at the micro size (−79 → 55).
- Not committed (`git add "week 8 - day 2"` when asked; never `-A`).

## Review — 2026-10-11 (main session, after the three agents)

- `02-course-info` and `17-next-class` are the Day 1 deck's clock with the `now` band on
  Wed–Thu (x 366–603, label at 485), produced by the same clock agent by substitution from
  Day 1's files, so the two decks cannot drift; see Day 1's PLAN.md review for the steps.
  Edit Day 1's clock first, then re-derive.
- `17`'s caption was two lines (slack 14); it is now one line at y 940, "Next week: lists
  and generics. The 9.1 and 9.2 modules are due Sunday." (slack 36).
- `02`'s notes: the homework gap was filled (eight problems, best four count).
- Vote text checked mechanically against the paste (tags stripped, whitespace removed):
  every 25-character window of the stem and options is on the slide.
- Sweep after the review, all 18 slides: no overflow; 17 = 36, 02 = 36, 05 = 13 (the ring,
  as in every deck since W3D1), everything else as in the Status block.
- Still to do by hand: confirm both keys (D, E) in Runestone's results view.
- Not committed (`git add "week 8 - day 2"` when asked; never `-A`).

## Revision — 2026-10-11 (type floor + prose)

The instructor's review: some fonts were too small, and the prose was mannered. Both passes
were applied to every slide and to this file.

**Type floor.** No slide text is below `--t-micro` (28) now, except the `.tlabel` under the
two vote clocks (`--t-tag`, the shared pattern). `--t-micro` is used for labels inside
drawings, signatures and the shared chrome (editor bar, gutter, `.moves__label`). Sentences,
options, tallies, the `%` table and the three tests are at `--t-small` (36) or larger.
`css/deck.css` is unchanged; every override is in a slide `<style>`. Changes per slide:

- 04: the call line and the `n` / `front` values `--t-micro` → `--t-small`.
- 04b, 04c, 04d: pill labels `--t-tag` → `--t-micro`; the pills 140 × 36 → 176 × 40; the
  strip SVG 1110 × 226 → 1152 × 230 (viewBox `-12 0 1152 230`, 12 px each side for the
  wider pills; the 108 px pitch and every translate are unchanged).
- 04b: the caption column 522 → 480 px.
- 04c: the table header `--t-tag` → `--t-small` (on two lines), the rows `--t-micro` →
  `--t-small`, side padding 16 → 8 px. The table no longer fits beside the strip, so the
  table and the captions swapped places: the table is beside the editor (560 px column,
  550 px table) and the captions are beside the strip (480 px).
- 04d: the three tests `--t-code` → `--t-small` (`code-mid` removed from the body, so the
  editor uses the default 36 px with the 96 px gutter; editor 990 → 1150 px); the caption
  column 642 → 490 px; the row gap 32 → 24 px.
- 06, 07: the cell index `--t-tag` → `--t-micro`.
- 07: the seven options `--t-micro` → `--t-small` at line-height 1.3. The line box
  (46.8 px) is under the 48 px disc, so the rows did not grow.
- 06b: the tally `--t-micro` → `--t-small` (line-height 1.6 → 1.4); the verdict
  `--t-micro` → `--t-small`; the pills as above (SVG 1618 × 262).
- 07b: the verdict `--t-micro` → `--t-small`; the pills as above (SVG 898 × 262). The count
  is the `.moves` numeral at `--t-h2`, as before.
- 11: the hints `--t-micro` → `--t-small`, rewritten as one sentence each, and the
  "think about" tag-size label removed; the class card label `--t-micro` → `--t-small`;
  the signpost `--t-micro` → `--t-small` and shortened to "PrairieLearn › Week 8: Queues —
  Coding Practice · best 4 of 8 count · due Friday"; the pills as above; the row gap
  24 → 16 px.

Left at `--t-micro`: the station captions on 05 (labels inside the ring drawing, which has
13 px of slack by design), the clock labels on 02 and 17, the cell indices, the pill labels,
the signatures and the field and method list on 11.

**Prose.** Headings, captions, plants, descriptions, notes, comments and this file were
rewritten as literal statements. Removed: figurative verbs for code and data (walks, lands,
travels, is gone, pile up, turns into a ring), dramatised scale ("at five entries or five
thousand", "whatever the size"), colon-for-effect fragments ("The trap: …", "The fix: …",
"Slot 4. Two."), second-person flourishes in the notes ("watch the pill move", "if you
picture ten slots"), and slogan headings. Vote stems and options, the "Answer: D —" and
"Answer: E —" openings and the video's table are unchanged. Examples:

- 04b caption: "One move per dequeue, at five entries or five thousand." → "One move per
  dequeue, for any number of entries."
- 04c plant: "% turns the strip into a ring: after slot 9 comes slot 0, for both indices."
  → "After slot 9, the next index is 0, for both frontIndex and backIndex."
- 04d heading: "Keep one slot unused, and full stops looking like empty" → "One unused slot
  makes full and empty different"; caption "The fix: the queue is full at nine, and slot 9
  stays unused." → "With slot 9 unused, the queue is full at nine entries."
- 07b caption: "Slot 4. Two." → "Slot 4 holds the second entry."

02 and 17 had their captions rewritten the same way ("Canvas: Weeks 8 and 9 are both
posted." → "Weeks 8 and 9 are both posted on Canvas."). They now differ from the Day 1
clock they were derived from. Apply the same caption edits to Day 1's 02/17, or re-derive
these from Day 1, before either deck changes again.

**Checks.** `lint.py` clean on all 18 files. Sweep (`timeout -k 5 150 tools/measure/run.sh
"$PWD"`), lowest slack over all steps: 01 319 · 01b 55 · 02 36 · 03 278 · 04 56 · 04b 64 ·
04c 64 · 04d 36 · 04e 366 · 05 13 (the ring, by design) · 06 34 · 06b 81 · 07 90 · 07b 78 ·
10 366 · 11 37 · 17 36 · 99 389. No overflow and no clipped code at any step; the only
"over" entries are the vote clocks in the head band, as before.

## Clock re-derived — 2026-10-11 (after the two prose passes)

- `02-course-info` and `17-next-class` were regenerated from the Day 1 deck's revised files
  by substitution (now band x 366–603, label at 485; "Wednesday and Thursday" in the desc,
  comment and aria text), keeping this deck's notes and 17's caption. The two decks' clocks
  are identical again apart from those parts. Edit Day 1's first, then re-derive.
- Sweep after the re-derivation: 02 = 36, 17 = 36, the rest as in the Revision block.

## Bridges — 2026-10-11

The instructor: the lecture flow lacked "bridges from last week and then between day 1 and
2". Two slides here and one in Day 1 (`02b-bridge-stack`), plus one sentence in 04's notes.

- **02b-bridge-linked** (`#slide-02b`, after `02-course-info`). Kicker `FROM DAY 1 TO DAY 2`,
  h2 "The same queue, stored in an array instead of a chain". One SVG (1664 × 250): left,
  Day 1's chain A → B → C with `firstNode` and `lastNode` (W8D1 04c's 130 × 76 boxes, no
  field labels); centre, `enqueue(x)`, `dequeue()`, `getFront()`, `isEmpty()`, `clear()` in
  mono at `--t-small`; right, a ten-slot strip with A–C in slots 0–2, `frontIndex` above
  slot 0 and `backIndex` below slot 2. **The strip is 72 px cells on an 80 px pitch**, not
  04b's 96/108: at 96/108 the three parts need about 2030 px of the 1664. Press 1: the
  chain grows in, the operations fade in, caption "Day 1 stored the queue on a linked
  chain, with firstNode at the front and lastNode at the back." Press 2: the strip grows
  in, caption "The operations are the same and the storage is different. The two
  references are replaced by two indices." (it stays). Press 3: "The queue is the third ADT
  stored two ways. ArrayBag and LinkedBag were Weeks 3 and 4, and ArrayStack and
  LinkedStack were Week 5." Press 4, in display maroon: "On a chain, dequeue moved
  firstNode. What does dequeue do to the array?" The brief's wording was rephrased to drop
  colon fragments. Notes end "Part 1 starts with the obvious design and counts its moves."
- **16-next-week** (`#slide-16`, before `17-next-class`). Kicker `NEXT WEEK`, h2 "Stacks and
  queues work at the ends. A list works anywhere." A table: stack (the top · the top ·
  Week 5), queue (the back · the front · Week 8, Days 1 and 2), deque (both ends · both
  ends · Week 8, Day 1), static; press 1 the list row (any position · any position ·
  Week 9, the 9.1 module, due Sunday) grows in with the orange tint, and the caption "Week
  9 puts a list on a chain and on an array, the fourth pair." fades in after it. Notes end
  "Next: the calendar."
- **04-walk-shift** notes: after "This design keeps the front of the queue at slot 0." the
  sentence "It is the stack from Week 5 with its top at slot 0, which shifted every entry on
  each push and pop, and it has the same cost."
- `add_sids.py` on the two new files only; `lint.py` clean on all 20. Sweep: 02b slack 144,
  16 slack 98 at their last steps; no overflow; the other slides unchanged.
- Not committed.

## Cross-browser — 2026-10-11

- Audit of css/, js/ and every slide: the decks use `:has()` (Chrome 105, Safari 15.4,
  Firefox 121 and later), `color-mix()` (Chrome 111, Safari 16.2, Firefox 113), variable
  WOFF2 fonts, `transform-box`, `clip-path: inset()`, dash-offset Creates and `fetch`
  (an HTTP server is required; `file://` has never worked). All current Chrome, Edge,
  Firefox and Safari releases render those alike. `text-wrap: pretty` is progressive.
- Fonts: `--font-body` and `--font-display` were system fonts (Verdana, Georgia) that
  are not installed on the authoring machine, where fontconfig substitutes Nimbus Sans and
  Nimbus Roman and every layout was measured. Real Verdana and Georgia are 10–15% wider,
  so Mac and Windows would wrap captions differently. Liberation Sans and Liberation
  Serif (OFL 1.1, metric-compatible with the Nimbus substitutes: 19.46 vs 19.33 px per
  character at 36 px) are now bundled in `assets/fonts/` as WOFF (1.6 MB per deck) and
  lead both stacks in `tokens.css`; the system fonts remain as fallbacks. The sweep after
  the change reports the same slack on every slide.
- Safari ignores the CSS `d` property, so the arrow swings written as `:has(...) .ref {
  d: path(...) }` never applied there. Each swung arrow now also carries
  `data-swing='[[step,"path"],…]'`, and `js/deck.js` sets the `d` attribute from it when
  `CSS.supports('d', …)` is false (the picture is right; the motion is not animated).
  Verified in headless Chromium with the support check forced off: the enqueue walk's
  `lastNode` arrow sits on the step-8 and step-11 paths at those steps.
- Not covered: the Week 4, 5 and 7 decks have the same system-font stacks, and W4D1 and
  W5D1 have swings without `data-swing`.
