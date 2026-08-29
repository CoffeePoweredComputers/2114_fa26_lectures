# Week 2 · Day 2 — reverse outline and transition plan

Written 2026-08-29 from the text-only draft of 2026-08-28; corrected the same
day after the draft's Project 1 turned out to be the Fall 2025 project. The draft had the
right *content* in the right *order*; what it lacked was the argument that
joins the slides, the chapter structure the sister decks use (today-tabs →
dividers → next-class), and the illustrated, stepped style of W1D2 / W2D1.

## The through-line

**"What does the code promise — and how do you know it kept the promise?"**

- Part 1 · An **interface** is the promise; a **data structure** is one way of
  keeping it. Project 1 (*Learning to Scope*, Weeks 3–5, teams of 3) asks both
  questions of every class in its specification — what it promises (method
  signatures) and how it keeps the promise (which structure, and why) — and
  its final deliverable checks the promise with JUnit tests.
- Part 2 · A **test** is how you check a promise. Three votes, escalating:
  does the fixture even exist (vote 1) → does the test cover every case
  (vote 2) → does 100 % coverage mean it is right (vote 3: **no**).
- Part 3 · **Every line ran and it still blew up.** Four practice questions:
  a class that keeps its parent's promise (UML → `Student`), then three
  references that promised an object and delivered `null`.

Each slide's last beat is the *plant*; the next slide's first beat is the
*pick-up*. Plants are named below as **→**.

## Chapter structure (manifest order)

| # | file | role |
|---|------|------|
| 1 | 01-title | cover (unchanged) |
| 2 | 01b-today | three chapter tabs (sister of W2D1 01b-today) |
| 3 | 02-course-info | this week's clock (sister of W2D1 02-course-info) → "and then Project 1 — next week" |
| 4 | 02b-chapter-1 | divider · PART 1 OF 3 · *Project 1, and the three words it needs* |
| 5 | 03-vocabulary | promise vs. keeping it → "your Project 1 spec asks both: the promise, and how you keep it" |
| 6 | 04-project-1 | Learning to Scope: the team walks the trail scope → spec → build (Weeks 3/4/5) → Deliverable 3 needs JUnit tests, one normal and one bad-input case per method — "what does a test actually prove?" |
| 7 | 04b-chapter-2 | divider · PART 2 OF 3 · *What does a test prove?* |
| 8 | 05-peer-plus | groups + routine (sister of W2D1 11-peer-plus) → "three questions, all on testing" |
| 9 | 06-vote-setup | VOTE 1 static (unchanged) |
| 10 | 06b-walk-setup | VOTE 1 · THE ANSWER — codewalk: JUnit builds the fixture *for you*; a local `myStr` is a second name that dies at the brace |
| 11 | 07-vote-cases | VOTE 2 static (unchanged) |
| 12 | 07b-walk-cases | VOTE 2 · THE ANSWER — the method is a fork with two exits; one assertion per exit; C passes and proves nothing → "a test can pass and prove nothing" |
| 13 | 08-vote-branch | VOTE 3 static (unchanged) |
| 14 | 08b-walk-branch | VOTE 3 · THE ANSWER — four lane-glyphs light up per option; D lights all three lanes **and fails** → "coverage says the line ran; it does not say it was right — Project 1 asks for a normal and a bad-input case per method" |
| 15 | 08c-chapter-3 | divider · PART 3 OF 3 · *Every line ran. It still blew up.* |
| 16 | 09-week1-practice | the callback to Monday's question (light touch) → "the short one is the one worth carrying into Project 1" |
| 17 | 10-week2-practice | the map: four stops on one trail, three marked with the null hazard → "three of the four are the same exception" |
| 18 | 11-uml-diagram | Person box, arrow, Student box build in → "write Student" |
| 19 | 12-uml-answer | diagram ↔ code, paired by colour, four steps → "everything in Person's box is still there — it was promised" |
| 20 | 13-npe-agemath | codewalk: two names, one null; line 4 throws, line 2 is the cause |
| 21 | 14-oldest-ask | stick-figure scene: coworker, three Persons in, one slot empty → "fix it, and explain it" |
| 22 | 15-oldest-code | every `getAge()` rings; the checks go *before* the comparisons |
| 23 | 16-npe-array | codewalk: `Employee[5]`, five nulls (sister of W2D1 13b) → "filled twice: the array, then each slot" |
| 24 | 17-next-class | the same clock as slide 3, drawn again (sister of W2D1 17-next-class) |
| 25 | 99-closing | dusk (unchanged) |

## Slide-by-slide: what it shows, how it builds, and the hand-off

### 01b-today · "Today" — three tabs
Copy W2D1 01b-today's tab component. Tabs: **1 Project 1, and the three
words it needs · 2 What does a test prove? · 3 Every line ran. It still blew
up.** Steps: tabs arrive one per step (plain fade). Notes: the whole hour in
three sentences.

### 02-course-info · "Week 2 — what lands this week"
Redraw as the sister of W2D1 02-course-info (same clock, this week's dates).
Three places work lives — Canvas (weeks 2, 3, 4 posted), PrairieLearn
(modules, then Week 2 homework due **Friday**), Lab (Challenge Exercise 01
due before your section; attendance counts from this week). Last step: a
stone marker at next Monday — **Project 1 · from Week 3**, teams formed in this
week's lab, Deliverable 1 (scope) at your Week 3 lab. It is a marker, not a bar:
Project 1 is next week's work. **→ "And then Project 1 — next week."**

### 02b-chapter-1 · divider
`PART 1 OF 3` / *Project 1, and the three words it needs*. `data-transition="fade"`.

### 03-vocabulary · "Three words we will use all semester"
Scene: a **client** (head-and-shoulders figure) at left faces a **contract
sheet** — the interface: `add · remove · contains · size`, a signature line.
A wall behind the sheet; behind the wall, two boxes that both keep the
promise: an **array of slots** and a **chain of linked nodes**.
Steps: 1 the sheet draws on and its label **Interface — written down**;
2 the array grows behind the wall — **Data structure — how**; 3 the chain
grows beside it — *a second way to keep the same promise*; 4 the wall's
label **Abstract data type — what** (the client only ever sees the sheet);
5 caption: **A Bag is an ADT. ArrayBag keeps the promise with an array.
Your Project 1 spec asks both: the promise, and how you keep it.**
**→ Project 1's specification asks these two questions of every class.**

### 04-project-1 · "Project 1 — Learning to Scope"
Kicker `PROJECT 1 · WEEKS 3–5`. The real Fall 2026 project (Canvas overview
+ `Class Planning(28).docx`): a small Java app of the team's own choosing,
teams of 3 formed in this week's lab (posted on Canvas), the loop **scope → spec → build**, one
deliverable per week due at your lab session, EMRN per deliverable, grading
sessions as oral exams, GitHub, robust exception handling, JUnit tests.
Left: Week 1's project table (W1D1 11-three-projects) with only the P1
column kept — tag, title, four terse rows that undim one per step (Teams ·
3, formed in lab this week; Week 3 · Scope; Week 4 · Spec; Week 5 · Final)
and the lesson line *Define before you build* — so it reads as a recall,
not a new explanation. Right: the trail with three waypoints (Week 3 ·
scope, Week 4 · spec, Week 5 · final) and a Labor Day tick before the first; three orange busts —
the team — grow at the trail head (step 1) and make a real move to each
waypoint (steps 2–4) where a document grows: a one-page scope sheet (five
questions), a blueprint with class boxes and arrows (the spec), a laptop
with a tick and a "3 min" tag (the build + lightning talk). Step 5: beside
the laptop a test list grows — *✓ normal case · ✓ bad input* — and the
caption: **Deliverable 3 needs JUnit tests — one normal case and one
bad-input case per method. So what does a test actually prove?**
**→ Part 2 answers that.** Notes carry the rest (EMRN/oral exam, GitHub,
exceptions, Labor Day, GenAI and seating rules, example ideas).

### 04b-chapter-2 · divider
`PART 2 OF 3` / *What does a test prove?*

### 05-peer-plus · "Move into your groups of 3 or 4"
Sister of W2D1 11-peer-plus: same routine, same figures-at-a-table glyph,
assignment name **Peer Instruction W2D2**. **→ "Three questions today, all
on unit testing."**

### 06-vote-setup · VOTE 1 (static, unchanged) — answer B.

### 06b-walk-setup · VOTE 1 · THE ANSWER · "JUnit builds the fixture for you"
Codewalk. Left: the test class with B filled in (`myStr = "foo";`), lines
stepped. Right: heap — the test object `Option` with field `myStr = null`.
1 JUnit constructs the test object (box grows, `this` pill wired);
2 *JUnit calls setUp() — you never do* (PC on setUp; caption is the D
debrief); 3 `myStr = "foo"` — field strikes `null` → `"foo"`;
4 `stringTest` reads the field — a green **passes** stamp;
5 the A debrief: a second pill `myStr` (local) wired to its own `"foo"`
String, then the unreachable wash: *a new local is a second name; it dies at
the brace and the field never changed*. Caption for C in notes: `SetUp` is
not `setUp`; `@Override` would have caught it.
**→ "A fixture is a promise the test can rely on. Next: does the test check
every case?"**

### 07-vote-cases · VOTE 2 (static, unchanged) — answer A.

### 07b-walk-cases · VOTE 2 · THE ANSWER · "Two exits, two assertions"
SVG scene: `createHokie` drawn as a **fork**: input `""` takes the left
path to `null`; `"Hannah"` takes the right path to a **Hokie** box.
1 left path Creates, `null` label; 2 right path Creates, Hokie box grows;
3 option A's two assertions stamp a tick on each exit; 4 the debrief marks
in a column: **B** ✗ *a Hokie never equals a String* · **C** ⚠ *passes, and
proves nothing* · **D** ✗ *does not compile*. Caption: *One assertion per
exit. C is the dangerous one: it passes.*
**→ "A passing test is not the same as a good test. How about 100 %?"**

### 08-vote-branch · VOTE 3 (static, unchanged) — answer D.

### 08b-walk-branch · VOTE 3 · THE ANSWER · "Covered — and wrong"
SVG: `getSign` as three **lanes** (`x > 0 → 1`, `x < 0 → −1`, `else → 0`),
drawn four times in a 2×2 of small glyphs, one per option. Steps 1–4: the
option's inputs appear at its lane mouths and each visited lane fills
(clip wipe); a counter reads **2 / 3**, **2 / 3**, **2 / 3**, **3 / 3**.
Step 5: on D, `assertEquals(1, getSign(0))` gets a maroon ✗ — the lane was
run and the expectation was wrong. Caption: **Coverage asks "did this line
run". It never asks "was it right". Project 1 asks for both: a normal case
and a bad-input case per method.**
**→ Part 3: code where every line runs and one still explodes.**

### 08c-chapter-3 · divider
`PART 3 OF 3` / *Every line ran. It still blew up.*

### 09-week1-practice · "Back to Monday's question first"
Keep the motto; add a small two-column glyph — the long version (three
lines, one extra box) and the short one (two lines) — both ticked. Step 1
the long one ticks, step 2 the short one ticks. **→ "Both correct. The
short one is the one worth carrying into Project 1."**

### 10-week2-practice · "Week 2 practice — we work these here"
The map: one trail, four stops (01 UML → child class · 02 find the line
that throws · 03 fix a method that breaks on null · 04 an array that holds
no objects). Steps 1–4 the stops appear; step 5 the **null hazard** marker
(a maroon ⌀-style glyph) stamps on 02, 03, 04. **→ "Three of the four are
the same exception. That is not an accident."**

### 11-uml-diagram · PRACTICE 1 · "Turn this diagram into the Student class"
Keep the UML boxes (already drawn); make them build: 1 Person box (already
written for you) draws on; 2 the generalisation arrow Creates from Student
up to Person; 3 the Student box grows (orange edge: "yours to write");
4 the caption. **→ write Student.**

### 12-uml-answer · PRACTICE 1 · THE ANSWER · "Diagram to code, line for line"
Left: the Student UML box (compact). Right: `Student.java`. Four steps, each
lighting a UML member with a colour ring and fading in its code lines in the
same colour: 1 the arrow → `extends Person`; 2 the two `−` fields →
`private` lines; 3 the constructor → the 5-arg constructor with `super(na,
ag, he)` first; 4 the two `+` getters → the getters. Caption: **Nothing from
Person is repeated — a Student already has all of it.**
**→ "Now: what happens when a reference promises an object and there is
none."**

### 13-npe-agemath · PRACTICE 2 · "Which line throws, and which line is the cause?"
Codewalk. 1 line 2: `personA` pill appears with **no wire** — the caption
says `null` is not an address; 2 line 3: `personB` pill + Person box grows
(`age = 10`), wire draws; 3 line 4 (`personA.getAge()`): the throw panel
stamps, PC goes dark (line 5 has no step); 4 the two answers: **line 4
threw** (maroon ring on the code line) · **line 2 is the cause** (orange
ring). Caption: *The stack trace names the line that dereferenced null,
never the line that put it there.*
**→ "Next one: the null comes in from outside."**

### 14-oldest-ask · PRACTICE 3 · "Make getOldest survive a null"
Stick-figure scene. A **coworker** figure at left holds out a sheet
(`getOldest`). Three **Person** figures stand in a row as the inputs; an
arrow to one output figure wearing the *oldest* mark. 1 the three inputs and
the output (how it should work); 2 the middle input figure fades to a dashed
empty slot — `null` — and a maroon ✗ stamps on the output; 3 the rule tile:
*with some nulls, the oldest of the rest; with all three null, `null`*;
4 a speech bubble from **you** to the coworker: *explain it, don't just patch
it*. **→ "Here is the code."**

### 15-oldest-code · PRACTICE 3 · THE CODE · "Where does this throw, and why?"
Editor + steps: 1 the PC bar lands on line 2 — *throws first, on whichever
of A or B is null*; 2 every `getAge()` call rings maroon at once — *the same
bug on every line; patching line 2 just moves the crash*; 3 a dashed orange
insertion band above line 2: *handle the nulls up front, before any
comparison*. **→ "One more, and you have seen it before."**

### 16-npe-array · PRACTICE 4 · "Five slots, zero Employees"
Codewalk, sister of W2D1 13b-walk-student, `Employee[5]`: 1 line 2 — the
array grows, five slots all `null`; 2 line 3 — probe `listOfEmployees[0] is
null`; 3 the throw stamps, PC goes dark; 4 the fix (dashed orange loop).
Caption on 4: *Same bug as Monday's `Student[80]`. An array of objects is
filled twice.* **→ next class.**

### 17-next-class · "Before next class"
Sister of W2D1 17-next-class, the same clock as slide 3 drawn again:
3.1 Bags content page (PrairieLearn, due **Monday** night) → Project 1 as a
stone bracket over Week 3 (teams from this week's lab, Deliverable 1 at your lab) → HW
Week 2 **Friday** · Challenge Exercise 01 before your lab section. Last
step: *Piazza first — turn instructor-post notifications on.*

## Rules every rewritten slide follows
- Motion is manim's only: Create (dashoffset draw-on), GrowFromCenter
  (scale with `opacity: 0` pending), FadeIn, Rotate about a point, real
  moves. No translate-in-reveal, no `fade-up`/`fade-down`/`slide-*`.
- All colour, size and spacing through tokens; slide-local `<style>` scoped
  by `#slide-NN`, opened with a prose comment ending "all values from
  tokens"; a `prefers-reduced-motion` block whenever the slide transitions.
- One `.slide__desc`, `role="img"` + `aria-label` on scene SVGs, `<defs>`
  ids prefixed `w2d2-`, `aside.notes` with the answer and the debrief.
- Vote slides are static; the reveal is the `b` slide after them.
