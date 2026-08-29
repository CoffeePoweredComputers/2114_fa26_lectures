# Week 2 Day 1 — review and finalization plan

Written 2026-08-29 after reading all 30 slides, `js/deck.js`, `js/code-walk.js`,
`css/deck.css`, `css/tokens.css`. Nothing has been edited yet; the deck was being
touched in another session minutes before this was written (01b, the four
dividers, 16c–16g at 00:02–00:03), so all edits below wait for a go-ahead.

## Verdict

The first three chapters are in good shape: every slide is drawn, the motion is
in vocabulary, the two walkthroughs run correctly end to end. Three things stop
the deck from being finished:

1. **It is not under version control.** `week 2 - day 1/` is entirely untracked
   (`git status` → `?? ./`). Thirty slides, ~3,900 lines, zero history, and
   Slide Studio rewrites files in place. Commit before any of the rework below
   (`git add "week 2 - day 1"` — `git add -u` does not pick up an untracked
   directory).
2. **The next-word slide (16d) demonstrates the wrong kind of model.** Its
   numbers come from `xlm-roberta-large`, a *masked* model: it fills a blank
   using the words on **both** sides. That is the only reason “in the afternoon”
   *after* the blank flips games → tennis. The model 16c describes (“predicts
   the next token, then the next one”) is causal — it sees only the words to the
   left and could not see “in the afternoon” at all. So the slide labelled NEXT
   WORD PREDICTION is showing fill-in-the-blank, and a sharp student can catch
   the contradiction with the previous slide. Any rebuild has to use a causal
   model and put the extra context **before** the blank.
3. **The LLM chapter is the odd one out.** Fifteen illustrated slides, then six
   bullet-list slides and one bar chart, in the longest chapter (9 slides),
   landing in the last ten minutes of the hour. It also repeats itself: 16h
   duplicates 16g (document your use / nothing on tests) and 16i (write from
   scratch / try it yourself first), and 16c's three bullets are the captions
   16d should be carrying.

## 1. Review findings, ranked

### Must fix

| # | Where | Finding |
|---|-------|---------|
| 1 | repo | Deck untracked; no commit to roll back to. |
| 2 | `16d-next-word` | Masked-LM numbers presented as next-word prediction (see Verdict 2). Kicker, title, prompts, numbers and footnote all change. |
| 3 | `02b`, `10b`, `13c` | `.slide__desc` says “part N of **3**”; the kicker says OF 4. Three a11y descriptions are wrong. (`15b` is right.) |
| 4 | `11-peer-plus` | The two `.lp__where` lines (Canvas → Peer Instruction W2D1 → PrairieLearn) were removed from the SVG — two blank lines remain under the comment and the `.lp__where` CSS is dead. The `.slide__desc` still describes them, the notes still say it. Nothing on screen now says where to vote. **Deliberate?** Either restore the two `<text>` lines or rewrite the desc. |

### Should fix

| # | Where | Finding |
|---|-------|---------|
| 5 | `16b`–`16i` | Chapter is text; duplicates itself; see §5. |
| 6 | `12b-walk-movie` | Fields inconsistent: `"Dune", sci-fi` (unlabelled) above `year = 2021` (labelled), while the vote slide's API tile lists `title, genre, year`. Draw three labelled fields. |
| 7 | `12b` | Step 1 grows an empty `Movie` box. `new Movie()` actually produces `title = null, genre = null, year = 0` — the same “default is null” fact 13b is built on. Showing the defaults at step 1 and replacing them at step 2 makes the two walkthroughs one lesson told twice. |
| 8 | `13b-walk-student` | The exception panel shows the pre-JDK-14 message. Eclipse on any current JDK prints `Cannot invoke "Student.setName(String)" because "myClass[0]" is null` — it **names the null reference**, i.e. it is the answer. The notes already say to read it aloud; the slide should show it. |
| 9 | `12b`, `13b` | Neither walkthrough returns to the vote. 09-tips told the room to strike each wrong answer and say why; the walkthroughs end at the console / the fix and the four options never come back on screen. |
| 10 | `13b` | The exception panel plain-fades in. It is the loudest event in the chapter; a stamp (grow from centre, opacity resolving early) is in vocabulary and reads as “this happened”. |
| 11 | memory | `data-roll="off"` does not exist in `code-walk.js` (the only roll opt-out is `.heap-obj__field--strike`). Corrected in memory; §4 adds the flag because item 7 needs it. |

### Fine — leave

- `js/*` and `css/deck.css` are byte-identical to day 2's. Good.
- Stale comments only: “three chapter tabs” in 02b/10b/13c; `deck.css` “three chapter dividers (03b, 08b, 13b)”; `.scan` “used by both vote slides” (unused here; shared file, leave).
- Open date questions (modules 3.x vs 2.1–2.4; when Project 1 starts) are still open and still neutral on screen. Fix `02` and `17` together when decided.

## 2. The pivot, in order of value

- **A.** Rebuild 16d as the animated, accurate next-token machine; fold 16c into it (§3).
- **B.** Sharpen the two walkthroughs (§4).
- **C.** Consolidate the LLM chapter — optional, instructor's call (§5).
- Plus the must-fixes (§1) first and the finalize checklist (§6) last.

## 3. Spec — 16d, “The next-token machine”

### What “accurate” means here (guardrails)

- **Causal.** Attention arcs go **backward only**. The extra context in the demo is prepended, never appended.
- **Tokens, not words.** Chips show the model's real tokens (GPT-2's BPE: `I`, ` like`, ` to`, ` play`) with their real IDs underneath.
- **A distribution over the whole vocabulary.** Show the top five *and say* “…of 50,257”. Their probabilities do not sum to 1 and the slide must not imply they do.
- **Softmax, then a pick.** “Usually a likely one — not always the top.” Never “the top one”.
- **Real numbers everywhere.** Embedding cells are the first 8 dims of the real embeddings; arc widths are real last-layer attention; bars are real probabilities; layer count is the real one (12 for `gpt2`). Cite model + prompt in the footnote, as now.
- **Not a perceptron.** No fully-connected-circles clip-art. The picture is embed → stack of transformer blocks (attention + feed-forward) → unembed + softmax.
- **Vocabulary of the captions:** ranks, scores, “what usually follows”. Never “understands”, “knows”, “decides”.
- Scale honesty: one caption may say Claude/ChatGPT are this loop, much bigger, then tuned — nothing more.

### Data (baked in as static numbers)

Scratchpad script, `transformers` + `torch` (torch 2.13 is installed; `transformers` is not — install into a venv in the scratchpad; `gpt2` weights ≈ 550 MB, the HF cache currently holds only `bert-base-cased` and `t5-base`, neither causal). Emit:

- token ids for prompt A and B;
- first 8 embedding dims per token (for the cell colours);
- last-layer attention from the last position, mean over heads (arc widths);
- top-5 next-token probabilities for A and for 3–4 candidate B's — pick the B with the clearest flip.

Prompt A: `I like to play`. Candidate B's (context **before** the blank): `In the afternoon, I like to play`, `On the piano, I like to play`, `After work, I like to play`. Expect function words (` with`, ` the`) near the top for `gpt2` — that is honest and usable (“it is not answering a question about you; it is continuing a sentence”). If `gpt2` is too degenerate to make the point, try `gpt2-medium` (1.4 GB) before anything larger.

### Composition (canvas 1920×1080; kicker + h2 head, body ≈ 1664×690, viewBox = body rect)

```
 ┌──── the machine (≈1040 wide) ─────────────────────────┐  ┌── the answer (≈580) ──┐
 │  [ I ][ like ][ to ][ play ][ · · · ]   ← token chips  │  │  ▇▇▇▇▇▇▇▇ with   0.xx │
 │    40    588    284    711              ← real ids     │  │  ▇▇▇▇▇    games  0.xx │
 │   ▒▒     ▒▒     ▒▒     ▒▒               ← 8-cell vecs  │  │  ▇▇▇      the    0.xx │
 │  ┌────────────────────────────────┐ ×12                │  │  ▇▇       a      0.xx │
 │  │ attention   ⟵⟵⟵ (arcs to play)│                    │  │  ▇        video  0.xx │
 │  │ feed-forward                   │  ← the stack       │  │  … 50,252 more        │
 │  └────────────────────────────────┘                    │  └───────────────────────┘
 │                        └──────────────────────────────►│   (from the LAST column only)
 │  ↺ pick one · append · go again                        │   caption rail (one line per step)
 └────────────────────────────────────────────────────────┘
```

Machine left, narration right — same split as the codewalks. The left panel needs room for 8 chips at the demo step (`In`, ` the`, ` afternoon`, `,`, ` I`, ` like`, ` to`, ` play` — 8 GPT-2 tokens), ≈ 110 px each at `--t-micro`.

### Steps

| step | what happens | caption (one line, `--t-small`) |
|------|--------------|----------------------------------|
| 0 | The prompt as one chip: `I like to play`, and a dotted empty chip after it. | — |
| 1 | **Tokenize.** The chip splits into four token chips (grow, staggered), ids grow under them. | Text becomes tokens — word pieces, each with a number. |
| 2 | **Embed.** Under each chip an 8-cell column grows (real values, coloured by sign/size). | Each token becomes a list of numbers — 768 of them in this model. |
| 3 | **Attend.** Inside the block, arcs draw from ` play` back to ` to`, ` like`, `I`, width ∝ weight. | Each position looks back at what came before it. Back only — never ahead. |
| 4 | **Stack.** The block multiplies to a stack “×12”; a pulse of colour rises through it. | Twelve layers of that. The numbers inside were set by reading a large slice of the internet — they encode what usually follows what. *(16c bullet 2)* |
| 5 | **Score.** A line draws from the top of the last column to the right; five bars race out with labels and probabilities; the “…50,252 more” line fades in. | A score for every token in the vocabulary — 50,257 of them. Softmax turns scores into probabilities. |
| 6 | **Pick.** The chosen bar takes the maroon edge; its word grows into the empty chip. | Pick one. Usually a likely one — not always the top. |
| 7 | **Loop.** An orange return arc draws from the new chip back to the start (11-peer-plus's closing arc). | Append it. Go again. That is the whole loop — the next token, then the next, then the next. *(16c bullet 1)* |
| 8 | **Same weights, more words.** Four chips grow in to the **left** of `I`; arcs redraw to include them; bars re-rank (widths morph, labels crossfade). A bracket under the row marks the window. | Same weights. Four more words in front — a different ranking. It only sees what is in the window. *(16c bullet 3 + the old 16d)* |
| 9 | **Payoff.** The machine dims; 16c's closing motto lands over it. | **It does not think, and it does not problem-solve.** It ranks what usually comes next. |

Nine steps — the same length as 12b. If step 8 crowds the drawing, split it: `16d2` is the same drawing in its end state with only step 8 (the deck already reuses one drawing twice: 02 / 17).

### Motion (manim vocabulary only — see memory `no-fade-drift-animations`)

- Chips, ids, cells: GrowFromCenter (pure scale, opacity resolving in the first 0.2 s), staggered by `--i`.
- Arcs, the score line, the loop arc: Create by `stroke-dashoffset` with `pathLength="100"`; arc widths are static attributes (real weights), not animated.
- The layer pulse: one `@keyframes` on `fill` rising through the stack, staggered per layer; plays once per step entry (slides are `display:none` until active, so it restarts on arrival, like `.sun-set`).
- Bars: `width` transition on the smootherstep — a bar's width *is* its value, so morphing it is a Transform, not drift. Labels and probabilities: two stacked sets, plain crossfade (the `.heap-val` stacking trick).
- The pick: a border-colour change + the word growing into the chip. No drift.
- Step 9: the machine group takes `filter: blur()` via `:has()` (07-the-deal's veil), the motto grows in.
- Reduced-motion block as on every other drawn slide; `html.no-motion` already kills everything.

### Implementation notes

- One inline SVG in canvas px, like 02/04/14; steps are `.frag` groups; the re-rank at step 8 is a `:has()` state machine off the step-8 frag (14's pill uses the same mechanism). **No JS.**
- Colour: `--fg-1` ink for structure; `--accent-2` for data in motion (arcs, bars — the deck's wire/reference blue); `--accent-3` for the loop arc (the thing that repeats); `--accent-1` for the chosen token. Three accents, no more.
- Slide-local `<style>`, all values from tokens, the prose comment explaining the choices — same shape as 14-equals-hints.
- New `.slide__desc`, new notes (fold 16c's note about “limited memory” into step 8's).
- 01b-today's chapter-4 drawing (prompt box over ranked bars) already matches the bars panel — no change.

## 4. Walkthrough fixes

### 12b-walk-movie

1. **Three labelled fields** in both objects: `title = "Dune"`, `genre = "sci-fi"`, `year = 2021`. Height: two objects × 3 lines ≈ 190 px each; heap ≈ 495 px + caps 110 — fits the 888 body.
2. **Defaults at step 1**: `title = null`, `genre = null`, `year = 0`, replaced at step 2 by plain crossfade (stacked `.heap-val--old` / `.heap-val` pairs). `year = 0 → 2021` must not roll — add `data-roll="off"` to `code-walk.js` (`build()` skips fields carrying it; four lines) and document it in the header comment. Three strikes at step 2 would be noise; crossfade is the right verb for “filled in”.
3. **Step 10 — the verdict strip** under the console: `A in 2021 · B in 1984 · C in 2024 · D in 1984, 2024`. A, C, D strike through in sequence (the `.heap-val__num::after` draw-on), B takes `--accent-1`. This is 09-tips' picture (tick one, strike three) done for real. Caption: “A assumed a copy. C assumed the last write reaches everything. D assumed the object remembers.” Left column budget: editor ≈ 440 + console ≈ 100 + strip ≈ 60 — fits.
4. Re-measure the heap run after the field change (memory: 210 px run, 722 of 763 with three pills).
5. Rewrite `.slide__desc` and notes.

### 13b-walk-student

1. **Helpful NPE message**, three lines at `--t-micro` (the current `--t-small` single line will not fit 763 px):
   ```
   java.lang.NullPointerException:
     Cannot invoke "Student.setName(String)"
     because "myClass[0]" is null
   ```
   Keep `at Main.main(Main.java:2)` as a fourth, dimmer line — the line number is part of the lesson.
2. The panel **stamps** in (scale 0.6 → 1 on `--ease-smooth`, opacity in the first 0.2 s) instead of fading.
3. **Step 5 — verdict strip**: `A won't compile · B NullPointerException · C Jordan · D none`. Caption: “It compiled — javac only sees the type. Nothing was ever printed.”
4. Rewrite desc and notes.

### Shared

- `.verdict` goes in `css/deck.css` (two slides use it → shared, per the deck's rule): a mono row, lettered, `--verdict-wrong` strikes drawn on by `--i` stagger, the right answer in `--accent-1`. Port to day 2's `deck.css` only if its walkthroughs adopt the strip; note the divergence in the file header until then.

## 5. LLM chapter consolidation (optional — instructor's call)

| slide | proposal |
|-------|----------|
| 16b | Keep. It is the chapter's thesis. |
| 16c | **Cut** — its three bullets become 16d's captions at steps 4, 7, 8; its opening motto becomes 16d's lede; its closing motto is 16d's step 9. |
| 16d | Rebuilt (§3). |
| 16e | Keep the three tiles. Optional: a two-weight-pen drawing per tile like 09-tips. Low value; skip unless time. |
| 16f | Draw it as a chat transcript — one question bubble, one answer bubble — so the joke (“we asked the chatbot”) is visible rather than explained by the kicker. Cheap. |
| 16g | Keep. |
| 16h | **Fold into 16i.** Four of its six lines are already on 16g or 16i. The two that are new — “understand and verify anything it hands you” and “the debugger and Python Tutor answer the same questions, about your actual code” — become 16i's last two steps. |
| 16i | Draw it as a cascade — you → the material → us → the LLM — in 14-equals-hints' grammar. The echo is deliberate: equals() asks four questions in order; so do you. |

Result: 9 slides → 7, one animated centrepiece, no repeated lines.

## 6. Finalize checklist

1. Commit the deck as it is now (“W2D1 deck, pre-review”).
2. §1 must-fixes 3 and 4, plus the two date questions if answered. Commit.
3. §4 walkthroughs + `data-roll="off"` + `.verdict`. Review in Slide Studio. Commit.
4. §3 numbers script → 16d rebuild → cut 16c from the manifest (leave the file until reviewed). Review. Commit.
5. §5 if approved. Commit.
6. Descs rewritten for every touched slide; `slide__desc` reads as a full description, not a caption list.
7. Manifest order re-checked; the on-screen `N / total` will shift by −1 or −2.

No Playwright passes; review is in Slide Studio (memory `no-playwright-verification`).

## 7. Decisions needed before starting

1. Commit now, before anything else? (Recommended — nothing here can be undone otherwise.)
2. 16c: fold into 16d (recommended), or keep it as a text slide in front of it?
3. The demo prompt: chosen from real `gpt2` output — veto if a specific sentence is wanted. Also: is `gpt2` (2019, 124 M parameters) acceptable as the cited model, given the caption will say “the big ones are this loop, bigger”?
4. Slide 11's centre text (Canvas → PrairieLearn): restore, or rewrite the desc to match its absence?
5. 16h: fold into 16i, or keep?
6. The two dates (modules; Project 1 start) — same as the standing open questions.

Effort, roughly: step 2 fifteen minutes; step 3 two hours; step 4 half a day (most of it the drawing); step 5 two hours.
