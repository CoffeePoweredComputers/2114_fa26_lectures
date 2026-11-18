# Week 13 · Day 1 — plan

Planned 2026-11-14 for Monday Nov 16 (MW, NCB 320) and Tuesday Nov 17 (TR, Squires): one
deck, both sections. Week 13 (Nov 16–20) is "Cloning & Trees"; the deck covers trees only
(instructor), and there is no test. Due this week: the homework "Week 13: Semester Review —
Coding Practice" (Fri Nov 20, 11:59 PM), CE 13 · Binary Tree (Fri Nov 20) and Project 3
Deliverable 4 (start of your lab). Thanksgiving break follows (Nov 21–29). The next class
for each section is Day 2, traversals (MW Wed Nov 18 / TR Thu Nov 19). Shared
css/js/assets/tools were cloned from `week 12 - day 2`. Three builders: A (`index.html`
manifest and every slide except 02 and 17), B (Day 2's deck), C (02, 17, this PLAN.md
skeleton; Day 2's 02, 16, 17). Sources: the shared brief `w13-brief.md` and outlines
`w13-outlines.md` (session scratchpad), including the Runestone paste of 2026-11-14 for both
votes (quoted verbatim, "Q-1: " dropped); `DECK-PROMPT.md`; the PL course repo
`~/Projects/pl-vt-cs2114` (twins named per slide); the 13.2 module videos (BinaryTreesIntro,
IntroToTraversals, ProgrammingTrees) and CE 13 via the brief; the earlier decks named per
slide below. Never `canvas-banks/*`.

## Through-line

**"A binary tree node has at most two children, so each level of a tree whose nodes all have
0 or 2 children and whose leaves share a level holds twice as many nodes as the level above;
height counts levels; and the same recursion that visits every node counts them and measures
that height."**

| part | title (divider and tab) | slides | time |
|---|---|---|---|
| — | title, today, clock, bridge | 01 · 01b · 02 · 02c | 5 min |
| 1 | Tree vocabulary | 03 · 04 · 04b | 9 min |
| 2 | Height and number of nodes | 05 · 06 · 06c · 07/07b/07c · 08/08b | 20 min |
| 3 | Trees in code | 09 · 10 · 10b · 10c | 7 min |
| — | next class clock, closing | 17 · 99 | 1.5 min |

## Manifest

| file | owner | role |
|---|---|---|
| 01-title | A | title card; kicker `CS 2114 · FALL 2026 · WEEK 13 · DAY 1` |
| 01b-today | A | three columns: the A–H tree · the 7-node two-children tree · a `BinaryNode` box; captions = the three divider titles |
| 02-course-info | C | the Week 13 / Thanksgiving break clock, `now` Mon–Tue; nine steps (step 4 = the ethics discussion, due Fri Nov 20, added 2026-11-15) |
| 02c-bridge-hang | A | FROM WEEK 12 TO WEEK 13: the chain 3 7 10 12 20, the same values hung as a tree, "How many nodes can a tree of a given height hold?" |
| 03-chapter-1 | A | PART 1 OF 3 · Tree vocabulary |
| 04-walk-words | A | the A–H tree in the centre, built one term per press, each term written on the part it names |
| 04b-walk-height | A | levels, the height convention, a four-node chain of height 4 |
| 05-chapter-2 | A | PART 2 OF 3 · Height and number of nodes |
| 06-walk-levels | A | the votes' shape level by level, per-level counts 1 · 2 · 4 only |
| 06c-peer-plus | A | the routine ring, `Peer Instruction W13D1` |
| 07-vote-height | A | VOTE 1 (vtcs2_trees_height_202601), static, clocks; key D |
| 07b-walk-height-answer | A | VOTE 1 · THE ANSWER: sums, n = 2^h − 1, h = log2(n + 1) |
| 07c-walk-height-others | A | VOTE 1 · THE OTHER OPTIONS, tested on n = 7 and n = 15 |
| 08-vote-size | A | VOTE 2 (vtcs2_trees_size), static, clocks; key A |
| 08b-walk-size | A | VOTE 2 · THE ANSWER: the level-rows drawing, counter `nodes so far` |
| 09-chapter-3 | A | PART 3 OF 3 · Trees in code |
| 10-walk-classes | A | BinaryNode and BinaryTree fields; the five-value box tree |
| 10b-walk-count | A | getNumberOfNodes on the five-value tree, counter `nodes counted` |
| 10c-walk-height-code | A | the level-counting height on the same tree |
| 17-next-class | C | the same clock as 02, static; caption "Next class is Day 2: visiting every node of a tree in order." |
| 99-closing | A | dusk (copy) |

File numbers are sort keys; the manifest order in `index.html` is the order on screen.

## Slide by slide (C)

- **02 / 17.** A new drawing for a break week on W12D2 02's geometry (§11 grid). Left half
  Week 13 (x 128–960), right half the Thanksgiving break (x 960–1792). `now` band Mon–Tue x 128–366, `now` at 247. Rows:
  modules y 496, homework 568, CE 640, project 712. Eight steps: 1 bracket `Week 13 · this
  week` (x 544) / `Thanksgiving break` (x 1376) / stone `Week 14 →`; 2 "Week 13: Semester
  Review" (blue) to the Friday pole x 722 (Nov 20); 3 "CE 13 · Binary Tree" (maroon) to the same
  pole; 4 "Project 3 · Deliverable 4" (accent-2), solid Monday 152–247 and fading to 698, range
  M247 818 H722 "your lab day"; 5 caption only, nothing due Sun Nov 22; 6 the five break
  weekday tracks x 960–1554, y 250–790, washed stone 12 %, one label at x 1257 in Liberation
  Serif at --t-small, no bars; 7 the modules pole, its due tick, "Sun" (end-anchored) and the
  label "14.1 + 14.3 + 14.4 modules" (blue, mono micro, right-anchored at the pole top, y 529),
  no bar across the wash; 8 the two tiles.
  Deviations: (a) the wash label is one `<text>` in two lines, "Thanksgiving break" / "no
  classes, no deliverables": the one-line form is 699 px against the 594 px wash. (b) The
  right-edge pole stands at x 1782, not 1792: at 1792 its round cap leaves the body, and at
  1786 Firefox padded its stroke box to x 1794 and flagged RIGHT on every step. (c) Step 7's
  caption drops "at 11:59 PM" (1,802 px with it, 1,617 without, body 1,664); the notes keep
  the time. (d) Step 1's caption is mine (the outline gives none): "Week 13 is this week, and
  Thanksgiving break follows it." Captions measured with PIL (Liberation Serif 36).
  The wash sits under the second tile (x 980–1280, y 232–402) on step 8; the tile is opaque.
  Both decks' 02 and 17 are written by one script (scratchpad `w13c/gen_clock.py`): only the
  now band, desc, notes and 17's caption differ. 17 is derived from 02 by the W11D1 recipe
  (` frag`, `data-step`, `data-anim` stripped, the caption group replaced by one caption, h2
  "Before next class", new desc and notes); edit the script, re-run it, then `add_sids.py`.
  17's caption: "Next class is Day 2: visiting every node of a tree in order."
  Sweep (run3, last step), Chromium / Firefox / WebKit: 02 36/35/36, 17 36/35/36; no flags
  (WebKit timed out once, passed on the retry).

## Unverified (C)

- The break wash covers the five weekday tracks only (x 960–1554), as the outline asks; the
  break itself is Sat Nov 21 to Sun Nov 29, as the caption and notes say.
- Nothing due Sun Nov 22 and the 14.1/14.3/14.4 due date Sun Nov 29 are from the brief; not
  checked against the PL repo's assessment dates.
- CE 13's due time: the brief gives Friday Nov 20 only, so CE 13 has no "11:59 PM".


## Slide by slide (A)

Builder A's slides were generated by small Python scripts (scratchpad `a/s*.py`, one file per
slide, each written once) and then stamped with `add_sids.py`. Step counts in brackets.

- **01 / 03 / 05 / 09 / 99** [0]. W12D1 copies with the facts changed (kicker WEEK 13 · DAY 1;
  the three divider titles from the outline; 99 unchanged).
- **01b-today** [3]. W12D1 01b grammar: the A–H tree (0.42 of the shared drawing), the votes'
  shape on three levels with no count anywhere, the `left | data | right` box with two blue
  references. Tree letters are 20 px in the 360 × 240 viewBox, about 29 px on screen.
- **02c-bridge-hang** [3]. As outlined. The SVG is 1664 × 344, not 300: three levels at the
  shared 130 px pitch need it. The step-2 caption is two sentences ("The same values can also
  hang from one node, and each node can have a left child and a right child. Where each value
  should go is the question for Week 14.") because the outline's first clause had no verb.
- **04-walk-words** [10]. As outlined, plus a tenth press for the plant (one change per press).
  Terms land as mono chips on the right (root, edge, parent, child, siblings, 0, 1 or 2
  children, leaf, inner node, subtree); steps 4 and 6 add nodes with a sentence but no chip.
  Steps 3 and 5 outline the nodes they are about in blue for that press only.
- **04b-walk-height** [8]. Four stone bands wipe across the full width, so the J–M chain on the
  right sits on the same levels; the convention is a stone card under the drawing; the single
  node (labelled N) is a card at the top right; the plant is press 8. Nothing is summed.
- **06-walk-levels** [5]. As outlined; nodes carry no letters; counts "1 node / 2 nodes /
  4 nodes" right-anchored. Plant is a full sentence around the votes' phrase: "The next
  two questions describe this tree as having nodes that either have 0 or 2 children and all
  leaves on the same level."
- **06c-peer-plus** [0]. W12D1 05 with Week 13 / W13D1 and the outline's plant (1,489 px).
- **07-vote-height / 08-vote-size** [2 each, the clocks]. Stem verbatim as the lede, six
  options full width; 07 at --t-small with 48 px discs and 6 px rows, 08 at the body size with
  56 px discs (numbers only). No drawing on either. h2 ends at x 1077 (07) and x 1262 (08),
  measured with PIL on Liberation Serif 56 px.
- **07b-walk-height-answer** [8]. As outlined; the fourth level grows in place under 06's shape
  (narrowed to leaves 110 px apart so the card fits beside it). Card lines use real
  superscripts/subscripts; the general rule (steps 6–7) is orange. Ends on the plant; 07c
  carries Vote 1's `.verdict`.
- **07c-walk-height-others** [4]. As outlined; option cards crossfade, a reference card names
  h 3 / h 4; verdict on press 4.
- **08b-walk-size** [12]. DEVIATIONS: (a) discs r 8 on a 22 px pitch and rows 36 px apart, not
  the brief's 24 px pitch: 64 discs at 24 px plus the "level 7 · 64" label need 1,754 px of the
  1,664 px body (Day 2's six-row 06b is unaffected). (b) The outline's single dismissal press
  is split into four (B 128 · F 64 · E 63 · C and D together), each a maroon outline round the
  rows that option counts; verdict on press 12, then 7 + 4 + 1 presses in all.
- **10-walk-classes** [7]. Fields as on ProgrammingTrees; the one `leftChild, rightChild`
  declaration is broken after the comma (continuation aligned) so the editor fits 760 px at
  --t-code. Box tree 240 × 76 at a 150 px pitch; nulls in stone under their cells on press 6;
  the plant is press 7.
- **10b-walk-count** [10]. The two long assignments are broken after the `=` (editor 954 px at
  --t-code); nothing else in the course's method is changed. The five-value tree is narrowed
  to 420 px (levels still 130 apart) so it fits over the 440 × 88 frame stack; the counter
  `nodes counted` sits beside the stack with its label wrapping. Return pills grow on the
  returning frame and move one pitch down into the caller; a pill that has been used fades.
  Plant on press 10.
- **10c-walk-height-code** [6]. The deck's own level-counting height (notes say so), the return
  broken after the comma (editor 1,092 px). Returned heights are pills beside their nodes; no
  stack (10b has it). The orange path 10 → 3 → 7 draws on with 10's return (press 5).

No-giveaway check (instructor, 2026-11-14): 01, 01b, 02c, 03, 04, 04b, 05, 06 and 06c contain no
sum of level counts, no 2^h / 2ʰ / log2, no 127 / 63 / 31, no "7 nodes" / "15 nodes" and no
height → nodes table in text, captions, descs, aria-labels or notes. A raw grep still finds
"31" and "63" inside `data-sid` counters (e.g. `01b-today:31`) and one `y="31"` coordinate on
02c; those are attributes, not text.

Sweep (run3, minimum slack over all steps), Chromium / Firefox / WebKit: 01 319 · 01b 166 ·
02c 156 · 04 286/284/286 · 04b 46 · 06 272 · 06c 36/35/36 · 07 152 · 07b 51/53/51 · 07c
308/309/308 · 08 104 · 08b 41/40/41 · 10 156 · 10b 80 · 10c 320; no RIGHT/LEFT/CLIPPED flags.
WebKit reports the vote clocks (top 64) as above y 95 on 07 and 08, as on every vote slide.

## Unverified (A)

- Vote keys: Vote 1 D and Vote 2 A come from the PL twins (`tree_formula`,
  `tree_formula_nodes`); to be confirmed in Runestone's results view (the notes say so).
- getNumberOfNodes: the brief gives `int leftNumber = 0, rightNumber = 0;`, recursion on
  non-null children and `return 1 + leftNumber + rightNumber;`; the accessor names
  `getLeftChild()` / `getRightChild()` and the `!= null` tests are as the brief writes them for
  height, not checked against the ProgrammingTrees slide image.
- The traversal-free height in 10c is the deck's; the ProgrammingTrees `getHeight` (edge count)
  is mentioned in the notes of 04b and 10c only.
- `add_sids.py` was run once on `slides/*.html` early on, so it also touched 02 and 17 (it only
  adds missing sids and keeps existing ones); later runs were on A's files only.

## Review (main session, 2026-11-14)
- Verified: lint clean; the vote texts match the Runestone paste (only "Q-1: " dropped);
  three-engine sweep (Chromium, Firefox, WebKit) with no overflow or clipping, slack ≥ 35.
- No-giveaway check (instructor's constraint): every slide before the first vote — visible
  text, sr-only descriptions, aria-labels and notes — was grepped for level sums, 2^h, log2,
  127/63/31 (Day 1) and for 2^h, log2, 127/64/63/62, "A B C D E"/"ABCDE" and "must be
  leaves" (Day 2 before each vote). Nothing found. The notes on D1 06 and 06c tell the
  instructor not to sum the levels or write a formula before the votes.
- Prose read through; one caption changed (D2 06b: "62 is neither" instead of a claim that
  every wrong option is a level or a total).
- Open for the instructor: keys D1 D / A, D2 D / C in Runestone's results view (the PL twin
  of D2 Q2 has other options and an incomplete key "A, E"); CE 13's exact string format.
- Prose pass (instructor, 2026-11-14, "clean, flowing, academic prose like a person might
  write in a class"): headings, captions, plants and notes rewritten as full sentences
  across 28 files in the two decks (e.g. "A is the root. It has no parent." → "A is the
  root, the one node that has no parent."; "Left, then root, then right:" → "The left
  subtree first, then the root, then the right subtree:"; every trailing "Next: …" fragment
  in the notes → a sentence). Vote text untouched. One option card on D2 06b shortened
  again after it overflowed.
