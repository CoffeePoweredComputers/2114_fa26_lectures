# Week 12 · Day 1 — plan

Planned 2026-11-07 for Monday Nov 9 (MW, NCB 320) and Tuesday Nov 10 (TR, Squires): one
deck, both sections. Week 12 (Nov 9–13) is "Team Project Work": no test, no challenge
exercise, no project deliverable. The next class for each section is Day 2, sorting an
array (MW Wed Nov 11 / TR Thu Nov 12). Shared css/js/assets/tools were cloned from
`week 11 - day 1`. Three builders: A (`index.html` manifest and every slide except 02 and
17), B (Day 2's deck), C (02, 17, this PLAN.md skeleton; Day 2's 02, 16, 17). Sources: the
shared brief `w12-brief.md` and outlines `w12-outlines.md` (session scratchpad), including
the Runestone paste of 2026-11-07 for both votes (quoted verbatim, "Q-1: " dropped);
`DECK-PROMPT.md`; the PL course repo `~/Projects/pl-vt-cs2114` (twins named per slide);
the 11.2 module's slide PDFs and textbook ch. 17 (via the brief); the earlier decks named
per slide below. Never `canvas-banks/*`.

## Through-line

**"A sorted list may stop a search at the first entry larger than the one sought, because
the order says where it would have to be; the same order is what an inherited add(int, T)
or set(int, T) lets a client destroy, so the textbook's revised base class hides those
methods from clients."**

| part | title (divider and tab) | slides | time |
|---|---|---|---|
| — | title, today, clock, bridge, peer-plus | 01 · 01b · 02 · 02c · 05 | 6 min |
| 1 | Searching a sorted list | 03 · 04 · 04b · 06/06b/06c | 15 min |
| 2 | What an inherited method lets a client do | 07 · 08 · 08b · 09/09b | 15 min |
| 3 | What each design costs | 10 · 11 | 3.5 min |
| — | next class clock, closing | 17 · 99 | 1.5 min |

The structural link (02c): last week's sorted add stopped at the first larger node; an
array holds the same order, and today's first question is whether contains may stop there
too.

## Manifest

| file | owner | role |
|---|---|---|
| 01-title | A | title card; kicker `CS 2114 · FALL 2026 · WEEK 12 · DAY 1` (copy W11D1 01) |
| 01b-today | A | three columns: a strip with a maroon stop mark · two UML boxes with a generalisation arrow · a 3×3 cost grid; captions = the three divider titles |
| 02-course-info | C | the Week 12/13 clock, `now` Mon–Tue; seven steps |
| 02c-bridge-stop | A | FROM WEEK 11 TO WEEK 12: the chain stop on 12, the same values as an array, "Does contains(10) have to look past 12?" |
| 03-chapter-1 | A | PART 1 OF 3 · Searching a sorted list |
| 04-walk-miss | A | the List contains loop on `sorted.contains(9)`: eight compares |
| 04b-walk-hit | A | the same loop on `sorted.contains(12)`: found stops it at four |
| 05-peer-plus | A | the routine ring, `Peer Instruction W12D1` |
| 06-vote-contains | A | VOTE 1, the stem and the loop (vtcs2_sortedLists_contains_2_202507), static, no clocks |
| 06a-vote-contains-opts | A | VOTE 1, the question and options A–E, clocks; key C |
| 06b-walk-contains | A | VOTE 1 · THE ANSWER: the early-exit loop (the deck's own code) |
| 06c-walk-distractors | A | VOTE 1 · THE OTHER OPTIONS: B, D, E, A in turn, then the verdict |
| 07-chapter-2 | A | PART 2 OF 3 · What an inherited method lets a client do |
| 08-walk-inherited | A | `sorted.add(2, 25)` and `sorted.replace(1, 30)` break the chain's order |
| 08b-walk-revised | A | LinkedChainBase<T> with protected inserts; LListRevised and LinkedSortedList as siblings |
| 09-vote-risk | A | VOTE 2, static, clocks (vtcs2_sortedLists_risks_202507), key A |
| 09b-walk-risk | A | VOTE 2 · THE ANSWER |
| 10-chapter-3 | A | PART 3 OF 3 · What each design costs |
| 11-cost-table | A | from scratch / composition on an array list / composition on a linked list (Fig. 16-9) |
| 17-next-class | C | the same clock as 02, static; caption "Next class is Day 2: sorting an array." |
| 99-closing | A | dusk (copy W11D1 99) |

File numbers are sort keys; the manifest order in `index.html` is the order on screen.

## Slide by slide (C)

- **02 / 17.** W11D1's clock moved one week, with the two-week layout of W9D2 02 (deadlines
  in both weeks). `now` band Mon–Tue x 128–366, `now` at 247. No test band. Rows: modules y 496 (Sunday), homework
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
  from one template (only the now band, desc and notes differ). 17's caption: "Next class is Day 2: sorting an array."
  Sweep (run3, last step), Chromium / Firefox / WebKit: 02 36/35/36, 17 36/35/36; no flags.

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

## Slide by slide (A)

Manifest change: Vote 1 is two slides, `06-vote-contains` (stem sentences, the loop at
--t-code, the question sentence; static, no clocks) and `06a-vote-contains-opts` (the
question sentence, A–E, the 90/150 clocks). The 1,030 px editor plus five options at
--t-small measured about 1,100 px against a 685 px body (options are 7 lines at 1,584 px,
18 lines beside the editor; PIL, Liberation Sans 36), so it follows W9D2 07/07a's split.
`index.html` has 21 entries; the manifest table above still lists 06 alone.

- **01 / 03 / 07 / 10 / 99.** Copies of W11D1 01, 05, 99 with this deck's kicker, titles,
  descs and notes.
- **01b.** W11D1 01b grammar, one column per press: eight cells with the fourth edged maroon
  and a maroon stop bar after it (orange direction arrow above); a base box over two boxes
  with a blue generalisation bus and hollow triangle; a 3 × 3 grid with a maroon last column.
- **02c.** 1664 × 260 SVG. 1: W11D1 06b's chain with 10 waiting (orange) under the 7–12 gap,
  a currentNode key, the ring moving 312 px 3 → 12. 2: strip 3 7 12 20 and a stone card
  `contains(10)`; caption 2 replaces caption 1 and stays. 3: maroon question. 3 steps.
- **04.** No kicker (the 11-line editor plus the strip need the 68 px). Q1's loop verbatim,
  1,030 px, line-height 1.15; right column: call, `numberOfEntries = 8` / `index · found`,
  compares counter, captions; strip 3 5 8 12 15 20 24 30 under both with the index pill.
  7 steps: init; 3, 5, 8, 12 one per press; 15–30 staggered in one press; return false + plant.
  Deviation: after the eighth pass the pill sits one pitch past slot 7 (index = 8, where the
  while test fails), not on slot 7.
- **04b.** Same layout, `contains(12)`. 7 steps: init; 3; 5; 8; 12 equals (found crossfades
  to true, cell blue); index 4 and the while test fails on `!found`; return true + plant
  ("A hit stops the loop at the entry, here after four compares. A miss has nothing to stop
  on. That is Vote 1.").
- **05.** W11D1 05b with `Week 12` / `Peer Instruction W12D1`; the 82-character plant is set
  in the body face (1,317 px; mono would be 1,771 px).
- **06 / 06a.** As above. Both h2 "How can contains run faster on a SortedList?" end at x
  1,137 (PIL, Liberation Serif 56). 06a options at --t-small, 56 px discs, 8 px rows.
- **06b.** VOTE 1 · THE ANSWER. The deck's own early-exit loop (no source ships one; the 11.2
  module states it in prose): `boolean past = false;`, `while (!found && !past && (index <
  numberOfEntries)) {`, `int c = list[index].compareTo(anEntry);`, `if (c == 0) found =
  true;`, `else if (c > 0) past = true;`, `else index++;` as walkline--new. Deviation: the
  editor shows the method body only (bar says so), ten lines at line-height 1.1, so the
  kicker, the editor and the strip fit (slack 31–32). 7 steps: init; 3; 5; 8; 12 > 9, past
  true, cell maroon and the stop bar Created; return false + plant; contains(12), cell blue,
  found true.
- **06c.** VOTE 1 · THE OTHER OPTIONS. An option card (letter, call, rule in mono) and the
  counter (reset to 0 per run, then rolls) over the strip; 5 steps: B on contains(12) (one
  compare, maroon cross on 12); D (pill appears on slot 7 and moves to 0, cells right to
  left, 8); E (lo above from 0, hi below from 7, meet in the middle, 8); A (card
  `return indexOf(anEntry) >= 0;`, index pill 0 → past the end, 8); verdict under the strip.
  The hi pill is below the strip (two 176 px pills cannot share a 108 px pitch).
- **08.** No kicker. Left: two client lines (`sorted.add(2, 25);`, `sorted.replace(1, 30);`)
  and captions; right: W11D1 06b's chain at 1:1. 6 steps as the outline; positions from 1
  (textbook LList); 3 → 30 is a Created maroon strike, then crossfade. Caption 4 says the
  vote calls this method set(int, T).
- **08b.** No kicker. 1664 × 546 SVG: abstract `LinkedChainBase<T>` (italic) with the six
  brief members and a stone "other members omitted" line, the two protected inserts in blue;
  `LListRevised<T>` left and `LinkedSortedList<T>` right beside the base's lower half, each
  generalisation line Created into the base's side, triangle after. 4: stone card
  `sorted.add(2, 25);` top right, maroon strike Created. 5: code card under the sorted box
  (`nodeBefore = getNodeBefore(newEntry);` / `addAfterNode(nodeBefore, newNode);`, --t-code).
  6: plant. Captions crossfade in one cell.
- **09.** VOTE 2, three options verbatim at the vote body size (80 px discs; at --t-small they
  were one line each and left 358 px). h2 ends at x 1,148. Clocks 90/150.
- **09b.** VOTE 2 · THE ANSWER. Left: three client lines under the PC bar, the nodes visited
  counter, the verdict (step 4); right: the chain and captions. 1 A: add(2, 25) in one press
  (grow, Created next, swing, maroon ring); 2 B: 25 fades, 3's next swings back, the
  currentNode ring walks 3 → 12, counter 0 → 3; 3 C: 7 and its link fade, 3's next swings
  over to 12; 4 verdict. Deviation: C is `remove(2)` (positions from 1, as on 08), not the
  outline's `remove(1)`, so that it removes 7.
- **11.** Grid table (method 560 px + three design columns), O(n²) in bold maroon; rows fade
  in on 1 and 2, the caption on 3, the Week 14 line (display maroon) on 4.

Sweep (run3, last step; Chromium / Firefox / WebKit, WebKit on the data-swing path):
01 319/319/319 · 01b 166 · 02c 240 · 03 366 · 04 36/35/36 · 04b 36/35/36 · 05 36/35/36 ·
06 81 · 06a 131/131 (Chromium/Firefox after the row-padding fix; 29 in all three before) · 06b 32/31/32 · 06c 84 ·
07 322 · 08 319 · 08b 49 · 09 60/60 (Chromium/Firefox after the body-size change; WebKit timed out three times on the re-run, so 06a and 09 are unmeasured there after the change) · 09b 40 · 10 366 ·
11 121 · 99 389. No overflow or clipping flags apart from the vote timers above the body.

## Unverified (A)

- Vote 2's key A is from the PL twin `sortedlists_inheritance`; confirm in Runestone.
- 06b's early-exit loop is the deck's own code (the module states the idea only in prose).
- 08b: the members of `LinkedChainBase` other than the six shown are not in any course
  source; the slide says they are omitted. That the textbook's LinkedSortedList keeps
  `remove(givenPosition)` (09b notes) is inferred from the brief, not checked in ch. 17.
- 11: the from-scratch chain's O(n) for add and contains is the deck's own reading of the
  W11D1 07b design; only the composition columns are from Fig. 16-9.
- Positions on 08/09b are 1-based (textbook LList); Runestone's remove(int index) in Vote 2
  does not say which base it uses.

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
