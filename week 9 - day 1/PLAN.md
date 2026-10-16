# Week 9 · Day 1 — plan

Built 2026-10-16 for Monday Oct 19 (MW, NCB 320) and Tuesday Oct 20 (TR, Squires): one deck, both
sections. Shared css/js/assets/tools were scaffolded from `week 8 - day 2`. `02-course-info`,
`02b-ssd` and `17-next-class` are written by another agent; this plan only places them in the
manifest.

Sources: the 9.1 Lists module's video slides in `~/Projects/pl-vt-cs2114/clientFilesCourse/slides/`
(`ListIntro24.pdf`, `LinkedListAdd.pdf`, `LinkedListRemove.pdf`, `LinkedListMoreDetails.pdf`, all
image-only, viewed page by page); the module page `questions/contentPages/09_01_lists/` (section
texts and checkpoints); the ListInterface UML in `questions/contentPages/11_02_sorted_lists/section_01/clientFilesQuestion/ListInterface.png`;
the homework `courseInstances/Fall2026/assessments/homeworks/09_lists_generics/infoAssessment.json`
and `questions/codeworkout/x708`–`x711` (`question.html`, `info.json`, starter `LinkedList.java`);
the PrairieLearn twin of Vote 2, `questions/dataStructures/lists/u11q05_sll_removenode_d`; the
Runestone text of both votes from the build brief (Peer Instruction W09D1).

## Through-line

**"A list lets you add and remove at any position, not only at the ends. On a linked chain that
means walking to the node before the position, and the first and last nodes are the special
cases."**

- Part 1 · A linked list adds at any position. `add(p, x)` is walked at position 0 (on an empty
  list, then on a one-node list), then in the middle with a `nodeBefore` ring, with a second run
  in which lines 8 and 9 trade places and the rest of the chain is lost; then adding at the end
  with `lastNode`.
- Part 2 · Removing means finding the node before. `remove(p)` for p > 0 is walked, then the ring
  and the two votes (addLast's empty case; the special cases of remove with a tail), each walked.
- Part 3 · This week's work: the four homework problems as cards.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `CS 2114 · FALL 2026 · WEEK 9 · DAY 1` |
| 01b-today | three chapter tabs: a chain with a new node arriving under the middle · a chain whose middle node is skipped by an arc · a homework sheet with an orange pencil → the captions are the divider titles |
| 02-course-info | (another agent) the Week 9/10 clock |
| 02b-ssd | (another agent) the SSD reminder for Test 2 |
| 02c-bridge-queue | FROM WEEK 8 TO WEEK 9 (bridge): the Week 8 linked queue (firstNode, lastNode; enqueue at the back, dequeue at the front) beside the same chain as a list with positions 0, 1, 2 and a new node arriving at position 1; then the list's ten operations → "A queue is a list that only uses two of the positions." |
| 03-chapter-1 | PART 1 OF 3 · A linked list adds at any position |
| 04-walk-add-front | `add(p, x)` under the PC bar: add(0, B) on an empty list (firstNode set; the caption says a list with lastNode must set it too), then add(0, A) → "Adding at position 0 writes two references, whatever the length of the list." |
| 04b-walk-add-middle | the same method: add(2, X) on A, B, C; a blue `nodeBefore` ring walks from A to B (getNodeAt(1)); X's next is set to C, then B's next swings to X; then lines 8 and 9 trade places and the same call runs again: B's next is set to X first, C turns stone, X's next refers to X → "Set newNode.next before nodeBefore.next changes." |
| 04c-walk-add-end | `add(x)` at the end with lastNode (the Week 8 enqueue) on A, B, C: the else branch only; C's next is set to D, lastNode swings → "lastNode makes adding at the end two writes. The empty list takes the if, and Vote 1 asks about that case." |
| 05-chapter-2 | PART 2 OF 3 · Removing means finding the node before |
| 06-walk-remove-middle | `remove(p)` for p > 0 on A, B, C, D: the ring walks to B, a second ring marks nodeToRemove = C, B's next swings over C to D, C turns stone, then fades on return → "Position 0 has no node before it, so it is a separate case." |
| 07-peer-plus | the routine ring, `Peer Instruction W09D1` → "Two questions: the empty-list case of addLast, and the steps of remove." |
| 08-vote-addlast | VOTE 1, static: stem lede, lines 16–24 at `code-mid`, the rest of the class in a second editor with lines 2–10 and 13–15 folded, the question sentence, four code options; two clocks |
| 08b-walk-addlast | VOTE 1 · THE ANSWER: addLast(5) then addLast(7) once per option (A, B, D, C) with line 19 replaced by the option → `.verdict` C |
| 09-vote-remove | VOTE 2, static: the verbatim stem as the heading, the four long options full width at `--t-small`; two clocks |
| 09b-walk-remove | VOTE 2 · THE ANSWER: `remove(p)` with head and tail on A, B, C, D: remove C (middle), remove A (first), remove D (last: B's next is null and tail must move to B) → `.verdict` B |
| 10-chapter-3 | PART 3 OF 3 · This week's work |
| 11-hw-insertionsort | WEEK 9 HOMEWORK: x709's example list 3 → 5 → 8 → 9 → 10 and a card of what the homework LinkedList already has; four problem cards → "PrairieLearn › Week 9: Lists & Generics — Coding Practice · best 2 of 4 count · due Friday" |
| 17-next-class | (another agent) the same clock, static |
| 99-closing | dusk |

## Slide by slide

- **Node grammar (02c, 04, 04b, 04c, 06, 08b, 09b, 11).** W8D1's Node boxes, `data | next`
  (08b: `value | next`, the vote's field names), blue arrows, `null` as the word in stone inside
  the next compartment until it is written. The list references (`firstNode`, `lastNode`; in the
  vote slides `head`, `tail`) are blue pills above the chain with a stone `null` beside a pill
  while it is null. A reference fades in when first assigned and then swings (CSS `d: path()`
  between same-shaped cubics, plus `data-swing` for Safari); a `next` written by an assignment
  Creates (shaft by dashoffset, separate head after it); a write washes the compartment orange
  for its step; the node built by the current call is the orange 18% tint with an orange
  `newNode` label. A node nothing refers to turns stone (lost) or fades (after return).
  Locals that refer to a node (`nodeBefore`, `nodeToRemove`) are rings around the node with a
  label under it: blue for `nodeBefore`, orange for `nodeToRemove`; a ring moves by
  `translateX` one pitch per step of getNodeAt (a real move).
- **Code.** The videos show no code for add or remove (only `getNodeAt`, LinkedListRemove.pdf
  slide 4). The walked methods are Carrano's LList methods with the videos' 0-based positions and
  the field notation of the vote (`newNode.next`, not `setNextNode`); `newPosition` and
  `newEntry` are shortened to `p` and `x`. The names `nodeBefore` and `nodeToRemove` are the
  video's (LinkedListRemove.pdf slide 6). `numberOfEntries++`/`--` are in the code but have no
  press.
- **02c.** One SVG (1664 × 300), one caption at a time under it, then the ten operations as two
  chip rows. Press 1: the queue, A → B → C with firstNode and lastNode, `dequeue()` stone label at
  the front and `enqueue(x)` at the back. Press 2: the same chain on the right as a list, with
  positions 0, 1, 2 under the nodes. Press 3: a new node X grows in under the gap between 0 and
  1 with an orange label `add(1, x)`. Press 4: the operations: by position `add(newPosition,
  newEntry)`, `remove(givenPosition)`, `replace(givenPosition, newEntry)`,
  `getEntry(givenPosition)`; on the whole list `add(newEntry)`, `contains(anEntry)`,
  `getLength()`, `isEmpty()`, `clear()`, `toArray()`; the caption ends "A queue is a list that
  only uses two of the positions."
- **04.** 9 presses: add(0, B) on empty (new node; p == 0; newNode.next = firstNode washes B's
  next and it stays null; firstNode = newNode, firstNode's arrow fades in), add(0, A) (new node to
  the left; p == 0; A's next Creates to B; firstNode swings to A), the rule on the closing brace.
  Caption 4 says that a list that also keeps lastNode must set it here too (the brief's rule: the
  empty case is shown here, not answered as Vote 1).
- **04b.** 10 presses: X grows below the chain; p == 0 is false; getNodeAt(1) puts the ring on A,
  then moves it to B (`data-hold`); X's next Creates to C; B's next swings to X. Press 7: the two
  lines trade places (W7D2 04b's line move, `translateY(±48px)`), the picture returns to its
  state after press 4 (X's arrow fades, B's next swings back to C), no PC. Press 8 (row 8 now
  holds `nodeBefore.next = newNode`): B's next swings to X and C turns stone. Press 9: X's next is
  set to nodeBefore.next, which is X itself (a loop Creates). Press 10: the rule.
- **04c.** 5 presses on A, B, C with both references: D is created, isEmpty() is false, C's next
  Creates to D, lastNode swings to D, the rule. The empty-list branch is in the editor (it is
  the Week 8 enqueue) but not walked: see "Translated" below.
- **06.** 6 presses on A, B, C, D, remove(2): ring on A, ring to B, the orange nodeToRemove ring
  grows on C, B's next swings over C to D (wash on B's next, C turns stone), return C (C, its
  link and the ring fade), the rule.
- **07.** W8D1's ring with `Peer Instruction W09D1` and the takeaway line.
- **08 (Vote 1).** The 25-line Runestone code does not fit at the type floor: at `--t-code`
  (48 px a line) the body holds about eleven lines beside the options, and even at 28 px the
  25 lines plus the options need about 750 px of an available 671. Choice: the left column
  holds the stem lede and lines 16–24 at `code-mid` (gutter numbered from 16) with the question
  sentence under the editor; the right column holds the rest of the class in a second
  `code-mid` editor with lines 2–10 folded to `private static class Node { … }` and lines 13–15
  folded to `/** … */` (gutter labels `2–10`, `13–15`), then the four options in mono at
  `--t-code`. The folded text is the only Runestone text not on the slide; the class is open on
  every student's laptop. **Deviation for review.**
- **08b.** 17 presses, editor = lines 16–24 with line 19 replaced by the option being run (a plain
  crossfade). A: node 5, head = newNode (tail stays null), node 7, `tail.next` throws
  NullPointerException (maroon plate), a press with no walkline so the PC fades. B: node 5,
  tail = newNode, node 7, head is still null so the if runs again and tail swings to 7; node 5
  turns stone. D: node 5, its next loops to itself; head and tail stay null. C: node 5, head and
  tail both refer to it, node 7, the else: 5's next Creates to 7, tail swings to 7. Verdict C.
  The h2 states the conclusion.
- **09 (Vote 2).** The four options are 148–312 characters. With a paraphrase h2, the stem as a
  lede and the options at `--t-small` (12 lines at 1600 px by PIL) the body needs about 760 px
  of 671. Choice: the verbatim stem is the heading (`h2` at `--t-small`, two lines beside the
  clocks), and the options run full width at `--t-small` with the 56 px discs. **Deviation for
  review** (every other vote has a paraphrase h2).
- **09b.** 13 presses, `remove(p)` with head and tail (11 lines, the vote's names): remove(2) on
  A, B, C, D (ring A → B, nodeToRemove C, B's next swings to D, the tail test is false, C
  fades); remove(0) (head swings to B, A fades, no node before it); remove(1) on B, D (ring on
  B, nodeToRemove D, B's next becomes null while tail still refers to D, which is where option A
  stops; the tail test is true; tail swings to B; D fades); a caption rules out C and D; the
  verdict (short labels for the four long options).
- **11.** W8D1 11's grammar: left (760 px) x709's own example `3 --> 5 --> 8 --> 9 --> 10`
  with firstNode, a card of what the homework's LinkedList already has (note: its Node method is
  `next()`, not `getNext()`), the signpost; right four cards one per press: PL title, signature
  without `public`, the part to think hardest about (no code).
- Timing: clock + SSD 4, bridge 3, the three add walks about 10, the remove walk 3, ring 1, votes
  about 8 each (1:30 + 2:30 plus the walk; 08b is long), homework 3, next class 1: about 40 of 50.

## Translated, dropped, unverified

- **The videos count positions from 0**, not 1 as the build brief assumed (Carrano's book is
  1-based): ListIntro24.pdf slide 3 numbers its example list 0–10; LinkedListAdd.pdf slide 4
  marks positions 0, 1, 2, 3 with "givenposition 2"; LinkedListRemove.pdf slide 4's getNodeAt
  has the precondition `0 <= givenPosition <= numberOfEntries - 1`, and slide 5 removes the
  first entry with `remove(0)`. The deck uses 0: the front is `add(0, x)`, the brief's
  "position 1" walk is position 0, and `getNodeAt(p - 1)` is still the node before.
- **No add/remove code in the videos.** Only getNodeAt is shown as code; add is drawn (with the
  local names `prev`/`curr` and `newNode`, `newEntry`) and remove is drawn with `nodeBefore`,
  `nodeToRemove`, `nodeAfter`, `desiredNode`. The walked code is the deck's (Carrano's shape,
  0-based, field notation). Fields vs. accessors: the video's getNodeAt uses `getNext()`; the
  deck uses `.next`, like the vote and LinkedListRemove.pdf slide 2 (`firstNode = firstNode.next`).
- **ListIntro24.pdf does not list the operations.** It is three slides: a bullet list ("Items
  in list have position … Items may be added anywhere … ArrayList provides list
  functionality"), a link to visualgo, and a hand-written example using `getEntry(4)`,
  `remove(5)`, `add("CapOne")`, `add(6, "Alphabet")`, `replace(2, "Amazon")`. The ten operations on
  02c are from the ListInterface UML in the 11.2 module page (add(T), add(int,T), remove(int),
  clear(), replace(int,T), getEntry(int), toArray(), contains(T), getLength(), isEmpty()); the
  parameter names are Carrano's. `ListInterface.java` itself is linked from the 9.1 page
  (courses.cs.vt.edu) and could not be fetched from this machine, so its parameter names are
  unverified.
- **Vote 1 vs. 04c (a conflict in the brief).** The brief asks 04c to show "the empty-list case
  sets both firstNode and lastNode" and also says the walk that covers the empty case must not
  answer Vote 1 outright. Resolution: the empty case is walked on 04 (add(0, B), firstNode only,
  with the caption that a list with lastNode must set it too); 04c's editor holds the Week 8
  enqueue shape, but only the non-empty run is walked, and its last caption names the empty
  case as Vote 1's question.
- **Vote keys.** Vote 1 C is by tracing; the PL twin `u11q02_linkedlist_addnode_*` is a different
  question. Vote 2 B is from the twin `u11q05_sll_removenode_d`, which is this question word for
  word (`correct="true"` on the "first or last node" option). Both are ASSUMED until they are
  confirmed in Runestone's results view before class.
- Vote text is quoted from the brief's Runestone paste, quirks kept: `this.next  = null;` and
  `tail      = newNode;` with their extra spaces, the javadoc's eight-space indent, the
  question's doubled "? ?", the curly apostrophes in "it’s". Vote 1's code lines 2–10 and 13–15
  are folded (see 08 above). The Runestone activity ids are not in the paste.
- `numberOfEntries` changes are in the code of 04, 04b, 04c and 06 without a press. 09b's
  method (the vote's head/tail) leaves out numberOfEntries and the one-node case of remove(0),
  where tail must also become null; the notes mention it.
- Homework: "Week 9: Lists & Generics — Coding Practice", 4 problems at 10 points,
  `bestQuestions: 2`, due Fri Oct 23 23:59:59 (`allowAccess`; three named students have to Sat
  Oct 24, not on the slide; a credit-0 window stays open to Dec 31). x710's `question.html`
  heading is "LinkedList: Insert After a Node"; the card uses the `info.json` title "LinkedList
  Insertion Sort: Insert After Node", which is what the assessment lists. The homework's Node
  class has `next()`, not `getNext()`.
- In the notes of 11 only: CE 09 "Linked List Debug" (Friday; where it is submitted is in no
  source), Project 2 Deliverable 4 (final build, writeup, presentation) at the start of your Week
  9 lab, Project 3 "Queue + MVC" teams re-form and D1 Scope is released this week (due at the Week
  10 lab).
- `Peer Instruction W09D1` is the assignment name from the brief's paste, not seen in Runestone.
- Dropped: the sentinel-node half of LinkedListMoreDetails.pdf (doubly linked list with dummy
  nodes) and the array list (Day 2's); the visualgo link.

## Status — 2026-10-16, first build

- 17 slides written here; `02-course-info`, `02b-ssd` and `17-next-class` were already in the
  folder from the clock agent, so the sweep ran on the real manifest (no temporary one).
  `add_sids.py` run on the 17 new slides only; `lint.py` clean on all 20.
- Sweep (`timeout -k 5 150 tools/measure/run.sh "$PWD"`), slack at the last step: 01 319 · 01b
  166 · 02 36 · 02b 120 · 02c 43 · 03 366 · 04 96 · 04b 96 · 04c 95 · 05 322 · 06 278 · 07 33
  (the inherited ring) · 08 88 · 08b 131 · 09 65 · 09b 144 · 10 366 · 11 53 · 17 36 · 99 389. No
  right/left overflow, no clipped code. The vote clocks on 08 and 09 are listed as "over"
  because they sit in the head band, as on every vote slide.
- Sizing change after the first sweep: 11 had 27 px (the left column: three-line signpost) →
  the example figure 160 → 150 px tall and the left stack gap 16 → 8 px (53 px).
- Checked mechanically: every `data-swing` parses as JSON; every `.cap--k` a rule names exists;
  the vote stems, quoted code lines and options are on the slides character for character
  (Vote 1's folded lines 2–10 and 13–15 excepted, by design).
- Not checked in a browser: the swings, washes, rings, the 04b line move and the 08b line-19
  crossfade (no Playwright, by rule).
- Open for review: the two vote-layout deviations (08: folded lines; 09: the stem as the
  heading); the 0-based positions; the assumed keys C and B.
- Not committed (`git add "week 9 - day 1"` when asked; never `-A`).

## Review — 2026-10-16 (main session, after the three agents)

- `02-course-info`, `02b-ssd`, `17-next-class` were written by the clock agent (Test 2 band
  on Week 10's Wed–Thu as step 1, P2 D4 at your lab, Project 3 released as a stone bracket
  with an a2 label that becomes the D1 bar at the Week 10 lab; SSD seat deadlines MW Fri
  Oct 23, TR Mon Oct 26). Day 2's three are derived from these by script; edit Day 1's first.
- Vote text checked piece by piece against the paste. Vote 2 matches in full. Vote 1
  matches except two folds made for the type floor: the Node class (lines 2–10) is shown
  as `private static class Node { … }` and the Javadoc (lines 13–15) as `/** … */`. The
  answer does not depend on those lines, and students have the full code open in
  Runestone. This is a quoting deviation for the instructor to accept or undo.
- Every CSS arrow swing has a matching `data-swing` entry (checked by script); nothing is
  under the type floor except the timer labels.
- Sweep after the review: no overflow; lowest slack 33 (the ring), then 36 (02, 17), 43
  (02c); the rest as in the Status block.
- Keys C (traced) and B (twin) to confirm in Runestone. Not committed.
