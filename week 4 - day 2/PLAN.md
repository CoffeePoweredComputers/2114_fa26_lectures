# Week 4 · Day 2 — plan

Built 2026-09-12 for Wednesday Sep 16 (MW, NCB 320) and Thursday Sep 17 (TR, Squires) —
one deck, both sections. No peer instruction (the schedule lists W4D1 only). Sources: the
instructor's brief of 2026-09-12 (review → PrairieLearn practice worked openly → ten
minutes of the practice exam through Canvas + LockDown Browser → questions; Test 1 next
week in class, MW Wednesday / TR Thursday, on PrairieLearn behind LockDown Browser);
`~/Downloads/S26 Week 4 Day 2.pdf` (an F25 deck: Course Info, F25 Project 2, "Class
Review Till Now", Debugger Demo — the last dropped on instruction, the rest stale);
the PrairieLearn repo (`practiceExams/test1` = "Test #1 Practice", 13 slots × 1-of-N
alternatives, 72 pts, `multipleInstance: true`; `contentPages/04_01_assessment_1_info`
for the rules); the Week 2 and Week 3 decks for the recall slides. Shared css/js/assets/
tools cloned from `week 3 - wednesday` and `week 3 - day 2/tools`; the clock is Day 1's.

## Through-line

**"Test 1 asks thirteen things you have already done — today we find the ones that
still feel slow, then open the exam browser once before it counts."**

- Part 1 · What Test 1 asks — the thirteen practice banks in five regions with their
  weights, then one recall per region: a question this room has already answered,
  the verdict on the next press. Hands, not Runestone.
- Part 2 · Practice, together — PrairieLearn "Test #1 Practice" in an ordinary browser:
  work one, compare, mark the slow region. ~12 minutes.
- Part 3 · Ten minutes in the exam browser — the rules of next week, then Canvas →
  LockDown Browser → a fresh practice instance with the ring at 10:00. The browser is
  the test today. Then the floor.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `WEEK 4 · DAY 2` |
| 01b-today | three tabs: a five-region map · two figures at one laptop · a laptop with a ring → captions are the divider titles |
| 02-course-info | Day 1's clock with the now band on Wed+Thu; the Test 1 band is one week out → "Part 3 rehearses exactly that" |
| 03-chapter-1 | PART 1 OF 3 · What Test 1 asks |
| 04-test-map | five tiles, one per press: Objects & references (16) · Testing & exceptions (28) · Types (12) · Bags on arrays (8) · Linked chains (8) → "the next five slides are the proof" |
| 05-recall-refs | W2D1 `12-vote-movie` re-shown; verdict on step 1 (B, 1984) |
| 06-recall-tests | W2D2 `07-vote-cases` re-shown; verdict on step 1 (A); the exception variant asked aloud |
| 07-recall-types | new: Shape/Circle upcast + a UML pair; verdict on step 1 (B, Circle's area runs) |
| 08-recall-bags | W3D1 `07-vote-cases` re-shown (spacer lines dropped); verdict on step 1 (D) |
| 09-recall-chain | the F25 sample MCQ with new values (7 3 9 4), the chain drawn as Monday drew it; verdict on step 1 (B, 3) → "go and find the slow region" |
| 10-chapter-2 | PART 2 OF 3 · Practice, together |
| 11-practice-together | signpost card (PrairieLearn › Assessments › Test #1 Practice) + three steps: alone · compare · mark the slow region |
| 12-chapter-3 | PART 3 OF 3 · Ten minutes in the exam browser |
| 12b-ssd | the same SSD slide as Day 1's 02b: letter in AIM, seat in RegisterBlast by Fri Sep 18 (MW) / Mon Sep 21 (TR) |
| 13-test-day | the rules as a checklist + DO / DON'T cards; Test 1 Redo Oct 1 |
| 14-lockdown-run | three steps into the exam browser + the deck's timer at 10:00, 400 px, centred → "the browser is the test today" |
| 15-questions | the five regions as chips; Piazza |
| 17-next-class | the same clock, static; caption: Test 1 one week out, practice stays open |
| 99-closing | dusk |

## Slide by slide

- **02 / 17** — Day 1's files with the `now` band moved two tracks (x 366–603). Notes say
  "same clock as Monday" and put Test 1 at exactly one week.
- **04** — the regions are the practice exam's 13 banks grouped by skill: p01 p07 p08 →
  Objects & references; p02 p03 p04 p06 → Testing & exceptions; p09 p10 p13 → Types;
  p05 → Bags on arrays; p11 p12 → Linked chains. Weights are the practice exam's own
  point values (5 × 8 + 8 × 4 = 72), which every student sees on opening it — not a leak.
- **05 / 06 / 08** — copies of shipped static vote slides, sids stripped and regenerated,
  `id` renumbered, desc and notes rewritten, kicker `RECALL · WEEK k · REGION`, a
  `.verdict` strip on step 1 spanning both columns. **Deliberate departure** from "answer
  on the b slide": these are ungraded recalls, the vote happened weeks ago, and a second
  slide per recall would cost the practice period its time. 08 drops the class pane's two
  blank spacer lines and halves the card margins so four cards and the strip fit in 685.
- **07** — the types region has no earlier vote; the slide is the deck's own smallest
  upcast (`Shape s = new Circle(2.0); s.area()`), ten lines at the chrome size, a UML pair
  in the deck's pen. It does not reuse any practice-pool wording.
- **09** — the F25 "Sample Optional MCQ" (`Link p = head; Link q = head.next; Link r =
  q.next; Integer myVal = q.data`) with the chain changed from 20 30 10 5 to 7 3 9 4 so
  it is not Monday's answer again; the semicolon the legacy slide dropped is restored.
- **11 / 13 / 14** — Part 2 and 3 are work periods, so the slides are signposts: a path,
  three numbered moves, a clock. `14` reuses `js/timer.js` unchanged (`data-timer="600"`,
  seed `10:00`) with a slide-local `position: static` and a 400 px arc; timer.js resets
  the ring when the slide is left, so the notes say "press once, then hands off".
- **13** — DO/DON'T are named actions (charge, ID, install today, log in once; no Eclipse,
  no phone, no talking until both sections are done, nobody leaves early), not principles.

## Translated, dropped, unverified

- Translated: "Lab 04 is due this week / Post Lab 04" → gone (no lab numbering in F26);
  "Start working on Project 2" → not this week (P2 D1 is Week 6); "Test 1 is next week" →
  kept, with section days; "Look @ Test 1 Review" → this deck IS the review.
- Dropped: the Debugger Demo (instructor: don't); the F25 Project 2 slide; "no lab week 7,
  weeks 11 & 12 required attendance" (not verified for F26).
- Test 1 facts: in class, MW Wed Sep 23 / TR Thu Sep 24 (instructor 2026-09-12); on
  PrairieLearn inside LockDown Browser from Canvas (instructor 2026-09-12); one attempt,
  closed book/notes/IDE/neighbour/web, laptop only, pen + paper OK, student ID, SSD via
  Canvas Testing Accommodations (the live 4.1 page); Test 1 Redo Thu Oct 1 (schedule).
- **Unverified / placeholders** (orange in Studio): `[45 minutes]` on 13 — the 4.1 page's
  figure for "quizzes"; `[practice assignment]` on 14 — the Canvas assignment that launches
  LockDown Browser; `[open date]` on 11 — the PrairieLearn assessment is **untracked in the
  PL repo with `allowAccess: []` as of 2026-09-12** and must be committed, pushed and
  opened before Wednesday. Whether the 4.1 page's LockDown + Canvas wording is being kept
  as the students' source (it also still names CodeWorkout and Labs).
- The review's weights and formats describe the practice exam as built in the PL repo on
  2026-09-12; re-check `practiceExams/test1/infoAssessment.json` if the pools change.
