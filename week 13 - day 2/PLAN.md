# Week 13 · Day 2 — plan

Planned 2026-11-14 for Wednesday Nov 18 (MW, NCB 320) and Thursday Nov 19 (TR, Squires):
one deck, both sections. Week 13 (Nov 16–20) is "Cloning & Trees"; the decks cover trees
only (instructor), and there is no test. Due this week: the homework "Week 13: Semester
Review — Coding Practice" (Fri Nov 20, 11:59 PM), CE 13 · Binary Tree (Fri Nov 20) and
Project 3 Deliverable 4 (start of your lab). Next week (Nov 21–29) is Thanksgiving break;
Week 14 (Nov 30–Dec 4) is Binary Search and Binary Search Trees, with no test (instructor).
Shared css/js/assets/tools were cloned from `week 12 - day 2`. Three builders: B
(`index.html` manifest and every slide except 02, 16 and 17), A (Day 1's deck), C (02, 16,
17, this PLAN.md skeleton; Day 1's 02 and 17). Sources: the shared brief `w13-brief.md` and
outlines `w13-outlines.md` (session scratchpad), including the Runestone paste of 2026-11-14
for both votes (quoted verbatim); `DECK-PROMPT.md`; the PL course repo
`~/Projects/pl-vt-cs2114` (twins named per slide); the 13.2 module videos (IntroToTraversals,
ProgrammingTrees) and CE 13 via the brief; the earlier decks named per slide below. Never
`canvas-banks/*`.

## Through-line

**"Preorder, inorder and postorder differ only in where the visit sits among the two
recursive calls; level order needs a queue instead; and an inorder listing with the root
known splits the tree into its left and right subtrees, which with the height fixes the
shape."**

| part | title (divider and tab) | slides | time |
|---|---|---|---|
| — | title, today, clock, bridge, peer-plus | 01 · 01b · 02 · 02c · 05 | 6 min |
| 1 | Three orders to visit a tree, and a fourth | 03 · 04 · 04b · 04c · 04d | 14 min |
| — | Vote 1 | 06 · 06b | 7 min |
| 2 | What an inorder listing tells you | 07 · 08 · 08b | 10 min |
| 3 | What CE 13 asks for, and next week | 09 · 10 · 16 | 4 min |
| — | next class clock, closing | 17 · 99 | 1.5 min |

## Manifest

| file | owner | role |
|---|---|---|
| 01-title | B | title card; kicker `CS 2114 · FALL 2026 · WEEK 13 · DAY 2` |
| 01b-today | B | three columns: the A–H tree with a numbered ring path · a strip A B C D E with B edged · a card `((B)A(C))` |
| 02-course-info | C | the Week 13 / Thanksgiving break clock, `now` Wed–Thu; nine steps (step 4 = the ethics discussion, due Fri Nov 20, added 2026-11-15) |
| 02c-bridge-visit | B | FROM DAY 1 TO DAY 2: Day 1's A–H tree, an empty output plate, "which letter is printed last?" |
| 03-chapter-1 | B | PART 1 OF 3 · Three orders to visit a tree, and a fourth |
| 04-walk-preorder | B | preorder(node) on the A–H tree: ring, call stack, output plate |
| 04b-walk-inorder | B | inorder, the visit between the two calls: ring, call stack, output plate (stack added 2026-11-17) |
| 04c-walk-postorder | B | postorder, the visit last: ring, call stack, output plate (stack added 2026-11-17) |
| 04d-walk-levelorder | B | level order with a queue |
| 05-peer-plus | B | the routine ring, `Peer Instruction W13D2` |
| 06-vote-size-6 | B | VOTE 1 (vtcs2_trees_size_2_202601), static, clocks; key D (no PL twin) |
| 06b-walk-size-6 | B | VOTE 1 · THE ANSWER: Day 1's level rows cut to six, counter `nodes so far` |
| 07-chapter-2 | B | PART 2 OF 3 · What an inorder listing tells you |
| 08-vote-inorder | B | VOTE 2 (vtcs2_trees_inorder_202601), static, clocks; key C by derivation |
| 08b-walk-inorder-answer | B | VOTE 2 · THE ANSWER: the tree rebuilt from A B C D E with B the root |
| 09-chapter-3 | B | PART 3 OF 3 · What CE 13 asks for, and next week |
| 10-ce13-strings | B | CE 13's parenthesised strings on A(B, C); size() and height() |
| 16-next-week | C | Thanksgiving break, then Week 14 · Binary Search and Binary Search Trees |
| 17-next-class | C | the same clock as 02, static; caption "Next week is Thanksgiving break. The 14.1, 14.3 and 14.4 modules are due Sunday Nov 29." |
| 99-closing | B | dusk (copy) |

File numbers are sort keys; the manifest order in `index.html` is the order on screen.

Vote 2's PL twin `tree_inordertraversal` has different options and an incomplete key
"A, E"; the deck derives C from the Runestone options.

## Slide by slide (C)

- **02 / 17.** A new drawing for a break week on W12D2 02's geometry (§11 grid). Left half
  Week 13 (x 128–960), right half the Thanksgiving break (x 960–1792). `now` band Wed–Thu x 366–603, `now` at 485. Rows:
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
  17's caption: "Next week is Thanksgiving break. The 14.1, 14.3 and 14.4 modules are due Sunday Nov 29."
- **16.** W12D2 16's grammar. h2 "Week 14 covers binary search and search trees" (the full
  name, 1,713 px at --t-h2, does not fit; it is on the name line). Left: name "Thanksgiving
  break, then Week 14 · Binary Search and Binary Search Trees" (two lines); a 1000×344 SVG with
  the sorted strip 3 7 10 12 20 (92 px cells, the middle cell edged maroon 6 px) beside Day 1's
  five-value circle tree (r 36, pitch 130; 10 (760, 42); 3 (630, 172), 12 (890, 172); 7 (695,
  302), 20 (955, 302)), whose root 10 is edged the same maroon to name the link (my addition);
  the caption and the due line as the outline. Step 1: the Week 14 card, title split into
  "Week 14" (--t-h3) and "Nov 30 to Dec 4" (--t-small), because the one-line title is 613 px
  against the card's 496 px; lines "Week 14 homework, Fri Dec 4" · "CE 14 · BST" · "No project
  deliverable, the first week back from break". Row gap 16 and line-height 1.25 on the caption
  and due line to reach 33 px bottom slack (it was −15 at W12D2's spacing).
- Sweep (run3, last step), Chromium / Firefox / WebKit: 02 36/35/36, 16 33/33/33, 17 36/35/36;
  no flags (WebKit timed out once, passed on the retry).

## Unverified (C)

- The break wash covers the five weekday tracks only (x 960–1554), as the outline asks; the
  break itself is Sat Nov 21 to Sun Nov 29, as the caption and notes say.
- Nothing due Sun Nov 22 and the 14.1/14.3/14.4 due date Sun Nov 29 are from the brief; not
  checked against the PL repo's assessment dates.
- CE 13's due time: the brief gives Friday Nov 20 only, so CE 13 has no "11:59 PM".
- 16: the Week 14 homework title is not in the brief, so the card says "Week 14 homework";
  CE 14's due date is not in the brief, so the card gives none. Week 15 (Dec 7–9, P3 Deliverable
  5 final build + lightning demo) and the final exam window Dec 11–16 are in the notes only.
- 16 notes: the Week 14 Day 1 dates (Mon Nov 30 MW / Tue Dec 1 TR) follow the section pattern.


## Slide by slide (B)

Builder B wrote index.html (the 20-file manifest) and every slide except 02, 16 and 17.
The walk slides are generated by scripts in the session scratchpad (`w13d2/gen_walks.py`
for 04/04b/04c, `gen_level.py` for 04d, `gen_size6.py` for 06b, `gen_inorder.py` for 08b,
`gen_votes.py` for 06/08); regenerate rather than hand-edit coordinates, then re-run
`add_sids.py`.

- **01-title / 99-closing.** W12D2 copies; kicker WEEK 13 · DAY 2; title notes name the three parts.
- **01b-today.** Three columns, one per press: the A–H tree with a blue ring on A and orange
  preorder numbers 1–8; the A–H tree's inorder listing D B F E G A C H with the root's cell
  (A) edged maroon; a card `((B)A(C))`. Captions = the three divider titles.
  **Deviation:** the outline drew the vote's listing A B C D E with B edged; it was replaced by
  the A–H tree's own listing so that no slide before 08 shows the vote's listing.
- **02c-bridge-visit.** 3 steps: Day 1's A–H tree at 1:1 (760×490 grammar); an empty output
  plate; the maroon question "If every call visits its own node before its children, which
  letter is printed last?" (answer H, given by 04). No counts or heights on the tree.
- **03 / 07 / 09.** Dividers: "Three orders to visit a tree, and a fourth" · "What an inorder
  listing tells you" · "What CE 13 asks for, and next week".
- **04-walk-preorder.** 10 steps, the outline's beats (A, B, D printed; D's null calls; E; F;
  G; back to A then C; H; all return) → "Root, then left, then right: A B D E F G C H."
  Ring in two axes, stack from the bottom up with "waiting on line 4/5", plate one letter
  per press.
- **04b-walk-inorder.** 9 steps (8 letters + plant) → "Left, then root, then right: D B F E G A C H."
- **04c-walk-postorder.** 9 steps → "Left, then right, then root. The root is printed last."
- **04d-walk-levelorder.** 10 steps: enqueue A; eight dequeues (letters travel as copies
  from the tree into the back of a five-cell queue, front at left; the front fades, the rest
  move one cell left); plant "One level at a time, with a queue instead of the call stack."
- **05-peer-plus.** W12D2 05 with Week 13 / Peer Instruction W13D2; the outline's plant (one
  line, 1,554 px measured).
- **06-vote-size-6.** Static; stem verbatim (no "Q-1:" in the source); A 127 · B 62 · C 64 ·
  D 63 in one row at the body size; clocks 90 s / 150 s; h2 ends at x 1262. Key D.
- **06b-walk-size-6.** 8 steps: rows 1, 2, 4, 8, 16, 32 (counter `nodes so far` 1 → 63);
  step 7 three notes beside the rows (127 = height 7, 62 = neither a level nor a total,
  64 = a seventh level alone); step 8 `.verdict` D. Plant in caption 6 "… total at 63, which
  is 2⁶ − 1."
- **08-vote-inorder.** Static; stem verbatim without "Q-1: "; five options in one row; h2 ends
  at x 791. Key C by derivation.
- **08b-walk-inorder-answer.** 10 steps as the outline (split at B; A as left child; the
  dashed frame for levels 2–3; candidates C and E on top struck because a node lands on
  level 4; D on top kept; leaf tint on A, C, E; B and D outlined to dismiss A/D and B/E;
  `.verdict` C).
- **10-ce13-strings.** 5 steps: `(B)`, `(C)`, the copies travel into `((B)A(C))`, the preorder
  and postorder rows, the size/height card; plant "CE 13 wants the three traversal strings,
  the size and the height."

Other deviations, all for fit or robustness:
- Day 2's walk tree (04–04d) keeps r 36 circles and the type sizes but uses a 110 px level
  pitch and narrower spacing (level 2 at ±150, level 3 at ±75, F/G at ±45 under E), so the
  stack (04) or the queue strip and plate (04d) fit beside/under it. 02c keeps Day 1's 1:1
  geometry.
- 04's frames are 290×80 on an 88 px pitch (not 440×88 / 96), so the stack fits beside the
  tree next to a 760 px editor; the wait note is in the body face at --t-micro.
- The output plate prints each letter as its own `<text>` frag (W7D2 10b), not a `<tspan>`:
  opacity on `<tspan>` is not reliable across engines.
- Editors use two-space indents so the longest traversal line (35 characters) fits 760 px at
  --t-code with the 2 % WebKit margin; 04d's queue loop drops the method header (9 lines).
- The vote timers report "over" (top 64 < 95) in the sweep; they sit in the top margin by design, with the same CSS as W12D2 06.

## Unverified (B)

- W13D2 Q1 key D (63) and Q2 key C (A, C, E) are as pasted / derived; confirm both in
  Runestone's results view. The PL twin `dataStructures/trees/tree_inordertraversal` has
  different options and an incomplete key "A, E"; Q1 has no PL twin.
- CE 13's string format is taken from the brief's examples (`((B)A(C))`, `(A(B)(C))`,
  `((B)(C)A)`); the empty-tree string is not shown on 10 (marked in its notes).
- The traversal and level-order code is the deck's own in the course's style; the notes on
  04 and 04d say so. `node` and `queue` in 04d are left undeclared (said in the notes).

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
