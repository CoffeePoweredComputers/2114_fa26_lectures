# Week 9 · Day 2 — plan

Built 2026-10-16 for Wednesday Oct 21 (MW, NCB 320) and Thursday Oct 22 (TR, Squires): one
deck, both sections. Shared css/js/assets/tools were scaffolded from `week 8 - day 2`.
Last class (Monday for MW, Tuesday for TR) covered lists on a singly linked chain; this deck
starts from its removal of the last node. `02-course-info`, `02b-ssd` and `17-next-class`
are written by the clock agent into this folder; they are in the manifest only.

Sources: the 9.1 and 9.2 module slide PDFs in `~/Projects/pl-vt-cs2114/clientFilesCourse/slides/`
(`LinkedListMoreDetails.pdf` 1 page, `ListEfficiency.pdf` 1, `ArrayListImplementation24.pdf` 5,
`MoreOnGenerics.pdf` 15, `LinkedListRemove.pdf` 6; all viewed page by page); the PrairieLearn
twins `questions/dataStructures/lists/u11q06_dll_{a,b,c,d}` and `u11q07_list_lastnoderef_{a,b,c,d}`;
the vote text from the Runestone paste in the build brief; the shared brief `week9-common.md`.

## Through-line

**"A doubly linked list can remove any node it holds a reference to without a search, but
only after it handles the first node, the last node and the only node. Which positions cost
O(n) depends on which references the list keeps. Generics with bounds let one sorted method
work for any type that can be compared, which is next week's sorting."**

- Part 1 · Removing a node from a doubly linked list. Two walks: the two general lines on a
  middle node, then the same lines on the first node (they throw) and the fix for the first
  and the last node.
- Part 2 · Where the cost is. The routine ring, Vote 1 (which code removes curr; shown over
  three slides) and its walk on four lists, Vote 2 (remove at three positions) and its walk
  with a counter, then the video's efficiency table.
- Part 3 · Generics with bounds. `isSorted` with and without `<T extends Comparable<T>>`, then
  the video's `sort(T[] items, Comparator<? super T> comp)` with one `Comparator<Number>`.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `CS 2114 · FALL 2026 · WEEK 9 · DAY 2` |
| 01b-today | three chapter tabs: three linked boxes with an arc over the middle one · a chain with a ring walking it · a small type tree with a bound; the captions are the divider titles |
| 02-course-info | (manifest entry only; written by the clock agent) |
| 02b-ssd | (manifest entry only; written by the clock agent) |
| 02c-bridge-singly | FROM DAY 1 TO DAY 2: last class's singly linked chain with a curr ring walking to the node before the last (three visits), beside a doubly linked chain whose last node's prev is that node; → "With prev and next on every node, which references change when curr is removed?" |
| 03-chapter-1 | PART 1 OF 3 · Removing a node from a doubly linked list |
| 04-walk-dll-middle | concept walk: curr on B in A ⇄ B ⇄ C; the two general lines; A's next swings to C, C's prev swings to A, B fades; → "The removal needs no search, because curr refers to the node and its prev refers to the node before it." |
| 04b-walk-dll-ends | the same lines on the first node throw a NullPointerException; the guarded version (`if (curr == firstNode)` … `else if (curr == lastNode)` … `else`) runs on A, then on C; → "The general lines need a node on each side of curr. The first and the last node each need their own lines." |
| 05-chapter-2 | PART 2 OF 3 · Where the cost is |
| 06-peer-plus | the routine ring, `Peer Instruction W09D2`; takeaway "The two questions are about removing curr and the cost of remove." (the brief's wording is a colon fragment and 2138 px at the plant size; see below) |
| 07-vote-dllremove | VOTE 1, static, clocks: the stem verbatim on the left with option A under it, option B on the right |
| 07a-vote-dllremove-cd | VOTE 1 continued, static: options C and D side by side |
| 07a2-vote-dllremove-e | VOTE 1 continued, static: option E, with the stem repeated beside it |
| 07b-walk-dllremove | VOTE 1 · THE ANSWER: E's code under the PC bar, four runs (only node, first of three, last of three, middle of three), A–D ruled out; `.verdict` E → "Only E handles the only node, the first node and the last node before the general case" |
| 08-vote-efficiency | VOTE 2, static, clocks: stem and five options verbatim |
| 08b-walk-efficiency | VOTE 2 · THE ANSWER: `remove(p)` on a five-node singly linked chain with firstNode and lastNode, a ring walking to the node before and a counter of nodes visited; a cost table filled per case, then the doubly linked row; `.verdict` C → "lastNode makes adding at the end O(1), not removing from it" |
| 09-walk-array-vs-linked | the video's efficiency table (ListEfficiency.pdf), one row per press, the remove row tinted; → the video's note "Three efficiencies are given for first; middle; last positions when givenPosition is a parameter." |
| 10-chapter-3 | PART 3 OF 3 · Generics with bounds |
| 11-walk-bounded | `isSorted` with `<T>` does not compile at `compareTo`; with `<T extends Comparable<T>>` it does; runs on Integer {3, 5, 9} and String {"pear", "apple"}; Object[] does not compile; → "The bound lets one isSorted work for Integer, String and every other class that implements Comparable." |
| 11b-walk-wildcard | the video's `sort(T[] items, Comparator<? super T> comp)`; one `Comparator<Number>` sorts an Integer[] and a Double[]; → "? super T lets one Comparator<Number> sort both arrays, because Number is a superclass of Integer and of Double." |
| 16-next-week | NEXT WEEK: Week 10 is comparing, sorting and iterators, and sorting calls compareTo; Test 2 in lecture, MW Wed Oct 28 and TR Thu Oct 29, LockDown Browser, bring your student ID |
| 17-next-class | (manifest entry only; written by the clock agent) |
| 99-closing | dusk |

File numbers are sort keys; the manifest order is the order on screen.

## Slide by slide

- **The DLNode grammar (02c, 04, 04b, 07b).** W8D1's boxes: `prev | data | next`, next
  arrows arc above the chain and prev arrows below it, both blue; `null` as the word in
  stone; firstNode and lastNode as blue pills above, `curr` as an orange-edged pill below
  (it is the method's local, the reference the work is done through). A reference that
  changes swings (CSS `d: path()` under `:has(.cap--k:not(.is-pending))` plus `data-swing`
  with the same paths); a node nothing in the list refers to fades. 04 and 04b use 240 × 80
  boxes; 07b uses 192 × 76 boxes without field labels (see sizing).
- **02c.** One SVG: left, last class's singly linked chain A → B → C → D with firstNode and
  lastNode; a curr ring moves A → B → C (three visits) to reach the node before D. Right,
  the same four values doubly linked; D's prev arrow takes the orange wash. Press 1 the
  left half and its caption; press 2 the right half and the second caption (the brief's
  wording); press 3 the question for Part 1 in display maroon.
- **04.** Editor (four lines: the two statements, each split after the first call so the
  editor is 780 px wide and the drawing gets 836 px). Steps: 1 the chain with curr on B;
  2 line 1–2: A's next swings to C; 3 lines 3–4: C's prev swings to A; 4 B fades; 5 the
  plant.
- **04b.** Editor of twelve lines; at first only the general lines (8–11) are visible,
  already inside the `else` (the other lines are `walkline--new`). 1 curr on A, the
  general first line; curr.getPrevious() is null; 2 the NullPointerException plate in
  maroon, the PC fades (no walkline at step 2); 3 the guard lines appear, `if (curr ==
  firstNode)` is true; 4 firstNode swings to B; 5 B's prev is set to null, A fades; 6 curr
  moves to C, `else if (curr == lastNode)` is true; 7 lastNode swings to B; 8 B's next is
  set to null, C fades; 9 the plant. The only-node case is left to Vote 1's walk, as the
  brief asked.
- **06.** W8D2's ring; the week, the assignment, the desc and the takeaway changed.
- **07 / 07a / 07a2 (Vote 1).** Five code options, 57 lines, at `--t-micro` mono with
  line-height 1.25 in tinted cards, each headed by a 48 px maroon key disc. They do not fit
  one slide or two (see sizing), so the vote is three slides: the stem with A and B, then
  C and D, then E with the stem repeated. The clocks are on 07 only. Every quirk is kept.
- **07b.** E's code, reformatted to K&R braces with 2-space indentation so it fits at
  `--t-code` (15 lines; the editor bar says so), under the PC. Four runs (`data-also`):
  only A; A of A ⇄ B ⇄ C; C of the same list; B of the same list. Then A ruled out, then
  B, C, D; then the verdict.
- **08.** The `.vote` text layout: the stem as the lede, the five options as `--long` rows
  on the right, a five-node singly linked chain with firstNode and lastNode on the left (no
  marks that point at an option). Two clocks.
- **08b.** The deck's own `remove(int p)` on a singly linked chain (0-based, as the video's
  `getNodeAt`), short names. Counter = nodes visited to find the node before. 1 remove(0):
  firstNode swings to B, 1 visit, table cell first = O(1); 2 remove(2) on the rebuilt
  chain: the ring visits A and B, 2; 3 B's next swings to D, cell middle = O(n); 4
  remove(4): the ring visits A, B, C, D, 4 = n − 1, because lastNode refers to E and the
  method needs D; 5 D's next is null, lastNode swings to D, cell last = O(n); 6 the
  doubly linked row O(1); O(n); O(1) with its reason; 7 the verdict.
- **09.** The video's table, eight rows one per press, the `remove(givenPosition)` row
  tinted orange. The column heads are shortened ("Array", "Singly linked, head only",
  "Singly linked, head and tail"); the video's full heads are in the notes and the desc.
- **11.** The editor holds `isSorted`; line 1 crossfades from `static <T>` to
  `static <T extends Comparable<T>>`. The right side holds a `T is …` pill, the array as
  cells, the compareTo result and an error plate. Steps: 1 the error at line 4; 2 the
  bound; 3–5 the Integer run (−1, −1, true); 6–7 the String run (15, false); 8 the Object[]
  call does not compile; 9 the plant.
- **11b.** The video's declaration plus a `ByNum implements Comparator<Number>` and two
  calls; right side, the video's Number tree reduced to Number over Integer and Double, and
  the two arrays whose values really move into sorted order.
- **16.** Two blocks: Week 10 (the topic, the line `a[i].compareTo(a[i + 1]) > 0` from 11,
  "sorting calls compareTo"), and the Test 2 card with dates and "LockDown Browser · bring
  your student ID". The topic list is a placeholder in the notes only.

## Sizing

- Vote 1: the stem at `--t-small` is 8 lines at 806 px (PIL, Liberation Sans). B, C and D
  have 47-character lines (790 px at 28 px mono), so two cards side by side need 1612 px
  without a gutter: the cards have no line numbers and 12 px side padding, the key disc
  sits above each card. A–D on one slide is 25 lines over two rows plus the stem, about
  1090 px; so 07 = stem + A (left) and B (right), 07a = C | D, 07a2 = E (19 lines, 681 px)
  with the stem on the right. E at `--t-code` would be 19 × 38 = 730 px, which does not fit;
  E stays at `--t-micro` (the brief's "larger" was not possible).
- 04 / 04b: a 47-character line at `--t-code` needs 972 px, which leaves 644 px for a
  three-node drawing of 240 px boxes; splitting each statement after its first call gives
  37 characters (780 px) and an 836 px drawing.
- 07b: E's general lines cannot be split (17 lines would not fit), so the editor is 972 px
  at line-height 1.25 and the drawing uses 192 px boxes (prev 68 | data 56 | next 68) without
  field labels; "null" (67 px at 28) fits a 68 px compartment.

## Translated, dropped, unverified

- **Vote keys are assumed** from the PrairieLearn twins, not seen in Runestone: Vote 1 **E**
  (`u11q06_dll_d`), Vote 2 **C** (`u11q07_list_lastnoderef_c`). **Confirm both in Runestone's
  results view before class.** The assignment name `Peer Instruction W09D2` is from the paste.
- **The twin's correct option differs from Runestone's E**: the twin `u11q06_dll_d` writes
  `if (curr == lastNode)` where Runestone's E has `else if (curr == lastNode)`. With the
  twin's `if`, removing the first node of a two-or-more-node list falls into the `else` and
  calls `curr.getPrevious().setNext(...)` on null. The twin's keyed answer throws; Runestone's
  E is correct. The twin should be fixed (not done here). The twin's C also differs
  (`setNext(prev.getNext())`); the slide follows Runestone, as the brief said.
- Vote 1's quirks are kept: the stem names `getPrevious()`/`setPrevious(Node n)` but A, B, C,
  D and E call `getPrev()`/`setPrev(...)`; B–D test `list.getSize()` though the list is
  `items`; C and D call `curr.getPrevious.setNext(...)` without parentheses. 07b treats
  `getPrev`/`setPrev` as the same methods, because every option uses them; the notes say so.
- **No video shows doubly linked removal code.** The 9.1 videos draw a doubly linked list
  only once, with sentinel nodes (LinkedListMoreDetails.pdf); LinkedListRemove.pdf is singly
  linked. 04 and 04b use the vote stem's method names (`getPrevious`, `setNext`, `getNext`,
  `setPrevious`), not names from a video.
- **The video's efficiency table has no doubly linked column.** 08b's doubly linked row
  (O(1); O(n); O(1)) is from the sister twin `u11q07_list_lastnoderef_b`, not from a video.
- The video's `remove(givenPosition)` cells read `O(1); O(n) ;O(n)` and `O(1); O(n) ; O(n)`
  (stray spaces); 09 normalises the spacing.
- **MoreOnGenerics.pdf's bounded example prints the wrong sum.** Slide 5's
  `System.out.println("Sum = " + first.doubleValue() + second.doubleValue());` concatenates
  strings: `add(3, 4)` prints `Sum = 3.04.0`, not 7.0. 11 does not use that example (it
  needs `compareTo`, per the brief); 11's notes mention it as the video's example and the
  bug.
- 11's `isSorted` and 11b's `ByNum` and calls are the deck's own code; the declarations
  `<T extends Comparable<T>> void sort(List<T> list)` and
  `<T> void sort(T[] items, Comparator<? super T> comp)` are the video's (pp. 10–15).
- **11b does not claim that `Comparator<T>` would fail**: with a `T[]` parameter, Java infers
  `T = Number` for `sort(Integer[], Comparator<Number>)` (arrays are covariant), so it would
  compile. The reason on the slide is the video's: one `Comparator<Number>` sorts an
  `Integer[]` and a `Double[]`. The difference matters for `List<T>`; the notes say so.
- The video's `? extends Number` slide has no code; it is in 11b's notes only.
- 08b's `remove(int p)` is the deck's own code, 0-based like the video's `getNodeAt`
  ("0 <= givenPosition <= numberOfEntries - 1"); it returns nothing and does not clear
  lastNode when the list empties (the notes say both).
- Test 2's topic list is in no source: 16's notes carry `[NOT IN ANY SOURCE: Test 2's topic
  list]`; the slide gives only the dates and "LockDown Browser · bring your student ID".
  Whether Test 2 runs in Canvas or PrairieLearn inside LockDown is not settled; the slide
  says neither.
- Day 1's deck was being built in parallel; 02c assumes, from the brief, that Day 1 walked
  the singly linked removal of the last node.

## Status — 2026-10-16, first build

- Written: 20 slides (every manifest entry except `02-course-info`, `02b-ssd` and
  `17-next-class`, which the clock agent wrote into this folder; not touched here).
  `add_sids.py` run on the 20 new slides only; `lint.py` clean on all 23 files. The vote
  text on 07/07a/07a2/08 was checked mechanically against the brief's paste (whitespace
  removed, every line present).
- Sweep (`timeout -k 5 150 tools/measure/run.sh "$PWD"`, all 23 slides present), lowest
  slack over all steps: 01 319 · 01b 166 · 02 36 · 02b 120 · 02c 240 · 03 322 · 04 206 ·
  04b 37 · 05 366 · 06 13 (the inherited ring, by design) · 07 127 · 07a 183 · 07a2 37 ·
  07b 38 · 08 58 · 08b 36 · 09 47 · 10 366 · 11 192 · 11b 192 · 16 273 · 17 36 · 99 389.
  No overflow and no clipped code at any step; the only "over" entries are the vote clocks
  in the head band, as on every vote slide since W6D1.
- The warmup body starts at y 274 under kicker + h2 (710 px), not the 250 assumed in the
  sizing notes above. Changes after the first sweep: 04b's code line-height 1.5 → 1.4
  (−1 → 37); 07b's code line-height 1.2 on the `li`, the SVG 296 → 282 px, the right
  column gap 24 → 16, the A–D verdict labels shortened to "No checks", "Tests size 1",
  "Missing ()", "Tests size 0" and set two to a line with E's sentence on its own line,
  captions 11–12 shortened (−16 → 38); 07a2's key disc moved beside the pane and the pane
  padding 8 → 4 px (−27 → 37); 08b's cost table moved from under both columns to under
  the editor, the code line-height 1.2, captions cut to three lines, the row gap 24 → 16
  (−18 → 36).
- The vote-card rules (key disc + tinted pane at `--t-micro`, no gutter) are repeated in
  the `<style>` of 07, 07a and 07a2 rather than added to `css/deck.css`, so the shared
  file stays identical to Week 8's. Move them to deck.css if the pattern is reused.
- Line-heights under 1.5 on `--t-code` editors (04b 1.4; 07b and 08b 1.2) are slide-local
  overrides; the type size is unchanged.
- Still to do by hand: confirm keys E (Vote 1) and C (Vote 2) in Runestone's results view;
  fix the PrairieLearn twin `u11q06_dll_d` (`if` → `else if`) if the instructor agrees;
  fill Test 2's topic list in 16's notes.
- Not committed (`git add "week 9 - day 2"` when asked; never `-A`).

## Review — 2026-10-16 (main session, after the three agents)

- `02-course-info`, `02b-ssd`, `17-next-class` are derived by script from Day 1's (now band
  Wed–Thu, x 366–603); edit Day 1's first.
- Vote text checked against the paste, option by option, across the three Vote 1 slides
  (07, 07a, 07a2) and on 08: the stems and all ten options match, quirks included.
- `02c` assumes Day 1 walked the removal of the last node: it does (Day 1 `09b`, step for D).
- Every CSS arrow swing has a matching `data-swing` entry (checked by script); nothing is
  under the type floor except the timer labels.
- Sweep after the review: no overflow; lowest slack 13 (the ring), then 36 (02, 08b, 17),
  37 (04b, 07a2); the rest as in the Status block.
- For the instructor: the PrairieLearn twin `u11q06_dll_d` keys `if (curr == lastNode)`
  where Runestone has `else if`; the twin's version throws on the first node and should
  be fixed in the PL repo. Keys E and C to confirm in Runestone. Not committed.
