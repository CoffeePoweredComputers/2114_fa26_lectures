# CS 2114 Fall 2026 lecture decks — build prompt

Paste this file (or `@DECK-PROMPT.md`) at the start of a session, then say what to
build, for example "Build week 4 day 1 from ~/Downloads/F25 Week 4 Day 1.pdf" or "Add a
vote + answer pair to week 3 day 2 for Runestone question X".
Compiled 2026-09-12 from the Week 1–3 decks, updated after Week 4 (2026-09-12) and after
Week 5 Day 1 (2026-09-20). Facts marked unverified are unverified; do not state them as
settled.

---

## 0. Summary

1. A deck is one folder `week N - day M/` with `index.html` (manifest), `css/`, `js/`,
   `assets/` and `slides/NN-name.html` fragments. No dependencies; it needs an HTTP server.
2. Clone `css/`, `js/`, `assets/fonts`, `assets/stone-edge.svg`, `studio.config.json` and
   `tools/` from `week 5 - day 1/`. Those are the newest shared copies (W4D1's block PC
   bar, two-ring timers and ligature fix; W5D1's `data-hold` and `.moves`).
3. Write `PLAN.md` first (through-line, chapter table, per-slide steps and plant, what was
   translated, dropped or left unverified). Then the slides. Then `add_sids.py`, `lint.py`,
   `measure/run.sh`. Then stop; the instructor reviews in Slide Studio.
4. Every slide has `<section id="slide-NN">`, `.slide__head`, one `.sr-only .slide__desc`,
   `.slide__body`, `.slide__number`, `aside.notes`, a slide-local `<style>` scoped by
   `#slide-NN`, values from `tokens.css` only, and motion from the list in §8 only.
5. Translate legacy policies to Fall 2026. Quote live Runestone/PrairieLearn question text
   verbatim. The clock rules in §11 override any source deck.

---

## 1. What a deck is

- Canvas 1920×1080, authored in canvas pixels; `js/deck.js` scales it with a transform.
  Padding `--s-7` (96) top/bottom and `--s-8` (128) left/right, so the body is 1664 wide
  (x 128–1792) and at most 888 tall (y 96–984). `.slide { overflow: hidden }`: overflow is
  clipped without warning and nothing scrolls.
- `index.html` holds `window.SLIDE_MANIFEST = [ '01-title.html', … ]`. Slide Studio
  rewrites that array literal in place, so keep the assignment in exactly that form.
  Scripts: `deck.js`, `studio-motion.js`, `code-walk.js`, and `timer.js` where used.
- `js/deck.js` fetches `slides/*.html`, one `<section>` each, in manifest order.
  Navigation by hash `#N` / `#N.K`; keys ← → space PgUp/PgDn Home End, `f` fullscreen,
  `m` toggles `html.no-motion`. Step engine: every `.frag[data-step]` gets
  `is-pending` / `is-current` / `is-past` against the current step. `maxStep` is the
  highest `data-step` (or `data-hold`) in the section, so steps must be dense from 1.
  `data-hold="M"` (added in W5D1's `deck.js`) keeps a frag `is-current` from its
  `data-step` through step M; use it for a loop body that stays under the PC bar while the
  right-hand side plays one iteration per press (W5D1 04, 04c, 06b, 09b). `data-also="7 8"`
  lists further steps at which a frag is current again: a code line that a second run of
  the same walkthrough revisits (W5D1 04, 04b, 04c). Studio's previews implement neither. Events: `slides:loaded`, `deck:stepchange`. `?embed=1` gives a
  passive presenter iframe.
- `css/tokens.css` holds the visual vocabulary (identical in every deck except W3+'s
  `--t-h1-sm: 100px` and W5D1's `--t-code: 32px`). `css/deck.css` holds every pattern used by two or more slides.
  `css/studio-anim.css` and `js/studio-motion.js` belong to Slide Studio; leave them.
- Slide Studio is the instructor's editor. Config: `studio.config.json`
  (`canvas 1920×1080, uploadDir assets`), `.slide-studio/permissions.json`. It needs a
  `data-sid="<basename>:<n>"` on every element (run `tools/add_sids.py`), writes
  `.slide__desc` with `data-hash`/`data-desc="auto"`, and its drag handles leave inline
  `style="width/height/left/margin…"` attributes, including on `<section>`. Strip those
  before reasoning about layout.
- Assets: `assets/fonts/` (Inter and JetBrains Mono variable woff2, OFL, `LICENSE.md`) and
  `assets/stone-edge.svg` (the mask for the left stone edge) go into every deck.
  Photos and screenshots also go in `assets/` (Studio's upload dir).
- Decks appear to be published at `https://ascend3.cs.vt.edu/slides/cs2114-fa26-weekN-dayM/`
  (from a W3D1 note; unverified).

### Which deck introduced what

| deck | contents |
|---|---|
| `week 1 - day 1` | tokens and deck.css; the title/dusk-closing pair; tiles; the semester map and three-projects table; the ethics arc. Also a spec sub-deck (`01-master-spec`, `02-design-system*`, `03-week1-deck*`, `05–09-legacy-*`, `10-asset-inventory*`) that inventories the legacy pptx decks and states the rule "reuse layouts and assets, never policies" |
| `week 1 - day 2` | the illustrated stepped style; `02-today` (room scene); the clock grammar (`03-keep-up`, `14-work-time`); the first vote/answer pairs (`09/09b`, `10/10b`); the codewalk component; chapter dividers; `.slide__desc` accessibility |
| `week 2 - day 1` | `01b-today` chapter tabs; the `02-course-info`/`17-next-class` clock pair; the peer-instruction chapter (`03`, `04`, `06`, `07-the-deal`, `10-icebreaker`, `11-peer-plus` ring); `.verdict` strip; `data-roll="off"`; the LLM chapter (`16d` is generated by `tools/next-token/gen16d.py`; never hand-edit it); `.chat` |
| `week 2 - day 2` | the three-chapter deck shape and `PLAN.md` as audit trail; testing votes (`06–08b`); `.dbr` debrief rows; Project 1 "Learning to Scope" (`04`, `new-slide` DO/DON'T cards); practice codewalks (`13`, `14`, `15`); Web-CAT appendix (`18*`) |
| `week 3 -day 1` | the deck.css specificity fixes; `.code-dense`/`.code-tag`; `.opts--code`; `PLAN-sizing.md`; the headless measure harness |
| `week 3 - day 2` | first deck built from an F25 PDF; `tools/` (add_sids, lint, measure); the linear-time vote |
| `week 3 - wednesday` | MW make-up deck (Labor Day); `js/timer.js` 5:00 discussion countdown |
| `week 4 - day 1` | first deck serving both sections: the two-track `now` band and the Test 1 band on the clock; SVG chain scenes (Link boxes `data \| next`, blue marker arrows that swing via a CSS `d: path()` transition) in `04`, `07b`, `09b`, `11`; a 2×2 `.opts--code` grid for four long code options (`09`); four synchronised lanes (`09b`) |
| `week 4 - day 2` | the review deck: `04-test-map` (regions), recall slides (copies of earlier static votes with a `.verdict` on step 1), the 10:00 `.timer` at 400 px (`14`), DO/DON'T cards (`13`) |
| `week 5 - day 1` | concept introduction as pseudocode walkthroughs (`04`–`04d`: real code under the PC bar, the array it touches, a rolling moves counter, the doubling test, then the graph that names O(1)/O(n)/O(n²)); every vote answer is the same walk of the real method; `data-hold` in `deck.js`; the shared `.moves` counter in `deck.css`; SVG array strips with exact travel (`06b`); values as opaque boxes that slide over neighbours (`09b`); a marker that moves (`10b`); a swinging `topNode` (`11b`) |

---

## 2. Starting a new deck

```
mkdir "week N - day M"/{css,js,assets,slides,tools}
cp "week 5 - day 1"/css/*.css            "week N - day M"/css/
cp "week 5 - day 1"/js/*.js              "week N - day M"/js/      # deck, code-walk, studio-motion, timer
cp -r "week 5 - day 1"/assets/fonts      "week N - day M"/assets/
cp "week 5 - day 1"/assets/stone-edge.svg "week N - day M"/assets/
cp "week 5 - day 1"/studio.config.json   "week N - day M"/
cp -r "week 5 - day 1"/tools/*           "week N - day M"/tools/
cp "week 5 - day 1"/index.html           "week N - day M"/        # then fix <title> + manifest
```

- Folder names contain spaces (`week 3 -day 1` has an irregular one). Quote paths.
- Shared-file divergence. `tokens.css` and `studio-*` are identical everywhere.
  `deck.css`: W3D1/W3D2/wednesday and later have the `.slide .editor__bar` / kicker /
  note / lede / tile__label specificity fixes and `.code-dense` / `.code-tag` /
  `.opts--code`; W2D1 alone has `.chat`; W2D2 alone has `.dbr`; W2D1/W3D2/wed and later
  have `.verdict`; wed and later have `.timer`; W4D1 and later have
  `font-variant-ligatures: none` on code; W5D1 has `.moves`. `code-walk.js`:
  `data-roll="off"` in W2D1, W3D2, wed and later; W4D1 and later make the PC bar cover
  every `.walkline` that shares the current step as one block. `timer.js`: W4D1 and later
  finish a timer once its step is past. `deck.js`: W5D1 has `data-hold`. Port `.dbr` from
  W2D2 or `.chat` from W2D1 if a slide needs them.
- Copy the always-present slides and change only the facts: `01-title` (kicker
  `CS 2114 · FALL 2026 · WEEK N · DAY M`; W3's version has the `--t-h1-sm` one-line fix),
  `01b-today`, `02-course-info`, the chapter dividers, `05-peer-plus`, `17-next-class`,
  `99-closing`.
- Section ids `#slide-NN` must be unique per deck. Slide-local CSS is scoped by them and
  applies across slides otherwise (wednesday renumbered its copies for this reason).
- `index.html` `<title>`: `CS 2114 — Software Design & Data Structures · Fall 2026 Week N Day M`.
- git: `git add -u` does not cover a new directory; run `git add "week N - day M"`.
  Never `git add -A`. Commit only when asked.

---

## 3. Build workflow

1. Read the sources (§11 lists the paths): the F25 PDF/pptx for that day, the Fall 2026
   schedule and deadline CSV, the Canvas project overview if a project is in play, and the
   live Runestone/PrairieLearn question text (ask the instructor to paste it if you cannot
   log in). Read the sister deck's PLAN.md and its `02`/`17` clock slides.
2. Write `PLAN.md` in the deck folder before any slide:
   - a one-sentence through-line in bold quotes, then the 2–3 chapters as bullets;
   - a manifest table (`file | role`), each role ending with the slide's plant (→);
   - a per-slide section: what it shows, how it builds step by step, the hand-off;
   - "Translated / dropped / unverified": every legacy policy changed, everything left out,
     every fact not confirmed;
   - a dated Status block appended after the instructor's review.
   The W2D2 and W3D2 PLAN.md files are the models.
3. Write the slides in the main session (seven slides take about 40 minutes). Subagents
   have stalled on this machine; if used, give each a spec of at most 300 lines, a short
   reading list, the instruction "Read tool only, one Write per slide", and check file
   mtimes before relaunching.
4. Tooling: `python3 tools/add_sids.py slides/*.html` (new slides only),
   `python3 tools/lint.py slides/*.html` (must be clean), `tools/measure/run.sh "$PWD"`
   (absolute path; a relative `.` symlinks the temp dir to itself and returns empty JSON;
   needs `chromium`; run with the sandbox disabled). Treat slack under 30 px as unfinished
   and re-measure after every layout change. On 2026-09-20 `chromium --headless=new
   --dump-dom` returned no DOM and hung for 5 minutes; if that recurs, compute the budget
   by hand (PIL plus greedy wrap, §6) and say that the sweep did not run. Never `pkill -f`
   a pattern that appears in your own command line; it kills the shell.
5. Stop. No Playwright, no screenshot loops; the instructor reviews in Slide Studio. Leave
   clearly marked placeholders for facts you do not have. List what is unverified.
6. The instructor edits concurrently in Slide Studio or another session. Check
   `git status` and mtimes before touching a file, and stay off files with fresh
   uncommitted changes. When told to decide without asking, decide, record the decision
   in PLAN.md, and do not ask again.

---

## 4. Slide anatomy

```html
<section class="slide" id="slide-NN">                      <!-- classes: slide--warmup | slide--title slide--center slide--nostone | slide--section slide--center divider -->
  <header class="slide__head">
    <p class="slide__kicker">PEER INSTRUCTION &middot; VOTE 1</p>   <!-- optional; CSS uppercases -->
    <h2>What does the last line print?</h2>
  </header>
  <p class="sr-only slide__desc">Full-sentence description of what the slide shows and how it builds, for a screen reader. Exactly one per slide, right after the heading.</p>

  <!-- Author's comment: what the slide shows in two or three sentences, then
       step 1: …
       step 2: …
       (viewBox = the body's rect, if a scene) -->
  <div class="slide__body">
    …
  </div>
  <div class="slide__number"></div>                        <!-- deck.js fills "N / total" -->
  <aside class="notes">Speaker notes. For an answer slide open with "Answer: B &mdash; …". Then "Step 1 &mdash; …" per step, and the spoken hand-off to the next slide.</aside>

  <style>
    /* Slide-local: why this slide needs its own rules (one paragraph: what the
       picture is, which motion each thing gets, the size trade-off). Used by
       this slide only, all values from tokens. */
    #slide-NN .x { … }
    @media (prefers-reduced-motion: reduce) {
      #slide-NN .x { transition-duration: 0s !important; transition-delay: 0s !important; }
    }
  </style>
</section>
```

The linter enforces: balanced tags; every `data-sid` unique and prefixed with the file's
basename; `data-anim` only `fade` or `none`; no raw hex (except `url(#…)`, `id=`,
`href`); every selector in the slide `<style>` starts with `#slide-NN`; no `.is-pending`
rule that combines `translate…` with `opacity`; dense `data-step` numbering; exactly one
`<section id>`; a `slide__desc` present.

Rules the linter does not check: HTML entities (`&mdash; &rsquo; &middot; &rarr;`) in
text; `role="img"` and a full-sentence `aria-label` on figure SVGs, `aria-hidden` on
decoration; `<defs>` ids namespaced per deck (`w4d1-NN-…`); patterns used by two or more
slides go to `deck.css` with a comment, single-slide patterns stay local with a comment;
comments state the reason for each choice.

---

## 5. Recurring slide types

| type | copy from | notes |
|---|---|---|
| title | `week 3 - day 2/slides/01-title.html` | ridge and mist decor, `slide--nostone`, kicker with week/day, `--t-h1-sm` one-liner |
| today (chapter tabs) | `week 2 - day 2/slides/01b-today.html` | 3 columns, each a 360-tall drawing on a rule, an orange numeral and a caption; columns GrowFromCenter one per step; the captions are the divider titles |
| this week's clock | `week 5 - day 1/slides/02-course-info.html` | two-week axis; §11 has the geometry and colour rules |
| chapter divider | `week 3 - day 2/slides/04b-chapter-2.html` | `slide--section slide--center divider`, `data-transition="fade"`, kicker `PART k OF n`, h2 = the tab caption; nothing builds |
| peer-instruction routine | `week 2 - day 2/slides/05-peer-plus.html` | five stations in a ring (centre 960,630 r 260), arcs draw on, station 2 orange (the silent first answer), plant under the ring |
| vote (static, code question) | `week 2 - day 1/slides/12-vote-movie.html` (short code); `week 3 -day 1` 07/08 (long code, `.opts--code` and `.code-tag`) | kicker `PEER INSTRUCTION · VOTE k`; `grid--code`: `.editor` left, `.tile--a2` API and `.opts` right; static; reveals nothing; notes open `Answer: X —` |
| vote (static, text question) | `week 5 - day 1/slides/06-vote-grow.html` (model), `09`, `10`, `11` (long options) | `deck.css .vote`: short paraphrase h2, the verbatim stem as a muted `.vote__stem` lede, `.vote__panels` = the structure drawn left (128 px `.vote__cell`s, an orange `.vote__top` marker where needed, or an SVG) and `.vote__opts` right (80 px maroon `.vote__key` disc + `.vote__text` at the body size; `--long` for options over ~25 characters); no gloss lines on the canvas; only the clocks build |
| vote answer (walkthrough) | `week 2 - day 1/slides/12b-walk-movie.html` (codewalk); `week 2 - day 2/slides/07b-walk-cases.html` / `08b-walk-branch.html` (SVG scenes); `week 3 - day 2/slides/06b-walk-gap.html` (ArrayBag slots); `week 5 - day 1` 06b/09b/10b/11b (the real method under the PC bar with a moves counter) | file `NNb-walk-*`, kicker `VOTE k · THE ANSWER`, h2 states the conclusion; ends on `.verdict` (or `.dbr` rows, or a board) |
| practice map | `week 2 - day 2/slides/10-week2-practice.html` | trail of stop discs numbered with the PL question numbers, plus the signpost "PrairieLearn › Assessments › Coding Practice" |
| practice codewalk | `week 2 - day 2/slides/13-npe-agemath.html`, `week 2 - day 1/slides/13b-walk-student.html` (NPE/array) | kicker `PRACTICE k`; the line after the throwing line gets no `data-step`, so the PC bar fades out on the throw |
| code + scene | `week 2 - day 2/slides/14-oldest-ask.html`, `15-oldest-code.html` | editor left, stick-figure scene right; rings on lines |
| stick-figure scene | `week 2 - day 1/slides/07-the-deal.html`, `04-why-peer-instruction.html`, `10-icebreaker.html`; `week 2 - day 2/slides/new-slide.html` (smith and card deck) | §10 |
| chat transcript | `week 2 - day 1/slides/16f-llm-risks.html` (`.chat`) | |
| before next class | `week 2 - day 2/slides/17-next-class.html` (poles rising one per step), `week 3 - day 2/slides/17-next-class.html` (static recall) | the same clock as `02`; the notes say "same clock"; last beat: Piazza instructor-post notifications |
| appendix with screenshots | `week 2 - day 2/slides/18-webcat-guide.html` and `18b–18e` | `<img>` on `--paper` plates; kicker `STEP k OF n` |
| closing | `week 1 - day 2/slides/99-closing.html` | dusk: sun sets, sky darkens, stars; `slide--dusk slide--nostone` |
| chain scene | `week 4 - day 1/slides/04-node-anatomy.html` (a walk down `class Link` under the PC bar: fields and reads washed or ringed blue, writes washed orange), `07b-walk-trace.html` (rewiring), `09b-walk-double.html` (four lanes), `11-linkedbag-add.html` | Link box 240×120 (or 170×100 / 130×80) with `data \| next` compartments, blue cubic arrows with `marker-end` (marker fill inline), `null` as the word in stone; swings = CSS `d: path()` under `:has(.cap--k:not(.is-pending))`; the codewalk engine cannot draw node-to-node wires |
| recall (ungraded) | `week 4 - day 2/slides/05-recall-refs.html`, `08-recall-bags.html` | a shipped static vote slide copied (strip sids first), kicker `RECALL · WEEK k · REGION`, `.verdict` on step 1 spanning both columns; the only case where the answer is on the same slide |
| homework operations | `week 4 - day 1/slides/13-hw-reads.html`, `13b-hw-writes.html` | the week's PL problems as pointer moves: a nine-line index with the problem numbers (the other slide's half dimmed), one static picture per press in the Node-box grammar (moved arrows orange, replaced arrow dashed stone, unreachable node stone), the rule as code in the caption. Generated by one Python script; regenerate rather than hand-edit coordinates |
| homework cards | `week 5 - day 1/slides/13-hw-linkedstack.html` | for a small homework set: the structure drawn on the left with a card listing what the class already has, one card per problem on the right with the result for the drawn instance, the signpost under the left column |
| SSD reminder | `week 4 - day 1/slides/02b-ssd.html` | two cards (letter in AIM; seat in RegisterBlast by exam minus 3 business days) and the SSD contact line |
| test rules | `week 5 - day 1/slides/15-test-day.html` | checklist of the rules on the left, DO / DON'T cards on the right, the redo line under the checklist |
| long timer | `week 4 - day 2/slides/14-lockdown-run.html` | the same `.timer` block, `data-timer="600"`, seed `10:00`, slide-local `position: static` and a 400 px arc |
| concept intro (counting walkthrough) | `week 5 - day 1/slides/04-count-contains.html`, `04b-count-add.html`, `04c-count-pairs.html`, `04d-big-o.html` | the instructor's standing rule (2026-09-20): a new concept gets a few slides of step-by-step pseudocode walkthroughs with animation. Real code with short names (a, n, x) at `--t-code` (`.code-mid`) under the PC bar, the structure it touches on the right, a `.moves` counter, one caption per press; then the structure GROWS IN PLACE (cells shrink and more grow in; a grid's extra tracks animate from 0) and the same lines run again (`data-also`) with the counter reset by a `data-roll="off"` pair; then the graph that names the shapes. Never a second copy of the structure beside the first |
| loop walk | `week 5 - day 1/slides/09b-walk-top0.html` (shift), `06b-walk-grow.html` (copy loop; two arrays in one SVG; `contents` swings) | `data-hold` on the loop's walklines; one iteration per press on the right; a value slides one pitch (`translateX(-pitch)`) and the value it overwrites fades out as it arrives; no opaque boxes (they showed as grey artifacts) |
| cost table | `week 5 - day 1/slides/12-cost-table.html` | two mono tables side by side, O(1) blue and O(n) maroon, exceptions in a footnote |

Deck shape since W2D2: `01-title → 01b-today → 02-course-info → [divider → chapter
slides → plant]×n → 17-next-class → 99-closing`. File numbers are a sort key, not the
position; inserted slides take `NNb`, `NNc`. The instructor refers to slides both by
on-screen position and by file prefix ("slide 03" = `03-vocabulary`); when it matters,
name the file in the reply.

---

## 6. Design vocabulary (css/tokens.css)

- Text: `--fg-0` #2c1a1f (ink), `--fg-1` #6b4a52 (muted). Surfaces: `--bg-0` #f2f1ed
  (ground), `--bg-1` #e9e3e4 (panels), `--paper` #ffffff (plates, QR cards). Accents:
  `--accent-1` #861f41 VT maroon, `--accent-2` #1c6091 blue, `--accent-3` #b35510 orange.
  `--stone` #7d8791, `--night` #0d1016. Mix: `color-mix(in srgb, var(--accent-1) 50%,
  var(--accent-3))` = deadline ink / `tile--a4`. No raw hex in a slide.
- Colour semantics, the same in every deck: `--fg-1` neutral; `--fg-0` live or the
  viewer's own; `--stone` past, inert, ghost; maroon = the rule, a failure, a heading, an
  assignment name to find; blue = tools, measures, wires and references, PrairieLearn;
  orange = whoever is doing the work, "yours to write", Project 1, the tab numerals; a
  piece of someone's work = orange 18% tint with an orange stroke. Project accent coding
  from W1D1: P1 = a3 orange, P2 = a4 mix, P3 = a2 blue.
- Fonts: body Verdana stack (`--font-body`; resolves to Nimbus Sans on this machine),
  headings Georgia (`--font-display`; resolves to Nimbus Roman), code JetBrains Mono
  (`--font-mono`, bundled).
- Type scale (px): h1 120 (`--t-h1-sm` 100), h2 80, h3 56, body 48, small 36, code 32
  (`--t-code`, W5D1: nine-to-ten-line editors read from the back row), micro 28 (editor
  bar, gutter), tag 21 (the floor: map labels, captions). Spacing: s-1 8 · s-2 16
  · s-3 24 · s-4 32 · s-5 48 · s-6 64 · s-7 96 · s-8 128. Radii: r-1 4 · r-2 10 · r-3 18.
  Easing: `--ease-smooth` (manim smootherstep).
- Measured budgets (do not estimate by eye; estimates have been wrong by 100+ px):
  body 752 tall under a bare h2 (starts y=232), 685 under kicker + h2; a `slide--warmup`
  h2 is h3-sized. Font advances measured with PIL on 2026-09-20: JetBrains Mono 21.6
  px/char at 36 px, 16.8 at 28, 12.6 at 21; Nimbus Sans (body) 19.0 at 36, 14.8 at 28,
  11.1 at 21; Nimbus Roman (display) 18.5 at 36. `--t-small` at 1.35 is about 49 px per
  line. An `.editor` line needs its text width plus 70 px (3 px borders, 48 px gutter,
  16 px right pad). For exact counts use PIL and a greedy wrap against the real inner
  width (`fc-match Verdana`). `.slide li` sets line-height 1.5 and overrides any
  line-height on the list; set it on the `li`. A `.frag` placed by grid auto-flow can land
  in an unexpected column; give every cell an explicit `grid-column`/`grid-row` (W4D2 13).
- Layout: content-board slides fill the frame (`grid-auto-rows: 1fr`); display slides
  centre their block. For stacked or overlaid panels use grid stacking (every card
  `grid-area: 1 / 1`, later in source on top); do not use `position: absolute; inset: 0`
  in a fixed-height box.

---

## 7. Shared components (css/deck.css)

`.slide__head` (with `.slide__kicker`, `.slide__lede`) · `.note` · `.tile` (`--a2 --a3
--a4 --display`, `.tile__label`) · `.grid` (`--2 --3 --code` = `1.15fr 1fr`, `--tiles`)
· `.stack` · `.chips` · `.checklist` · `.steps` (display numerals) · `.editor`
(`.editor__bar`, `.editor__pc`, `.editor__code > li`, `.tok-key`, `.tok-num`; body
modifiers `.code-mid` (32px) / `.code-dense` (28px) / `.code-tag` (21px): one class on the
slide body, no local editor type rules; the default is 36px with a 96 px gutter, the
modifiers use a 48 px gutter and a 16 px right pad, so a line needs its text width plus 70) · `.opts` (lettered answers; `.opts__code`, `.opts--code`) ·
`.refs` (the old static reference diagram; prefer codewalk) · `.slide--warmup` (h2 at h3
size; vote and walk slides) · `.scan` (QR plate) · codewalk (§9) · `.verdict`
(`<ol class="verdict frag" data-step="N">` of `.verdict__opt--wrong` (`style="--i: k"`)
/ `--right`, each wrapping `.verdict__txt`) · `.dbr` debrief rows (W2D2) · `.chat`
(W2D1) · `.timer` (copy the whole `<div class="timer frag" data-step="1"
data-timer="300" …>` SVG block from a vote slide; the markup is in `js/timer.js`'s
header. Vote slides since W4D1 run two rings: `timer--vote` `data-timer="150"` on step 1
and `timer--discuss` `data-timer="240"` on step 2, side by side at the top right with a
`.tlabel` under each; the second press starts the discussion clock and `timer.js`
finishes a timer whose step has passed) · `.vote` (W5D1; the text-question vote layout, §5) · `.moves` (W5D1; must sit inside a `.codewalk`.
A display numeral that counts: one `.heap-obj__field` old/new pair per increment, the
pairs stacked in one cell, only the latest non-pending pair visible, digits rolled by
`code-walk.js`; `--ok` for the blue counts that stay small. This is the only permitted
digit roll, because a tally of moves counts up) · `.motto` (`--tight`) · `.divider`,
`.divider__n` · `.slide--title --section --center --nostone --dusk` · decor:
`.decor--ridge`, `.ridge-far/mid/near`, `.mist--a/b/c`, `.sun-set`, `.night`, the
`.slide::before` stone edge (72px, on every slide unless `--nostone`) ·
`.img-placeholder[data-src]` · `.frag--dim` · `.sr-only`.

Known trap (fixed in W3+ copies): bare-class `<p>` components lose to the `.slide p`
type ramp. Any new `<p>` component in deck.css needs the `.slide ` prefix.

---

## 8. Motion

The instructor rejects fade-while-translating. A position change must mean that the
thing moved. Allowed entrances: FadeIn (opacity only), GrowFromCenter (scale only, with
opacity resolving early), Create (a stroke drawing on), wipe (a bar filling from where it
starts), a real move (Transform / TransformFromCopy: the thing travels). Exits: plain
fade. Replaced values: plain crossfade or the strike variant; no digit roll on
assignments or setters (it reads as incrementing); the roll is only for values that
count.

Never: `data-anim="fade-up|fade-down|slide-*|scale-*"`, any `translate` in an
`.is-pending` state, `opacity: 1; scale(.1)` pending states (a small visible thing sits
there before it grows).

Recipes (all from shipped slides):

```css
/* GrowFromCenter — HTML element */
#slide-NN .x { transform-origin: 50% 50%; transition: opacity .25s ease, transform .5s var(--ease-smooth); }
#slide-NN .frag.x.is-pending { opacity: 0; transform: scale(0.4); }
/* GrowFromCenter — SVG <g> or shape: add transform-box */
#slide-NN .g { transform-box: fill-box; transform-origin: 50% 50%; transition: opacity .25s ease, transform .5s var(--ease-smooth); }
/* Create — a stroke draws on (put pathLength="100" on the path) */
#slide-NN .p { stroke-dasharray: 100; transition: stroke-dashoffset .5s var(--ease-smooth); }
#slide-NN .frag.p.is-pending { opacity: 1; stroke-dashoffset: 100; }
/* wipe — a bar fills from its left end */
#slide-NN .bar { clip-path: inset(0 0 0 0); transition: clip-path .6s var(--ease-smooth); }
#slide-NN .frag.bar.is-pending { opacity: 1; clip-path: inset(0 100% 0 0); }
/* FadeIn — the deck default; or data-anim="fade" on the frag; delay it behind the thing it labels */
#slide-NN .frag.label.is-current, #slide-NN .frag.label.is-past { transition-delay: .45s; }
/* stagger siblings: style="--i: k" on each */
#slide-NN .frag.row.is-current, #slide-NN .frag.row.is-past { transition-delay: calc(.3s + var(--i) * .12s); }
/* caption row: one sentence at a time */
#slide-NN .frag.cap.is-past { opacity: 0; }
/* Create an ARROW — the shaft draws on, the head is a SEPARATE path that fades in after it (W4D1 04).
   No marker-end on a drawn-on arrow: markers ignore the dash offset, so the head would sit at the tip
   before the shaft exists. Markers are fine on arrows that are static or that swing. */
#slide-NN .arr  { stroke-dasharray: 100; transition: stroke-dashoffset .45s var(--ease-smooth); }
#slide-NN .frag.arr.is-pending { opacity: 1; stroke-dashoffset: 100; }
#slide-NN .head { transition: opacity .2s ease; }                        /* <path class="head frag" data-anim="fade" d="M224 150 L212 144 L212 156 Z"> */
#slide-NN .frag.head.is-current, #slide-NN .frag.head.is-past { transition-delay: .4s; }
/* Swing — an SVG arrow re-points (Transform): two cubics with the same command shape, W4D1 07b */
#slide-NN .arr { transition: d .7s var(--ease-smooth); }               /* d="M260 130 C 320 130, 390 130, 454 130" in the markup */
#slide-NN .slide__body:has(.cap--4:not(.is-pending)) .arr--20 { d: path("M260 130 C 330 130, 150 250, 150 344"); }
/* Rotate about a point (an arm, a hammer) — W1D2 07-help-balance */
#slide-NN .arm { transform-box: fill-box; transform-origin: 0 100%; transition: transform .5s var(--ease-smooth); }
#slide-NN .frag.arm.is-pending { opacity: 1; transform: rotate(70deg); }
#slide-NN .frag.arm.is-current, #slide-NN .frag.arm.is-past { transform: rotate(0deg); }
/* Slide one cell over (a real move, W5D1 09b): the value is an opaque box inside its cell */
#slide-NN .mv { position: absolute; inset: 0; transition: transform .6s var(--ease-smooth), opacity .3s ease; }   /* no opaque box: it showed as a grey artifact */
#slide-NN .tp__right:has(.cap--2:not(.is-pending)) .mv--1 { transform: translateX(-108px); }
#slide-NN .tp__right:has(.cap--2:not(.is-pending)) .mv--0 { opacity: 0; }                                        /* the overwritten value fades as the mover arrives */
```

Every slide with local transitions ends with the `prefers-reduced-motion` block.
Slide-to-slide: only dividers carry `data-transition="fade"`.

---

## 9. Codewalk (js/code-walk.js; its header is the full guide)

```html
<div class="slide__body grid grid--code">
  <div class="stack">
    <div class="editor">
      <p class="editor__bar">your program</p>
      <div class="editor__pc"></div>
      <ol class="editor__code">
        <li class="walkline frag" data-step="1">Movie film1 = <span class="tok-key">new</span> Movie();</li>
        <li class="walkline frag walkline--new" data-step="4">…</li>   <!-- --new: hidden until reached (answer lines) -->
        <li class="walkline frag" data-step="5" data-hold="8">for (…) {</li>  <!-- held: current for steps 5–8 -->
      </ol>
    </div>
    <ol class="verdict frag" data-step="N">…</ol>
  </div>
  <div class="codewalk">
    <div class="codewalk__heap">
      <p class="heap-name frag" data-step="1" data-wire="1:a 7:c" style="grid-row: 1">film1</p>
      <div class="heap-obj frag" data-step="1" data-obj="a" style="grid-row: 1">
        <p class="heap-obj__type">Movie</p>
        <div class="heap-obj__field" data-roll="off">                <!-- stacked crossfade -->
          <p class="heap-val heap-val--old frag" data-step="2">title = null</p>
          <p class="heap-val frag" data-step="2">title = "Dune"</p>
        </div>
        <div class="heap-obj__field heap-obj__field--strike">        <!-- before/after: id = ~~456~~ 789 -->
          <p class="heap-val heap-val--old frag" data-step="4">year = <span class="heap-val__num">2021</span></p>
          <p class="heap-val frag" data-step="4"><span class="sr-only">now </span>1984</p>
        </div>
        <div class="heap-obj__gone frag" data-step="7">unreachable</div>
      </div>
      <svg class="heap-wires" aria-hidden="true"></svg>
    </div>
    <div class="moves">                                             <!-- a counter that rolls; W5D1 -->
      <p class="moves__label">moves</p>
      <div class="moves__stack">
        <div class="heap-obj__field"><p class="heap-val heap-val--old frag" data-step="2">0</p><p class="heap-val frag" data-step="2">1</p></div>
        <div class="heap-obj__field"><p class="heap-val heap-val--old frag" data-step="3">1</p><p class="heap-val frag" data-step="3">2</p></div>
      </div>
    </div>
    <div class="codewalk__caps">
      <p class="walkcap frag" data-step="1">One object on the heap, fields at their defaults.</p>
    </div>
  </div>
</div>
```

- The heap is a grid: names in column 1, objects in column 3, inline `grid-row` integers
  only, never pixels. `data-wire="step:objId …"` is the reference timeline (step 0 =
  wired from load, for recaps); arrows draw on, swing on re-point, retract on back-step;
  state is a function of the deck step.
- House style: show Java defaults (`null, null, 0`) at `new` time; strike variant for
  setters and assignments; `data-roll="off"` for replaced text; a field with a default
  and a later strike uses the `.heap-val--default` pattern (W2D1 12b); `walkline--ran`
  for recap code; `.heap-obj--dead` static for recap garbage.
- Width budget: default tracks `max-content 250px max-content`, `.heap-obj` min 380; the
  `grid--code` right column is about 763 px, so with 3+ name pills set the run to 210 px
  and `--t-micro` on `.heap-name`/`.heap-val` in slide-local CSS (measures 722). With a
  720 px editor: names 108 + run 100 + seven 76 px slots + ellipsis = 874 of 912 (W3D2 06b).
- The write-pulse rule uses child combinators: put `frag` on the field div; do not wrap
  fields.
- Several `walkline`s with the same `data-step` are one block and the bar spans them.
  With `data-hold` the block stays under the bar through the held steps.
- The `.moves` counter needs no heap: the engine scans `.heap-obj__field` pairs anywhere
  in a section that has an `.editor__pc`. Its `.codewalk` wrapper supplies the CSS.
- NPE/array: draw no ghost object for a null slot; the line after the throwing line gets
  no `data-step`, so the PC bar fades out on the line that threw.
- A locals-under-the-heap pattern (value pills outside the grid) and slot strips (`.slots`,
  76 px pitch + 8 gap, so a copy travels N × 84 px) are in W3D2 06b/07b. Array strips
  drawn in one SVG with exact travel distances are in W5D1 06b.
- Captions (`.walkcap`) are `--t-small` at 1.35, grid-stacked in one cell, so the caption
  block is as tall as its longest caption; keep captions to three lines of the column.

---

## 10. Illustrated scenes

- `.slide__body { position: relative }` plus one `<svg viewBox="128 232 1664 752"
  preserveAspectRatio="xMidYMax meet" role="img" aria-label="…">` positioned
  `absolute; inset: 0; width/height 100%; overflow: visible`, so every SVG coordinate is a
  canvas pixel. Under kicker + h2 the body top is about 299; use `128 299 1664 685`.
- Stick figures are bare strokes with no class library. Copy from: bust r=24 `#s02-seat`
  (W1D2 02-today), `#w2-lab-seat` (W2D1 02); r=30 at a table `#w2-deal-person`
  (`<circle cy="-40" r="30"/><path d="M-50 40v-14a50 50 0 0 1 100 0v14"/>`, W2D1 07/10);
  turned busts `#w2-bust-l/-r` (W2D1 04); whole-body 5-path (W2D1 07 `.dl__lead`:
  `<circle cx="370" cy="560" r="26"/><path d="M370 586V700M370 616L332 664M370 616L408 660M370 700L346 776M370 700L394 776"/>`,
  stroke 9 round); raised hands grow from the wrist (W1D2 02 `.td__hand`); rotating arm
  (W1D2 07 `.hb__arm`); hammers (W2D1 10, W2D2 new-slide); laptop, contract sheet, code
  lines (W2D2 01b); fork and lanes (W2D2 07b/08b); ring of stations (W2D2 05).
- Pen: stroke-width 5 for the world (`--fg-1`), 7–9 for the live figure (`--fg-0`), 8 for
  a maroon failure cross; `stroke-linecap/linejoin: round`.
- Studio renderer trap: class rules on `<defs>` children do not reach `<use>` clones
  (glyphs render as black silhouettes deck-wide). Put fill and stroke inline on the defs
  content, or style the `<use>` element; inherited stroke from the `<use>`'s parent works
  for per-use colour.
- Text inside SVG: `<text>` with a `<tspan x y>` per line; `font-family: var(--font-mono)`
  at `--t-micro` for labels, `--font-display` for captions and numerals; set
  `text-anchor` explicitly.

---

## 11. Course facts, Fall 2026 (verify anything dated; sources at the end)

Sections: two lecture sections, MW 12:20–1:10 NCB 320 and TR 11:00–11:50 Squires Aud.
"Day 1" = Mon/Tue, "Day 2" = Wed/Thu. One deck serves both sections; since Week 4 the
clock's `now` column is a two-track band (Day 1: Mon+Tue x 128–366, `wk__cta` at 247;
Day 2: Wed+Thu x 366–603, cta 485). Labs begin Week 2. Labor Day Sep 7 removed the MW
Week 3 Monday, hence `week 3 - wednesday`.

The weekly clock (instructor-confirmed 2026-09-07; overrides any source deck):
- PrairieLearn modules N.x are due the Sunday evening before Week N (4.x Sun Sep 13, 5.x
  Sun Sep 20, 6.x Sun Sep 27, 7.x Sun Oct 4, 8.1 Sun Oct 11). Blue.
- Homework "Week N: topic" is due Friday 11:59 PM of Week N on PrairieLearn. Blue.
- Challenge Exercise NN is due Friday (CE 02 onward; CE 01 was "before your lab").
  Maroon (a builder's choice; the instructor only asked that Project 1 differ). Numbering
  CE 03 = Week 3, CE 04 = Week 4, CE 05 = Week 5, CE 06 = Week 6 (schedule page).
- Only project deliverables land in lab, due at the start of the lab session; drawn as a
  solid Monday cell plus a fading Tue–Fri tail over a "your lab day" range line under the
  axis. Project 1 orange, Project 2 the a4 mix. Never a Friday pole, never a Sunday date.
- Geometry (both `02` and `17`): axis y=790; 14 day tracks of 118.86 px from x=128; ticks
  at x = 247 366 485 603 722 (Fri) 841 960 (Sun) 1079 1198 1317 1435 1554 (Fri) 1673
  1792 (Sun); the "now" band is the lecture days' tracks; captions y=940; poles draw up by
  dashoffset, bars wipe from where they start; a Week-2 marker for a project that has not
  started is a stone bracket, not a bar. A test is drawn as a maroon-outlined band over
  the two lecture days (y 250–790, fill maroon 8%, dashed maroon stroke) with `Test 1` at
  the display size and `in lecture · Wed MW · Thu TR` under it; its own step, drawn
  before the bars. In W4D1/W4D2 the band sits on next week (x 1317–1554); in W5D1 it sits
  on this week (x 366–603) as step 1, and the Redo band uses the same drawing on Week 6.

Schedule ahead (`cs2114-schedule-fall2026.html`, `cs2114-deadline-schedule.csv`):

| week | dates | topic | modules (due the Sunday before) | HW (Fri) | CE | project | other |
|---|---|---|---|---|---|---|---|
| 4 | Sep 14–18 | Linked Chains & Linked Bags | 4.1 Assessment 1 Info · 4.2 Linked Chains (Pointers) · 4.3 Linked Bags | Week 4: Linked Chains | 04 Grocery Bags | P1 D2 Spec | PI W4D1 only |
| 5 | Sep 21–25 | Efficiency & Stacks | 5.1 Efficiency · 5.2 Stacks | Week 5: Efficiency & Stacks | 05 Ice Cream Stack | P1 D3 final build + writeup + presentation | Test 1 in lecture, MW Wed Sep 23 / TR Thu Sep 24; PI W5D1 |
| 6 | Sep 28–Oct 2 | Ethics & Software Design | 6.1 Ethics · 6.2 Software Design and MVC | Week 6: Ethics & Design | 06 ArrayBasedStack | P2 D1 Scope · teams re-form | Test 1 Redo in lecture, MW Wed Sep 30 / TR Thu Oct 1; PI W6D1 |
| 7 | Oct 5–9 | Recursion | 7.2 Assessment 2 Info · 7.3 Recursion · 7.4 Midterm Checkpoint | Week 7: Recursion | — | P2 D2 Spec · declare generic type | Fall Break Fri Oct 9; PI W7D1 + W7D2 |
| 8 | Oct 12–16 | Queues | 8.1 Queues | Week 8: Queues | 08 Carrano Deque | P2 D3 Prototype + tests · 2+ element types | PI W8D1 + W8D2 |

Later modules: 9.1 Lists, 9.2 More on Generics (Sun Oct 18); 10.1 Assessment 3 Info,
10.2 Comparing and Sorting, 10.3 Iterators (Sun Oct 25); 11.3 Project 5 (Sun Nov 1).
Homework: Week 9 Lists & Generics, Week 10 Sorting & Iterators, Week 12 Team Project.

Test 1 (instructor, 2026-09-12 and 2026-09-20): in class, in each section's own lecture,
MW Wed Sep 23 and TR Thu Sep 24, inside LockDown Browser launched from Canvas. Test 1 Redo
is the second class of Week 6 for each section: MW Wed Sep 30, TR Thu Oct 1, in lecture.
Delivery platform, unsettled as of 2026-09-20: the instructor's post-build edits to W4D2
(slides 13 and 14) replaced "PrairieLearn" with "Canvas" ("On Canvas, inside LockDown
Browser"; "Canvas › Trial quiz … access code TrialDuringClass"; "Inside it: Canvas ›
Test #1 Practice") and removed the test map's point values ("~15 questions", no points).
W5D1 follows those edits. The PrairieLearn practice exam below may still be the question
source. Ask before asserting either platform. The Week 3 decks carried no Test 1 mention;
from Week 4 it is on both clocks. Rules per the live 4.1 page: one attempt, closed
book/notes/IDE/neighbour/web, laptop only, pen and paper allowed, student ID, SSD via the
Canvas Testing Accommodations link; its "45 minutes" is unverified for F26 and the page
still names CodeWorkout and Labs. Practice: PrairieLearn "Test #1 Practice" (set Practice
Exams → PE1, module week05, 13 slots × 1-of-N alternatives from 154 parametrized
questions, 5×8 + 8×4 = 72 pts, `multipleInstance: true`); the 13 banks group into five
regions (objects & references · testing & exceptions · types · bags on arrays · linked
chains; W4D2 `04-test-map`). As of 2026-09-12 it was untracked in `pl-vt-cs2114` with
`allowAccess: []`; check before pointing a slide at it. W4D2 ran it openly (Part 2), then
a fresh instance for 10 minutes through Canvas and LockDown Browser (Part 3).

Projects: EMRN rubric per deliverable, submitted via GitHub, TA grading sessions run as
oral exams; described by the instructor as apprenticeship-like: no single right answer,
TAs give feedback, teams iterate. Project 1 "Learning to Scope" = Java + Exceptions, no
data structures, teams of 3 (or 4) formed in the Week 2 lab and posted on Canvas, Weeks
3–5 (Sep 7–25): D1 one-page scope (W3 lab) → D2 spec (W4 lab) → D3 final build + writeup
+ 3-minute lightning talk (W5 lab); JUnit tests, one normal and one bad-input case per
key method; robust exception handling; the full brief is the Canvas "Project 1 ·
Overview" page. Project 2 "Bag + Generics" runs Weeks 6–8; teams re-form. Do not couple
ADT/Bag vocabulary to P1.

SSD / testing accommodations (ssd.vt.edu, 2026-09-13): Services for Students with
Disabilities, 310 Lavery Hall, ssd@vt.edu, 540-231-3788. Two student actions per test:
the semester's Course Accessibility Letter requested in AIM
(elbert.accessiblelearning.com/VT; accommodations are not retroactive), and the seat
booked in RegisterBlast through the Testing Accommodations link in the Canvas course, at
least three business days in advance (Wed test → prior Fri, Thu test → prior Mon). Tests
are taken at the Werth Testing Center (310 Lavery Hall). Instructor side: the RegisterBlast
exam submission block at least 5 business days before it starts, materials at least 2
business days before, or reservations are cancelled. W4D1 `02b-ssd` / W4D2 `12b-ssd` is
the slide; reuse it for Test 2 with new dates.

Peer instruction (every lecture): runs in Runestone, course `virginiatech_peerplus_fall26`,
assignment "Peer Instruction W0MDN" (W02D2, W03D1, W04D1, W05D1 confirmed; W03D2's name
unverified), opened from the Canvas home page. Week 4 has peer instruction on Day 1 only;
so does Week 5. Routine: silent first answer → on the instructor's prompt discuss in
groups of 3–4 → second answer → go through it together, wrong answers included; credit
for both rounds, not for being right. Known Runestone source bugs still pending (need the
instructor logged in): W03D1 Q1 missing `;` after `250`, Q2 `getFrequencyOf` missing `)`,
Q3 no stem or class code. W05D1's four questions have PrairieLearn twins in
`questions/dataStructures/efficiency` (`u08q08_efficiency_arraybag_c` is Q1 verbatim,
key O(n); `u08q10_efficiency_arraystack_c/_d` are Q2/Q3, keys O(n)/O(1)).

Coding practice: PrairieLearn › Assessments › Coding Practice. W2 set = `x752` (ageMath)
and `x754` (getOldest) walked, plus x753/x755/x804/x805/x798/x800 not walked; W3 = X789
ArrayBag toString (W3D1 slide 10, duplicated on W3D2); W4 = "Week 4: Linked Chains —
Coding Practice", 19 problems best 5 (x680–x684 LinkedBag, x729–x735 + x781–x788 chain
walks), W4D1 `13-practice-map`; W5 = "Week 5: Efficiency & Stacks — Coding Practice",
x685 LinkedStack toString, x686 toArray, x687 getBaseOfStack, 10 pts each (the class uses
`topNode` and `numberOfEntries`), W5D1 `13-hw-linkedstack`. The PrairieLearn course repo
is `~/Projects/pl-vt-cs2114` (Fall 2026 instance; assessments under
`courseInstances/Fall2026/assessments/`, questions under `questions/`; module slide PDFs
under `clientFilesCourse/slides/`, most of them images).

Tools (W1D1 13-tools, amended): PrairieLearn (modules, homework, coding practice), Canvas
(home page, calendar, schedule, project overview pages), Runestone (peer instruction),
Piazza (Q&A; "turn instructor-post notifications on" is every deck's last beat), GitHub
(project code), Eclipse (IDE; CE 01 was the setup), LockDown Browser (Respondus, installed
from a Canvas link; wraps the test). Web-CAT is contested: W1D1 said "automated grading
for projects" (wrong for F26; projects are EMRN via GitHub); W2D2 carries an
instructor-imported appendix (18-webcat-*) showing Eclipse → Web-CAT submission for
homework/CE and a "Using WebCat for Challenge Exercises" tab; the Week 3+ decks draw no
Web-CAT pill. Ask before drawing one.

Dropped from the course (never draw them): CodeWorkout, My Digital Hand, Lucidchart,
trial quizzes as a graded thing, "lab and postlab", Web-CAT as project grader, the Fall
2025 Bag/ArrayBag Project 1, percentage grading.

Sources (outside the repo, `~/Downloads/`): `cs2114-schedule-fall2026.html`,
`cs2114-deadline-schedule.csv`, `CS2114_Projects_Fall2026(3).imscc` →
`wiki_content/project-1-overview.html`, `Class Planning(28).docx` (and later numbers),
`F25 Week N Day M*.pdf` legacy decks (W1D1, W1D2, W2D1, W2D2, W3D2 present as of
2026-09-12; W3D1's PDF/pptx are inside `week 3 -day 1/`), `S26 Week 4 Day 1.pdf`, `S26
Week 4 Day 2.pdf`, `S26 Week 5 Day 1.pdf` (all three are F25 decks by their metadata),
`S26 Week 1 Day 2.pptx`, `Submitting Your Assignment - Web-CAT Guide.pptx`. Canvas
gradebook CSVs also land there.

---

## 12. Legacy decks: translate policies, quote questions

A legacy F25/S26 deck is a source of layouts, examples and question text, not of
policies. Before authoring, check every date, tool and policy in it against §11 and the
W1D1 `08-legacy-*` / `09-redesign-hints*` slides; record each translation in PLAN.md
under "Translated / dropped / unverified". Legacy screenshots of code are rendered
natively in an `.editor`.

Vote and practice slides quote the question the room has open. `.editor` code and
`.opts` text are quoted material: verify against the live Runestone/PrairieLearn text
(which outranks the F25 PDF), keep its quirks, and change only the deck's own answer
slide, captions and notes. If the source itself is broken, the fix goes into the source
with the instructor's approval; the slide stays clean.

---

## 13. The instructor's standing rules

- A new concept is introduced by walking code (2026-09-20, W5D1): a few slides of
  step-by-step pseudocode walkthroughs with animation, and every vote answer walked the
  same way. Not a definition slide, not a bare graph first. Web research for framings is
  allowed. To show growth, transform the structure on screen and run the walk again;
  do not add a second copy next to it. Shorten variable names to make code larger.
- Chapter titles and the agenda say what the chapter is about in plain words
  (2026-09-20: "Counting moves" was too opaque; "Big-O: count the moves, then watch them
  grow" replaced it).
- Design questions with real alternatives go to three agents with different briefs,
  then a compare-and-contrast and one consolidated implementation (2026-09-20, the vote
  slide).
- Concrete over abstract: named, sized DO/DON'T examples, not principle statements (W2D2:
  "the scope sheet is not a pitch…" was replaced by "a text game with character classes
  and GenAI-made text files, not the next Skyrim"). "Don't give away the answer" protects
  graded artifacts only; calibration examples are wanted.
- Part titles must be true ("What does a test prove?" became "What does a passing test
  tell you?", because a passing test proves nothing).
- A correction is applied fully and literally; partial fixes are rejected.
- No fade-drift; no digit roll on replaced values (§8); GrowFromCenter must be invisible
  while small.
- Vote slides are static; the answer is on the `b` slide; no in-place highlighting.
  Exception (2026-09-12, W4D2): an ungraded recall of an old vote may reveal its
  `.verdict` on step 1 of the same slide.
- No Playwright or screenshot passes; leave placeholders; the instructor reviews in Slide
  Studio.
- No placeholders with question marks for facts the instructor has already given; ask
  instead (2026-09-20).
- Export to Google Slides or pptx, if asked: native editable objects, one output slide per
  reveal step, Chromium as the layout engine; the multi-MB pptx is dragged into Drive by
  hand.
- Global: stay on task; simple, robust solutions; no feature creep; question rather than
  agree; `git add -u` (plus explicit new dirs), never `-A`.
- Documentation and replies in plain prose: no rhetorical asides, quoted-anecdote
  flourishes or figurative phrasing (2026-09-20).

---

## 14. Before you stop

- [ ] PLAN.md exists with through-line, manifest table with plants, translated/dropped/unverified
- [ ] index.html `<title>` and manifest updated in the exact literal form
- [ ] every slide: unique `#slide-NN`, one `.slide__desc`, `aside.notes` (answers first), scoped `<style>`, reduced-motion block, tokens only
- [ ] vote text verbatim from the live source; answer slides end on `.verdict`, `.dbr` rows or a board
- [ ] clock slides follow §11 (Sun modules blue, Fri HW/CE, lab-day projects in their project colour, "now" on the right days, tests as bands)
- [ ] `add_sids.py` on new slides → `lint.py` clean → `measure/run.sh` slack ≥ 30 everywhere, or the hand budget with a note that the sweep did not run
- [ ] `git status` checked for the instructor's concurrent edits; nothing of theirs overwritten
- [ ] unverified facts listed in the reply, not asserted
