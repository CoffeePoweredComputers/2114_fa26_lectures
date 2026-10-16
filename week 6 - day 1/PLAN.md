# Week 6 · Day 1 — plan

Shell built 2026-09-25 for Monday Sep 28 (MW, NCB 320) and Tuesday Sep 29 (TR, Squires) —
one deck, both sections. The instructor asked for the template with the usual start and end
slides only; the content of the hour arrives separately and is not in this deck yet.
Shared css/js/assets/tools cloned from `week 5 - day 1` (DECK-PROMPT §2: the newest copies,
with `data-hold`/`data-also` in `deck.js` and `.moves` in `deck.css`). Sources for the
clock: `~/Downloads/cs2114-schedule-fall2026.html` and `cs2114-deadline-schedule.csv`.

## Through-line

**"Everyone missed different questions, so the chart is a map; and the person who flips a
setting never meets the people it lands on, so you need words for saying why that is
wrong."**

- Part 1 · Test 1: how it went, and where to practice — the results chart by topic, one
  practice pill per question (five minutes).
- Part 2 · Peer instruction — the ring, then the W06D1 votes (the questions are not in the
  deck yet; a placeholder slide says what to add).
- Part 3 · Ethics, part 2: three ways to say why it matters — fifteen minutes: three lenses
  (utilitarianism, virtue ethics, Kantian ethics), each as a question in plain words, then
  moral distance as the reason they are hard to apply, then ten minutes in groups on a
  concern of their own.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `WEEK 6 · DAY 1` |
| 01b-today | three chapter tabs: a mini dot chart · two heads and a speech bubble · three lens rings over a question mark → the captions are the divider titles |
| 02-course-info | the Week 6/7 clock: now band on Mon+Tue; **Test 1 Redo band on Wed–Thu of this week, step 1**; Fri ethics module (no Week 6 homework) + CE 06; P2 D1 (scope, teams re-form) at your lab in the P2 mix; 7.x modules Sunday; Week 7 rows (HW to a Friday marked Fall Break, no CE, P2 D2 spec over "your Week 7 lab", 8.1 module Sunday) → "next class is the redo" |
| 03-chapter-1 | PART 1 OF 3 · Test 1: how it went, and where to practice |
| 04-test1-graph | TEST 1 RESULTS: a dot-and-whisker chart of all 16 positions grouped by the five W4D2 test-map topics, laid out as a table (question number, short name, a rule under every row); x = average score 0–100%, the dot at the student-weighted mean, the whisker from the lowest- to the highest-scoring variant; at the right a blue pill naming the Test #1 Practice question that drills the type; no good/bad colouring; one topic per press → "find the rows you lost points on, drill those pills" |
| 04b-chapter-2 | PART 2 OF 3 · Peer instruction: three questions |
| 05-peer-plus | the routine ring, W06D1 wording; plant "Three questions: a stack trace, a class hierarchy, a requirement" → straight into Vote 1 |
| 05b-vote-stack | VOTE 1, static (Runestone question 1 of 3, `vtcs2_stacks_tracing`): the stem verbatim (its stray "?." kept) at the full width; left, the eight operations in a 700 px editor at the dense size; right, the four options in mono; two clocks → discuss "what does the first pop return, and where does it go?" |
| 05c-walk-stack | VOTE 1 · THE ANSWER: the eight lines under the PC bar, one per press; the stack drawn top-up as a column of cells on the right — pushes grow a cell in, pops fade one out (`:has()` on the popping step's caption), the first pop's value lands in a `str = "R"` pill and the last push grows R back on top; one caption per press; `.verdict` C (R V P K) → "push(str) is the trap" |
| 06-vote-store | VOTE 2, static (Runestone question 2 of 3, `vtcs2_inhertance_override_2_202507-2`): the verbatim question line as the lede; left, the stem's first sentence over its four bullets as cards (the shared requirement outlined in orange); right, options A–E verbatim at the micro size; two clocks → discuss "which fields do all three share, and where should a shared field live?" |
| 06b-walk-store | VOTE 2 · THE ANSWER: three UML boxes each repeating productID and price; Product grows in above and the six shared lines travel up into it (three copies converge), the boxes shrink to their own fields, the generalisation arrows draw on; a two-line caption dismisses B, C, D, E (is-a; written twice; three times; an interface holds no fields); `.verdict` A → "a hierarchy is a decision you can defend with two tests" |
| 07-vote-reqs | VOTE 3, static (question 3 of 3, `vtcs2_design_nonfunctionalreqs_202507`): stem verbatim; left, a laptop with a cart and three users (neutral ink, nothing points at an option); right, the five "shall" statements verbatim; two clocks → discuss "sort the five into two piles and name the piles" |
| 07b-walk-reqs | VOTE 3 · THE ANSWER: two dashed bins ("what the system does" / "how well it does it"), the five statements as cards between them; one card per press slides into its bin and a stone tag lands beside the bin (availability, security, performance, behaviour, capacity); caption "How-well requirements are where values get written down: who it protects, who it serves"; `.verdict` D → the bridge to Part 3 |
| 14-chapter-3 | PART 3 OF 3 · Ethics, part 2: three ways to say why it matters |
| 14b-acm-code | ACM CODE OF ETHICS · THE FIRST FOUR PRINCIPLES: the 2018 Code's headings 1.1–1.4 verbatim on a paper sheet; step 1 the vague words (well-being, harm, honest, fair, discriminate) wash orange one by one; step 2 "You probably have reasonable questions about how to navigate this. And you have concerns of your own."; step 3 the W1D1 veil drops with "I'm not an ethicist, so I'm not going to be able to answer these well."; step 4 "So I'm going to ask one." |
| 14c-pipeline | HOW THIS WILL GO: five stations in a row, an arrow drawing on into each — I introduce a few ideas (today) · you put your questions in a form (today, orange) · I interview an ethicist with some of them · you watch the short clips (orange) · we discuss them, briefly, in class; plant "your questions steer what I ask; the form stays open after class" |
| 16-three-lenses | THREE LENSES, the overview: three tiles in the garden's colours, a drawing and the one question each (utilitarianism · virtue ethics · Kantian ethics); no words yet → "one lens at a time" |
| 16b-utilitarianism | LENS 1 OF 3 · OUTCOMES: the balance large on the left; right, the definition + chips (consequences · the greatest good · everyone counts), the question to ask ("Who ends up better off, and who ends up worse off?" …), the weakness ("a few people can be badly hurt and the average still looks fine") |
| 16c-virtue-ethics | LENS 2 OF 3 · CHARACTER: the mirror; chips (character · habit · honesty, courage, fairness); "What kind of person, or company, does building this make you?" …; the weakness ("honesty is easy when nothing is at stake; the test is when the deadline is close") |
| 16d-kantian | LENS 3 OF 3 · DUTY: the tablet; chips (duty · a rule for everyone · never merely a means · consent); "What if everyone did it?" with the false promise and the taxi driver ("would it still work" was vague, 2026-09-27) … (reworded twice 2026-09-27; final wording from SEP "Kant's Moral Philosophy": universalisability as a consistency test, not a consequence test; humanity formula with consent as the practical test; weakness = the murderer at the door); the weakness ("no exceptions, even when the result is terrible: the murderer at the door"); the notes carry "three reasons, hold more than one" |
| 15-moral-distance | MORAL DISTANCE: WHY THE LENSES ARE HARD TO APPLY (after the lenses, 2026-09-27): one engineer at a laptop, a dashed gap draws across the slide to a crowd of twenty ("the people it affects, whom you never meet"), captions "every lens asks about the people your code affects" / "you will never meet most of them", then the definition, then three chips (not my department · many hands · a number, not a person); no case → "ten minutes on a concern of your own" |
| 16e-discussion | SMALL GROUPS · TEN MINUTES: three moves (name something in technology and AI that concerns you, with five starter chips · put it as a question using one of the four words, each word with its question written out in plain speech · or ask about the words themselves and how they relate to you, a future technologist); the 10:00 timer at 240 px over the form plate (QR + link, **placeholders until the form URL arrives**) |
| 17-next-class | the same clock, static; caption: next class is the Test 1 Redo — charged laptop, student ID, LockDown Browser |
| 99-closing | dusk |

## Slide by slide

- **Review 3 (2026-09-25, later still): "add a bit more space between rows".** The kicker
  line (about 68 px) was traded for row pitch: no kicker, the h2 reads "Test 1 results:
  average score, and where to practice", the body starts at y 208, rows sit at a 40 px
  pitch (was 33) with a 12 px gap between topics and a heavier rule closing each topic
  (was an 18 px gap alone); the axis at y 920, tick labels at 944, sweep slack 34. The
  rows are generated from a data table in the build script (mean and variant range of
  percent correct per position); regenerate rather than hand-edit coordinates.
- **Review 2 (2026-09-25, later):** "I want the x axis to just be average score. none of
  this 'missed it'. make each question have a line under it with a question number. Then
  put pills off to the right that say the pool on PrairieLearn where you can practice that
  topic. also, get rid of the review slides and the 'fill in the [filled slots] first' —
  every student might have gotten a different question wrong." Applied fully: 02b's axis
  is average score, every row is a table line with its test question number and a
  practice pill, the maroon/stone "hard" coding is gone (ink dots), and 02c (practice
  map) and 02d (three worked stand-ins) are out of the deck. Their files are not in
  `slides/` any more; copies sit in the session scratchpad
  (`removed-02c-test1-practice.html`, `removed-02d-test1-examples.html`) in case the
  stand-ins are wanted again, and the paragraphs below describe what they were.
- **02b / 02c / 02d — the Test 1 debrief, as first built** (added 2026-09-25 on the instructor's request: an
  overview of the hardest question types, a few examples, and where to practice; rebuilt
  the same day after the review "super text heavy, divide things up, theme them by
  general topic, make the graph look like a difficulty graph with error bars": the ranked
  list became a chart grouped by the W4D2 test-map topics plus a separate practice map).
  The whisker is the only spread the data carries: each position was served as 1–4
  variants and the CSV gives each variant's percent correct, so the whisker runs from the
  easiest to the hardest variant (Q1 was one fixed item: a dot, no whisker). The binomial
  95% interval on 348 answers is ±3 to ±5 points, smaller than a dot, and is not drawn.
  Topic membership follows the W4D2 map: testing & exceptions Q1 Q3 Q4 Q6 Q15 Q16;
  objects & references Q2 Q7 Q8; bags on arrays Q5 Q14; linked chains Q11 Q12; types Q9
  Q10 Q13. Topics are ordered by their mean share missed (35.8 · 33.6 · 29.2 · 27.8 ·
  23.3), rows within a topic hardest first. Per position, mean and variant range of the
  share missed: Q4 55.2 (41.7–76.4) · Q2 50.8 (37.3–62.1) · Q13 50.9 (28.4–74.4) · Q5
  50.6 (43.1–57.5) · Q1 48.9 · Q16 40.5 (13.8–69.0) · Q8 35.1 (18.9–51.4) · Q3 32.8
  (17.5–47.5) · Q12 27.9 (12.2–48.7) · Q11 27.6 (10.4–60.3) · Q6 23.6 (18.8–28.1) · Q7
  14.9 (14.1–15.3) · Q15 13.5 (0.0–23.9) · Q10 10.6 (6.2–15.7) · Q9 8.3 (6.9–11.0) · Q14
  7.8 (2.1–12.6).
  Sources: `~/Downloads/Test1_items_for_study_guidance.csv` (Canvas item analysis of
  Test 1: 50 items over 16 quiz positions, 348 students, per-item percent correct and the
  distractor counts), `~/Projects/pl-vt-cs2114/canvas-banks/*.md` (the Canvas bank text,
  copied 2026-09-15; the key is not on the page, so the keys come from the CSV's
  `correct_answer` column), and
  `courseInstances/Fall2026/assessments/practiceExams/test1/infoAssessment.json` ("Test #1
  Practice", set Practice Exams, `multipleInstance: true`, open 2026-09-16 to 2026-12-31,
  16 slots of 2–7 alternatives, 8 or 4 points, in the order p01…p16).
  The per-position difficulty is the student-weighted mean of that position's items:
  Q4 testing equals 44.8% correct · Q13 generics 49.1 · Q2 writing equals 49.2 · Q5 bag
  intersection 49.4 · Q1 counting test cases 51.1 · Q16 JUnit setUp 59.5 · Q8 null slot
  64.9 · Q3 testing remove throws 67.2 · Q12 72.1 · Q11 72.4 · Q6 76.4 · Q7 85.1 · Q15 86.5
  · Q10 89.4 · Q9 91.7 · Q14 92.2. 02b draws the eight under 70% as "missed by" bars
  (100 − that figure, rounded) and folds the rest into one line.
  Practice slot per test position (the practice exam mirrors the test one slot per
  position, by the folder names and titles): Q1→4 (p04 count test cases), Q2→1 (p01
  equals impl), Q3→2, Q4→3, Q5→5, Q6→6, Q7→7, Q8→8, Q9→9, Q10→10, Q11→11, Q12→12,
  Q13→13, Q14→14, Q15→16 (p16 covering test method), Q16→15 (p15 JUnit setUp). The
  practice exam is not shuffled, so its on-screen question numbers are the slot numbers.
  02d does not show the test items (instructor, 2026-09-25: "I can't show them real test
  questions"). Each card is one instance of the practice exam's own generator for the
  same slot, instantiated by hand with parameters the generator can draw:
  slot 4 `count_cases_guard_clauses` with g = 2 (the null-id and full-array guards; key
  g + 1 = 3; options 2 3 4 5), slot 1 `pick_correct_equals_two_fields` with the Marquee
  tuple, showing its `cast_first` card with the combined guard (the same defect as the
  option 70 of 189 chose on the test), slot 13 `generic_method_call_compiles` with
  Confection / Macaron and Integer, five of its six lines (E dropped, as the generator
  drops one), the primitive-array line being the test's trap. The "On the test" line on
  each card states what the room did with that TYPE on the test (112 of 348 one fewer
  than the key; 70 of 189 the cast-first shape; 30 of 86 accepted the int[] call) and
  never quotes the test item. Q1/Q4 are treated as one skill (count the ways out) in the
  link line. The Generics `_because` item (39% correct) was left out on purpose: its key
  ("related by inheritance") over the popular pick ("determined later by the client") is
  arguable. The pane is 1010 px (the combined guard line is 55 characters at 28 px), the
  side column 622; code leading 1.3 on `li` and `li::before`.

- **02 / 17** — W5D1's clock one week on. The Redo band takes the Test 1 band's place
  (Wed–Thu of this week, x 366–603) and its step-1 slot, labelled as W5D1 labelled the
  Redo (`Test 1` / `Redo` / `in lecture` / `Wed MW · Thu TR`). Project 1 is over, so the
  project row is Project 2 in the P2 accent on both halves: D1 this week as a solid Monday
  cell plus the fading tail over "your lab day", D2 next week as the fading bar over "your
  Week 7 lab". Week 7 has no challenge exercise (schedule page), so that row is empty on
  the right half. The Week 7 Friday tick is labelled `Fri · Fall Break` because the
  deadline CSV still puts the recursion homework at Fri Oct 9 11:59 PM, which is Fall
  Break. The 8.x row says `8.1 module` because only 8.1 Queues is due Sun Oct 11.
  17 is generated from 02 by the build script (strip `frag`/`data-step`/`data-anim`,
  swap heading, desc, comment, captions, notes); edit 02 first and re-derive.
- **01b** — W5D1's layout with the three drawings replaced by dashed stone plates and the
  titles by orange placeholders, so the shell shows where the content goes without
  pretending to have it.
- **05** — W5D1's ring; only the week, the assignment name and the plant changed.

- **Part 3, the ethics arc, part 2 (instructor, 2026-09-25):** "leave 15 minutes: 5 for an
  ethics overview and 10 for a small group discussion … introduce 'moral distance' then
  three frameworks: utilitarianism, virtue ethics, and Kantian moral philosophy … a super
  lightweight review to give them some buzzwords, then come up with questions about ethical
  concerns they have and how they could be understood through something in the framework.
  Look at day 1's ethics thing and do it in a similar style; this is like a part 2."
  Part 1 (W1D1 20–26b) planted three ideas in the brain garden — privilege and
  responsibility (the doctor's sentence, on whose backs), the implications of our work (von
  Braun, move fast), agency (the wheelbarrow) — in quiet typographic beats, veils, and
  two-weight line drawings on tiles. Part 2 keeps that pen and adds the vocabulary:
  `15` a scene (one engineer, the gap, the crowd), `16` three tiles in the garden's three
  colours (orange, the mix, blue), `16b` the same case through the three, `16c` the
  discussion on the deck's 10:00 timer. The running case is the one the students read for
  6.1 (reading 4): the Facebook emotional-contagion study, Kramer, Guillory and Hancock,
  PNAS 2014 — 689,003 users, one week in January 2012, News Feeds tuned to show fewer
  positive or fewer negative posts, small but measurable effects on what people then
  wrote, no consent beyond the Data Use Policy. The 6.1 module's own frameworks are the
  ACM Code and JMU's Eight Key Questions (fairness, outcomes, responsibilities, character,
  liberty, empathy, authority, rights), the 8KQ chips on the lens slides were removed 2026-09-27
  ("confusing"). "Not my department" on 15 is the Lehrer line from Week 1's
  von Braun slide. The discussion output is oral (two groups read theirs out); where
  the questions should be collected, if anywhere, is not specified.
- Timing (timers shortened 2026-09-27: vote 1:30, discuss 2:30, was 2:30 + 4:00): Part 1
  about 5 minutes; Part 2 three votes at 4 minutes of clock each plus about 2 of walk, so
  about 18 plus the routine; Part 3: 14b (1 min), 14c (1), 16 (0.5), 16b–16d (0.5–1 each),
  15 (1), 16e (10) — about 16. Total about 42 of the 50, leaving 8 for the clock slides,
  dividers and transitions.

- **Finalised 2026-09-26 (plan `i-think-each-of-greedy-rocket`):** the instructor pasted
  Peer Instruction W06D1 (five questions; the paste held 1, 3, 4, 5 and 5 again, so
  question 2 of 5 was never seen) and asked for the two most relevant to ethics / design /
  MVC: questions 4 (the store hierarchy) and 5 (functional vs non-functional) — confirmed.
  Ethics: "give the overview then one slide per" lens; the discussion restructured on the
  instructor's words ("come up with some things you're concerned about with what is going
  on in Technology and AI. Articulate that question in the form of some of the keywords you
  just learned about. You're also welcome to articulate questions generally about what
  these terms mean and how they relate to you as future technologists"); the output is a
  form each student fills with as many questions as they like (URL to come).
- **The final assignment (instructor, 2026-09-27):** Peer Instruction W06D1 now has three
  questions, all run: 1 `vtcs2_stacks_tracing` (push K P G R, pop into str, pop, push V,
  push str; key C = R V P K by tracing), 2 the store hierarchy, 3 the requirements. The
  earlier five-question paste (with the linked-chain pop and the constructor/override
  trace) was superseded. `05b`/`05c` added; 06/07 renumbered Votes 2 and 3; the ring's
  plant, the divider and the agenda say three questions. 05b's stem is 262 characters,
  so it runs at the full 1664 width (three lines, four at the 1440 cap) and the four
  option rows take 16 px padding; the ring's plant is capped at about 77 mono characters
  at the small size (80 ran 32 px past each edge).
- **06 / 07 (the votes):** the deck's `.vote` layout with `--long` options, but the left
  panel narrowed to 640 px and the options at the micro size with 8 px row padding,
  because five 70–110-character options do not fit the shared layout at the small size
  (first sweep: 06 ran 71 px over, 07 had 6 px of slack). 06 quotes the whole stem: the
  question line as the lede, the first sentence over the four bullets as cards. 07's
  drawing is deliberately featureless (a laptop, a cart, three users) so nothing on the
  left points at an option.
- **06b (fields go up):** UML boxes in canvas px; the argument is the move — the two
  shared field lines translate (`translate(var(--dx), -218px)`) out of all three boxes
  into one Product box while the kept lines close up 72 px and the rect's `height`
  transitions to `--h2`; then the generalisation bus draws on and its hollow triangle
  fades in. The `:has(.ws__prod:not(.is-pending))` idiom drives the move off the Product
  frag. Options dismissed in one caption each (is-a; twice; three times; no fields).
- **07b (the sort):** the cards are frags that never hide (`.is-pending { opacity: 1 }`)
  and translate into their bin on their step; the tag lands beside the bin, not inside the
  card (a tag inside overlapped the third text line). Card text is JetBrains Mono at 21 px:
  30 characters a line inside a 432 px card with the text at x+40 — 32 characters ran 19 px
  past the bin on the first sweep.
- **16 / 16b–16d:** the overview keeps the three tiles and drawings with one question
  each; every lens slide is the same shape — the drawing at 640 px, then three beats:
  definition + chips, the lens as a question in plain words (the
  feed study through each lens was dropped on 2026-09-27: "don't use this random
  example"; the plain-words question is the same sentence 16e hands back), the catch. Headings are one line at the warmup
  size (about 70 characters is the limit; the Kantian heading at 72 wrapped and pushed the
  column 76 px over, so all three were shortened) and the Kantian definition was cut to two
  lines; its coda line is spoken (notes).
- **14b / 14c (instructor, 2026-09-26):** "lead with a slide with the first few items from
  the ACM code of ethics and highlight a few of the vaguer terms, and say you probably have
  reasonable questions on how to navigate this and you have your own concerns. Then have a
  blur effect with 'I'm not an ethicist so I'm not going to be able to answer these well!
  (So I'm going to ask one)'. Then introduce the pipeline …". 14b quotes the Code's four
  headings (short, attributed on the sheet; the Code is CC BY-ND) and carries the veil as
  its last two presses (W1D1 24's wash: blurred, whitened, the sentence in display type),
  so the blur falls over the code itself. 14c is the pipeline in the practice-map grammar
  laid out in a line; the students' two stations take the orange edge. The sweep flags
  14b's veil as overflow because it covers the whole 1920×1080 slide, which is the design
  (W1D1 22 and 24 do the same). Dates for the interview, the clips and the discussion are
  placeholders in 14c's notes.
- **15, review 2026-09-26 ("I have no idea what these numbers mean")** put the feed study's
  case on the slide as captions. **Review 2026-09-27 ("add moral distance to the end after
  the Kantian thing and phrase it as a way to talk about why things are hard to apply;
  don't use this random example"):** 15 now follows 16d in the manifest (file name and sids
  unchanged), the feed study is gone from it and from the three lens slides, the h2 reads
  "Moral distance: why the lenses are hard to apply" at the warmup size (the SVG keeps its
  232–984 viewBox and sits at 1:1 on the body's bottom edge), the captions are "Every lens
  asks about the people your code touches" / "You will never meet most of them. None of
  them are in the room", the crowd has no number, and the notes bridge to the discussion.
- **16e:** the timer at 240 px so the form plate fits under it (review 2026-09-27: the arc
  overlapped the plate because the deck's `.timer` box is 150 px while the arc was 320; the
  slide now sizes the box and the arc together; the QR is pinned at 180 px so the real
  image keeps the plate's height); the starter chips in neutral ink; the four words with
  their questions as a `dl` (review 2026-09-27: "the ask-a-question chips are too short;
  'who is in the sum' is not how any novice would phrase it and does not summarise") in
  the lens colours plus maroon for moral distance, the same sentences as the lens slides'
  plain-words beat; move 3 shortened to two lines to fit; the `.steps` numeral is
  suppressed on the nested chip list.

## Translated, dropped, unverified

- The assignment name `Peer Instruction W06D1` follows the W02D2–W05D1 pattern; not yet
  seen in Runestone.
- **Test 1 Redo**: drawn from the schedule page ("Test 1 Redo Thu Oct 1 — in class") and the
  instructor's 2026-09-20 statement (second class of Week 6 for each section: MW Wed Sep 30,
  TR Thu Oct 1). Who takes it, whether it is optional, and how it counts are not in any
  source; the notes on 02 and 17 carry a bracketed placeholder. The 17 caption assumes the
  same rules as Test 1 (Canvas, LockDown Browser, laptop, ID).
- Homework "Week 7: Recursion" due Fri Oct 9 (deadline CSV) coincides with Fall Break;
  drawn as the CSV says and labelled, not corrected.
- Project 2 Deliverable 1 = "Scope · teams re-form" and Deliverable 2 = "Spec · declare
  generic type" (schedule page); the Canvas Project 2 overview page was not read.
- No source names the lab weekdays; projects keep the "your lab day" range.
- The 02d stand-ins are hand-drawn instances of parametrized practice questions; a student
  who opens slot 4 / 1 / 13 will see a different draw (other guards, another class name,
  another hierarchy) of the same shape.
- Test 1 numbers are from the Canvas item analysis CSV; "348 students" is the count on the
  fixed position 1. "Full code coverage" is read as branch coverage (both sides of every
  if), which is what the keys of Q1 (3) and Q4 (6) imply.
- The practice slot numbers assume PrairieLearn shows the 16 zone questions in file order
  (no `shuffleQuestions`); check one attempt in the instructor view.
- **Runestone keys** are assumed for all three: question 1 C (by tracing: R V P K), question 2
  A (one Product superclass), question 3 D (apply a discount code) — the pastes show no key;
  confirm in Runestone's results view before class.
- 14c: who the ethicist is, when the interview happens, where the clips are posted and
  which class discusses them are not given; bracketed placeholders in the notes, nothing
  dated on the slide.
- The discussion form (2026-09-27): a Google Form in the VT account, "CS2114 F26 ethics questions,
  Week 6" (topic · question · lenses as checkboxes; anonymous; resubmit link on), reached at
  https://tinyurl.com/2114-ethics; the QR is `assets/w6d1-form-qr.png` (qrencode -s 10 -m 2 -l M)
  on 16e's plate with the short link under it. The right column is 380 px so the 24-character
  link fits at the tag size; the timer box and arc are both 200.
- Ethics content: the study's figures (689,003 users, January 2012, feeds tuned toward
  fewer positive or fewer negative posts, nobody asked beyond the terms of use) are from
  the PNAS 2014 paper and the article the 6.1 reading links; the three-lens summaries are
  textbook-level (Bentham/Mill, Aristotle, Kant's categorical imperative and the humanity
  formula) and deliberately lightweight. "Moral distance" is used in its everyday sense
  (Milgram, Bauman); no source is cited on the slide.
- Placeholders (orange in Studio): the form link and QR on 16e; the redo sentence in 02/17's
  notes.

## Status — 2026-09-25, shell only

- 24 slides after the 2026-09-27 stack vote (05b 68 · 05c 122 in the sweep), 22 after the 2026-09-26 finalisation (14b ACM code + veil, 14c pipeline added later that day; sweep 14b fits at steps 0–2, 14c 83) (votes 06/06b/07/07b, lenses 16b–16d, the
  discussion 16e); `add_sids.py` run on the new ones; `lint.py` clean on all 20; sweep
  slack: 06 86 · 06b 45 · 07 86 · 07b 35 · 16 0 (tiles fill the frame by design) · 16b 104
  · 16c 153 · 16d 105 · 16e 20 (after the 2026-09-27 review) · 15 35 · 04 34 · 05 13 (inherited).
- Layout: every slide is a measured W5D1 layout with the same geometry; the new strings
  were checked by arithmetic (PIL advances, DECK-PROMPT §6). See the reply for whether
  the Chromium sweep ran.
- Not committed (`git add "week 6 - day 1"` when asked; never `-A`).
- **Plain-wording pass (2026-09-27, "do a pass for mannered prose, get rid of all of it, e.g.
  'in 5 moves'"):** across slide text and notes: "moves"/"stations" → steps; "the catch" →
  "the weakness"; "in plain words, ask" → "the question to ask"; "lands on"/"touches" →
  "affects"; "none of them in the room" cut; the three-lens questions reworded ("does the
  most good for the most people", "what do we owe people, no matter how it turns out"); the virtue and
  Kantian weaknesses rewritten as sentences instead of aphorisms; 14c's h2 is "How your
  questions get to an ethicist, and back"; 16e's h2 is "Your concern, as a question"; 06b/07b
  captions say "move up", "subclass", "non-functional requirements"; "the plant" → "the
  takeaway" in notes. Rule for this deck: say it the way a student would.
- **Lens slides, closing question (2026-09-27, "each of the three lenses gets a final question
  that ties the lens to technology; centred at the bottom, under the content, big"):** a
  `.ln__tech` p (deck.css: full-width grid row, centred, display h3 maroon) on the last press
  of 16b/16c/16d, pinned to the body's bottom by `grid-template-rows: 1fr auto` — "Whose
  week does your code make better, and whose worse?" · "What kind of engineer does shipping
  this make you?" · "If every app did this, would anyone still trust an app? / Did your users agree to what you do with their data?" ("did they agree to what?", 2026-09-27) (two lines, one per principle, 2026-09-27). 16d's right
  column had to lose its "the two principles" label and the weakness shrank to "No
  exceptions, not even to a murderer at the door." to make room; 16d's column gap is s-2.
  Sweep: 16b/16c/16d slack 0 by design (the question sits on the bottom edge), no overflow.
