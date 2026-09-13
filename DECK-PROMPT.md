# CS 2114 Fall 2026 lecture decks — build prompt

Paste this file (or `@DECK-PROMPT.md`) at the start of a session, then say what to
build, e.g. **"Build week 4 day 1 from ~/Downloads/F25 Week 4 Day 1.pdf"** or
**"Add a vote + answer pair to week 3 day 2 for Runestone question X"**.
Everything below was distilled 2026-09-12 from the Week 1–3 decks in this repo and
updated the same day after the Week 4 decks were built;
where a fact was still unverified at that date it says so — do not launder it into a
certainty.

---

## 0. The short version

1. A deck = one folder `week N - day M/` with `index.html` (manifest) + `css/` + `js/` +
   `assets/` + `slides/NN-name.html` fragments. Zero dependencies; needs an HTTP server.
2. Clone `week 3 - wednesday/`'s `css/`, `js/`, `assets/fonts`, `assets/stone-edge.svg`,
   `studio.config.json` and `week 3 - day 2/tools/` — the most complete shared copies.
3. Write `PLAN.md` first (through-line, chapter table, per-slide beats + plant, what was
   translated/dropped/unverified). Then the slides. Then `add_sids.py`, `lint.py`,
   `measure/run.sh`. Then **stop** — the instructor reviews in Slide Studio.
4. Every slide: `<section id="slide-NN">`, `.slide__head`, ONE `.sr-only .slide__desc`,
   `.slide__body`, `.slide__number`, `aside.notes`, slide-local `<style>` scoped by
   `#slide-NN`, all values from `tokens.css`, motion in manim's vocabulary only.
5. Facts: translate legacy policies to Fall 2026; quote live Runestone/PrairieLearn
   question text verbatim; the instructor's clock rules (§11) beat any source deck.

---

## 1. What a deck is

- **Canvas** 1920×1080, authored in canvas pixels; `js/deck.js` scales it with a
  transform. Padding `--s-7` (96) top/bottom, `--s-8` (128) left/right → the body is
  1664 wide (x 128…1792) and at most 888 tall (y 96…984). `.slide { overflow: hidden }`
  — overflow is clipped **silently**; nothing ever scrolls.
- **`index.html`** holds `window.SLIDE_MANIFEST = [ '01-title.html', … ]`. Slide Studio
  rewrites that array literal in place — keep the assignment in exactly that form.
  Scripts: `deck.js`, `studio-motion.js`, `code-walk.js` (+ `timer.js` where used).
- **`js/deck.js`** fetches `slides/*.html`, one `<section>` each, in manifest order.
  Navigation by hash `#N` / `#N.K`; keys ← → space PgUp/PgDn Home End, `f` fullscreen,
  `m` toggles `html.no-motion`. Step engine: every `.frag[data-step]` gets
  `is-pending` / `is-current` / `is-past` against the current step; `maxStep` = the
  highest `data-step` in the section, so steps must be **dense from 1**. Events
  `slides:loaded` and `deck:stepchange`; `?embed=1` = passive presenter iframe.
- **`css/tokens.css`** — the whole visual vocabulary (identical in every deck except
  W3+'s `--t-h1-sm: 100px`). **`css/deck.css`** — every pattern used by 2+ slides.
  `css/studio-anim.css` + `js/studio-motion.js` are Slide Studio's (safe to leave).
- **Slide Studio** is the instructor's editor: `studio.config.json`
  (`canvas 1920×1080, uploadDir assets`), `.slide-studio/permissions.json`. It needs a
  `data-sid="<basename>:<n>"` on every element (run `tools/add_sids.py`), writes
  `.slide__desc` with `data-hash`/`data-desc="auto"`, and its drag handles leave inline
  `style="width/height/left/margin…"` — even on `<section>` — strip those before
  reasoning about layout.
- **Assets**: `assets/fonts/` (Inter + JetBrains Mono variable woff2, OFL, `LICENSE.md`)
  and `assets/stone-edge.svg` (the mask for the Hokie-Stone left edge) must be copied
  into every new deck. Photos/screenshots go in `assets/` too (Studio's upload dir).
- Decks appear to be published at `https://ascend3.cs.vt.edu/slides/cs2114-fa26-weekN-dayM/`
  (from a W3D1 note; unverified).

### Where each idea came from (so you know which deck to open)

| deck | what it established |
|---|---|
| `week 1 - day 1` | tokens + deck.css, the title/dusk-closing pair, tiles, the semester map & three-projects table, the ethics arc; also a **spec sub-deck** (`01-master-spec`, `02-design-system*`, `03-week1-deck*`, `05–09-legacy-*`, `10-asset-inventory*`) that inventories the legacy pptx decks and states "reuse layouts and assets, never policies" |
| `week 1 - day 2` | the illustrated stepped style, `02-today` (room scene), the **clock** grammar (`03-keep-up`, `14-work-time`), the first vote/answer pairs (`09/09b`, `10/10b`), the **codewalk** component, chapter dividers, `.slide__desc` accessibility |
| `week 2 - day 1` | `01b-today` chapter tabs, `02-course-info`/`17-next-class` clock pair, peer-instruction chapter (`03`, `04`, `06`, `07-the-deal`, `10-icebreaker`, `11-peer-plus` ring), `.verdict` strip, `data-roll="off"`, the LLM chapter (`16d` is **generated** by `tools/next-token/gen16d.py` — never hand-edit), `.chat` |
| `week 2 - day 2` | the three-chapter deck shape + `PLAN.md` as audit trail, testing votes (`06–08b`), `.dbr` debrief rows, Project 1 "Learning to Scope" (`04`, `new-slide` DO/DON'T cards), practice codewalks (`13`, `14`, `15`), Web-CAT appendix (`18*`) |
| `week 3 -day 1` | the deck.css **specificity fixes**, `.code-dense`/`.code-tag`, `.opts--code`, `PLAN-sizing.md`, the headless measure harness |
| `week 3 - day 2` | first deck built straight from an F25 PDF; `tools/` (add_sids, lint, measure); the linear-time vote |
| `week 3 - wednesday` | MW make-up deck (Labor Day); `js/timer.js` 5:00 discussion countdown; most complete css/js |
| `week 4 - day 1` | first deck serving both sections: the **two-track `now` band**, the **Test 1 band** on the clock; SVG **chain scenes** (Link boxes `data \| next`, blue marker arrows that **swing** via a CSS `d: path()` transition) in `04`, `07b`, `09b`, `11`; a 2×2 `.opts--code` grid for four long code options (`09`); four synchronised lanes (`09b`) |
| `week 4 - day 2` | the review deck: `04-test-map` (regions + weights), **recall slides** (copies of earlier static votes with a `.verdict` on step 1), the 10:00 `.timer` at 400 px (`14`), DO/DON'T cards (`13`) |

---

## 2. Starting a new deck

```
mkdir "week N - day M"/{css,js,assets,slides,tools}
cp "week 3 - wednesday"/css/*.css            "week N - day M"/css/
cp "week 3 - wednesday"/js/*.js              "week N - day M"/js/      # deck, code-walk, studio-motion, timer
cp -r "week 3 - wednesday"/assets/fonts      "week N - day M"/assets/
cp "week 3 - wednesday"/assets/stone-edge.svg "week N - day M"/assets/
cp "week 3 - wednesday"/studio.config.json   "week N - day M"/
cp -r "week 3 - day 2"/tools/*               "week N - day M"/tools/
cp "week 3 - wednesday"/index.html           "week N - day M"/        # then fix <title> + manifest
```

- Folder names carry spaces (and `week 3 -day 1` has an odd one) — quote paths.
- Shared-file divergence as of 2026-09-08: `tokens.css`, `deck.js`, `studio-*` identical
  everywhere. `deck.css`: W3D1/W3D2/wednesday have the `.slide .editor__bar` /
  kicker / note / lede / tile__label specificity fixes and `.code-dense` / `.code-tag`
  / `.opts--code`; W2D1 alone has `.chat`; W2D2 alone has `.dbr`; W2D1/W3D2/wed have
  `.verdict`; wed alone has `.timer`. `code-walk.js`: `data-roll="off"` in W2D1, W3D2,
  wed only; **W4D1's copy** also makes the PC bar cover every `.walkline` that shares the
  current step as one block (a braced constructor, W4D1 04); W4D1's `timer.js` finishes
  a timer once its step is past (the vote/discussion pair) — clone those copies for new
  decks. Port `.dbr` from W2D2 or `.chat` from W2D1 if a slide needs them.
- Copy the always-present slides and change only the facts: `01-title` (kicker
  `CS 2114 · FALL 2026 · WEEK N · DAY M`; W3's version has the `--t-h1-sm` one-line
  fix), `01b-today`, `02-course-info`, the chapter dividers, `05-peer-plus`,
  `17-next-class`, `99-closing`.
- Section ids `#slide-NN` must be **unique per deck** — slide-local CSS is scoped by
  them and cross-applies otherwise (that is why wednesday renumbered its copies).
- `index.html` `<title>`: `CS 2114 — Software Design & Data Structures · Fall 2026 Week N Day M`.
- git: `git add -u` never covers a new directory — `git add "week N - day M"` explicitly.
  **Never `git add -A`.** Commit only when asked.

---

## 3. The build workflow (how the past decks were actually made)

1. **Read the sources** (§11 for paths): the F25 PDF/pptx for that day, the Fall 2026
   schedule + deadline CSV, the Canvas project overview if a project is in play, and the
   live Runestone/PrairieLearn question text (ask the instructor to paste it if you
   cannot log in). Read the sister deck's PLAN.md and its `02`/`17` clock slides.
2. **Write `PLAN.md`** in the deck folder before any slide:
   - a one-sentence **through-line** in bold quotes, then the 2–3 chapters as bullets;
   - a **manifest table** (`file | role`), the role ending with the slide's **plant** (→);
   - a per-slide section: what it shows, how it builds step by step, the hand-off;
   - **Translated / dropped / unverified** — every legacy policy you changed, every
     thing you left out, every fact you could not confirm;
   - a **Status** block appended after the instructor's review, dated.
   The W2D2 and W3D2 PLAN.md files are the models.
3. **Write the slides** directly in the main session (seven slides ≈ 40 minutes by
   hand). Subagents have stalled on this machine; if used at all give each a ≤300-line
   spec, a short reading list, "Read tool only, one Write per slide", and check file
   mtimes before relaunching.
4. **Tooling pass**: `python3 tools/add_sids.py slides/*.html` (new slides only),
   `python3 tools/lint.py slides/*.html` (must be clean), `tools/measure/run.sh
   "$PWD"` (absolute path — a relative `.` symlinks the temp dir to itself and returns
   empty JSON; needs `chromium`, run with the sandbox disabled). Treat <30px slack as
   unfinished; re-measure after every layout change.
5. **Stop.** No Playwright, no screenshot loops — the instructor reviews in Slide Studio
   ("dont do playwright. just make the edits and I'll fill it in"). Leave clearly marked
   placeholders for facts you do not have. Say what is unverified.
6. The instructor edits concurrently in Slide Studio / another session: check
   `git status` and mtimes before touching a file, and stay off files with fresh
   uncommitted changes. When they say "just get it done like an expert would", decide,
   record the decision in PLAN.md, and do not ask again.

---

## 4. Slide anatomy — the template

```html
<section class="slide" id="slide-NN">                      <!-- classes: slide--warmup | slide--title slide--center slide--nostone | slide--section slide--center divider -->
  <header class="slide__head">
    <p class="slide__kicker">PEER INSTRUCTION &middot; VOTE 1</p>   <!-- optional; CSS uppercases -->
    <h2>What does the last line print?</h2>
  </header>
  <p class="sr-only slide__desc">Full-sentence description of what the slide shows and how it builds, for a screen reader. Exactly one per slide, right after the heading.</p>

  <!-- Author's comment: the idea of the slide in two or three sentences, then
       step 1: …
       step 2: …
       (viewBox = the body's rect, if a scene) -->
  <div class="slide__body">
    …
  </div>
  <div class="slide__number"></div>                        <!-- deck.js fills "N / total" -->
  <aside class="notes">Speaker notes. For an answer slide open with "Answer: B &mdash; …". Then "Step 1 &mdash; …" per step, and the spoken hand-off to the next slide.</aside>

  <style>
    /* Slide-local: why this slide needs its own rules (one prose paragraph — what
       the picture is, which motion each thing gets, the size trade-off). Used by
       this slide only, all values from tokens. */
    #slide-NN .x { … }
    @media (prefers-reduced-motion: reduce) {
      #slide-NN .x { transition-duration: 0s !important; transition-delay: 0s !important; }
    }
  </style>
</section>
```

Rules the linter enforces: balanced tags; every `data-sid` unique and prefixed with the
file's basename; `data-anim` only `fade` or `none`; no raw hex (except `url(#…)`,
`id=`, `href`); every selector in the slide `<style>` starts with `#slide-NN`; no
`.is-pending` rule that combines `translate…` with `opacity` (a drift reveal); dense
`data-step` numbering; exactly one `<section id>`; a `slide__desc` present.

House rules the linter cannot check: HTML entities (`&mdash; &rsquo; &middot; &rarr;`)
in text; `role="img"` + full-sentence `aria-label` on figure SVGs, `aria-hidden` on
decoration; `<defs>` ids namespaced per deck (`w4d1-NN-…`); patterns used by 2+ slides
go to `deck.css` with a comment, single-slide patterns stay local with a prose comment;
comments explain *why* in the deck's voice (read a few — they are part of the style).

---

## 5. Recurring slide types — copy these files

| type | copy from | notes |
|---|---|---|
| title | `week 3 - day 2/slides/01-title.html` | ridge + mist decor, `slide--nostone`, kicker with week/day, `--t-h1-sm` one-liner |
| today (chapter tabs) | `week 2 - day 2/slides/01b-today.html` | 3 columns, each a 360-tall drawing on a rule + orange numeral + caption; columns GrowFromCenter one per step; the captions ARE the divider titles |
| this week's clock | `week 3 - day 2/slides/02-course-info.html` | two-week axis; see §11 for the geometry and colour rules |
| chapter divider | `week 3 - day 2/slides/04b-chapter-2.html` | `slide--section slide--center divider`, `data-transition="fade"`, kicker `PART k OF n`, h2 = the tab caption; nothing builds |
| peer-instruction routine | `week 2 - day 2/slides/05-peer-plus.html` | five stations in a ring (centre 960,630 r 260), arcs draw on, station 2 orange (the silent first answer), plant under the ring |
| vote (static) | `week 2 - day 1/slides/12-vote-movie.html` (short code), `week 3 -day 1` 07/08 (long code, `.opts--code` + `.code-tag`) | kicker `PEER INSTRUCTION · VOTE k`; `grid--code`: `.editor` left, `.tile--a2` API + `.opts` right; **static, gives nothing away**; notes open `Answer: X —` |
| vote answer (walkthrough) | `week 2 - day 1/slides/12b-walk-movie.html` (codewalk), `week 2 - day 2/slides/07b-walk-cases.html` / `08b-walk-branch.html` (SVG scenes), `week 3 - day 2/slides/06b-walk-gap.html` (ArrayBag slots) | file `NNb-walk-*`, kicker `VOTE k · THE ANSWER`, h2 states the conclusion; ends on `.verdict` (or `.dbr` rows) |
| practice map | `week 2 - day 2/slides/10-week2-practice.html` | trail of stop discs numbered with the PL question numbers + signpost "PrairieLearn › Assessments › Coding Practice" |
| practice codewalk | `week 2 - day 2/slides/13-npe-agemath.html`, `week 2 - day 1/slides/13b-walk-student.html` (NPE/array) | kicker `PRACTICE k`; the crashing line's successor gets **no** `data-step` so the PC bar fades out on the throw |
| code + scene | `week 2 - day 2/slides/14-oldest-ask.html`, `15-oldest-code.html` | editor left, stick-figure scene right; rings on lines |
| stick-figure scene | `week 2 - day 1/slides/07-the-deal.html`, `04-why-peer-instruction.html`, `10-icebreaker.html`; `week 2 - day 2/slides/new-slide.html` (smith + card deck) | §10 |
| chat transcript | `week 2 - day 1/slides/16f-llm-risks.html` (`.chat`) | |
| before next class | `week 2 - day 2/slides/17-next-class.html` (poles rising one per step), `week 3 - day 2/slides/17-next-class.html` (static recall) | the same clock as `02`, "say 'same clock' out loud"; last beat: Piazza / instructor-post notifications |
| appendix with screenshots | `week 2 - day 2/slides/18-webcat-guide.html` + `18b–18e` | `<img>` on `--paper` plates; kicker `STEP k OF n` |
| closing | `week 1 - day 2/slides/99-closing.html` | dusk: sun sets, sky darkens, stars; `slide--dusk slide--nostone` |
| chain scene | `week 4 - day 1/slides/04-node-anatomy.html` (a walk down `class Link` under the PC bar: fields and reads washed/ringed blue, writes washed orange), `07b-walk-trace.html` (rewiring), `09b-walk-double.html` (four lanes), `11-linkedbag-add.html` | Link box 240×120 (or 170×100 / 130×80) with `data \| next` compartments, blue cubic arrows + `marker-end` (marker fill inline), `null` as the word in stone; swings = CSS `d: path()` under `:has(.cap--k:not(.is-pending))`; codewalk cannot do node→node |
| recall (ungraded) | `week 4 - day 2/slides/05-recall-refs.html`, `08-recall-bags.html` | a shipped static vote slide copied (strip sids first), kicker `RECALL · WEEK k · REGION`, `.verdict` on step 1 spanning both columns — the one place the answer is on the same slide |
| homework operations | `week 4 - day 1/slides/13-hw-reads.html`, `13b-hw-writes.html` | the week's PL problems as pointer moves: a nine-line index with the problem numbers (other slide's half dimmed), one static picture per press in the Node-box grammar (moved arrows orange, replaced arrow dashed stone, unreachable node stone), the rule as code in the caption. Generated from one Python grammar — regenerate, don't hand-edit coordinates |
| SSD reminder | `week 4 - day 1/slides/02b-ssd.html` | two cards (letter in AIM · seat in RegisterBlast by exam − 3 business days) + the SSD contact line |
| long timer | `week 4 - day 2/slides/14-lockdown-run.html` | the same `.timer` block, `data-timer="600"`, seed `10:00`, slide-local `position: static` + 400 px arc |

The deck shape since W2D2: `01-title → 01b-today → 02-course-info → [divider → chapter
slides → plant]×n → 17-next-class → 99-closing`. File numbers are a sort key, not the
position — inserted slides take `NNb`, `NNc`. The instructor has referred to slides both
by on-screen position and (most recently, 2026-09-01) by file prefix ("slide 03" =
`03-vocabulary`); when it matters, name the file back.

---

## 6. Design vocabulary (css/tokens.css)

- **Text**: `--fg-0` #2c1a1f (ink), `--fg-1` #6b4a52 (muted). **Surfaces**: `--bg-0`
  #f2f1ed (mortar ground), `--bg-1` #e9e3e4 (panels), `--paper` #ffffff (plates,
  QR cards). **Accents**: `--accent-1` #861f41 VT maroon, `--accent-2` #1c6091 Blue
  Ridge blue, `--accent-3` #b35510 burnt orange. `--stone` #7d8791, `--night` #0d1016.
  Mixes: `color-mix(in srgb, var(--accent-1) 50%, var(--accent-3))` = deadline ink /
  `tile--a4`. **Never a raw hex in a slide.**
- **Colour semantics** (consistent across every deck): `--fg-1` the neutral world ·
  `--fg-0` what is live/you · `--stone` past, inert, ghost · **maroon** = the rule, the
  failure, the heading, the assignment name to find · **blue** = tools, measures,
  wires/references, PrairieLearn · **orange** = whoever is doing the work, "yours to
  write", Project 1, the tab numerals · a piece of someone's work = orange 18% tint +
  orange stroke. Project accent coding from W1D1: P1 = a3 orange, P2 = a4 mix, P3 = a2 blue.
- **Fonts**: body Verdana stack (`--font-body`; resolves to Nimbus Sans on this Linux
  box), headings Georgia (`--font-display`), code JetBrains Mono (`--font-mono`, bundled).
- **Type scale** (px): h1 120 (`--t-h1-sm` 100), h2 80, h3 56, body 48, small 36,
  micro 28 (chrome: editor bar, gutter), tag 21 (floor: map labels, captions).
  **Spacing**: s-1 8 · s-2 16 · s-3 24 · s-4 32 · s-5 48 · s-6 64 · s-7 96 · s-8 128.
  **Radii**: r-1 4 · r-2 10 · r-3 18. Easing: `--ease-smooth` (manim smootherstep).
- **Measured budgets** (do not eyeball — these were wrong by 100+px when guessed):
  body 752 tall under a bare h2 (starts y=232), **685 under kicker + h2**;
  body 36px ≈ 16.3 px/char, 28px ≈ 12.7; mono 36 = 21.6, 28 = 16.8, 21 = 12.6 px/char;
  `--t-small` at 1.35 ≈ 49px/line → a text column beside an 840px scene holds ~12
  wrapped lines total; ~80 chars ≈ 3 lines at 658px. A 49-char mono line at 28px
  needs ≥909px. For exact counts: PIL + greedy wrap against the real inner width with
  `fc-match Verdana`. `.slide li` sets line-height 1.5 and beats any line-height on the
  list — set it on the `li`. A `.frag` placed by grid auto-flow can land in a column you
  did not expect; give every cell an explicit `grid-column`/`grid-row` (W4D2 13).
- Layout rules: content-board slides fill the frame (`grid-auto-rows: 1fr`); airy
  display slides centre their block. For stacked/overlaid panels use grid stacking
  (every card `grid-area: 1 / 1`, later-in-source on top) — never `position: absolute;
  inset: 0` in a fixed-height box.

---

## 7. Shared components (css/deck.css) — names to reuse, not reinvent

`.slide__head` (+ `.slide__kicker`, `.slide__lede`) · `.note` · `.tile` (`--a2 --a3
--a4 --display`, `.tile__label`) · `.grid` (`--2 --3 --code` = `1.15fr 1fr`, `--tiles`)
· `.stack` · `.chips` · `.checklist` · `.steps` (display numerals) · `.editor`
(`.editor__bar`, `.editor__pc`, `.editor__code > li`, `.tok-key`, `.tok-num`; body
modifiers `.code-dense` (28px) / `.code-tag` (21px) — one class on the slide body, never
local editor type rules) · `.opts` (lettered answers; `.opts__code`, `.opts--code`) ·
`.refs` (the old static reference diagram — prefer codewalk) · `.slide--warmup` (h2
drops to h3 size; vote/walk slides) · `.scan` (QR plate) · **codewalk** (§9) ·
`.verdict` (`<ol class="verdict frag" data-step="N">` of `.verdict__opt--wrong`
(`style="--i: k"`) / `--right`, each wrapping `.verdict__txt`) · `.dbr` debrief rows
(W2D2) · `.chat` (W2D1) · `.timer` (wed; copy the whole `<div class="timer frag"
data-step="1" data-timer="300" …>` SVG block from a wednesday vote slide — the markup
is in `js/timer.js`'s header; **W4D1 vote slides run two rings**: `timer--vote`
`data-timer="150"` on step 1 and `timer--discuss` `data-timer="240"` on step 2, side by
side at the top right with a `.tlabel` under each — the second press starts the
discussion clock and **W4D1's `timer.js` finishes a timer whose step has been passed**
(0:00, done); older copies leave it running) · `.motto` (`--tight`) · `.divider`, `.divider__n` · `.slide--title
--section --center --nostone --dusk` · decor: `.decor--ridge`, `.ridge-far/mid/near`,
`.mist--a/b/c`, `.sun-set`, `.night`, the `.slide::before` stone edge (72px, on every
slide unless `--nostone`) · `.img-placeholder[data-src]` · `.frag--dim` · `.sr-only`.

Known trap (fixed in W3+ copies only): bare-class `<p>` components lose to the
`.slide p` type ramp — any new `<p>` component in deck.css needs the `.slide ` prefix.

---

## 8. Motion — manim's vocabulary, nothing else

The instructor "really hates" fade-while-translating. Position change must mean
something moved. Allowed entrances: **FadeIn** (pure opacity), **GrowFromCenter** (pure
scale, with opacity resolving early), **Create** (a stroke drawing on), **wipe** (a bar
filling from where it starts), a **real move** (Transform / TransformFromCopy — the thing
actually travels). Exits: plain fade. Replaced values: plain crossfade or the strike
variant — **no digit roll** on assignments/setters ("it makes it look like you're
incrementing"); the roll is only for values that truly count.

Never: `data-anim="fade-up|fade-down|slide-*|scale-*"`, any `translate` in an
`.is-pending` state, `opacity: 1; scale(.1)` pending states (a tiny visible thing sits
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
   Never marker-end on a drawn-on arrow: markers ignore the dash-offset, so the head sits at the tip
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
```

Every slide with local transitions ends with the `prefers-reduced-motion` block.
Slide-to-slide: only dividers carry `data-transition="fade"`.

---

## 9. Codewalk — code walkthroughs (js/code-walk.js; its header is the full guide)

```html
<div class="slide__body grid grid--code">
  <div class="stack">
    <div class="editor">
      <p class="editor__bar">your program</p>
      <div class="editor__pc"></div>
      <ol class="editor__code">
        <li class="walkline frag" data-step="1">Movie film1 = <span class="tok-key">new</span> Movie();</li>
        <li class="walkline frag walkline--new" data-step="4">…</li>   <!-- --new: hidden until reached (answer lines) -->
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
    <div class="codewalk__caps">
      <p class="walkcap frag" data-step="1">One object on the heap, fields at their defaults.</p>
    </div>
  </div>
</div>
```

- Heap is a grid: names col 1, objects col 3, **inline `grid-row` integers only**, never
  pixels. `data-wire="step:objId …"` is the reference timeline (step 0 = wired from
  load, for recaps); arrows draw on, swing on re-point, retract on back-step; state is a
  pure function of the deck step.
- House style: show Java defaults (`null, null, 0`) at `new` time; strike variant for
  setters/assignments; `data-roll="off"` for replaced text; a field with a default then
  a later strike uses the `.heap-val--default` trick (W2D1 12b); `walkline--ran` for
  recap code; `.heap-obj--dead` static for recap garbage.
- Width budget: default tracks `max-content 250px max-content`, `.heap-obj` min 380;
  the `grid--code` right column is ~763px, so **3+ name pills → run 210px + `--t-micro`
  on `.heap-name`/`.heap-val`** in slide-local CSS (measures 722). With a 720px editor:
  names 108 + run 100 + seven 76px slots + ellipsis = 874 of 912 (W3D2 06b).
- The write-pulse rule uses child combinators: put `frag` **on** the field div, never
  wrap fields.
- Several `walkline`s with the same `data-step` are one block: the bar spans them
  (W4D1's `code-walk.js`; older copies highlight only the first).
- NPE/array: draw no ghost object for a null slot; the successor of the throwing line gets
  no `data-step` so the PC bar fades out on the line that threw.
- A locals-under-the-heap pattern (value pills outside the grid) and slot strips (`.slots`,
  76px pitch + 8 gap so a copy travels N × 84px) live in W3D2 06b/07b.

---

## 10. Illustrated scenes

- `.slide__body { position: relative }` + one `<svg viewBox="128 232 1664 752"
  preserveAspectRatio="xMidYMax meet" role="img" aria-label="…">` positioned
  `absolute; inset: 0; width/height 100%; overflow: visible` — so every SVG coordinate is
  a canvas pixel. (Under kicker + h2 the body top is ~299; adjust the viewBox.)
- Stick figures are bare strokes, no class library. Copy from: bust r=24 `#s02-seat`
  (W1D2 02-today), `#w2-lab-seat` (W2D1 02); r=30 at a table `#w2-deal-person`
  (`<circle cy="-40" r="30"/><path d="M-50 40v-14a50 50 0 0 1 100 0v14"/>`, W2D1 07/10);
  turned busts `#w2-bust-l/-r` (W2D1 04); whole-body 5-path (W2D1 07 `.dl__lead`:
  `<circle cx="370" cy="560" r="26"/><path d="M370 586V700M370 616L332 664M370 616L408 660M370 700L346 776M370 700L394 776"/>`,
  stroke 9 round); raised hands grow from the wrist (W1D2 02 `.td__hand`); rotating arm
  (W1D2 07 `.hb__arm`); hammers (W2D1 10, W2D2 new-slide); laptop / contract sheet /
  code lines (W2D2 01b); fork and lanes (W2D2 07b/08b); ring of stations (W2D2 05).
- Pen: stroke-width 5 for the world (`--fg-1`), 7–9 for the live figure (`--fg-0`), 8
  for a maroon failure cross; `stroke-linecap/linejoin: round`.
- **Studio renderer trap**: class rules on `<defs>` children do NOT reach `<use>` clones
  (glyphs rendered as black silhouettes deck-wide). Put fill/stroke inline on the defs
  content, or style the `<use>` element; inherited stroke from the `<use>`'s parent works
  for per-use colour.
- Text inside SVG: `<text>` with `<tspan x y>` per line, `font-family: var(--font-mono)`
  `--t-micro` for labels, `--font-display` for captions/numerals, `text-anchor` set
  explicitly.

---

## 11. Course facts — Fall 2026 (verify anything dated; sources listed at the end)

**Sections**: two lecture sections — MW 12:20–1:10 NCB 320 and TR 11:00–11:50 Squires
Aud. "Day 1" = Mon/Tue, "Day 2" = Wed/Thu. One deck serves both sections; since Week 4
the clock's `now` column is a **two-track band** (Day 1: Mon+Tue x 128–366, `wk__cta` at
247; Day 2: Wed+Thu x 366–603, cta 485). Labs begin Week 2; Labor Day Sep 7 ate the MW
Week 3 Monday (hence `week 3 - wednesday`).

**The weekly clock** (instructor-confirmed 2026-09-07; these beat any source deck):
- PrairieLearn **modules N.x are due the Sunday evening before Week N** (4.x Sun Sep 13,
  5.x Sun Sep 20, 6.x Sun Sep 27, 7.x Sun Oct 4, 8.1 Sun Oct 11). Blue.
- **Homework "Week N: topic" due Friday 11:59 PM** of Week N, PrairieLearn. Blue.
- **Challenge Exercise NN due Friday** (CE 02 onward; CE 01 was "before your lab"). Maroon
  (my pick, not the instructor's — they only asked that Project 1 differ). Numbering
  CE 03 = Week 3, CE 04 = Week 4 (from the schedule page; the bar label was the
  instructor's own edit).
- **Only project deliverables land in lab** — due at the *start* of your lab session,
  drawn as a solid Monday cell + fading Tue–Fri tail over a "your lab day" range line
  under the axis. Orange. Never a Friday pole, never a Sunday date.
- Geometry (both `02` and `17`): axis y=790, 14 day tracks of 118.86px from x=128; tick
  x = 247 366 485 603 **722 (Fri)** 841 **960 (Sun)** 1079 1198 1317 1435 **1554 (Fri)**
  1673 **1792 (Sun)**; "now" column = the lecture day's track; captions y=940; poles draw
  up by dashoffset, bars wipe from where they start; a Week-2 marker for a project that
  has not started is a stone bracket, not a bar. **A test** is an hour in the room, not a
  midnight: a maroon-outlined **band over the two lecture days** (W5 Wed–Thu = x 1317–1554,
  y 250–790, fill maroon 8 %, dashed maroon stroke) with `Test 1` at the display size and
  `in your lecture · Wed MW · Thu TR` under it — its own step, drawn before the bars.

**Schedule ahead** (`cs2114-schedule-fall2026.html`, `cs2114-deadline-schedule.csv`):

| week | dates | topic | modules (due the Sunday before) | HW (Fri) | CE | project | other |
|---|---|---|---|---|---|---|---|
| 4 | Sep 14–18 | Linked Chains & Linked Bags | 4.1 Assessment 1 Info · 4.2 Linked Chains (Pointers) · 4.3 Linked Bags | Week 4: Linked Chains | 04 Grocery Bags | P1 D2 Spec | PI W4D1 only |
| 5 | Sep 21–25 | Efficiency & Stacks | 5.1 Efficiency · 5.2 Stacks | Week 5: Efficiency & Stacks | 05 Ice Cream Stack | P1 D3 final build + writeup + presentation | **Test 1 Thu Sep 24 in class**; PI W5D1 |
| 6 | Sep 28–Oct 2 | Ethics & Software Design | 6.1 Ethics · 6.2 Software Design and MVC | Week 6: Ethics & Design | 06 ArrayBasedStack | P2 D1 Scope · teams re-form | Test 1 Redo Thu Oct 1; PI W6D1 |
| 7 | Oct 5–9 | Recursion | 7.2 Assessment 2 Info · 7.3 Recursion · 7.4 Midterm Checkpoint | Week 7: Recursion | — | P2 D2 Spec · declare generic type | Fall Break Fri Oct 9; PI W7D1 + W7D2 |
| 8 | Oct 12–16 | Queues | 8.1 Queues | Week 8: Queues | 08 Carrano Deque | P2 D3 Prototype + tests · 2+ element types | PI W8D1 + W8D2 |

Later modules: 9.1 Lists, 9.2 More on Generics (Sun Oct 18); 10.1 Assessment 3 Info,
10.2 Comparing and Sorting, 10.3 Iterators (Sun Oct 25); 11.3 Project 5 (Sun Nov 1);
HW Week 9 Lists & Generics, Week 10 Sorting & Iterators, Week 12 Team Project.
**Test 1** (instructor, 2026-09-12): in class, in each section's own lecture — **MW Wed
Sep 23, TR Thu Sep 24** — on **PrairieLearn inside LockDown Browser, launched from
Canvas**; Test 1 Redo Thu Oct 1. The Week 3 decks had cut every Test 1 mention as too
early; from Week 4 it is on both clocks (see the band rule above). Rules per the live 4.1
page: one attempt, closed book/notes/IDE/neighbour/web, laptop only, pen + paper OK,
student ID, SSD via the Canvas Testing Accommodations link; its "45 minutes" is
unverified for F26 and it still names CodeWorkout and Labs. **Practice**: PrairieLearn
"Test #1 Practice" (set Practice Exams → PE1, module week05, 13 slots × 1-of-N
alternatives from 154 parametrized questions, 5×8 + 8×4 = 72 pts, `multipleInstance:
true`); the 13 banks group into five regions (objects & references · testing &
exceptions · types · bags on arrays · linked chains — W4D2 `04-test-map`). As of
2026-09-12 it is **untracked in `pl-vt-cs2114` with `allowAccess: []`** — check before
pointing a slide at it. W4D2 runs it openly (Part 2), then a fresh instance for 10
minutes through Canvas + LockDown Browser (Part 3).

**Projects**: EMRN rubric per deliverable, submitted via GitHub, TA grading sessions run
as oral exams; "apprenticeship-like" — no right answer, TAs give feedback, teams iterate.
**Project 1 "Learning to Scope"** = Java + Exceptions, **zero data structures**, teams of 3
(–4) formed in the Week 2 lab and posted on Canvas, Weeks 3–5 (Sep 7–25): D1 one-page
scope (W3 lab) → D2 spec (W4 lab) → D3 final build + writeup + 3-minute lightning talk
(W5 lab); JUnit tests, one normal + one bad-input case per key method; robust exception
handling; the full brief is the Canvas "Project 1 · Overview" page. **Project 2 "Bag +
Generics"** Weeks 6–8, teams re-form. Do not couple ADT/Bag vocabulary to P1.

**SSD / testing accommodations** (ssd.vt.edu, 2026-09-13): Services for Students with
Disabilities, 310 Lavery Hall, ssd@vt.edu, 540-231-3788. Two student actions per test:
the semester's **Course Accessibility Letter** requested in **AIM**
(elbert.accessiblelearning.com/VT; "accommodations are not retroactive"), and the seat
booked in **RegisterBlast** through the **Testing Accommodations link in the Canvas
course**, "at least three (3) business days in advance" (exam − 3 business days: Wed test
→ prior Fri, Thu test → prior Mon). Tests are taken at the Werth Testing Center (310
Lavery Hall). Instructor side: the RegisterBlast exam submission block ≥ 5 business days
before it starts, materials ≥ 2 business days before, or reservations are cancelled.
W4D1 `02b-ssd` / W4D2 `12b-ssd` is the slide; reuse it for Test 2 with new dates.

**Peer instruction** (every lecture): runs in **Runestone**, course
`virginiatech_peerplus_fall26`, assignment "Peer Instruction W0MDN" (W02D2, W03D1,
W04D1 confirmed; W03D2's name unverified), opened from the Canvas home page. Week 4 has
peer instruction on Day 1 only. Routine: silent
first answer → on the instructor's prompt discuss in groups of 3–4 → second answer →
go through it together, wrong answers included; credit for both rounds, not for being
right. Known Runestone source bugs still pending (need the instructor logged in): W03D1
Q1 missing `;` after `250`, Q2 `getFrequencyOf` missing `)`, Q3 no stem/class code.

**Coding practice**: PrairieLearn › Assessments › Coding Practice; W2 set = `x752`
(ageMath), `x754` (getOldest) walked, plus x753/x755/x804/x805/x798/x800 not walked;
W3 = X789 ArrayBag toString (spent on W3D1 slide 10 and duplicated on W3D2); W4 =
"Week 4: Linked Chains — Coding Practice", 19 problems best 5 (x680–x684 LinkedBag,
x729–x735 + x781–x788 chain walks), the graded homework — W4D1 `13-practice-map`.

**Tools** (W1D1 13-tools, amended): PrairieLearn (modules, homework, coding practice),
Canvas (home page, calendar, schedule, project overview pages), Runestone (peer
instruction), Piazza (Q&A — "turn instructor-post notifications on" is every deck's
last beat), GitHub (project code), Eclipse (IDE; CE 01 was the setup), **LockDown
Browser** (Respondus, installed from a Canvas link; wraps PrairieLearn for tests). **Web-CAT is
contested**: W1D1 said "automated grading for projects" (wrong for F26 — projects are
EMRN via GitHub); W2D2 carries an instructor-imported appendix (18-webcat-*) showing
Eclipse → Web-CAT submission for homework/CE, and a "Using WebCat for Challenge
Exercises" tab; the Week 3 decks draw no Web-CAT pill. Ask before drawing one.

**Dropped from the course** (never draw them): CodeWorkout, My Digital Hand, Lucidchart,
trial quizzes, "lab and postlab", Web-CAT as project grader, the
Fall 2025 Bag/ArrayBag Project 1, percentage grading.

**Sources** (outside the repo, `~/Downloads/`): `cs2114-schedule-fall2026.html`,
`cs2114-deadline-schedule.csv`, `CS2114_Projects_Fall2026(3).imscc` →
`wiki_content/project-1-overview.html`, `Class Planning(28).docx` (and later numbers),
`F25 Week N Day M*.pdf` legacy decks (W1D1, W1D2, W2D1, W2D2, W3D2 present as of
2026-09-12; W3D1's PDF/pptx are inside `week 3 -day 1/`), `S26 Week 1 Day 2.pptx`,
`Submitting Your Assignment - Web-CAT Guide.pptx`. Canvas gradebook CSVs also land there.

---

## 12. Translate, don't transcribe

A legacy F25/S26 deck is a source of **layouts, examples and question text**, never of
policies. Before authoring: diff every date, tool and policy in it against §11 and the
W1D1 `08-legacy-*` / `09-redesign-hints*` slides; record each translation in PLAN.md's
"Translated / dropped / unverified". Legacy screenshots of code get rendered natively in
an `.editor`.

**Vote and practice slides quote the question the room has open.** `.editor` code and
`.opts` text are quoted material — verify against the live Runestone/PrairieLearn text
(which outranks the F25 PDF), keep its quirks, and fix only the deck's own answer
slide, captions and notes. If the *source* is broken, the fix goes into the source with
the instructor's say-so; the slide stays clean.

---

## 13. The instructor's standing preferences (each learned the hard way)

- **Concrete over abstract**: named DO/DON'T examples, sized, not principle statements
  ("the scope sheet is not a pitch…" was replaced by "a text game with character
  classes and GenAI-made text files, not the next Skyrim"). "Don't give away the
  answer" protects graded artifacts only — calibration examples are wanted.
- Part titles must be true: "What does a test prove?" was "nonsense" (a passing test
  proves nothing) → "What does a passing test tell you?".
- Half-measures on a correction get rejected; be literal about what they asked.
- No fade-drift, no digit roll on replaced values (§8); GrowFromCenter must be invisible
  while tiny.
- Vote slides static, answer on the `b` slide, no in-place highlighting. Exception,
  decided 2026-09-12 for W4D2: an **ungraded recall** of an old vote may reveal its
  `.verdict` on step 1 of the same slide.
- No Playwright / screenshot passes; leave placeholders; they review in Slide Studio.
- Export to Google Slides / pptx, if asked: native editable objects, one output slide
  per reveal step, Chromium as the layout engine; the multi-MB pptx must be dragged
  into Drive by hand.
- Global: stay on task, simple robust solutions, no feature creep; be more questioning
  than agreeable; `git add -u` (plus explicit new dirs), never `-A`.

---

## 14. Before you stop

- [ ] PLAN.md exists with through-line, manifest table with plants, translated/dropped/unverified
- [ ] index.html `<title>` and manifest updated in the exact literal form
- [ ] every slide: unique `#slide-NN`, one `.slide__desc`, `aside.notes` (answers first), scoped `<style>`, reduced-motion block, tokens only
- [ ] vote text verbatim from the live source; answer slides end on `.verdict`/`.dbr`
- [ ] clock slides follow §11 (Sun modules blue, Fri HW/CE, lab-day project orange, "now" on the right day)
- [ ] `add_sids.py` on new slides → `lint.py` clean → `measure/run.sh` slack ≥ 30 everywhere
- [ ] `git status` checked for the instructor's concurrent edits; nothing of theirs overwritten
- [ ] unverified facts listed in the reply, not silently asserted
