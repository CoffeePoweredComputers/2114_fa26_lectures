"""Generate slides/16d-next-word.html from gpt2-medium.json + head.json.
Run from anywhere: python tools/next-token/gen16d.py  (no ML libraries needed —
the JSON inputs were produced by sweep.py / head.py with transformers + torch).
Every number in the slide (ids, embedding cells, attention widths, bar
lengths, probabilities) comes from those files. Geometry is computed here so
the chip row, vector columns, residual lines and arcs share one set of x's.
"""
import json, pathlib, html

SP = pathlib.Path(__file__).parent
M = json.load(open(SP / "gpt2-medium.json"))
HD = json.load(open(SP / "head.json"))
OUT = SP.parent.parent / "slides" / "16d-next-word.html"      # tools/next-token/ → the deck root

A = M["prompts"]["A"]; B = M["prompts"]["B1"]
LAYERS, DIM, VOCAB, HEADS = M["layers"], M["dim"], M["vocab"], M["heads"]
NHEADS = LAYERS * HEADS
topA, topB = HD["A"]["top5"], HD["B"]["top5"]
wA, wB = HD["A"]["head_w"], HD["B"]["head_w"]          # layer 18 head 7, last query
POKER = HD["poker"]
assert topB[0][0] == " poker"
# With context in front, "I" is tokenised as " I" (id 314, not 40): a different
# token with a different embedding. The chip morphs at step 6 — real, and shown.

# ------------------------------------------------------------------ sids
_n = [0]
def sid():
    _n[0] += 1
    return f'data-sid="16d-next-word:{_n[0]}"'

# ------------------------------------------------------------------ geometry (canvas px; viewBox = body rect)
BX, BY, BW, BH = 128, 300, 1664, 684
X0, GAP, CH, PAD, MINW, NEXTW = 176, 14, 16.8, 28, 52, 130
CHIP_Y, CHIP_H = 300, 68
def disp(t): return ("·" + t[1:]) if t.startswith(" ") else t
def cw(t): return max(MINW, round(len(disp(t)) * CH + PAD))

chips = []          # dicts: tok, x, w, cx, id, emb, grp ('B'|'A')
x = X0
for t, i, e in zip(B["tokens"][:4], B["ids"][:4], B["emb8"][:4]):
    w = cw(t); chips.append(dict(tok=t, x=x, w=w, cx=x + w / 2, id=i, emb=e, grp="B", alt=None)); x += w + GAP
AX0 = x
for k, (t, i, e) in enumerate(zip(A["tokens"], A["ids"], A["emb8"])):
    bt, bi, be = B["tokens"][4 + k], B["ids"][4 + k], B["emb8"][4 + k]
    alt = None if bt == t else dict(tok=bt, id=bi, emb=be)
    w = max(cw(t), cw(bt))
    chips.append(dict(tok=t, x=x, w=w, cx=x + w / 2, id=i, emb=e, grp="A", alt=alt)); x += w + GAP
AX1 = x - GAP
NX = x; NCX = NX + NEXTW / 2
BLK_X0, BLK_X1 = X0, 1140
VEC_Y, CELL_W, CELL_H, CELL_G = 430, 26, 14, 2
VEC_H = 8 * CELL_H + 7 * CELL_G
BLK_Y0, BAND, BLK_Y1 = 590, 680, 770
ARC_Y = 652
PANEL_X0, PANEL_X1 = 1206, 1792
BAR_X0, BAR_W = 1220, 560
ROW0, ROWH = 366, 62
PMAX = max(p for _, p in topA + topB)
def barw(p): return round(BAR_W * p / PMAX)

# ------------------------------------------------------------------ pieces
def esc(s): return html.escape(s, quote=False)
def tokbody(t):
    d = disp(t)
    return (f'<tspan class="nt__sp">·</tspan>{esc(d[1:])}' if d.startswith("·") else esc(d))
def chip(c, step, i, extra=""):
    """a token chip: rect + token text (dot = leading space) + id. A chip whose
    token changes once context is in front carries both readings (vA / vB)."""
    alt = c.get("alt")
    va = " nt__vA" if alt else ""
    inner = (f'<text class="nt__tok{va}" x="{c["cx"]:.0f}" y="{CHIP_Y + 30}">{tokbody(c["tok"])}</text>'
             f'<text class="nt__id{va}" x="{c["cx"]:.0f}" y="{CHIP_Y + 58}">{c["id"]}</text>')
    if alt:
        inner += (f'<text class="nt__tok nt__vB" x="{c["cx"]:.0f}" y="{CHIP_Y + 30}">{tokbody(alt["tok"])}</text>'
                  f'<text class="nt__id nt__vB" x="{c["cx"]:.0f}" y="{CHIP_Y + 58}">{alt["id"]}</text>')
    return (f'<g class="nt__chip{extra} frag" data-step="{step}" style="--i: {i}" {sid()}>'
            f'<rect x="{c["x"]}" y="{CHIP_Y}" width="{c["w"]}" height="{CHIP_H}" rx="10"/>{inner}</g>')
def cell_color(v):
    op = 0.12 + 0.88 * min(1.0, abs(v) / 0.2)
    return ("nt__c--pos" if v >= 0 else "nt__c--neg"), round(op, 2)
def vec(cx, emb, step, i, extra=""):
    cells = ""
    for r, v in enumerate(emb):
        cls, op = cell_color(v)
        cells += (f'<rect class="{cls}" x="{cx - CELL_W / 2:.0f}" y="{VEC_Y + r * (CELL_H + CELL_G)}" '
                  f'width="{CELL_W}" height="{CELL_H}" rx="2" opacity="{op}"/>')
    return f'<g class="nt__vec frag{extra}" data-step="{step}" style="--i: {i}" {sid()}>{cells}</g>'
def resid(cx, step, i, cls="nt__res"):
    return (f'<line class="{cls} frag" data-step="{step}" style="--i: {i}" pathLength="100" '
            f'x1="{cx:.0f}" y1="{VEC_Y + VEC_H}" x2="{cx:.0f}" y2="{BLK_Y1}" {sid()}/>')
def arc(sx, tx, wa, wb, step, i, to):
    dist = sx - tx
    h = min(52, 16 + 0.05 * dist)
    mx = (sx + tx) / 2
    d = f"M{sx:.0f} {ARC_Y} Q{mx:.0f} {ARC_Y - h:.0f} {tx:.0f} {ARC_Y}"
    return (f'<g class="nt__att frag" data-step="{step}" style="--i: {i}; --wa: {wa:.1f}px; --wb: {wb:.1f}px" {sid()}>'
            f'<path class="nt__arc" pathLength="100" d="{d}"/>'
            f'<circle class="nt__dot" cx="{tx:.0f}" cy="{ARC_Y}" r="5"/></g>')
def width(w): return 2 + 14 * w

# ------------------------------------------------------------------ svg body
S = []
add = S.append
play = chips[-1]; src = play["cx"]

# step 0: the whole prompt as one chip, and the empty slot for the next token
add(f'<!-- step 0: the prompt as text, and the slot the machine will fill -->')
add(f'<g class="nt__whole frag" data-step="1" {sid()}>'
    f'<rect x="{AX0}" y="{CHIP_Y}" width="{AX1 - AX0}" height="{CHIP_H}" rx="10"/>'
    f'<text class="nt__tok" x="{(AX0 + AX1) / 2:.0f}" y="{CHIP_Y + 43}">{esc(A["text"])}</text></g>')
add(f'<g class="nt__slot" {sid()}><rect x="{NX}" y="{CHIP_Y}" width="{NEXTW}" height="{CHIP_H}" rx="10"/>'
    f'<text class="nt__id nt__slotcap frag" data-step="7" x="{NCX:.0f}" y="{CHIP_Y + 43}">next?</text></g>')

# step 1: tokenize
add('<!-- step 1: the sentence becomes four tokens, each with its id -->')
for i, c in enumerate([c for c in chips if c["grp"] == "A"]): add(chip(c, 1, i))

# step 2: embed
add('<!-- step 2: each token becomes a column of numbers (first 8 of ' + str(DIM) + ' drawn, real values) -->')
for i, c in enumerate([c for c in chips if c["grp"] == "A"]): add(vec(c["cx"], c["emb"], 2, i, " nt__vA" if c["alt"] else ""))

# step 4: the stack behind (drawn first so it sits behind the front block)
add('<!-- step 4: the other layers, behind -->')
for k in (3, 2, 1):
    add(f'<rect class="nt__layer frag" data-step="4" style="--i: {k}" x="{BLK_X0 + 12 * k}" y="{BLK_Y0 + 12 * k}" '
        f'width="{BLK_X1 - BLK_X0}" height="{BLK_Y1 - BLK_Y0}" rx="12" opacity="{1 - 0.22 * k:.2f}" {sid()}/>')
add(f'<text class="nt__id nt__count frag" data-step="4" x="{BLK_X1 + 36}" y="{BLK_Y1 + 68}" {sid()}>&times;{LAYERS} layers</text>')

# step 3: one transformer block, the residual streams into it, and one head's attention
add('<!-- step 3: one block; each column runs down into it; one attention head, drawn -->')
add(f'<g class="nt__block frag" data-step="3" {sid()}>'
    f'<rect class="nt__layer nt__layer--front" style="--i: 0" x="{BLK_X0}" y="{BLK_Y0}" width="{BLK_X1 - BLK_X0}" height="{BLK_Y1 - BLK_Y0}" rx="12"/>'
    f'<line class="nt__band" x1="{BLK_X0}" y1="{BAND}" x2="{BLK_X1}" y2="{BAND}"/>'
    f'<text class="nt__lab" x="{BLK_X0 + 20}" y="{BAND - 10}">attention</text>'
    f'<text class="nt__lab" x="{BLK_X0 + 20}" y="{BLK_Y1 - 10}">feed-forward</text></g>')
for i, c in enumerate([c for c in chips if c["grp"] == "A"]): add(resid(c["cx"], 3, i))
for i, c in enumerate([c for c in chips if c["grp"] == "A"][:-1]):
    add(arc(src, c["cx"], width(wA[i]), width(wB[4 + i]), 3, i, c["tok"]))

# step 5: the last column's output goes to the vocabulary
add('<!-- step 5: the last position leaves the stack and is scored against every token -->')
add(f'<path class="nt__exit frag" data-step="5" pathLength="100" '
    f'd="M{src:.0f} {BLK_Y1} V{BLK_Y1 + 50} C{src:.0f} {BLK_Y1 + 120} {PANEL_X0 - 120} 500 {PANEL_X0 - 8} 500" {sid()}/>')
add(f'<path class="nt__exithead frag" data-step="5" d="M{PANEL_X0} 500 L{PANEL_X0 - 22} 490 L{PANEL_X0 - 22} 510 Z" {sid()}/>')
add(f'<rect class="nt__panel" x="{PANEL_X0}" y="{BY}" width="{PANEL_X1 - PANEL_X0}" height="412" rx="12" {sid()}/>')
add(f'<text class="nt__id nt__phead frag" data-step="5" x="{BAR_X0}" y="{BY + 26}" {sid()}>the next token, ranked</text>')
for k in range(5):
    y = ROW0 + ROWH * k
    a, b = topA[k], topB[k]
    add(f'<g class="nt__row" style="--i: {k}; --a: {a[1] / PMAX:.4f}; --b: {b[1] / PMAX:.4f}" {sid()}>'
        f'<rect class="nt__bar nt__bar--{k} frag" data-step="5" x="{BAR_X0}" y="{y + 10}" width="{BAR_W}" height="12" rx="6"/>'
        f'<text class="nt__tok nt__lbl nt__lblA frag" data-step="5" x="{BAR_X0}" y="{y}">{esc(disp(a[0]))}</text>'
        f'<text class="nt__id nt__prob nt__lblA frag" data-step="5" x="{PANEL_X1 - 14}" y="{y}">{a[1]:.3f}</text>'
        f'<text class="nt__tok nt__lbl nt__lblB nt__lblB--{k} frag" data-step="6" x="{BAR_X0}" y="{y}">{esc(disp(b[0]))}</text>'
        f'<text class="nt__id nt__prob nt__lblB frag" data-step="6" x="{PANEL_X1 - 14}" y="{y}">{b[1]:.3f}</text></g>')
add(f'<text class="nt__id nt__more frag" data-step="5" x="{BAR_X0}" y="{ROW0 + ROWH * 5 + 14}">&hellip; and {VOCAB - 5:,} more, all scored, all summing to 1</text>'.replace('frag" data-step="5"', f'frag" data-step="5" {sid()}', 1))

# step 6: four more words in front — same weights
add('<!-- step 6: context arrives in FRONT (causal: the model can only look back) -->')
add(f'<g class="nt__ctx frag" data-step="6" {sid()}></g>')   # state sentinel for :has()
for i, c in enumerate([c for c in chips if c["grp"] == "B"]):
    add(chip(c, 6, i)); add(vec(c["cx"], c["emb"], 6, i)); add(resid(c["cx"], 6, i))
add('<!-- "I" is a different token once something precedes it: its column changes too -->')
for c in [c for c in chips if c["grp"] == "A" and c["alt"]]: add(vec(c["cx"], c["alt"]["emb"], 6, 4, " nt__vB"))
for i, c in enumerate([c for c in chips if c["grp"] == "B"]):
    add(arc(src, c["cx"], 0, width(wB[i]), 6, 3 - i, c["tok"]))

# step 7: pick one — it travels to the empty slot
add('<!-- step 7: the pick: the top token becomes the next chip -->')
y0 = ROW0 + 10 + 6
bx1 = BAR_X0 + barw(topB[0][1])
add(f'<g class="nt__pick frag" data-step="7" {sid()}>'
    f'<path class="nt__link" pathLength="100" d="M{bx1} {y0} C{bx1 - 160} {y0} {NX + NEXTW + 170} {CHIP_Y + 34} {NX + NEXTW + 8} {CHIP_Y + 34}"/>'
    f'<path class="nt__linkhead" d="M{NX + NEXTW} {CHIP_Y + 34} L{NX + NEXTW + 22} {CHIP_Y + 24} L{NX + NEXTW + 22} {CHIP_Y + 44} Z"/></g>')
pk = dict(tok=topB[0][0], x=NX, w=NEXTW, cx=NCX, id=POKER["ids"][0], emb=POKER["emb8"], grp="P")
add(chip(pk, 7, 0, " nt__chip--pick"))

# step 8: go again — the new token gets its column; the window
add('<!-- step 8: append it and go again; the window is all it can see -->')
add(f'<g class="nt__loop frag" data-step="8" {sid()}></g>')
add(vec(NCX, POKER["emb8"], 8, 0)); add(resid(NCX, 8, 0))
add(f'<path class="nt__win frag" data-step="8" pathLength="100" d="M{X0} {CHIP_Y + 84} v8 H{NX + NEXTW} v-8" {sid()}/>')
add(f'<text class="nt__id nt__wincap frag" data-step="8" x="{(X0 + NX + NEXTW) / 2:.0f}" y="{CHIP_Y + 114}">the context window &mdash; everything it can see</text>')

SVG = "\n      ".join(S)

# ------------------------------------------------------------------ captions / prose
caps = [
    (1, "Text becomes tokens &mdash; word pieces, each with a number. The dot is a space: it belongs to the token."),
    (2, f"Each token becomes a list of numbers &mdash; {DIM:,} of them in this model. Eight are drawn."),
    (3, f"Each position looks back at what came before it &mdash; never ahead. One of the model&rsquo;s {NHEADS} attention heads is drawn."),
    (4, f"{LAYERS} layers of that. Their numbers were set by reading a slice of the internet: what usually follows what."),
    (5, f"A score for every token in the vocabulary &mdash; {VOCAB:,} of them. Softmax turns the scores into probabilities."),
    (6, "Same weights, four words in front &mdash; and I is now &middot;I, a different token. The head finds casino; the ranking changes."),
    (7, "Pick one. Usually a likely one &mdash; not always the top."),
    (8, "Append it. Go again: the next token, then the next. It only ever sees what is in this window."),
]
CAPS = "\n        ".join(f'<p class="nt__cap frag" data-step="{s}" {sid()}>{t}</p>' for s, t in caps)

desc = (
    "An animated diagram of a language model choosing one token. Along the top, the prompt, I like to play, sits in a chip with an empty slot after it. "
    "Step one splits the chip into four token chips, each with its number. Step two hangs a column of eight coloured cells under each token, a slice of its list of numbers. "
    "Step three draws one transformer block under the columns, runs each column down into it, and draws one attention head as arcs from the last token, play, back to the earlier ones, thicker where it looks harder: on this prompt it looks almost only at the first word. "
    "Step four stacks the other layers behind the block and sends a pulse up through them. Step five runs a line out of the last position into a panel on the right where five bars race out: "
    + ", ".join(f"{disp(t).lstrip(chr(183))} at {p:.3f}" for t, p in topA)
    + f", with a line noting the other {VOCAB - 5:,} tokens are scored too. "
    "Step six adds four chips in front of the prompt, At the casino comma; the I chip becomes space-I, number 314, a different token with a different column; and the same head swings from I to casino while the bars re-rank: "
    + ", ".join(f"{disp(t).lstrip(chr(183))} at {p:.3f}" for t, p in topB)
    + ". Step seven picks poker: its bar turns maroon and a line carries the word into the empty slot. Step eight hangs a column under the new token and draws a bracket under the whole row, the context window. "
    "Last, the drawing blurs and one line stands over it: it does not think, and it does not problem-solve."
)

notes = (
    "This is the mechanism slide and the demonstration in one; take it slowly, it is eight steps. Step 1: tokens, not words &mdash; the space is part of the token, which is why "
    "&ldquo; with&rdquo; and &ldquo;with&rdquo; are different tokens. Step 2: numbers, not meaning &mdash; 1,024 per token in this model; the colours are the real first eight. "
    "Step 3: attention looks BACK only; say that twice, because the previous version of this slide used a fill-in-the-blank model that reads both ways and that is not what an LLM is. "
    "The head drawn is layer 18, head 7 of 384; on a bare prompt it parks on the first word, which is a known quirk. Step 4: the numbers inside the layers came from training &mdash; "
    "this is 16c&rsquo;s second bullet: its predictions come from what it was trained on. Step 5: the top five of 50,257; the five shown sum to about 0.3, the rest of the mass is spread thin. "
    "Notice &ldquo;with&rdquo; at the top: it is not answering a question about you, it is continuing a sentence. Step 6 is the old slide&rsquo;s point, made honestly: context goes in FRONT, the same head "
    "swings to &ldquo;casino&rdquo;, and poker and cards appear from nowhere &mdash; nothing about the model changed, only the words in front of it. Small honest detail: &ldquo;I&rdquo; at the start of a text and "
    "&ldquo; I&rdquo; after a comma are different tokens (40 and 314), which is why that chip changes too. Step 7: it usually samples, so the same prompt can give a "
    "different answer tomorrow. Step 8: 16c&rsquo;s first and third bullets &mdash; it does this once per token, and it only sees the window: not your project, not last week&rsquo;s chat, not the constraint "
    "you gave it forty messages ago unless that text is still in front of it. Step 9 is the sentence they should leave with. Model: openai-community/gpt2-medium, 2019, 355 million parameters &mdash; "
    "ChatGPT&rsquo;s grandparent, small enough to run on a laptop; the models they use are this loop, a thousand times bigger, then tuned to be helpful. Every number on the slide is the model&rsquo;s own."
)

# ------------------------------------------------------------------ the slide
page = f'''<section class="slide" id="slide-16d" data-sid="16d-next-word:0">
  <header class="slide__head" {sid()}>
    <p class="slide__kicker" {sid()}>NEXT-TOKEN PREDICTION</p>
    <h2 {sid()}>How the next word gets picked</h2>
  </header>
  <p class="sr-only slide__desc" {sid()}>{desc}</p>

  <!-- The mechanism, drawn from a real model rather than described: tokens ->
       numbers -> one block with one attention head -> the stack -> a score for
       every token -> a pick -> the loop. Generated by tools/next-token/gen16d.py from
       openai-community/gpt2-medium: every id, cell colour, arc width and bar
       length is the model's own. Causal on purpose (the earlier version used a
       masked model, which reads both ways): the context in step 6 goes in FRONT
       of the prompt and the arcs only ever point back. One SVG in canvas px
       (viewBox = the body's rect); captions and the closing line are HTML so
       they wrap and blur. -->
  <div class="slide__body nt" {sid()}>
    <svg class="nt__svg" viewBox="{BX} {BY} {BW} {BH}" preserveAspectRatio="xMinYMin meet" role="img"
         aria-label="A language model drawn as tokens, columns of numbers, a stack of layers and a ranked list of next tokens"
         {sid()}>
      {SVG}
    </svg>
    <div class="nt__caps" {sid()}>
        {CAPS}
    </div>
    <p class="nt__cite" {sid()}>gpt2-medium (2019) &middot; layer 18, head 7 drawn &middot; every number is the model&rsquo;s own</p>
  </div>
  <div class="slide__number" {sid()}></div>

  <!-- step 9: the machine goes soft and the sentence is left -->
  <div class="nt__veil frag" data-step="9" {sid()}>
    <p class="nt__veil-card motto motto--tight" {sid()}>It does <b>not</b> think, and it does <b>not</b> problem-solve.<br><span class="nt__veil-sub">It ranks what usually comes next.</span></p>
  </div>

  <aside class="notes" {sid()}>{notes}</aside>

  <style>
    /* Slide-local: the next-token machine. Used by this slide only, all values
       from tokens; the SVG's viewBox is the body's rect so its units are canvas
       px, and the HTML caption rail and citation are positioned in the same px.

       Colour carries the reading: neutral ink for structure (chips, block,
       residual streams), the deck's wire blue for data in motion (attention
       arcs, the exit line, the bars), orange for negative cell values against
       blue positives, and the heading maroon for the one token that gets
       picked. Three accents, no more.

       Motion is manim's only. Chips, cells and layers GrowFromCenter (pure
       scale, opacity resolving in the first beat); arcs, residual streams, the
       exit line, the pick's link and the window bracket Create by dashoffset;
       bars are a Transform of their own length (a bar's width IS its value, so
       re-ranking morphs it in place) and their labels crossfade; the layer
       pulse is one keyframe on fill rising deepest-first. Nothing drifts.

       State beyond step order — the re-rank, the attention swing, the pick, the
       dimming of the old run — is a :has() machine off four sentinel frags
       (.nt__ctx, .nt__pick, .nt__loop, .nt__veil), so scrubbing backwards
       undoes every one of them. */
    #slide-16d .nt {{ position: relative; }}
    #slide-16d .nt__svg {{ position: absolute; left: 0; top: 0; width: {BW}px; height: {BH}px; overflow: visible; }}

    /* --- chips --- */
    #slide-16d .nt__chip rect, #slide-16d .nt__whole rect {{ fill: var(--bg-1); stroke: var(--fg-1); stroke-width: 3; }}
    #slide-16d .nt__slot rect {{ fill: none; stroke: var(--stone); stroke-width: 3; stroke-dasharray: 8 7; transition: stroke .4s ease, stroke-dasharray .4s ease; }}
    #slide-16d .nt__tok {{ font-family: var(--font-mono); font-size: var(--t-micro); fill: var(--fg-0); text-anchor: middle; }}
    #slide-16d .nt__sp {{ fill: var(--stone); }}
    #slide-16d .nt__id {{ font-family: var(--font-mono); font-size: var(--t-tag); fill: var(--fg-1); text-anchor: middle; }}
    #slide-16d .nt__chip {{ transform-box: fill-box; transform-origin: 50% 50%; transition: opacity .2s ease, transform .45s var(--ease-smooth); }}
    #slide-16d .frag.nt__chip.is-pending {{ opacity: 0; transform: scale(0.3); }}
    #slide-16d .frag.nt__chip.is-current, #slide-16d .frag.nt__chip.is-past {{ transition-delay: calc(var(--i) * .08s); }}
    /* the un-tokenised prompt leaves as the tokens arrive */
    #slide-16d .nt__whole {{ transition: opacity .25s ease; }}
    #slide-16d .frag.nt__whole.is-pending {{ opacity: 1; }}
    #slide-16d .frag.nt__whole.is-current, #slide-16d .frag.nt__whole.is-past {{ opacity: 0; }}
    #slide-16d .nt__slotcap {{ fill: var(--stone); transition: opacity .25s ease; }}
    #slide-16d .frag.nt__slotcap.is-pending {{ opacity: 1; }}
    #slide-16d .frag.nt__slotcap.is-current, #slide-16d .frag.nt__slotcap.is-past {{ opacity: 0; }}
    #slide-16d .nt__chip--pick rect {{ stroke: var(--accent-1); }}
    #slide-16d .nt__chip--pick .nt__tok {{ fill: var(--accent-1); font-weight: 700; }}
    #slide-16d .frag.nt__chip--pick.is-current, #slide-16d .frag.nt__chip--pick.is-past {{ transition-delay: .45s; }}
    #slide-16d:has(.nt__pick:not(.is-pending)) .nt__slot rect {{ stroke: var(--accent-1); stroke-dasharray: 0 0; }}
    /* "I" → "·I" once something precedes it: the chip's two readings crossfade, and so do its columns */
    #slide-16d .nt__vA, #slide-16d .nt__vB {{ transition: opacity .3s ease; }}
    #slide-16d .nt__vB {{ opacity: 0; }}
    #slide-16d:has(.nt__ctx:not(.is-pending)) .nt__vA {{ opacity: 0; }}
    #slide-16d:has(.nt__ctx:not(.is-pending)) .nt__vB {{ opacity: 1; transition-delay: .3s; }}

    /* --- the numbers --- */
    #slide-16d .nt__c--pos {{ fill: var(--accent-2); }}
    #slide-16d .nt__c--neg {{ fill: var(--accent-3); }}
    #slide-16d .nt__vec {{ transform-box: fill-box; transform-origin: 50% 0; transition: opacity .2s ease, transform .4s var(--ease-smooth); }}
    #slide-16d .frag.nt__vec.is-pending {{ opacity: 0; transform: scale(0.2); }}
    #slide-16d .frag.nt__vec.is-current, #slide-16d .frag.nt__vec.is-past {{ transition-delay: calc(var(--i) * .08s); }}

    /* --- the block and the stack --- */
    #slide-16d .nt__layer {{ fill: var(--bg-1); stroke: var(--stone); stroke-width: 3; }}
    #slide-16d .nt__layer--front {{ stroke: var(--fg-1); }}
    #slide-16d .nt__band {{ stroke: var(--stone); stroke-width: 2; stroke-dasharray: 6 6; }}
    #slide-16d .nt__lab {{ font-family: var(--font-mono); font-size: var(--t-tag); fill: var(--fg-1); paint-order: stroke; stroke: var(--bg-1); stroke-width: 8px; }}
    #slide-16d .nt__block {{ transform-box: fill-box; transform-origin: 50% 50%; transition: opacity .2s ease, transform .5s var(--ease-smooth); }}
    #slide-16d .frag.nt__block.is-pending {{ opacity: 0; transform: scale(0.5); }}
    #slide-16d rect.nt__layer.frag {{ transform-box: fill-box; transform-origin: 50% 50%; transition: opacity .2s ease, transform .4s var(--ease-smooth); }}
    #slide-16d rect.frag.nt__layer.is-pending {{ opacity: 0; transform: scale(0.5); }}
    #slide-16d rect.frag.nt__layer.is-current, #slide-16d rect.frag.nt__layer.is-past {{ transition-delay: calc((3 - var(--i)) * .08s); }}
    #slide-16d .nt__count {{ text-anchor: end; transition: opacity .3s ease; }}
    #slide-16d .frag.nt__count.is-current, #slide-16d .frag.nt__count.is-past {{ transition-delay: .3s; }}
    /* the pulse: computation rising through the layers, deepest first; replays on re-entry */
    #slide-16d:has(rect.nt__layer.frag.is-current) .nt__layer {{ animation: nt-pulse .6s var(--ease-smooth) both; animation-delay: calc(.35s + (3 - var(--i)) * .14s); }}
    @keyframes nt-pulse {{
      0% {{ fill: var(--bg-1); }}
      45% {{ fill: color-mix(in srgb, var(--accent-3) 45%, var(--bg-1)); }}
      100% {{ fill: var(--bg-1); }}
    }}

    /* --- streams and attention --- */
    #slide-16d .nt__res {{ stroke: var(--stone); stroke-width: 2; opacity: .55; stroke-dasharray: 100; transition: stroke-dashoffset .45s var(--ease-smooth); }}
    #slide-16d .frag.nt__res.is-pending {{ opacity: .55; stroke-dashoffset: 100; }}
    #slide-16d .frag.nt__res.is-current, #slide-16d .frag.nt__res.is-past {{ transition-delay: calc(.2s + var(--i) * .06s); }}
    #slide-16d .nt__arc {{ fill: none; stroke: var(--accent-2); stroke-width: var(--wa); stroke-linecap: round; opacity: .9;
      stroke-dasharray: 100; transition: stroke-dashoffset .5s var(--ease-smooth), stroke-width .6s var(--ease-smooth), opacity .4s ease; }}
    #slide-16d .nt__dot {{ fill: var(--accent-2); transition: opacity .3s ease; }}
    #slide-16d .frag.nt__att.is-pending {{ opacity: 1; }}
    #slide-16d .nt__att.is-pending .nt__arc {{ stroke-dashoffset: 100; }}
    #slide-16d .nt__att.is-pending .nt__dot {{ opacity: 0; }}
    #slide-16d .nt__att.is-current .nt__arc, #slide-16d .nt__att.is-past .nt__arc {{ transition-delay: calc(.5s + var(--i) * .12s), 0s, 0s; }}
    #slide-16d .nt__att.is-current .nt__dot, #slide-16d .nt__att.is-past .nt__dot {{ transition-delay: calc(.9s + var(--i) * .12s); }}
    /* step 6: the same head, re-weighted by the new context */
    #slide-16d:has(.nt__ctx:not(.is-pending)) .nt__arc {{ stroke-width: var(--wb); }}
    /* step 8: that run is over */
    #slide-16d:has(.nt__loop:not(.is-pending)) .nt__arc, #slide-16d:has(.nt__loop:not(.is-pending)) .nt__dot {{ opacity: .22; }}

    /* --- the exit and the ranking --- */
    #slide-16d .nt__exit {{ fill: none; stroke: var(--accent-2); stroke-width: 4; stroke-linecap: round; stroke-dasharray: 100; transition: stroke-dashoffset .55s var(--ease-smooth); }}
    #slide-16d .frag.nt__exit.is-pending {{ opacity: 1; stroke-dashoffset: 100; }}
    #slide-16d .nt__exithead {{ fill: var(--accent-2); transition: opacity .2s ease; }}
    #slide-16d .frag.nt__exithead.is-current, #slide-16d .frag.nt__exithead.is-past {{ transition-delay: .5s; }}
    #slide-16d .nt__panel {{ fill: none; stroke: var(--stone); stroke-width: 3; }}
    #slide-16d .nt__phead, #slide-16d .nt__more {{ text-anchor: start; transition: opacity .3s ease; }}
    #slide-16d .frag.nt__phead.is-current, #slide-16d .frag.nt__phead.is-past {{ transition-delay: .5s; }}
    #slide-16d .frag.nt__more.is-current, #slide-16d .frag.nt__more.is-past {{ transition-delay: 1.1s; }}
    #slide-16d .nt__bar {{ fill: var(--accent-2); transform-box: fill-box; transform-origin: 0 50%; transform: scaleX(0);
      transition: transform .55s var(--ease-smooth), fill .3s ease, opacity .1s ease; }}
    #slide-16d .frag.nt__bar.is-pending {{ opacity: 1; transform: scaleX(0); }}
    #slide-16d .frag.nt__bar.is-current, #slide-16d .frag.nt__bar.is-past {{ transform: scaleX(var(--a)); transition-delay: calc(.55s + var(--i) * .08s); }}
    #slide-16d:has(.nt__ctx:not(.is-pending)) .frag.nt__bar.is-past {{ transform: scaleX(var(--b)); transition-delay: calc(.4s + var(--i) * .06s); }}
    #slide-16d .nt__lbl {{ text-anchor: start; }}
    #slide-16d .nt__prob {{ text-anchor: end; }}
    #slide-16d .nt__lblA, #slide-16d .nt__lblB {{ transition: opacity .3s ease, fill .3s ease; }}
    #slide-16d .frag.nt__lblA.is-current, #slide-16d .frag.nt__lblA.is-past {{ transition-delay: calc(.6s + var(--i) * .08s); }}
    #slide-16d:has(.nt__ctx:not(.is-pending)) .nt__lblA {{ opacity: 0; transition-delay: 0s; }}
    #slide-16d .frag.nt__lblB.is-current, #slide-16d .frag.nt__lblB.is-past {{ transition-delay: calc(.5s + var(--i) * .06s); }}
    /* step 7: the pick */
    #slide-16d:has(.nt__pick:not(.is-pending)) .nt__bar--0 {{ fill: var(--accent-1); }}
    #slide-16d:has(.nt__pick:not(.is-pending)) .nt__lblB--0 {{ fill: var(--accent-1); font-weight: 700; }}
    #slide-16d .nt__link {{ fill: none; stroke: var(--accent-1); stroke-width: 3; stroke-linecap: round; stroke-dasharray: 100; transition: stroke-dashoffset .5s var(--ease-smooth); }}
    #slide-16d .nt__linkhead {{ fill: var(--accent-1); transition: opacity .2s ease; }}
    #slide-16d .frag.nt__pick.is-pending {{ opacity: 1; }}
    #slide-16d .nt__pick.is-pending .nt__link {{ stroke-dashoffset: 100; }}
    #slide-16d .nt__pick.is-pending .nt__linkhead {{ opacity: 0; }}
    #slide-16d .nt__pick.is-current .nt__link, #slide-16d .nt__pick.is-past .nt__link {{ transition-delay: .3s; }}
    #slide-16d .nt__pick.is-current .nt__linkhead, #slide-16d .nt__pick.is-past .nt__linkhead {{ transition-delay: .75s; }}
    /* step 8: the window */
    #slide-16d .nt__win {{ fill: none; stroke: var(--fg-1); stroke-width: 3; stroke-linecap: round; stroke-dasharray: 100; transition: stroke-dashoffset .6s var(--ease-smooth); }}
    #slide-16d .frag.nt__win.is-pending {{ opacity: 1; stroke-dashoffset: 100; }}
    #slide-16d .frag.nt__win.is-current, #slide-16d .frag.nt__win.is-past {{ transition-delay: .4s; }}
    #slide-16d .nt__wincap {{ transition: opacity .3s ease; }}
    #slide-16d .frag.nt__wincap.is-current, #slide-16d .frag.nt__wincap.is-past {{ transition-delay: .9s; }}

    /* --- narration rail and citation (HTML, in the same canvas px) --- */
    #slide-16d .nt__caps {{ position: absolute; left: {PANEL_X0 - BX}px; top: {732 - BY}px; width: {PANEL_X1 - PANEL_X0}px; display: grid; align-content: start; }}
    #slide-16d .nt__cap {{ grid-area: 1 / 1; margin: 0; font-size: var(--t-small); line-height: 1.35; color: var(--fg-1); transition: opacity .4s ease; }}
    #slide-16d .frag.nt__cap.is-pending, #slide-16d .frag.nt__cap.is-past {{ opacity: 0; }}
    #slide-16d .nt__cite {{ position: absolute; left: {X0 - BX}px; bottom: 0; margin: 0; font-family: var(--font-mono); font-size: var(--t-tag); line-height: 1.3; color: var(--stone); }}

    /* --- step 9: the sentence --- */
    #slide-16d .slide__head, #slide-16d .slide__body {{ transition: filter .6s var(--ease-smooth); }}
    #slide-16d:has(.nt__veil:not(.is-pending)) .slide__head,
    #slide-16d:has(.nt__veil:not(.is-pending)) .slide__body {{ filter: blur(var(--s-2)); }}
    #slide-16d .nt__veil {{
      position: absolute; inset: 0; padding: 0 240px;
      display: flex; align-items: center; justify-content: center;
      background: color-mix(in srgb, color-mix(in srgb, var(--bg-0) 80%, var(--fg-0)) 70%, transparent);
      transition: opacity .5s ease;
    }}
    #slide-16d .nt__veil-card {{
      padding: var(--s-4) var(--s-6);
      background: var(--paper); border-radius: var(--r-3);
      text-align: center;
    }}
    #slide-16d .nt__veil-sub {{ display: inline-block; margin-top: var(--s-3); font-size: var(--t-h3); color: var(--fg-1); }}

    @media (prefers-reduced-motion: reduce) {{
      #slide-16d .nt__chip, #slide-16d .nt__whole, #slide-16d .nt__slotcap, #slide-16d .nt__vec, #slide-16d .nt__block,
      #slide-16d rect.nt__layer, #slide-16d .nt__count, #slide-16d .nt__res, #slide-16d .nt__arc, #slide-16d .nt__dot,
      #slide-16d .nt__exit, #slide-16d .nt__exithead, #slide-16d .nt__phead, #slide-16d .nt__more, #slide-16d .nt__bar,
      #slide-16d .nt__lblA, #slide-16d .nt__lblB, #slide-16d .nt__link, #slide-16d .nt__linkhead, #slide-16d .nt__win,
      #slide-16d .nt__wincap, #slide-16d .nt__cap, #slide-16d .nt__veil, #slide-16d .nt__slot rect,
      #slide-16d .slide__head, #slide-16d .slide__body {{ transition-duration: 0s !important; transition-delay: 0s !important; }}
      #slide-16d .nt__layer {{ animation: none !important; }}
    }}
  </style>
</section>
'''
OUT.write_text(page)
print(f"wrote {OUT} ({page.count(chr(10))} lines, {_n[0]} sids)")
print("chips:", [(c['tok'], c['x'], c['w']) for c in chips], "next", NX)
print("bars A:", [(t, barw(p)) for t, p in topA]); print("bars B:", [(t, barw(p)) for t, p in topB])
