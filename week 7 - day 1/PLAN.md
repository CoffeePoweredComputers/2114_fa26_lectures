# Week 7 · Day 1 — plan

Built 2026-10-04 for Monday Oct 5 (MW, NCB 320) and Tuesday Oct 6 (TR, Squires): one deck,
both sections. Shared css/js/assets/tools cloned from `week 6 - day 1` (the newest copies).
Week 7 Day 2 is built separately in its own folder and uses the same call-stack drawing.

## Through-line

**"The first two questions finish the ethics week: each one puts one of its two tools, the
Eight Key Questions and the ACM Code, to work on a real case. Then recursion: a method that
calls itself, where every call gets its own frame on the call stack."**

- Part 1 · Ethics: two cases, and which question to ask — the ring, Vote 1 (a deny list,
  the Eight Key Questions), Vote 2 (a curious DevOps manager, the ACM Code).
- Part 2 · Recursion: a method that calls itself — three walkthroughs of `fact(3)`: the
  calls go down, the returns come back up, and what happens with no base case.
- Part 3 · Trace it: which calls happen, in what order — Vote 3 (countDown), walked on the
  same call-stack drawing.

## Manifest

| file | role |
|---|---|
| 01-title | title card; kicker `CS 2114 · FALL 2026 · WEEK 7 · DAY 1` |
| 01b-today | three chapter tabs: two case sheets (a blocked globe, a padlock) · three stacked frames, the top one orange · an output plate reading 0... 1... 2... → the captions are the divider titles |
| 02-course-info | the Week 7/8 clock: now on Mon+Tue; no test band; Week 7 homework to the Friday tick marked Fall Break; no CE; P2 D2 (spec) at your lab; 8.1 Queues Sunday; Week 8 rows (HW, CE 08 Carrano Deque, P2 D3 over "your Week 8 lab", 9.1 + 9.2 Sunday); tiles → "the recursion homework is due Friday, which is Fall Break" |
| 03-chapter-1 | PART 1 OF 3 · Ethics: two cases, and which question to ask |
| 05-peer-plus | the routine ring, `Peer Instruction W07D1` → "Three questions: a deny list, a customer's records, a countdown." |
| 06-vote-deny | VOTE 1, static: the three-paragraph stem verbatim as a text panel on the left at the micro size, the question sentence set apart in ink; the five options right; two clocks → "which of the five is not one of the eight?" |
| 06b-walk-deny | VOTE 1 · THE ANSWER: the Eight Key Questions as a board of eight cards (name + the handbook's question, verbatim); one press each lights Fairness (D), Outcomes (E), Responsibilities (A), Liberty (C) with a concrete sentence about the deny list and the option letter on the card; then B gets a dashed stone chip with no card; `.verdict` B → "money can be one outcome, but it is not one of the eight questions" |
| 07-vote-devops | VOTE 2, static: the stem verbatim ("curiousity" kept) at the small size on the left, the three ACM principles right; two clocks → "what does the manager actually do: say something, pass something on, or look?" |
| 07b-walk-devops | VOTE 2 · THE ANSWER: 1.3, 1.6, 1.7 quoted on a paper sheet; one press per principle tested against the one action (looking): 1.3 nobody was told anything false, 1.7 nothing was disclosed, 1.6 curiosity is not a legitimate end; `.verdict` C → "being authorized to access is not a reason to look" |
| 08-chapter-2 | PART 2 OF 3 · Recursion: a method that calls itself |
| 09-walk-calls | RECURSION · THE CALLS GO DOWN: `fact` under the PC bar; `fact(3)`, `fact(2)`, `fact(1)` each push a frame with its own n; callers wait on line 5; stop at the base case → "this is the Week 5 stack: the newest call is on top" |
| 09b-walk-returns | RECURSION · THE RETURNS COME BACK UP: the same picture with three frames; each return is a blue pill that travels into the waiting frame below as that frame pops; 1, 2 × 1, 3 × 2, 6 reaches main → "each frame finishes its own multiply after the call above it returns" |
| 09c-walk-base | RECURSION · NO BASE CASE: lines 2–4 struck in place, the same call runs again, frames grow past the top of the box (fact(0), fact(-1), …), `StackOverflowError` in maroon; then the stack clears, the lines come back, and the two parts are named on the code → "base case: stops; recursive case: a smaller problem" |
| 10-chapter-3 | PART 3 OF 3 · Trace it: which calls happen, in what order |
| 11-vote-countdown | VOTE 3, static: the stem verbatim as the lede, countDown in an editor at the dense size, the four options in mono at the tag size (21 px); two clocks → "which way does leadTime move, and when does it stop?" |
| 11b-walk-countdown | VOTE 3 · THE ANSWER: countDown under the PC bar, the call stack on the right with an output plate; one press per call (frame grows, output gains 0... to 5...), 5 < 5 is false, GAMEOVER prints, the frames pop; captions rule out A/B (+ 1, not − 1) and D (4 < 5 calls 5); `.verdict` C → "the calls after countDown(0) are 1, 2, 3, 4, 5" |
| 17-next-class | the same clock, static; next class: what a call does after its recursive call returns, and recursion on a linked chain; Piazza notifications |
| 99-closing | dusk |

## Slide by slide

- **02 / 17** — W6D1's clock one week on. Left half = Week 7 (Oct 5–9), right half = Week 8
  (Oct 12–16). The Redo band is gone (Test 2 is Oct 29), so the steps are renumbered from 1:
  1 bracket (Weeks 7 and 8 posted; Week 9 past the edge), 2 Week 7 homework to the Friday
  pole (no CE row this week), 3 Project 2 Deliverable 2 (solid Monday cell + fading tail over
  "your lab day"), 4 the 8.1 Queues module to Sunday Oct 11, 5 Week 8 (homework and CE 08 to
  Friday, P2 D3 over "your Week 8 lab", 9.1 + 9.2 to the Sunday at the edge), 6 the two
  tiles. The Week 7 Friday tick is labelled `Fri · Fall Break` from the start (a fact about
  the day, not a beat), so "your lab day" moves left to x 420 to clear it. 17 is 02 with
  `frag`/`data-step`/`data-anim` stripped, one caption, new heading, desc and notes.
- **01b** — W6D1's tab grammar; three new drawings in the two-weight pen.
- **05** — W6D1's ring; week, assignment name and the takeaway line changed.
- **06 (Vote 1)** — the stem is about 1,050 characters. PIL greedy wrap (Nimbus Sans at
  28 px, 1080 px wide): 8 + 4 + 2 lines for the three paragraphs, 2 for the question
  sentence; at 36 px it is 17 lines and does not fit. So the left panel is 1080 px of
  micro text, the question sentence under a rule in ink, and the five short options sit
  right at the small size. No drawing.
- **06b** — eight cards in a 4 × 2 grid, the handbook's order (fairness, outcomes,
  responsibilities, character, liberty, empathy, authority, rights), each with the name in
  display type and the handbook's first question for it, verbatim. A lit card takes the
  orange tint and edge and a maroon letter disc grows in at its corner; the concrete
  sentence for each press is the caption row under the board. Step 5 grows a dashed stone
  chip "B · Monetary gains/losses" beside the caption: no card. Step 6 the verdict.
- **07 (Vote 2)** — stem 449 characters: 9 lines at 36 px in a 900 px panel; options at the
  small size on the right. The h2 is the deck's own short form of the PrairieLearn twin's
  question line, because the Runestone paste has none.
- **07b** — the sheet quotes 1.3, 1.6 and 1.7 (heading + one sentence each) in numeric
  order; the presses go 1.3, 1.7, 1.6 so the walk ends on the answer. Each tested item
  takes an orange edge while current; a ruled-out item turns stone; the phrase each test
  turns on is a `<mark>` that washes orange. The takeaway is the last caption, with the
  verdict.
- **09 / 09b / 09c (recursion intro)** — the standing rule: a new concept is walked, not
  defined. `fact` with the base case `n == 1` (see below), six lines at `--t-code`. The
  call-stack grammar (shared with the Day 2 deck): one SVG in canvas px on the right,
  frames 440 × 88 at a 96 px pitch inside a thin stone box (four frames tall), `main` at
  the bottom, `call stack` under the box; the running frame orange 18% tint + orange
  stroke, waiting frames `--bg-1` + `--fg-1` with a stone note `waiting on line 5`; a
  returned value is a blue pill that really moves (translateY one pitch) into the frame
  below; maroon only for the overflow. 09: one line per press, a frame per call, nine
  presses. 09b starts with the three frames and walks the returns (seven presses). 09c
  strikes lines 2–4 in place, reruns the same call (frames climb past the box: fact(0),
  fact(-1), a stone ellipsis), the box edge turns maroon with `StackOverflowError`, then
  the stack clears, the strikes retract and lines 2–4 / line 5 are tinted and named
  (base case: stops · recursive case: a smaller n).
- **11 (Vote 3)** — the editor at the dense size is 927 px (the 51-character signature);
  the options run in the remaining column in JetBrains Mono at the tag size (21 px) with
  56 px key discs and 8 px row padding (the micro size ran 117 px over).
- **11b** — the code at the dense size; the frames carry `countDown` and
  `leadTime = k` (the call with both arguments does not fit 440 px at a readable size);
  the output plate beside the stack gains one token per press. Steps 1–5 hold the PC on
  lines 3–6 while one call per press grows a frame; 6 = countDown(5) prints and the test
  fails; 7 = the else prints GAMEOVER; 8 = the frames pop top first in one press
  (nothing runs after the call in this method; that is Day 2's topic); 9 = verdict, in
  the caption cell.
- Timing: clock 3 min, ring 1, Votes 1–2 about 7 each (2:00 + 3:00 of clock plus the
  walk), the recursion intro about 10, Vote 3 about 8, next class 1: about 37 of 50,
  leaving room for questions during the walks.

## Translated, dropped, unverified

- **Runestone keys are ASSUMED for all three votes** (a paste never carries the key;
  confirm in Runestone's results view before class): Vote 1 B (Monetary gains/losses is
  not one of JMU's Eight Key Questions; the other four options are), Vote 2 C (1.6 Respect
  privacy; the PrairieLearn twin `javaFundamentals/ethicsDevOps/ethicsdevops_a` marks 1.6
  correct), Vote 3 C (by tracing; the twin `dataStructures/recursion/u09q02_recursion_countdown_c`
  has the same code and marks the 1–5 option correct).
- **Vote 2's Runestone stem has no question sentence.** The twin's is "Which ethical
  principle could possibly be violated if you give in to curiosity and look at the
  customer's financial information? Choose the ACM Ethical Principle that BEST applies".
  The slide keeps the stem as pasted; the h2 paraphrases the twin. The Runestone question
  may be missing that line: check it in Runestone and fix the source if so.
- Vote quirks kept verbatim: Vote 1's "deny list" and "whitelisted", "… an ethical
  solution." without "is"; Vote 2's "curiousity" (the twin spells it "curiosity"); Vote 3's
  curly quotes `”GAMEOVER”` in the stem and `“GAMEOVER”` in the options, and its `{ }` /
  `else {` layout (the twin has no braces).
- Runestone activity ids for the three W07D1 questions are not known; the notes say
  "question k of 3" only. The assignment name `Peer Instruction W07D1` follows the pattern.
- **ACM Code quotations on 07b are unverified.** acm.org returned 403 to the fetch (and the
  archive could not be reached), so the three headings are as printed in the PrairieLearn
  twin and the one body sentence for each is quoted from memory of the 2018 Code. Check
  them against https://www.acm.org/code-of-ethics before class.
- The Eight Key Questions wording on 06b is from `~/Downloads/8kq-handbook-web.pdf` (JMU,
  2018): the first question under each heading.
- `fact`: the 7.3 module's factorial (RecursionExample.pdf, slide 3) is
  `if (n > 1) return n * factorialRecurse(n-1); else return 1;`; its sum example (slide 1)
  uses `if (n == 1)` as the base case. The deck uses `if (n == 1) { return 1; } return n *
  fact(n - 1);` so that striking the base case on 09c leaves code that still compiles and
  recurses forever. Vocabulary from the module's RecursionIntro.pdf: "Base Case: Where the
  recursion stops", "Recursive Case: That gets you one step closer to the base case".
- Clock facts: the deadline CSV puts the Week 7 homework at Fri Oct 9 11:59 PM, which is
  Fall Break; drawn as the CSV says and labelled, not moved (**unverified** whether it
  stays there). Whether Friday labs meet during Fall Break is in no source; the notes say
  so and no rule is drawn. No Challenge Exercise in Week 7 (schedule page). Project 2 is
  "Project 2 · Linked Chains + Generics" on Canvas (the schedule page's "Bag + Generics"
  is older). The Canvas week page lists 7.3 Recursion (due Sun Oct 4), "Optional Concept
  Practice" and "Week 7: Recursion Coding Exercises" (PrairieLearn title "Week 7:
  Recursion — Coding Practice", five problems, best three count).
- Lab weekdays are in no source; projects keep the "your lab day" range.
- Dropped: nothing from a legacy deck; this deck had no F25 source.

## Status — 2026-10-04, first build

- 18 slides built by an agent from the brief. `add_sids.py` run on all new slides;
  `lint.py` clean on all 18. Sweep (`timeout -k 5 150 tools/measure/run.sh "$PWD"`, ran in
  about a minute), slack at the last step: 01b 166 · 02 36 · 05 13 (the ring's takeaway
  line at y 960, inherited from W6D1 by design) · 06 30 · 06b 30 · 07 241 · 07b 86 · 09 30
  · 09b 30 · 09c 30 (the three recursion SVGs are 690 px tall by design) · 11 68 · 11b 42 ·
  17 36; dividers, title and closing 319–389. No right/left overflow. The timers are
  listed as "over" because they sit in the head band (top 64), as in every vote slide.
- First sweep: 11 ran 117 px over (options at the micro size wrap to five lines in the
  617 px text column) → options at the tag size (21 px mono); 11b ran 54 px over → the
  verdict takes the caption cell at step 9 instead of its own row.
- 07 has 241 px of slack: the stem at 48 px would need about 13 lines; left as is.
- Not committed (`git add "week 7 - day 1"` when asked; never `-A`).

## Review — 2026-10-04 (second pass, after the build)

- `07b`: the 1.7 sentence now reads "nonpublic business strategies, financial information"
  (the build had "nonpublic business or financial information"). Both versions are from
  memory: acm.org returned 403 to every fetch and the archive was unreachable. All three
  quoted sentences still need a manual check against acm.org/code-of-ethics.
- `07`: the stem and options are centred in the body (slack 241 at the bottom became 120
  above and below).
- `11`: each call in an option is a `nowrap` span, so lines break only between calls: two
  whole calls per line (key disc 48 px, column gap s-3, 657 px for 643 px of text). Text
  unchanged. Sweep slack unchanged at 68, so the options did not grow.
- The Day 2 deck's `02` and `17` are derived from this deck's by moving the `now` band to
  Wed–Thu. Edit this deck's clock first, then re-derive.
- Sweep after the review: no overflow; slack as in the Status block except 07 = 120.

## 09c, the crash — 2026-10-04 (instructor: "the stack growing out of control, the slide fizzling out and producing an error like my computer crashed, and play a sound"; of three designs, the blue screen was chosen)

- Press 7 is now one timed sequence run by a slide-local script (about 7 s): 2.8 s of
  runaway (the lettered frames become script-drawn bars that pile past the slide's top and
  then share the same height among up to 96 bars; a maroon counter runs 5 → 16,555), 0.9 s
  of freeze (a pale haze, the sound stuck), then a crash screen in the tool blue (":(",
  "Your lecture ran into a problem and needs to restart", a percentage to 100, stop code
  STACK_OVERFLOW, "What failed: fact(-16551), no base case"). Press 8 is the restart: the
  screen fades, the two parts are named as before, and a note beside the stack says the
  computer is fine and Java prints StackOverflowError.
- 16,555 is measured, not invented: `fact` with no base case on this laptop (OpenJDK 27,
  default 1 MB thread stack) overflowed at 16,555 / 16,688 / 16,904 calls in three runs,
  and Java printed 1,024 trace lines each time (`MaxJavaStackTraceDepth`). The number
  differs by machine and run; the notes say "about 16,500".
- Sound is synthesised with Web Audio (no files, nothing to license): a triangle tone
  under a 1200 Hz low-pass that rises 110 → 520 Hz while a sine pulse on its volume speeds
  up 4 → 24 Hz, the same tone stuck at a 12 Hz pulse during the freeze, then two falling
  sine notes (D5, G4). Master gain 0.12. Softened 2026-10-04 ("that noise is annoying,
  make it a little softer"): it was a square wave to 1100 Hz with a hard 64 Hz gate at 0.2.
  Browsers need a user gesture first; the context is unlocked by any key press while the
  slide is up. No sound in presenter previews (`?embed=1`).
- The sequence plays only when step 7 is reached forward from step 6. Stepping back from
  8, a direct link, motion off (`m`) or reduced motion shows the crash screen still.
  Leaving step 7 cancels timers and sound.
- Tuning knobs at the top of the script: `END` (the count), `RUN` and `HANG` (ms),
  and `0.12` in `ready()` (volume).
- Nothing flashes: each brightness change happens once (WCAG 2.3.1).
- Checked: lint clean; `node --check` on the script; the standard sweep (step 7 reports
  BOTTOM/RIGHT/LEFT because the crash screen covers the whole slide by design, as W6D1
  14b's veil does; step 8 slack 30). NOT checked: the timed run and the sound in a real
  browser; a headless test of them was not run.
