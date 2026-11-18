# Week 12 · Day 2 — plan

Planned 2026-11-07 for Wednesday Nov 11 (MW, NCB 320) and Thursday Nov 12 (TR, Squires):
one deck, both sections. Week 12 (Nov 9–13) is "Team Project Work": no test, no challenge
exercise, no project deliverable. Next week (Nov 16–20) is Cloning and Trees. Shared
css/js/assets/tools were cloned from `week 11 - day 1`. Three builders: B (`index.html`
manifest and every slide except 02, 16 and 17), A (Day 1's deck), C (02, 16, 17, this
PLAN.md skeleton; Day 1's 02 and 17). Sources: the shared brief `w12-brief.md` and outlines
`w12-outlines.md` (session scratchpad), including the Runestone paste of 2026-11-07 for
both votes (quoted verbatim, "Q-1: " dropped); `DECK-PROMPT.md`; the PL course repo
`~/Projects/pl-vt-cs2114` (twins named per slide); the 10.2 insertion sort reading and
SelectionSort.pdf (code via the brief); the earlier decks named per slide below. Never
`canvas-banks/*`.

## Through-line

**"Both sorts walk the same five entries; insertion sort shifts larger entries right until
the held value fits, selection sort finds the smallest and swaps it into place; both make
about n²/2 compares, selection sort makes n swap calls, and the rows of a trace show which
one ran."**

| part | title (divider and tab) | slides | time |
|---|---|---|---|
| — | title, today, clock, bridge, peer-plus | 01 · 01b · 02 · 02c · 05 | 6 min |
| 1 | Insertion sort shifts entries right to make room | 03 · 04 · 04b · 04c · 06/06b | 16 min |
| 2 | Selection sort finds the smallest and swaps it into place | 07 · 08 · 08b · 09/09b | 15 min |
| 3 | What the two sorts cost, and next week | 10 · 11 · 16 | 4 min |
| — | next class clock, closing | 17 · 99 | 1.5 min |

The structural link (02c): Day 1 searched an array that was already in order; today's
array 64 25 12 22 11 is not, and sorting is what puts it in order.

## Manifest

| file | owner | role |
|---|---|---|
| 01-title | B | title card; kicker `CS 2114 · FALL 2026 · WEEK 12 · DAY 2` |
| 01b-today | B | three columns: a strip with one value raised over a gap · a strip with two values crossing · a three-row cost grid; captions = the three divider titles |
| 02-course-info | C | the Week 12/13 clock, `now` Wed–Thu; seven steps |
| 02c-bridge-sorted | B | FROM DAY 1 TO DAY 2: Day 1's strip with the stop on 12, then 64 25 12 22 11 |
| 03-chapter-1 | B | PART 1 OF 3 · Insertion sort shifts entries right to make room |
| 04-walk-insert-one | B | insertInOrder(data, 1): one compare, one shift |
| 04b-walk-insert-rest | B | the three remaining passes: ten compares, nine shifts |
| 04c-walk-insert-sorted | B | sorted input: four compares, no shifts |
| 05-peer-plus | B | the routine ring, `Peer Instruction W12D2` |
| 06-vote-rows | B | VOTE 1, static, clocks (vtcs2_sorting_insertionSort), key A |
| 06b-walk-rows | B | VOTE 1 · THE ANSWER: each row is one insertInOrder; B, C, D struck |
| 07-chapter-2 | B | PART 2 OF 3 · Selection sort finds the smallest and swaps it into place |
| 08-walk-select-one | B | findSmallest and one swap: four compares, one swap |
| 08b-walk-select-rest | B | the remaining passes: ten compares, five swap calls |
| 09-vote-selection | B | VOTE 2, static, clocks 120 / 150 (vtcs2_sorting_selectionSort_2, select all), key B and D |
| 09b-walk-selection | B | VOTE 2 · THE ANSWER |
| 10-chapter-3 | B | PART 3 OF 3 · What the two sorts cost |
| 11-cost-table | B | insertion worst / insertion sorted / selection / library sorts |
| 16-next-week | C | Week 13 · Cloning and trees: a Link box beside a tree node; the Week 13 card |
| 17-next-class | C | the same clock as 02, static; caption "Next week is Cloning and Trees. The 13.1 and 13.2 modules are due Sunday Nov 15." |
| 99-closing | B | dusk (copy W11D1 99) |

File numbers are sort keys; the manifest order in `index.html` is the order on screen.

## Slide by slide (C)

- **02 / 17.** W11D1's clock moved one week, with the two-week layout of W9D2 02 (deadlines
  in both weeks). `now` band Wed–Thu x 366–603, `now` at 485. No test band. Rows: modules y 496 (Sunday), homework
  y 568 (Friday), CE y 640 (Friday), project y 712 (lab). Steps: 1 Canvas bracket
  `Week 12 · this week` (centred x 544; no Redo band to avoid) / `Week 13 · next week` /
  stone `Week 14 →`; 2 homework "Week 12: Mid-Semester Review" (blue) to the Friday pole
  x 722 (Nov 13); 3 caption only (no CE, no deliverable; the Week 12 CE and project rows
  stay empty); 4 "13.1 + 13.2 modules · due Sunday evening" from Week 12's Monday to the
  Sunday pole and due tick at x 960 (Nov 15); 5 "Week 13: Semester Review" (blue) and
  "CE 13 · Binary Tree" (maroon, `wk__ink--ce` as W9D2) to the Friday pole x 1554 (Nov 20);
  6 "Project 3 · Deliverable 4" in accent-2, solid Monday x 960–1079 plus the fading
  Tue–Fri tail, range M1079 818 H1554 labelled "your Week 13 lab" (x 1257, as W9D2); 7 the
  two tiles. Captions measured with PIL (Liberation Serif 36 px), widest 1,378 px.
  The outline's "solid Monday x 1079–1198" is Tuesday on the §11 grid (a tick marks the
  end of its day); the bar uses W9D2's Week-two Monday, 984..1079 after the rounded cap.
  17 is derived from 02 by a script substitution, W11D1's recipe (sids dropped, ` frag`, `data-step`
  and `data-anim` stripped, the caption group replaced by one caption, new h2 "Before next
  class", desc and notes): edit 02 first, then re-derive and run `add_sids.py`. Both decks' 02 come
  from one template (only the now band, desc and notes differ). 17's caption: "Next week is Cloning and Trees. The 13.1 and
  13.2 modules are due Sunday Nov 15."
  Sweep (run3, last step), Chromium / Firefox / WebKit: 02 36/35/36, 17 36/35/36; no flags.
- **16.** W9D2 16's grammar: kicker NEXT WEEK, h2 "Week 13 covers cloning and trees". Left:
  "Week 13 · Cloning and trees" (display maroon, body size); a 1000 × 260 SVG at 1:1 with a
  list node `data | next` (W11D1 06b's box ink, widened to 260 so the field names fit above
  the fields at micro; value 12 at small mono; one blue arrow out of next) beside a tree
  node `left | data | right` (390 wide, two arrows down-left and down-right; marker
  `w12d2-16-head`); caption "A list node has one next reference. A tree node has two."; due
  line "The 13.1 Cloning and 13.2 Trees modules are due Sunday, Nov 15." Step 1: the Week 13
  card grows in (plain 3 px `--fg-1` outline on `--bg-1`, not the dashed test band): "Week
  13" · "Week 13: Semester Review homework, Fri Nov 20" · "CE 13 · Binary Tree, Fri Nov 20" ·
  "Project 3 Deliverable 4, the second prototype with tests, at the start of your lab".
  Sweep: slack 175 in all three engines.

## Unverified (C)

- "Weeks 12 and 13 are both on the Canvas calendar" (02 step 1) is carried over from W11D1,
  which already flagged it as unconfirmed for the following week.
- CE 13's due time: the brief gives Friday Nov 20 only, so the caption and notes say
  "Friday Nov 20" for CE 13 and "11:59 PM" only for the homework and the modules.
- DECK-PROMPT §11 (instructor, 2026-11-02) says nothing is due during Week 12; the brief
  (2026-11-07) has the Week 12: Mid-Semester Review homework due Fri Nov 13, and the clock
  follows the brief. §11 should be updated if the brief is right.
- The Week 13 Day 1 dates in Day 2's 16/17 notes (Mon Nov 16 MW / Tue Nov 17 TR) follow the
  section pattern; no Week 13 deck exists yet.

## Slide by slide (B)

Built 2026-11-07. The six walk slides (04, 04b, 04c, 06b, 08, 08b, 09b) were generated by
Python scripts in the session scratchpad (`gen/s04.py` … `s09b.py`), so that each value's
cumulative position per step is computed rather than typed; later edits can be made by hand
in the HTML. Sweep (run3, last step; Chromium / Firefox / WebKit): 01 319 · 01b 110 · 02c
300 · 03 322 · 04 47/47/47 · 04b 58 · 04c 58 · 05 36/35/36 · 06 90/89/90 · 06b 148 · 07 322
· 08 58 · 08b 58 · 09 80/79/80 · 09b 64 · 10 366 · 11 105/106/105 · 99 389. No overflow and
no clipped code lines in any engine; the only flags are the vote timers above y 95 on 06 and
09, which the W11D1 vote slides share. WebKit timed out twice and ran after
`pkill -x MiniBrowser; pkill -x Xvfb`.

- **01 / 01b / 99.** W11D1's title and closing; 01b's three drawings: a strip with 25
  raised over the gap it left (orange edge), a strip whose first and last cells (orange)
  exchange along two arcs, a three-row table reading n², n², n log n. Captions = the
  divider titles (Part 3's is "What the two sorts cost").
- **02c.** One SVG 1664 × 200: Day 1's strip 3 5 8 12 15 20 24 30 (cells read blue, 12
  maroon, a maroon stop bar after it, 15–30 in stone), then 64 25 12 22 11. Three presses as
  in the outline.
- **03 / 07 / 10.** Dividers.
- **04.** 6 steps as in the outline. 13-line editor (the reading's code, modifiers and the
  for loop's braces left out as in the brief) at --t-code, 900 px; right column 732 px: the
  call, `unsorted = — → 25 · j = — → 0 → −1` (crossfades), counters **compares** and
  **shifts** side by side, the strip (cells 96 on 108, held cell dashed one pitch above slot
  i labelled `unsorted`, i pill above, j pill below, a stone −1 index left of slot 0), the
  captions. 25 rises by translateY(−108), 64 moves +108, 25 drops diagonally into slot 0.
  Plant on step 6.
- **04b.** 11 steps: the outline's 10 plus the plant on its own press. i pill and held cell
  move one pitch per call; j pill appears at its first slot. Step 9 staggers the four
  compares/shifts 0.45 s apart; the j pill goes from 0 to −1 at the end of that press (it
  cannot visit 3, 2, 1 inside one press). Counters 1/1 → 10/9.
- **04c.** 5 steps. Each call's whole body is one held block; the value rises into the held
  cell and drops back into its own slot (two nested groups, so one press can go up and down
  and a back-step reverses it). Compares 1 → 4, shifts a static 0.
- **05.** W11D1 05b with `Peer Instruction W12D2`; plant "Both questions ask how insertion
  sort and selection sort differ in what they move." set in the body face (82 characters,
  1,288 px; the outline's wording is 88 characters and in mono would not fit one line).
- **06.** Static vote: the stem as the lede (one line, max width lifted), the five rows
  verbatim as a 5 × 5 grid of 64 px cells on 72, "Which sorting algorithm is this?" under it,
  A–D at the body size. Timers 90/150. h2 ends at x 1091.
- **06b.** 8 steps. Four 5 × 5 grids in a row: the vote's rows (A) and the rows that
  selection, bubble and merge sort would produce on the same input, each growing in with its
  first differing row edged maroon and its label struck. Steps 1–4 colour the vote's rows
  (moved cells blue for the press, sorted prefix washed). Step 8 `.verdict`.
- **08.** 8 steps. Editor 916 px. smallestIndex pill (240 × 40) under the strip; at the
  return it fades and an rh pill fades in at the same place (below, not above slot 4 as in
  the outline, so that rh and lh never overlap when rh = lh on 08b). The swap: 64 rises into
  the dashed temp cell, travels right and drops into slot 4 while 11 dips into the lane under
  the indices, travels left and rises into slot 0, on one press (three nested groups per
  value; nothing passes over another value). Counters **compares** 0 → 4 and **swaps**
  0 → 1 (swaps in the blue of a count that stays small).
- **08b.** 11 steps: lh = 1 (three presses, the return with the last compare), swap + lh++;
  lh = 2 (two), swap + lh++; lh = 3 (one), swap(3, 3) + lh++; lh = 4 (no compare,
  swap(4, 4)); plant. Self-swaps are drawn as the value rising into temp and dropping back.
  The bar covers lines 2–4 as one block on the swap presses. Counters 4/1 → 10/5.
- **09.** Static vote, W11D1 07's full-width long options, five options one line each,
  timers 120/150. h2 ends at x 1140.
- **09b.** 6 steps, no editor: 08's strip at the start of 08b beside a 560 px inset. 1 B:
  three maroon compare arcs; 2 D: the swap of 25 and 12 (slot 1 washed); 3 A: a dashed arc
  from 25 back to 11 with a maroon cross; 4 C: caption only; 5 E: the inset from 04 (64
  moving from j to j + 1); 6 `.verdict`. No counter: code-walk.js only scans sections with an
  `.editor__pc`, so the three compares are in the caption.
- **11.** One table, one row per press, plant on step 5. Columns: sort · compares · shifts or
  swaps · growth · n = 5, walked (04b 10 and 9, 04c 4 and 0, 08b 10 and 5). The library row
  has no formulas.

Deviations from the outline, and why:
- The walk slides 04, 04b, 04c, 08 and 08b have no kicker and the strip sits in the right
  column, not under both columns: each editor is 13 lines at --t-code (about 710 px with its
  bar), which leaves no room under it; without the kicker the right column ends with 47–58 px
  of slack.
- Selection code: `array` is renamed `a` (DECK-PROMPT §13, shorten names to make code
  larger), `private` is dropped, findSmallest's for braces are dropped and the code is
  re-indented at 2 spaces, so the widest line is 43 characters (with `array`, line 3 needs a
  1,070 px editor and the strip no longer fits beside it). swapElements is not in the editor
  (18 lines would not fit at --t-code); its three statements are in 08's step-7 caption and
  in the notes, and the temp cell carries them.
- Outline errors corrected from the code: 04b step 8 puts 22 in slot 1, not slot 2 (Vote 1's
  fourth row is 12 22 25 64 11); 06b step 3 has 22 at index 1; 08 step 5 compares 11 < 12
  (the smallest so far), not 11 < 22; 09b's arcs are 25–12, 12–22, 12–64, not 25–12, 25–22,
  25–64.
- 06b's merge sort: the outline split 64 25 | 12 22 11. The textbook's mergeSort splits at
  mid = first + (last − first) / 2 = 2, so it sorts 64 25 12 first and its rows 2 and 3
  match the vote's; its row 4 (12 25 64 11 22) is the first that differs, and the caption
  says so. All three wrong options are drawn as full five-row traces rather than one row.
- Two `.moves` counters on one slide work without engine changes: code-walk.js `build()`
  collects every `.heap-obj__field` old/new pair in a section with an `.editor__pc`, and each
  `.moves__stack` hides its own superseded pairs (sibling combinators), so both roll.
- Swap back-steps: the end state of every step is exact, but a reversed swap travels through
  the other lane (the destination rule's delays run the vertical moves in forward order).

## Unverified (B)

- Vote keys A (Q1) and B, D (Q2) come from the brief and the PL twins; confirm in Runestone.
- 06b's merge sort rows assume the textbook's mergeSort split; the course has not shown merge
  sort code. Bubble sort's rows assume the left-to-right neighbour pass.
- 07's notes cite "the course's SelectionSort slides" (`clientFilesCourse/slides/
  SelectionSort.pdf`); which module page links them was not checked.
- 11's library row (Arrays.sort, Collections.sort, O(n log n)) is the brief's statement; the
  slide gives no formula for their compares or moves.
- 02c's Day 1 strip (3 5 8 12 15 20 24 30, contains(9)) matches Day 1's 04-walk-miss as
  built on 2026-11-07; if Builder A changes that strip, 02c must follow.
- Not seen in a browser (no screenshots): the motion timing of the staggered press on 04b
  step 9, the swaps on 08/08b/09b, and the counters rolling. The sweep checks layout only.

## Review (main session, 2026-11-07)
- Verified: lint clean; the vote texts match the Runestone paste (only "Q-1: " dropped);
  three-engine sweep (Chromium, Firefox, WebKit) with no overflow or clipping.
- Prose pass at the instructor's request ("banish AI, mannered prose"): plants and notes
  rewritten as full sentences (D1 04, 04b, 05, 06b, 06c h2, 11 h2; D2 04b, 04c, 06b notes,
  08b). Verdict-strip labels stay short, as on every earlier deck.
- D2 06 and 09 had two lines of CSS outside the style block, visible as text; removed.
- Open for the instructor: the four keys (D1 C, A; D2 A, B+D) in Runestone's results view;
  (resolved 2026-11-09: the instructor confirmed Project 3 Deliverable 3 is due at the Week 12
  lab; 02/17 now draw it as a blue Project 3 bar over "your lab day" on step 3, with the
  caption, desc and notes changed to match).
