# Week 8 · Day 1 — plan

Built 2026-10-11 for Monday Oct 12 (MW, NCB 320) and Tuesday Oct 13 (TR, Squires): one deck,
both sections. The last class was before Fall Break (Fri Oct 9). Shared css/js/assets/tools
and `.slide-studio/permissions.json` cloned from `week 7 - day 2` (the newest copies).
`02-course-info` and `17-next-class` (the Week 8/9 clock) are written by another agent; this
plan only places them in the manifest.

Sources: the 8.1 module's video slides in `~/Projects/pl-vt-cs2114/clientFilesCourse/slides/`
(`QueueIntro.pdf`, `LinkedQueuesEnqueue.pdf`, `LinkedQueueRemove.pdf`, `DequeIntro.pdf`,
`DequeRemoveAndWrapUp.pdf`); the homework `questions/codeworkout/x700`–`x703` and
`courseInstances/Fall2026/assessments/homeworks/08_queues/infoAssessment.json`; the
PrairieLearn twins of the two votes, `questions/dataStructures/queues/u10q07_linkeddeque_tracing_b`
and `_c`; the Runestone paste in the build brief (Peer Instruction W08D1).

## Through-line

**"A queue adds at the back and removes at the front, so a linked queue keeps two references,
firstNode and lastNode. A deque removes at the back too, so its nodes need prev as well as
next. Every special case today is what happens to those two references when the chain is
empty or has one node."**

- Part 1 · A linked queue keeps two references. enqueue is walked three times, dequeue is
  walked until the queue is empty and then called once more, then 04c shows why the class
  keeps lastNode.
- Part 2 · Each node in a deque has prev and next. addToBack and removeFront are walked on a
  doubly linked chain, then the ring and the two votes (removeBack, isEmpty), each walked.
- Part 3 · This week's work: the four LinkedQueue homework problems as cards.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `CS 2114 · FALL 2026 · WEEK 8 · DAY 1` |
| 01b-today | three chapter tabs: a chain with two orange references, one at each end · two nodes with an arrow each way · a homework sheet with an orange pencil → the captions are the divider titles |
| 02-course-info | (another agent) the Week 8/9 clock |
| 02b-bridge-stack | FROM WEEK 7 TO WEEK 8 (bridge, 2026-10-11): W7's call stack, W5's LinkedStack chain with topNode, the same chain relabelled firstNode with lastNode added, the stack/queue/deque comparison from DequeRemoveAndWrapUp.pdf slide 3 |
| 03-chapter-1 | PART 1 OF 3 · A linked queue keeps two references |
| 04-walk-enqueue | `enqueue(x)` under the PC bar, three calls on an empty queue; the empty case sets both references, the next two link through `lastNode.setNext` and `lastNode` swings → "enqueue writes one link and lastNode, whatever the length of the chain." |
| 04b-walk-dequeue | `dequeue()` as the video writes it (with `firstNode.setData(null)`), two calls on A, B: firstNode swings and A's node fades; the second removes the last node and the `if` sets lastNode null; a third call throws `EmptyQueueException` at `getFront()` → "The one-node case needs the extra line." |
| 04c-walk-lastnode | enqueue without lastNode visits each node of a six-node chain with a `curr` ring and a maroon counter (1, 2, 3, 6), against two lines with lastNode and a blue counter (1) → "One extra reference makes enqueue O(1)." |
| 05-chapter-2 | PART 2 OF 3 · Each node in a deque has prev and next |
| 06-walk-addtoback | DLNode (`prev | data | next`, next arrows above, prev arrows below) and `addToBack` from the video, two adds; the constructor already writes prev, the else writes next → "Each link is two references, so addToBack writes two of them." |
| 06b-walk-removefront | `removeFront` from the video on A ⇄ B: the else branch (`setPrev(null)`), then the one-node deque (both references null) → "firstNode changed on every call. lastNode changed only when the last node was removed." (primes Vote 1, never names removeBack) |
| 07-peer-plus | the routine ring, `Peer Instruction W08D1` → "Two questions, both about the back of a doubly linked deque." |
| 08-vote-removeback | VOTE 1, static: the stem's lead-in as the lede, `removeBack` verbatim in an editor at `code-mid`, the question sentence above the four options; two clocks |
| 08b-walk-removeback | VOTE 1 · THE ANSWER: `removeBack` walked on A ⇄ B (else branch), then on the one-node deque (line 4 true, both references null), then once more on the empty deque (`getBack()` throws; maroon); captions rule out C, then A and B; `.verdict` D |
| 09-vote-isempty | VOTE 2, static: the stem verbatim as the lede, the `isEmpty` frame in an editor, the four expressions as options in mono; two clocks |
| 09b-walk-isempty | VOTE 2 · THE ANSWER: a board, one column per state (empty, one node, two nodes; each drawn in its column head, one per press), rows "is it empty?" and A–D filled with true/false; D's one-node cell takes the orange tint and D's disc fills maroon; `.verdict` D |
| 10-chapter-3 | PART 3 OF 3 · This week's work |
| 11-hw-linkedqueue | WEEK 8 HOMEWORK: the PL problems' own example queue (1 → 2 → 3) left with a card of what LinkedQueue already has; four problem cards right (title, signature, the part to think hardest about); signpost → "8 problems, your best 4 count, due Friday" |
| 17-next-class | (another agent) the same clock, static |
| 99-closing | dusk |

## Slide by slide

- **Node grammar (04, 04b, 04c, 11).** W4D1/W7D2 Node boxes: `data | next`, blue arrows,
  `null` as the word in stone inside the next compartment until it is written. The
  references `firstNode` and `lastNode` are blue pills above the chain (the tool blue: they
  are references) with a stone `null` beside a pill while it is null. A reference arrow
  fades in when first assigned and then SWINGS (CSS `d: path()` between two same-shaped
  cubics) when re-pointed; it fades out when set to null. A `next` arrow written by
  `setNext` Creates (shaft by dashoffset, a separate head fades in after). Writes wash the
  compartment orange for that step; a node that nothing refers to fades. The node being
  built in the current call (`newNode`) takes the orange 18% tint with a small orange
  `newNode` label under it, and goes back to the panel colour when the call returns
  (no separate newNode pill: the tint says it without another arrow).
- **DLNode grammar (06, 06b, 08b, 09b).** Boxes 240 × 80 (revised 2026-10-11; first build 210 × 80),
  three 80 px compartments `prev | data | next`, labels at `--t-micro`; `next` arrows arc ABOVE the chain, `prev`
  arrows arc BELOW it, both blue; the same pills and nulls as above. The DLNode field order
  in the video's class is `data, next, prev`; the drawing follows the constructor
  `DLNode(prev, data, next)` and the video's hand drawing (prev left, next right).
- **04.** 12 presses: enqueue(A) on empty (new node, isEmpty true, firstNode, lastNode),
  enqueue(B) (new node, else, setNext, lastNode swings), enqueue(C) (new node and the test
  as one block, setNext, lastNode swings), the rule. firstNode is unchanged after press 3.
  Names: `newEntry` shortened to `x` (`Node newNode = new Node(x, null);` is 37 characters:
  37 × 19.2 + 70 = 780 px at `--t-code`); `newNode`, `firstNode`, `lastNode` kept.
- **04b.** 13 presses: run 1 (front = A, setData(null) washes A's data and A becomes null,
  firstNode swings to B and A's node fades, the if is skipped, return A); run 2 (front = B,
  B's data null, firstNode becomes null while lastNode still refers to B, the if is true,
  lastNode = null and B fades, return B); run 3: getFront() throws `EmptyQueueException`
  (maroon plate); press 13 has no walkline, so the PC bar fades out on the throw.
- **04c.** Two editors on the left: the non-empty part of an enqueue without lastNode
  (`curr` from firstNode, `while (curr.getNext() != null)`, `curr.setNext(newNode)`) and the
  two lines with lastNode. Right: a six-node chain (boxes 130 × 76, value 56 | next 74, no field labels, pitch
  156; first build 116 × 76 with labels) with both
  pills, a blue `curr` ring that moves node to node (translateX, a real move), and two
  `.moves` counters labelled "nodes visited": maroon for the walk (1, 2, 3, then 6 in one
  press: D, E, F), blue `--ok` for lastNode (1). The write is an orange wash on F's next
  compartment; the new node is not drawn (the slide is about the visits). 8 presses; the
  last has no walkline.
- **06.** 9 presses: addToBack(A) on empty (constructor, isEmpty true, firstNode,
  lastNode), addToBack(B) (the constructor's prev arrow draws below the chain at once, the
  else, `lastNode.setNext` draws the next arrow above, lastNode swings), the rule. The
  video's `DLNode newNode = new DLNode(lastNode, newEntry, null);` is split over two lines
  (one PC block) and `newEntry` shortened to `x` so the editor is 800 px at `--t-code`.
- **06b.** 11 presses: run 1 on A ⇄ B (front = A, firstNode swings to B while B's prev
  still points at A, the else, `setPrev(null)` washes B's prev, the prev arrow fades and A's
  node fades, return A); run 2 on the one-node deque (front = B, firstNode null, the if is
  true, lastNode = null and B fades, return B); the closing line. removeBack is not named.
- **07.** W7D1's ring; week 8, `Peer Instruction W08D1`, the takeaway line.
- **08 / 09 (votes).** W7D2 06's layout (the lede, the editor left, the question sentence
  and the options right), the editor at `code-mid`. Two clocks copied from W7D2 06
  (1:30 vote, 2:30 discuss) so each vote is about 7 minutes with its walk. 09's options are
  code, set in mono (at `--t-small` since the revision, A wrapping after `&&`).
- **08b.** 13 presses: run 1 on A ⇄ B (back = B, lastNode swings back to A, the else,
  `setNext(null)` washes A's next, the next arrow fades and B fades, return B); run 2 on the
  one-node deque (back = A, lastNode becomes A's prev = null, line 4 is true, `firstNode =
  null` and A fades, return A); press 11 runs it once more on the now empty deque:
  `getBack()` throws (maroon plate), so C's state never reaches line 4; press 12 rules out A
  and B; press 13 the verdict in the caption cell; the h2 is the conclusion.
- **09b.** One HTML grid: a label column (580 px since the revision; 770 at first build) and
  one column per state (345 px). The
  column head is the state drawn small (pills, mini DLNodes); under it five cells: "is it
  empty?" and the four options, `true`/`false` in mono. A column (head and cells) arrives
  per press, cells staggered. A, B and C match "is it empty?" in every column; D's
  one-node cell takes the orange tint and D's letter disc fills maroon. Press 4 is the
  verdict in the caption cell. **Deviation from the brief**: the brief drew the three states
  on the left and the board on the right; here each state heads its own column, so a
  drawing and its values are in the same column.
- **11.** W5D1 13's grammar: left (760 px) the PL problems' own example
  `(firstNode) 1 --> 2 --> 3 (lastNode)` drawn as three nodes with both pills, a card of
  what LinkedQueue already has, the signpost; right four cards one per press: PL title,
  signature without `public`, the part to think hardest about as one short sentence pair
  (no code).
- Timing: clock 3, the three queue walks about 10, the two deque walks about 6, ring 1,
  votes about 7 each (1:30 + 2:30 of clock plus the walk), homework 3, next class 1:
  about 38 of 50.

## Translated, dropped, unverified

- **Vote keys come from the PrairieLearn twins**, not from Runestone: Vote 1 D
  (`u10q07_linkeddeque_tracing_b`, the same stem, code and options, keyed "removing from a
  deque with one item"), Vote 2 D (`u10q07_linkeddeque_tracing_c`, keyed
  "(firstNode == lastNode)"). Both agree with tracing. Confirm in Runestone's results view
  before class.
- Vote quirks kept from the Runestone paste: `public T removeBack(){` with no space, the
  braceless if/else; Vote 2's "NOT", "< fill in code here >", and lowercase `public` (the
  twin has "Public" and no question mark; Runestone's text is used). The twin's options
  start lowercase ("removing from …"); Runestone's "Removing" is used.
- **The video differs from the brief in `dequeue()`**: LinkedQueueRemove.pdf has
  `firstNode.setData(null);` between `T front = getFront();` and
  `firstNode = firstNode.getNext();` (and a comment "handle case when dequeued the only
  node remaining" above the if). The video's version is used: 04b walks the setData line; the comment is
  left out to save a line.
- The video's queue constructor is `LinkedQueue()`; its deque has a method `initialize()`
  instead of a constructor (DequeIntro.pdf slide 6). Not shown on any slide.
- `@Override` and `public` are dropped from the walked methods (not the vote code) to save
  width; `newEntry` is shortened to `x` in 04 and 06.
- **Which line throws is not in the videos.** The videos say only that dequeue on an empty
  queue gives an EmptyQueueException (LinkedQueueRemove.pdf slide 4); the deck follows
  Carrano's code, where `getFront()` (queue) and `getBack()` (deque) throw
  `EmptyQueueException`. The homework's own `LinkedQueue` differs: its `getFront()` returns
  null on an empty queue and its `dequeue()` throws `NoSuchElementException` (x702/x703
  starter code). The homework slide does not mention either.
- 04c's enqueue without lastNode is the deck's own code (the module only says enqueue is
  O(1) "with use of lastNode reference"); it shows only the non-empty case.
- Homework: "Week 8: Queues — Coding Practice", 8 problems at 10 points, `bestQuestions: 4`,
  due Fri Oct 16 23:59:59 (`allowAccess`; three named students have to Sat Oct 17, not on
  the slide; a credit-0 window stays open to Dec 31). x700's method is `enqueuePractice`,
  not `enqueue` (the card shows the PL signature).
- Challenge Exercise 08 "Carrano Deque" (Friday; where it is submitted is in no source,
  so the notes name it only) and Project 2 "Linked Chains + Generics" Deliverable 3
  (prototype + tests on 2+ element types, at the start of your lab) are in the notes of 11.
- The Runestone activity ids `vtcs2_deque_edgeCases` and `vtcs2_deque_isEmpty` and the
  assignment name `Peer Instruction W08D1` are from the brief's paste, not seen in
  Runestone.
- Dropped: nothing from a legacy deck; this deck had no F25 source. The ArrayQueue half of
  the module (one unused location, ensureCapacity, wrap-around) is Day 2's.

## Status — 2026-10-11, first build

- 17 slides written here (all but 02 and 17, which the clock agent wrote into the folder
  before the sweep; they were in place, so no temporary manifest was needed).
  `add_sids.py` run on the 17 new slides only; `lint.py` clean on all 19.
- Sweep (`timeout -k 5 150 tools/measure/run.sh "$PWD"`, about a minute), slack at the
  last step: 01 319 · 01b 166 · 02 36 · 03 322 · 04 143 · 04b 182 · 04c 166 · 05 322 ·
  06 95 · 06b 134 · 07 33 · 08 46 · 08b 156 · 09 56 · 09b 73 · 10 366 · 11 43 · 17 14 ·
  99 389. No right/left overflow, no clipped code. The vote clocks on 08 and 09 are
  listed as "over" because they sit in the head band, as on every vote slide.
  **17-next-class has 14 px of slack** (not this build's file; left for its author).
- Sizing changes after the first sweep: 08 ran 25 px over with the shared 80 px key discs
  → 56 px discs (as W7D1 11). 11 ran 126 px over → one-line hints (PIL: the longest,
  "right after the first: 1 → 4 → 2 → 3; mind a one-node queue", is 738 px in a 770 px
  card), tighter card padding, the API line "Node: getData() · getNext() · setNext()"
  (with `Node<T>:` it wrapped), the figure 150 px tall with its label under the chain,
  the signpost wording exactly as briefed ("best 4 count"), 16 px gaps. 07's plant line
  moved from baseline 960 to 940 (W7D1's ring had 13 px of slack).
- Not checked in a browser: the swings, washes and fades (no Playwright, by rule).
- Not committed (`git add "week 8 - day 1"` when asked; never `-A`).

## Review — 2026-10-11 (main session, after the three agents)

- `02-course-info` and `17-next-class` were written by a third agent from W7D1's clock: left
  half Week 8 (Oct 12–16), right half Week 9 (Oct 19–23); steps 1 bracket (Weeks 8 and 9
  posted, Week 10 past the edge), 2 Week 8 homework (blue) + CE 08 Carrano Deque (maroon)
  to the Friday pole, 3 P2 D3 at your lab, 4 the 9.1 + 9.2 modules Sunday, 5 Week 9 (HW +
  CE 09 Linked List Debug Friday, P2 D4 final over "your Week 9 lab", 10.1–10.3 to the
  Sunday at the edge), 6 the Home page / Canvas calendar tiles. No test band (Test 2 Thu
  Oct 29 is in the notes only; the MW day is not announced). "your lab day" at x 583; the
  Friday tick is static. 17 is 02 made static.
- `17`'s caption was two lines (slack 14); it is now one line at y 940, "Next class: a
  queue on an array. Homework and Challenge Exercise 08 are due Friday." (slack 36).
- `02`'s notes: the "[NOT IN ANY SOURCE: how many problems …]" gap was filled (eight
  problems, four linked-queue and four array-queue, 10 points each, best four count). The
  remaining gap, the length of the D4 presentation, is in no source.
- Vote text checked mechanically against the paste (tags stripped, whitespace removed):
  every 25-character window of the stem, code and options is on the slide.
- Sweep after the review, all 19 slides: no overflow; 17 = 36, 02 = 36, 07 = 33 (the ring,
  raised 20 px by the builder), everything else as in the Status block.
- Still to do by hand: confirm both keys (D, D) in Runestone's results view.
- Not committed (`git add "week 8 - day 1"` when asked; never `-A`).

## Revision — 2026-10-11 (type floor + prose)

The instructor's review: "some fonts are too small" and "do a pass for mannered prose".

Type floor: no slide text under `--t-micro` (28 px); `--t-micro` only for labels inside
drawings; sentences at `--t-small` (36 px) or larger. The only `--t-tag` left is the
`.tlabel` under the two vote clocks on 08 and 09 (the shared pattern). Fits were checked
with PIL (Nimbus Sans, Nimbus Roman) and the mono advance of 0.6 em before the sweep.

| slide | sizes changed |
|---|---|
| 04, 04b | node field labels, `null` and the `newNode` label 21 → 28; field labels at baseline 178, the `next` label 4 px left so 67 px fits the 76 px compartment |
| 04c | the 21 px field labels are dropped (a 28 px "data" does not fit a 56 px compartment; 04 and 04b name the parts); boxes 116 → 130 wide (value 56 \| next 74), pitch 156 kept; values 28 → 36; F's `null` 21 → 28; curr ring, F ring and the lastNode arrow moved to the new box centres |
| 06, 06b, 08b | DLNode boxes 210 → 240 (compartments 70 → 80) so the 28 px labels fit; labels and `null` 21 → 28; every arrow end, wash and swing target moved with the boxes |
| 07 | the five station labels 28 → 36 mono, rewrapped so that each clears the ring, the body edges and the plant; station 1 now reads "from the Canvas home page, open / Peer Instruction W08D1 in Runestone" ("the Week 8 assignment" dropped for width); station 4 reads "and change it if the group changed your mind" |
| 08 | no change to the options: they are already `--t-small`; at `--t-body` they need about 90 px more than the 46 px of slack |
| 08b | the verdict 28 mono → 36 in the body face (843 px for the longest option in an 886 px column); the caption cell reserves 215 px |
| 09 | options 32 → 36 mono with 56 px discs; the text is capped at 23.5ch so A wraps after `&&` |
| 09b | label column 770 → 580 px, option code 28 → 36 mono (A wraps after `&&`), letter discs 44 → 48 px with 36 px letters, verdict 28 → 36 mono; the mini drawings redrawn at 340 × 150 with pill text and `null` 21 → 28 |
| 11 | hints 28 → 36 (one short sentence pair each, longest 730 px in 770); example nodes 120 → 150 wide, field labels, `null` and the caption 21 → 28, values 28 → 36; card padding and gaps tightened. The signatures and the class card stay mono at 28: at 36 "Node<T> firstNode · Node<T> lastNode" is 778 px in a 690 px card |

Captions on every walk were already `--t-small`; no caption size changed.

Slack after the revision (sweep, minimum over all steps): 01 319 · 01b 166 · 02 36 ·
03 366 · 04 143 · 04b 182 · 04c 166 · 05 322 · 06 95 · 06b 134 · 07 33 (the ring) · 08 46 ·
08b 111 · 09 103 · 09b 37 · 10 366 · 11 43 · 17 36 · 99 389. No overflow. `lint.py` clean.
Not checked in a browser: the text inside the SVG drawings (the sweep measures the SVG
box, not each label); the fits there are by the advances above.

Prose: headings, captions, `.slide__desc`, notes, HTML comments and this file. Removed:

- figurative verbs for code and data: "B lets go of A" → "firstNode.setPrev(null) sets
  B's prev to null"; "lastNode moves to C" → "lastNode now refers to C"; "the queue empties"
  → "the last node is removed"; "each node knows both neighbours" → "each node in a deque has
  prev and next";
- dramatised scale: "Six visits for one link; 1,000 nodes, 1,000 visits." → "curr.setNext(newNode)
  writes one link after six visits. With n nodes it takes n visits."; "however long the chain
  is" → "whatever the length of the chain";
- colon-for-effect fragments: "isEmpty() is true: firstNode is null." → "isEmpty() is true
  because firstNode is null."; "Canvas: Weeks 8 and 9 are both posted." → "Weeks 8 and 9 are
  both posted on Canvas.";
- slogan headings: "The one-node case is the one with the extra line" → "The one-node case
  needs the extra line"; "removeFront(): the new front node forgets the old one" →
  "removeFront() sets the new front node's prev to null";
- em-dash asides in the notes ("Step 1 &mdash; …" → "Step 1. …"); the only `&mdash;` left in
  the notes is the "Answer: D &mdash;" opener on 08, 08b, 09 and 09b.

Chapter titles changed with the prose pass (01b, 03, 05 and the manifest): "A queue on a
linked chain: two references" → "A linked queue keeps two references"; "A deque: each node
knows both neighbours" → "Each node in a deque has prev and next". Vote text, `.editor` code
and option text are unchanged.

## Bridges — 2026-10-11

The instructor: the lecture flow lacked "bridges from last week and then between day 1 and
2". One slide here, two in Day 2 (see its PLAN.md).

- **02b-bridge-stack** (`#slide-02b`, after `02-course-info`). Kicker `FROM WEEK 7 TO WEEK 8`,
  h2 "A stack is last in, first out. A queue is first in, first out." One SVG (1664 × 210,
  canvas px), one caption at a time under it at `--t-small`, the table under that.
  Press 1: W7D1 09's call stack at reduced size (frames 300 × 56 on a 64 px pitch,
  fact(1) running in orange on top of fact(2) and fact(3)) grows in. Press 2: the Week 5
  LinkedStack chain (W8D1 04's 190 × 90 Node boxes, A → B → C → null) with one pill,
  `topNode`, grows in. Press 3: the pill's label crossfades to `firstNode`, a `lastNode`
  pill grows in above C and its arrow Creates (head after the shaft). Press 4: the
  comparison table fades in, quoted from DequeRemoveAndWrapUp.pdf slide 3: stack adds
  `push(item)` and removes `pop()` at the front (top); queue adds `enqueue(item)` at the
  back and removes `dequeue()` at the front; deque adds `addFront(item)` / `addBack(item)`
  and removes `removeFront()` / `removeBack()` at the front / back. The video's peek(),
  getFront() and getBack() are in the notes only.
- Captions were rewritten from the brief to avoid colon fragments ("Week 7: a frame is
  pushed …" → "In Week 7, a frame is pushed on each call …"). The chain is labelled A, B, C
  left to right in both views so the queue matches 04's state (firstNode → A, lastNode → C).
- `add_sids.py` on the new file only; `lint.py` clean on all 20. Sweep: 02b slack 51 at
  its last step; no overflow; the other slides unchanged.
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
