# Week 3 · Day 2 — plan

Built 2026-09-07 from `~/Downloads/F25 Week 3 Day 2-1.pdf` (12 pages). The legacy deck
was: course info (lab, Peer+, CW Week 3, trial quiz, "Test 1 in 2 weeks") → Project 1
setup list → two Peer+ questions → CW Q4 X789 ArrayBag toString → trial quiz → next week.
Engine, CSS and JS are W3D1's copies (the fixed deck.css), plus `.verdict` and
`data-roll="off"` ported from W2D1.

## Through-line

**"Taking one thing out of a bag: one move, because a bag has no order."**

- Part 1 · Two votes. Vote 1: what to do with the gap an entry leaves (answer C, the last
  entry moves into it). Vote 2: which ArrayBag operation still takes linear time (answer B,
  contains). The answer to vote 1 walks the four lines of `removeEntry`, so vote 2's trap —
  A, removing an unspecified entry — is one move the room has already watched run.
- Part 2 · The toString workout — the same bound (`numberOfEntries`, not 25).

## Manifest

| file | role |
|---|---|
| 01-title | cover, kicker DAY 2 |
| 02-course-info | this week's clock — now column on **Thursday**; homework, CE 03 and the 4.x modules run from Monday (all posted at the week's start) |
| 04b-chapter-2 | divider · PART 1 OF 2 · Peer Instruction: What an ArrayBag costs |
| 05-peer-plus | the vote loop, assignment **Peer Instruction W03D2** (name assumed from W03D1 — unverified), plant: two questions |
| 06-vote-gap | VOTE 1 static — stem + four options verbatim (Runestone `vtcs2_arraybags_efficiency`); the array with a gap at index 2 drawn on the left |
| 06b-walk-gap | VOTE 1 · THE ANSWER — codewalk: `removeEntry`'s four lines under the program-counter bar; on the heap `this` → an `ArrayBag` box (count as a struck field, the array as a slot strip), `givenIndex`/`result` as value pills; a COPY of fox travels from slot 5 into slot 2, slot 5 nulls, the count strikes 6 → 5; then A/B/D debriefed in rows |
| 07-vote-linear | VOTE 2 static — stem quoted (O(n) in text) over the vote 1 bag, six live cells and a free slot, a two-line gloss of linear/constant under it; the four options verbatim. Replaced 2026-09-08: the live Runestone W03D2 Q2 is this question, not the F25 remove() one. 07-vote-remove/07b-walk-remove stay on disk, out of the manifest |
| 07b-walk-linear | VOTE 2 · THE ANSWER — verdict board under the same bag, dealt D → C → A → B; each verdict lights what its operation touches (count box, free slot, last slot, all blue), B's sweep across every live slot in maroon stays |
| 08c-chapter-3 | divider · PART 2 OF 2 · toString |
| 10-practice-tostring, 10b-tostring-code | copied from W3D1 (the PDF's CW Q4 is X789) — plant reworded to "same bound as removeEntry" |
| 17-next-class | the 02 clock again, static |
| 99-closing | dusk |

## Translated, dropped, unverified

- **Trial Quiz (lockdown browser, passcode)** — dropped: not a Fall 2026 thing.
- **"Lab and PostLab", Web-CAT, CodeWorkout** — dropped (Fall 2026: PrairieLearn, GitHub,
  EMRN; labs carry Project 1 deliverables).
- **Project 1 setup list (JRE, TestableRandom, Web-CAT responses)** — that was the Fall
  2025 Bag project; Fall 2026's P1 is Learning to Scope, already on 02's clock (D1 at this
  week's lab, D2 at next week's).
- **"Test 1 in 2 weeks, there is an information sheet"** — dropped entirely, 2026-09-08 at
  the user's ask: the runway slide and its Part 1 divider were taken out of the manifest and
  then deleted from disk, and the test is not mentioned anywhere in the deck — 17's notes lost
  the "off the right edge" sentence and 02's and 17's notes no longer name the 4.1 module.
  The parts are numbered 1 of 2 / 2 of 2.
- **Runestone**: the live W03D2 text was checked 2026-09-08 (the user pasted it) — vote 1 is
  verbatim (`vtcs2_arraybags_efficiency`), vote 2 was the wrong question and is now the
  linear-time one. The assignment name and vote 2's activity id are still unverified, and
  whether the O(n) in vote 2's stem renders is worth a look on the projector.
- **toString is also W3D1's Part 3** (slides 10/10b). It is in this deck because it is in
  the PDF; drop it from whichever day does not use it.
- The now column sits on Thursday (TR section). Monday was Labor Day, so the MW section
  has one lecture in Week 3; if that section gets this deck on Wednesday the clock still
  reads correctly (all bars end Friday / Sunday).

## Rules followed
Manim motion only (grow, fade, draw-on, real moves); tokens only; slide-local `<style>`
scoped by `#slide-NN`; one `.slide__desc`; `aside.notes` with the answer; vote slides
static, answers on the `b` slide; question text quoted, not corrected.
