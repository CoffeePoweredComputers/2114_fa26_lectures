# W3D1 — sizing audit and correction plan

> **Status — executed 2026-09-07.** All fixes below are applied and re-measured:
> 15 manifest slides, zero elements past the canvas or body, no clipped code lines,
> no slide-number collisions. Slack (body bottom minus lowest content): 06 = 81,
> 06b = 52, 07 = 88, 07b = 51, 08 = 88, 01b = 110, tips = 273; 02/03/05/17 fill the
> body by design. Two additions beyond the plan, found while fixing the bar:
> `.slide__kicker`, `.note`, `.slide__lede` and `.tile__label` lost to `.slide p` the
> same way, so every kicker rendered at 48px with a 24px margin — now 36px/16px as the
> tokens say, and every kicker slide's body grew by 25px. 06b keeps "Final value:
> found = false"; the row/notes margins stepped down one token instead. 08-walkthrough
> is out of the manifest; its file is renamed `slide-08w` and kept consistent.

Measured 2026-09-07 in headless Chromium at scale 1 (canvas 1920×1080, every slide
at its last step, transitions off). Same fontconfig as Slide Studio on this machine
(Verdana → Nimbus Sans, Georgia → Nimbus Roman, JetBrains Mono bundled), so the
numbers below are what Studio shows. Budget: body = 752px tall under a bare h2,
685px under kicker + h2 (the `slide--warmup` header is 174px). Body width 1664.

## Two root causes, both in css/deck.css

Almost every code slide is over because of these — fix them first, then re-measure
before touching any slide layout.

1. **The editor filename bar renders at 48px with a 24px bottom margin.** `.editor__bar`
   is a bare class (0,1,0); the type ramp `.slide p` is (0,1,1) and wins on both
   `font-size` and `margin`. Every bar is 113px tall instead of 58px. Fix: scope the
   rule as `.slide .editor__bar` (keep `margin: 0; font-size: var(--t-micro)`). This
   reclaims 55px per editor on 06, 06b, 07, 07b, 08, 08-walkthrough. The same bug is in
   W2D1's and W2D2's deck.css — not touched here; their code slides were laid out with
   the 113px bar, so fixing it there will move things.
2. **21px code gains no height.** `.editor__code li::before` (the gutter numeral) is
   pinned to `--t-micro` (28px) and inherits `line-height: 1.2`, so on the 07/08 slides
   every 21px line box is 33.6px, not 25.2px. The "token floor" trick was buying nothing.
   Fix inside the 21px variant: `li::before { font-size: inherit }`.

Also fix while there:

- `.slide .opts__code` (0,2,0) loses to `.slide .opts li p` (0,2,2) — option code never
  goes mono/28px. Rescope as `.slide .opts li .opts__code`.
- Replace the per-slide copies of "28px code + compact gutter" (06, 06b, 07b) and
  "21px code, lh 1.2, 8px padding, 32+16 gutter" (07, 08, 08-walkthrough) with two body
  modifiers in deck.css, one class per slide instead of a local `<style>` block each:
  - `.code-dense .editor__code { font-size: var(--t-micro) }` + gutter `width: var(--s-4); margin-right: var(--s-2)`
  - `.code-tag .editor__code { font-size: var(--t-tag); line-height: 1.2; padding: var(--s-1) var(--s-2) var(--s-1) 0 }` + gutter as above + `li::before { font-size: inherit }`

Component metrics after the fixes: editor = bar 58 + borders 6 + code padding 32 +
n×42 (dense) — or padding 16 + n×25.2 (tag).

## Studio drag residue — strip all of it

Every `style="…"` below is a hand-drag left by Slide Studio's resize box. None of
them should survive; the slide-local CSS carries geometry.

| file | element (data-sid) | inline style | effect today |
|---|---|---|---|
| 01-title | `01-title:5` h1 | `width/max-width: 1750px` | one-line title, 33px past the body each side |
| 02-course-info | `<section>` | `left: -3px` | whole slide shifted 3px left |
| 02-course-info | `:30` svg text | `position: absolute` | no-op |
| 05-peer-plus | `:7` svg | `left: 2px` | scene shifted 2px right |
| 06-vote-setup | `:6` body | `width: 1693px; flex: 0 0 498px` | body 29px past the right edge, 498px tall |
| 06-vote-setup | `:7 :8 :9 :10 :24 :26 :37` | heights, widths, −32px margin, font sizes | see slide 06 |
| 06b-walk-setup | `<section>` | `height: 1137px` | slide taller than the canvas |
| 06b-walk-setup | `:6 :41 :42 :43 :45 :47 :48 :50 :51` | heights, `#820f1e` `#8c0d0c` raw hex, width 825 | see slide 06b |
| 07b-walk-cases | `:8 :9 :10 :21 :33–:48` | 726/661px widths, −24px margin, 101×102 cells, `flex: 0 0 309px` | see slide 07b |

(`--i: n` custom properties on cells are legitimate stagger indices — keep those.)

## Per-slide findings

Content edges are measured; "slack" is body bottom (984) minus lowest content.

| # | slide | measured | verdict | fix |
|---|---|---|---|---|
| 1 | 01-title | h1 text 1729px wide on one line (x 95→1825); natural wrap = 2 lines, 1188 wide | fine visually; residue | keep one line, codify: `#slide-01 h1 { max-width: none }`, drop inline |
| 2 | 01b-today | content ends 874, 110 slack; drawings 360px, titles 48px | **OK** | none |
| 3 | 02-course-info | "Deliverable 1 · Scope, at your lab (Week 3)" end-anchored at x 722 runs to x = 0 (off canvas, over the stone edge); "Deliverable 2 …" runs to 1805 (13px past body) | **broken** | both sub-flags start-anchored at 1099 under "Project 1" (y 640, 672), shortened to `Deliverable 1 · Scope · Week 3 lab` / `Deliverable 2 · Spec · Week 4 lab` (571px wide → ends 1670); Deliverable 1's `data-step` 4→5 so it lands with the marker; strip section `left:-3px` |
| 4 | 02b-chapter-1 | — | **OK** | none |
| 5 | 03-vocabulary | tiles 572 tall in a 658 body, 86 slack at the bottom, icons 320 wide in 820 tiles | under-filled | fill the body: `#slide-03 .grid { height: 100%; grid-auto-rows: 1fr }`, `.dtile { justify-content: center }`, icon `max-width: 400px` |
| 6 | 04b-chapter-2 | — | **OK** | none |
| 7 | 05-peer-plus | clean except the 2px shift | residue | strip inline |
| 8 | 05-peer-plus-tips | content ends 676 of 984 (31% used); nested items render at **48px, larger than their 36px parents** (nested `ul` falls back to `.slide ul`), and inherit the checkbox marker | inverted hierarchy | slide-local: `.checklist { font-size: var(--t-body) }`; nested `ul { font-size: var(--t-small); padding-left: var(--s-6) }`; nested `li::before { content: none }`. Ends ≈ 760 |
| 9 | 06-vote-setup | second editor at y 898→1157: `boolean found = false;` is **entirely below the canvas**, `int searchedValue = 250;` half cut; options column ends at x 1882 | **broken** | see below |
| 10 | 06b-walk-setup | section 1137 tall; left editors clip 165/216px horizontally (`println` line and the array literal cut mid-word — 250 and 500 are not visible); right column ends 1224, takeaway over the slide number | **broken** | see below |
| 11 | 07-vote-cases | left editor 840 tall (ends 1139); options end 1558 — option D entirely off canvas | **broken** | shared fixes + strip the `public boolean contains…{` / `}` lines from each option (as 08-vote-branch already does). Result: left 609, right 583 |
| 12 | 07b-walk-cases | editor at x 104 clips 82px (`contents[i])) {` cut); takeaway ends 1233 | **broken** | see below |
| 13 | 08-vote-branch | left 1139, options end 1225 | **broken** | shared fixes alone → left 609, right 583 |
| 14 | 08-walkthrough | grid ends 1010, prompt row 1034→1106 | **broken**; third copy of the same question | drop from the manifest (see below). If kept: shared fixes alone → 650 |
| 15 | 17-next-class | — | **OK** | none |
| 16 | 99-closing | — | **OK** | none |

`10-peer-arrays-tracing.html` is not in the manifest — it is the un-hacked original of
06 (same content at 36px, 1012px tall). Delete it or leave it; it does not render.

## The complex ones — options and decisions

### 06 + 06b · vote 1 and its walkthrough

The constraint: `System.out.println("found " + searchedValue);` is 49 mono chars —
823px at 28px — so the code column must be ≥ 909 (compact gutter). Two stacked
editors (12 + 3 lines) are 806px tall even after the bar fix; they never fit in 685.

- **A. One merged editor (values first, then the loop), 16 lines.** 752px at lh 1.5;
  needs lh 1.3 and no blank line to reach 662. Tight, and the array literal (52 chars,
  1008px) forces a 1010px column, leaving 630 for the trace — eight cells don't fit.
- **B. Values move to the other column.** 06: values editor above the options on the
  right; 06b: values become a caption over the array row (the row *is* the array).
  Left column is the 12-line editor alone on both slides, same width, so the code does
  not jump between the vote and its answer.
- **C. 21px code like 07/08.** Fits trivially, but this is the simplest question and
  its answer walkthrough; the smallest legible size is the wrong place to spend it.

**Decision: B.** Both slides: `grid-template-columns: 920px minmax(0, 1fr)`,
`align-items: start`, body class `code-dense`. Left editor = 600px (85 slack).

06 right column (720 wide): values editor with the literal broken over two lines
(formatting only — flag it against Runestone):

    int[] values = { 3, 6, 10, 12,
        100, 200, 250, 500 };
    int searchedValue = 250;
    boolean found = false;

264px; then `.opts` with each answer in `<code>` (32px mono, semantically output),
no `margin-left`: 340px incl. D wrapping once. Total 620 (65 slack).

06b right column (720 wide), top to bottom:

1. caption `searchedValue = 250 · found = false`, 28px mono `--fg-1` — 57
2. array row: 8 cells 76×76, gap 12 (692 wide, 28 slack), digits 28px mono — 108
3. **the three notes stack in one grid cell** (`grid-area: 1 / 1`, current one visible,
   the `.walkcap` convention): step-2 hit, step-3 miss, step-4 result. The cell colours
   keep the history (blue hit at 250, maroon miss at 500), so nothing is lost when the
   250 note yields to the 500 note. Result box drops "Final value: found = false" (the
   miss flag already says it). Tallest = 172 — 204
4. takeaway, row 1 shortened to "The problem: the next non-match writes found back to
   false." (2 lines at 666 wide; the original is 3) — 278

Total 649 (36 slack). Rejected: both notes visible side by side (799, over by 114);
folding the result into the takeaway (738).

### 07b · vote 2 walkthrough

Widest code line `if (anEntry.equals(contents[i])) {` needs a 792px editor. Six
132px cells need 872 on the right. 800 + 32 + 832 = 1664, so cells go to 120
(800 wide, 32 slack). Editor = 516. The fix panel under the code needs 162
(two rows, `--s-3` padding): 516 + 24 + 162 = 702 — 17 over, and every padding
squeeze lands within 15px of the edge.

- **A. Shrink the callout text to 28px and move the panel to the right column.** Fits
  (right 489 + 24 + 146 = 659) but the fix sits away from the line it fixes and the
  exception line drops a size on the slide whose point it is.
- **B. Drop the editor's bar** ("option D — contains(T)" repeats the h2). Left becomes
  458 + 24 + panel, but the memory-rule sentence makes the panel 274–326 → still over.
- **C. Fix strip spans both columns.** Grid becomes editor | array with a third area
  underneath: one row `✗ i <= numberOfEntries   ✓ i < numberOfEntries` (923px wide,
  106 tall). Left ends 815, right ends 811, strip at 839→945 (39 slack). The memory
  rule ("n entries live at indexes 0 to n−1.", one line at 603px) moves into the
  caption slot, stacked with the step-2 miss note: note at steps 2–3, rule at step 4.
  Caption above the row shortens to `numberOfEntries = 5 → valid indexes 0 to 4`
  (one line); the miss note to `anEntry isn't in the Bag: 0 to 4 all miss.`

**Decision: C.** Nothing drops a size, the ring on the `while` line and the ✗/✓ pair
read as one gesture across the bottom, and the panel that could not fit under the
code was only ever the one sentence that already has a slot.

### 07 · 08-vote-branch · 08-walkthrough · the contains question, three times

Three slides carry the same four options. 07 and 08-vote-branch are the class code
(21 lines) beside the options; 08-walkthrough is a 2×2 of the options alone.

- **L1 (07 / 08-vote-branch)**: 44 lines of Java in 685px means ~22 per column →
  a 26px ceiling; 28px fails even with blank lines removed (718). So 21px stays, and
  after the two shared fixes it fits with 76/102 slack. B and C call `getIndexOf` /
  `getFrequencyOf`, so the class code has to be on the slide.
- **L2 (08-walkthrough)**: fits at 21px after the shared fixes (650), would fit at 28px
  only without the prompt row and blank lines (647) — but it has no class code, so B
  and C cannot be judged from it.

**Decision: L1.** 07 adopts 08-vote-branch's option bodies (no signature/brace —
the h2 already says `contains`), both take `code-tag`. Remove 08-walkthrough from the
manifest (its content is 08-vote-branch's, minus the class). Whether 07 and 08 are
really two different votes (C misspelled vs. not) is a content call, not sizing.

## Not sizing, but seen on the way

- Duplicate section ids: `slide-05` (05-peer-plus, 05-peer-plus-tips) and `slide-08`
  (08-vote-branch, 08-walkthrough). Slide-local `#slide-08 …` rules cross-apply.
  Rename to `slide-05t` / `slide-08w` (or drop 08-walkthrough).
- `data-anim="fade-up"` on 03's tiles and every 05-peer-plus-tips item (8 total), and
  `translateY(20px)` pending states on 06b's and 07b's cells — the drift entrances
  the decks avoid. Plain `fade` / grow instead.
- Raw hex on 06b `:47` (`#820f1e`, `#8c0d0c`) → `var(--accent-1)`.
- Copied-forward content: PLAN.md is W2D2's verbatim; 02's caption "Weeks 3, 3 and 4",
  "Challenge Exercise 03" in the bar vs "01" in the caption and 17; 02's notes point at a
  Web-CAT appendix (18-webcat-*) this deck does not have; 17 still says 3.1 Bags is due
  Monday; 05's plant says three questions "all on bags" while vote 1 is an array search;
  01b promises a Part 3 ("Using WebCat for Challenge Exercises") that has no divider or
  slides.

## Order of work

1. deck.css: `.slide .editor__bar`, `.slide .opts li .opts__code`, `.code-dense`,
   `.code-tag`. Re-measure — 07, 08-vote-branch, 08-walkthrough should already fit.
2. Strip every inline style in the table above; fix the duplicate ids.
3. 01, 02, 03, 05, tips: the one-line fixes.
4. 06 + 06b (decision B), 07b (decision C), 07 options.
5. Re-measure all 16 at every step; anything under 30px slack gets looked at again.
