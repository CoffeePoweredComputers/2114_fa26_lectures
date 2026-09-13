"""Generate slides/13-hw-reads.html and slides/13b-hw-writes.html — the Week 4
homework as pointer moves, one picture per press. Edit the grammar here and
rerun (then tools/add_sids.py on both files); never hand-edit coordinates.
Usage: python3 tools/gen_hw_slides.py   (from the deck folder)"""
import os
NW, NH, PITCH, X0 = 160, 80, 190, 124          # box, box, node pitch, first node x
DIV = 90                                         # data | next divider offset
def node(x, y, val, cls='', nul=False, label='Node'):
    n = (f'<text class="hw__type" x="{x+4}" y="{y-8}">{label}</text>'
         f'<rect class="hw__box{(" "+cls) if cls else ""}" x="{x}" y="{y}" width="{NW}" height="{NH}" rx="8"/>'
         f'<path class="hw__div" d="M{x+DIV} {y}v{NH}"/>'
         f'<text class="hw__f" x="{x+8}" y="{y+22}">data</text><text class="hw__f" x="{x+DIV+8}" y="{y+22}">next</text>'
         f'<text class="hw__v" x="{x+DIV//2}" y="{y+62}">{val}</text>')
    if nul: n += f'<text class="hw__null" x="{x+DIV+(NW-DIV)//2}" y="{y+60}">null</text>'
    return n
def arr(x1, y1, x2, y2, cls='hw__arr', c1=None, c2=None, head='r'):
    c1 = c1 or (x1+(x2-x1)/3, y1); c2 = c2 or (x2-(x2-x1)/3, y2)
    heads = {'r': f'M{x2} {y2} L{x2-12} {y2-6} L{x2-12} {y2+6} Z', 'l': f'M{x2} {y2} L{x2+12} {y2-6} L{x2+12} {y2+6} Z',
             'd': f'M{x2} {y2} L{x2-6} {y2-12} L{x2+6} {y2-12} Z', 'u': f'M{x2} {y2} L{x2-6} {y2+12} L{x2+6} {y2+12} Z'}
    return f'<path class="{cls}" d="M{x1} {y1} C {c1[0]} {c1[1]}, {c2[0]} {c2[1]}, {x2} {y2}"/><path class="hw__ah" d="{heads[head]}"/>'
def link(x, y, cls='hw__arr'): return arr(x+NW, y+NH//2, x+PITCH, y+NH//2, cls)
def firstnode(y, x0=X0, cls='hw__arr'):
    return (f'<rect class="hw__pill hw__pill--first" x="0" y="{y+NH//2-20}" width="100" height="40" rx="6"/>'
            f'<text class="hw__pt" x="50" y="{y+NH//2+7}">firstNode</text>' + arr(100, y+NH//2, x0, y+NH//2, cls))
def pill(cx, y, name, w=90):
    return (f'<rect class="hw__pill" x="{cx-w//2}" y="{y}" width="{w}" height="36" rx="6"/><text class="hw__pt" x="{cx}" y="{y+25}">{name}</text>'
            f'<path class="hw__arr" d="M{cx} {y} C {cx} {y-6}, {cx} {y-12}, {cx} {y-18}"/><path class="hw__ah" d="M{cx} {y-20} L{cx-6} {y-8} L{cx+6} {y-8} Z"/>')
def ring(x, y, lab=None):
    r = f'<rect class="hw__ring" x="{x-6}" y="{y-6}" width="{NW+12}" height="{NH+12}" rx="12"/>'
    if lab: r += f'<text class="hw__lab" x="{x+NW/2}" y="{y-28}">{lab}</text>'
    return r
X = [X0 + i*PITCH for i in range(5)]
Y1, Y2 = 70, 250
PILLY = Y1 + NH + 20      # pills under the nodes
def chain(vals, y=Y1, xs=None, cls='hw__arr', last_null=True):
    xs = xs or X[:len(vals)]; s = ''
    for i,(x,v) in enumerate(zip(xs, vals)):
        s += node(x, y, v, nul=(last_null and i == len(vals)-1))
        if i < len(vals)-1: s += link(x, y, cls)
    return s
def pic(step, aria, body):
    return f'      <svg class="hw__pic frag" data-step="{step}" data-anim="fade" viewBox="0 0 1056 340" role="img" aria-label="{aria}">\n        {body}\n      </svg>'

# ---------- reads ----------
R = [
 pic(1, "A chain A B C D; curr on the last node, D, which is ringed",
     firstnode(Y1) + chain(list('ABCD')) + pill(X[3]+NW//2, PILLY, 'curr') + ring(X[3], Y1)),
 pic(2, "A chain A B C D; curr on C, and D, the node curr.getNext() refers to, is ringed",
     firstnode(Y1) + chain(list('ABCD')) + pill(X[2]+NW//2, PILLY, 'curr') + ring(X[3], Y1, 'curr.getNext()')),
 pic(3, "A chain A B A C with value A: the first match, node one, and the last match, node three, are ringed",
     firstnode(Y1) + chain(list('ABAC')) + ring(X[0], Y1, 'first') + ring(X[2], Y1, 'last') + f'<text class="hw__lab hw__lab--big" x="{X[3]+NW//2}" y="{PILLY+26}">value = A</text>'),
 pic(4, "A chain A B C D E; slow on C, fast on E",
     firstnode(Y1) + chain(list('ABCDE')) + pill(X[2]+NW//2, PILLY, 'slow') + pill(X[4]+NW//2, PILLY, 'fast') + ring(X[2], Y1, 'middle')),
]
# ---------- writes ----------
kx = (X[1] + X[2]) // 2 + 15
W = []
W.append(pic(1, "A chain A B C D; a new node K below, between B and C; orange arrows from B to K and from K to C; the old arrow from B to C dashed",
  firstnode(Y1) + node(X[0],Y1,'A') + link(X[0],Y1) + node(X[1],Y1,'B') + link(X[1],Y1,'hw__arr hw__arr--old') + node(X[2],Y1,'C') + link(X[2],Y1) + node(X[3],Y1,'D',nul=True)
  + node(kx, Y2, 'K')
  + arr(X[1]+NW, Y1+NH//2, kx+NW//2, Y2, 'hw__arr hw__arr--o', c1=(X[1]+NW+40, Y1+NH//2), c2=(kx+NW//2, Y2-60), head='d')
  + arr(kx+NW, Y2+NH//2, X[2]+NW//2, Y1+NH+4, 'hw__arr hw__arr--o', c1=(kx+NW+60, Y2+NH//2), c2=(X[2]+NW//2, Y1+NH+60), head='u')
  + f'<rect class="hw__pill" x="{kx-170}" y="{Y2+NH//2-18}" width="130" height="36" rx="6"/><text class="hw__pt" x="{kx-105}" y="{Y2+NH//2+7}">newNode</text>' + arr(kx-40, Y2+NH//2, kx, Y2+NH//2, 'hw__arr')
  + f'<rect class="hw__pill" x="{X[1]+NW//2-45}" y="6" width="90" height="36" rx="6"/><text class="hw__pt" x="{X[1]+NW//2}" y="31">node</text>' + arr(X[1]+NW//2, 42, X[1]+NW//2, Y1, 'hw__arr', head='d')))
W.append(pic(2, "A chain A B C D; an orange arrow from A over B to C; the old arrow from A to B dashed; B greyed and labelled unreachable",
  firstnode(Y1) + node(X[0],Y1,'A') + link(X[0],Y1,'hw__arr hw__arr--old') + node(X[1],Y1,'B','hw__box--gone') + link(X[1],Y1,'hw__arr hw__arr--gone') + node(X[2],Y1,'C') + link(X[2],Y1) + node(X[3],Y1,'D',nul=True)
  + arr(X[0]+NW, Y1+NH//2, X[2], Y1+NH//2, 'hw__arr hw__arr--o', c1=(X[0]+NW+60, Y1-70), c2=(X[2]-60, Y1-70))
  + f'<text class="hw__gone" x="{X[1]+NW//2}" y="{Y1+NH+40}">unreachable</text>'
  + pill(X[0]+NW//2, PILLY+20, 'prev') + pill(X[2]+NW//2, PILLY+20, 'curr.getNext()', w=190)))
sx = [X0+60, X0+60+PITCH, X0+60+2*PITCH]
W.append(pic(3, "A chain A B C D; a second chain X Y Z below; orange arrows from A down to X and from Z up to B; the old arrow from A to B dashed",
  firstnode(Y1) + node(X[0],Y1,'A') + link(X[0],Y1,'hw__arr hw__arr--old') + node(X[1],Y1,'B') + link(X[1],Y1) + node(X[2],Y1,'C') + link(X[2],Y1) + node(X[3],Y1,'D',nul=True)
  + chain(list('XYZ'), y=Y2, xs=sx, last_null=False)
  + arr(X[0]+NW, Y1+NH//2, sx[0]+NW//2, Y2, 'hw__arr hw__arr--o', c1=(X[0]+NW+30, Y1+NH//2), c2=(sx[0]+NW//2, Y2-50), head='d')
  + arr(sx[2]+NW, Y2+NH//2, X[1]+NW//2, Y1+NH+4, 'hw__arr hw__arr--o', c1=(sx[2]+NW+80, Y2+NH//2), c2=(X[1]+NW//2, Y1+NH+90), head='u')
  + f'<text class="hw__lab" x="{sx[0]+NW//2}" y="{Y2-26}">first2</text><text class="hw__lab" x="{sx[2]+NW//2}" y="{Y2-26}">last2</text>'
  + f'<rect class="hw__pill" x="{X[0]+NW//2-45}" y="6" width="90" height="36" rx="6"/><text class="hw__pt" x="{X[0]+NW//2}" y="31">node</text>' + arr(X[0]+NW//2, 42, X[0]+NW//2, Y1, 'hw__arr', head='d')))
# rotate: A B C D E with newHead = D -> D E A B C
body4 = firstnode(Y1, cls='hw__arr hw__arr--old')
for i,v in enumerate('ABCDE'):
    body4 += node(X[i], Y1, v, nul=(v=='C'))
    if i < 4: body4 += link(X[i], Y1, 'hw__arr hw__arr--old' if v=='C' else 'hw__arr')
body4 = body4.replace('class="hw__null" x', 'class="hw__null hw__null--o" x')
body4 += arr(X[4]+NW, Y1+NH//2, X[0], Y1+NH//2, 'hw__arr hw__arr--o', c1=(X[4]+NW+40, Y1+200), c2=(X[0]-40, Y1+200))       # E -> A, under
body4 += arr(100, Y1+NH//2, X[3]+NW//2, Y1, 'hw__arr hw__arr--o', c1=(100, Y1-60), c2=(X[3]+NW//2, Y1-60), head='d')      # firstNode -> D, over
body4 += pill(X[2]+NW//2, PILLY+40, 'prev') + pill(X[3]+NW//2, PILLY+40, 'newHead') + pill(X[4]+NW//2, PILLY+40, 'last')
W.append(pic(4, "A chain A B C D E with newHead D: an orange arrow from E back to A under the chain, an orange arrow from firstNode over the top to D, C's next now null, the old arrows from firstNode to A and from C to D dashed", body4))
body5 = firstnode(Y1, cls='hw__arr hw__arr--o') + node(X[0], Y1, 'dog', 'hw__box--new') + arr(X[0]+NW, Y1+NH//2, X[1], Y1+NH//2, 'hw__arr hw__arr--o')
body5 += node(X[1], Y1, 'ant') + link(X[1], Y1) + node(X[2], Y1, 'bee') + link(X[2], Y1) + node(X[3], Y1, 'cat', nul=True)
mid = (X0 + X[3] + NW) // 2
body5 += f'<text class="hw__lab hw__lab--big" x="{mid}" y="{PILLY+26}">numberOfEntries = 4</text><text class="hw__type" x="{mid}" y="{PILLY+62}" text-anchor="middle">toString(): "[dog,ant,bee,cat]"</text>'
W.append(pic(5, "A LinkedBag chain: firstNode points at a new node dog, whose orange arrow points at ant, then bee, then cat; numberOfEntries equals 4", body5))

INDEX = [("Walk to the end", "729 · 681"), ("Look one ahead", "730 · 734"), ("Match by value", "732 · 733"), ("Two pointers", "731 · 788"),
         ("Add after a node", "735"), ("Remove a node", "781 · 782"), ("Splice a chain in", "785 · 786 · 787"), ("Rotate, reverse", "783 · 784"), ("LinkedBag", "680 · 681 · 682 · 684")]
def index(active):
    return '\n'.join(f'      <li class="{"hw__i--on" if (i in active) else "hw__i--off"}"><b>{n}</b> <span>{p}</span></li>' for i,(n,p) in enumerate(INDEX, start=1))
READS_CAPS = '''        <p class="walkcap cap--1 frag" data-step="1">curr = firstNode; while (curr.getNext() != null) curr = curr.getNext(); &mdash; curr ends on the last node. Empty chain: firstNode is null, return null. toString is the same walk, building a String.</p>
        <p class="walkcap cap--2 frag" data-step="2">Look at curr.getNext() before moving: stop when its next is null (second-to-last) or its data equals the value (node before). Guard: while (curr != null &amp;&amp; curr.getNext() != null). One-node or empty chain: null.</p>
        <p class="walkcap cap--3 frag" data-step="3">curr.getData().equals(value): for the first match, return curr at once; for the last, remember it and keep walking to the end. No match: null.</p>
        <p class="walkcap cap--4 frag" data-step="4">slow moves one node, fast moves two, while (fast != null &amp;&amp; fast.getNext() != null). Middle: slow when the loop ends (A B C D: C). Loop: fast comes round and equals slow instead of reaching null.</p>'''
WRITES_CAPS = '''        <p class="walkcap cap--1 frag" data-step="1">newNode.setNext(node.getNext()); node.setNext(newNode); &mdash; in that order. node null: newNode.setNext(firstNode); firstNode = newNode. value null: unchanged. numberOfEntries++.</p>
        <p class="walkcap cap--2 frag" data-step="2">prev.setNext(curr.getNext()); nothing refers to the node any more. If the node is firstNode: firstNode = firstNode.getNext(). Not in the chain: unchanged. numberOfEntries--. removeAll: firstNode = null; numberOfEntries = 0.</p>
        <p class="walkcap cap--3 frag" data-step="3">Walk the other chain to last2, counting. last2.setNext(node.getNext()); node.setNext(first2). Concatenate: node is this chain&rsquo;s last node. This chain empty: firstNode = first2. Other empty: unchanged. numberOfEntries += nodes added.</p>
        <p class="walkcap cap--4 frag" data-step="4">Find prev (before newHead) and last first. prev null &mdash; newHead already first, or not in the chain: unchanged. Then last.setNext(firstNode); prev.setNext(null); firstNode = newHead. Reverse a prefix: cut after givenNode, reverse it with prev/curr/next, reattach the rest. Count unchanged.</p>
        <p class="walkcap cap--5 frag" data-step="5">LinkedBag: add puts the new node at the front (the add slide). toString is the walk from step 1. removeAll: firstNode = null; numberOfEntries = 0. addLikeASet: if (contains(entry)) return false; then add.</p>'''
def hilite(sid, steps, offset):
    return '\n'.join(f'    #slide-{sid} .hw:has(.cap--{k}.is-current) .hw__index li:nth-child({k+offset}), #slide-{sid} .hw:has(.cap--{k}.is-current) .hw__index li:nth-child({k+offset})::before {{ color: var(--accent-1); }}' for k in steps)
def slide(sid, h2, active, pics, caps, desc, notes, offset):
    return f'''<section class="slide" id="slide-{sid}">
  <header class="slide__head">
    <p class="slide__kicker">HOMEWORK &middot; WEEK 4</p>
    <h2>{h2}</h2>
    <p class="slide__lede">PrairieLearn &rsaquo; Assessments &rsaquo; Week 4: Linked Chains &mdash; Coding Practice &middot; best 5 &middot; Fri 11:59 PM</p>
  </header>
  <p class="sr-only slide__desc">{desc}</p>

  <!-- GENERATED by tools/gen_hw_slides.py — edit the grammar there and rerun.
       The nineteen homework problems are nine pointer moves; this slide and
       its pair show the moves, one picture per press, with the problem
       numbers on an index that stays on screen. Pictures are slide 5's Node
       boxes (the homework's class is Node with firstNode, not Runestone's
       Link and head) at 160 × 80 on a 190 px pitch in a 1056 × 340 box; on
       the writes slide the arrows a line moves are orange, the arrow it
       replaces is dashed stone, a node nothing refers to is stone. Each
       picture is static; the caption under it is the rule as code and the
       edge case the problem names. -->
  <div class="slide__body hw">
    <ol class="hw__index">
{index(active)}
    </ol>
    <div class="hw__right">
      <div class="hw__pics">
{pics}
      </div>
      <div class="codewalk">
        <div class="codewalk__caps">
{caps}
        </div>
      </div>
    </div>
  </div>
  <div class="slide__number"></div>
  <aside class="notes">{notes}</aside>

  <style>
    /* Slide-local: the index at 560 px on the left (one line per move, the
       numbers in stone at the tag size; the current move in the heading
       maroon, the other slide's moves dimmed), the pictures stacked in one
       cell on the right with the caption under them. Node boxes as on slide 5
       at 160 × 80 with room around the field names and values; pills are ink,
       firstNode blue; arrows blue, moved arrows orange, replaced arrows dashed
       stone. Pictures FadeIn one at a time (a past picture hides). The lede
       drops to the small size and the head's width cap is lifted so the
       signpost stays on one line. All values from tokens; used by this slide
       only. */
    #slide-{sid} .slide__head {{ max-width: none; }}
    #slide-{sid} .slide__lede {{ font-size: var(--t-small); max-width: none; }}
    #slide-{sid} .hw {{ display: grid; grid-template-columns: 560px minmax(0, 1fr); column-gap: var(--s-5); align-items: start; }}
    #slide-{sid} .hw__index {{ list-style: none; margin: 0; padding: 0; counter-reset: mv; }}
    #slide-{sid} .hw__index li {{ counter-increment: mv; margin: 0 0 var(--s-2); padding-left: var(--s-5); position: relative; font-family: var(--font-mono); font-size: var(--t-micro); line-height: 1.3; color: var(--fg-1); transition: color .3s ease; }}
    #slide-{sid} .hw__index li::before {{ content: counter(mv); position: absolute; left: 0; top: 0; width: var(--s-4); color: var(--fg-1); }}
    #slide-{sid} .hw__index li b {{ font-weight: 400; color: inherit; }}
    #slide-{sid} .hw__index li span {{ font-size: var(--t-tag); color: var(--stone); margin-left: var(--s-1); }}
    #slide-{sid} .hw__index li.hw__i--off, #slide-{sid} .hw__index li.hw__i--off::before {{ color: var(--stone); }}
    /* the current move on the index */
{hilite(sid, range(1, len(active)+1), offset)}
    #slide-{sid} .hw__right {{ display: grid; row-gap: var(--s-2); }}
    #slide-{sid} .hw__pics {{ display: grid; }}
    #slide-{sid} .hw__pic {{ grid-area: 1 / 1; display: block; width: 100%; height: 340px; overflow: visible; transition: opacity .3s ease; }}
    #slide-{sid} .frag.hw__pic.is-past {{ opacity: 0; }}
    #slide-{sid} .codewalk__caps {{ min-height: 160px; }}
    #slide-{sid} .codewalk .walkcap {{ font-size: var(--t-micro); }}

    #slide-{sid} .hw__pill {{ fill: var(--fg-0); }}
    #slide-{sid} .hw__pill--first {{ fill: var(--accent-2); }}
    #slide-{sid} .hw__pt {{ font-family: var(--font-mono); font-size: var(--t-tag); fill: var(--bg-0); text-anchor: middle; }}
    #slide-{sid} .hw__box {{ fill: var(--bg-1); stroke: var(--fg-1); stroke-width: 4; }}
    #slide-{sid} .hw__box--gone {{ stroke: var(--stone); fill: var(--bg-0); }}
    #slide-{sid} .hw__box--new {{ fill: color-mix(in srgb, var(--accent-3) 18%, var(--bg-1)); stroke: var(--accent-3); }}
    #slide-{sid} .hw__div {{ fill: none; stroke: var(--fg-1); stroke-width: 4; }}
    #slide-{sid} .hw__type, #slide-{sid} .hw__f {{ font-family: var(--font-mono); font-size: var(--t-tag); fill: var(--fg-1); }}
    #slide-{sid} .hw__v {{ font-family: var(--font-mono); font-size: var(--t-micro); fill: var(--fg-0); text-anchor: middle; }}
    #slide-{sid} .hw__null {{ font-family: var(--font-mono); font-size: var(--t-tag); fill: var(--stone); text-anchor: middle; }}
    #slide-{sid} .hw__null--o {{ fill: var(--accent-3); }}
    #slide-{sid} .hw__gone {{ font-family: var(--font-mono); font-size: var(--t-tag); fill: var(--stone); text-anchor: middle; }}
    #slide-{sid} .hw__arr {{ fill: none; stroke: var(--accent-2); stroke-width: 4; stroke-linecap: round; }}
    #slide-{sid} .hw__ah {{ fill: var(--accent-2); }}
    #slide-{sid} .hw__arr--o {{ stroke: var(--accent-3); stroke-width: 5; }}
    #slide-{sid} .hw__arr--o + .hw__ah {{ fill: var(--accent-3); }}
    #slide-{sid} .hw__arr--old {{ stroke: var(--stone); stroke-dasharray: 8 8; }}
    #slide-{sid} .hw__arr--old + .hw__ah {{ fill: var(--stone); }}
    #slide-{sid} .hw__arr--gone {{ stroke: var(--stone); }}
    #slide-{sid} .hw__arr--gone + .hw__ah {{ fill: var(--stone); }}
    #slide-{sid} .hw__ring {{ fill: none; stroke: var(--accent-2); stroke-width: 5; }}
    #slide-{sid} .hw__lab {{ font-family: var(--font-mono); font-size: var(--t-tag); fill: var(--accent-2); text-anchor: middle; }}
    #slide-{sid} .hw__lab--big {{ font-size: var(--t-micro); fill: var(--fg-0); }}
    @media (prefers-reduced-motion: reduce) {{
      #slide-{sid} .hw__pic, #slide-{sid} .hw__index li {{ transition-duration: 0s !important; transition-delay: 0s !important; }}
    }}
  </style>
</section>
'''
READS_DESC = "A signpost under the heading: PrairieLearn, Assessments, Week 4: Linked Chains, Coding Practice; best five count; Friday 11:59 PM. On the left, an index of nine moves with their problem numbers: walk to the end, look one ahead, match by value, two pointers, add after a node, remove a node, splice a chain in, rotate and reverse, LinkedBag; the last five are dimmed on this slide. On the right, one picture per step with a caption. Step one: a chain A B C D with curr on the last node, ringed. Step two: curr on C and D ringed as curr.getNext(). Step three: a chain A B A C with value A, the first and last matching nodes ringed. Step four: a chain A B C D E with slow on C and fast on E; C ringed as the middle."
READS_NOTES = "The homework is nineteen problems; the reads are four moves. Problem numbers are on the index; best five count, due Friday 11:59 PM. The class here is Node with firstNode &mdash; Runestone&rsquo;s questions say Link and head; same idea. Step 1: walk to the end &mdash; getLastNode (729), and toString (681) is the same walk building a String; check for an empty chain first. Step 2: look one ahead &mdash; second-to-last (730) stops when curr.getNext().getNext() is null; node before a value (734) stops when curr.getNext().getData() equals it; the guard is while (curr != null &amp;&amp; curr.getNext() != null). Step 3: match by value &mdash; first (732) returns at the first equals; last (733) remembers the latest match and keeps walking. Step 4: two pointers &mdash; middle (731): slow one step, fast two; when fast runs out, slow is the middle (closer to the back for even length); detect loop (788): the same two pointers, and a loop means fast meets slow. Next slide: the writes."
WRITES_DESC = "The same signpost and index; the first four moves are dimmed on this slide. One picture per step with a caption. Step one, add after a node: a new node K below the chain between B and C, orange arrows from B to K and from K to C, the old B to C arrow dashed. Step two, remove a node: an orange arrow from A over B to C, B greyed and labelled unreachable. Step three, splice a chain in: a second chain X Y Z below, orange arrows from A down to X and from Z up to B. Step four, rotate: a chain A B C D E with newHead D; an orange arrow from E back to A under the chain, firstNode&rsquo;s orange arrow over the top to D, and C&rsquo;s next now null. Step five, LinkedBag: firstNode points at a new node dog in front of ant, bee, cat; numberOfEntries equals 4."
WRITES_NOTES = "The writes are five moves; every one changes numberOfEntries except rotate and reverse, and the problems say so. Step 1: add after a node (735) &mdash; two assignments, in that order: newNode.setNext(node.getNext()) first, then node.setNext(newNode); swap them and the rest of the chain is lost. A null node means add at the front; a null value means do nothing. Step 2: remove a node (781, 782) &mdash; one assignment, prev.setNext(curr.getNext()); the node is unreachable. If the node is firstNode, move firstNode instead; if it is not in the chain, do nothing. removeAll (682) is firstNode = null and count zero. Step 3: splice a chain in (786, 787) &mdash; find the other chain&rsquo;s last node, count as you go; last2.setNext(node.getNext()) then node.setNext(first2). Concatenate (785) is the same with node = this chain&rsquo;s last node. Empty cases: this chain empty, firstNode = first2; other empty, nothing. Step 4: rotate (783) &mdash; the picture is A B C D E with newHead D; the problem&rsquo;s example is A to F with E. Find prev and last first; if prev is null (newHead is already first, or not in the chain) do nothing; otherwise last.setNext(firstNode), prev.setNext(null), firstNode = newHead. Partial reverse (784): cut after givenNode, reverse the front part with prev/curr/next, reattach the rest. Step 5: the LinkedBag four &mdash; add at the front is the add slide; toString is step 1&rsquo;s walk; removeAll is firstNode = null; addLikeASet is contains, then add. Pick five: one from each move you find hard."
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'slides')
open(os.path.join(out, '13-hw-reads.html'), 'w', encoding='utf-8').write(slide('13', 'Nineteen problems: the reads', {1,2,3,4}, '\n'.join(R), READS_CAPS, READS_DESC, READS_NOTES, 0))
open(os.path.join(out, '13b-hw-writes.html'), 'w', encoding='utf-8').write(slide('13b', 'Nineteen problems: the writes', {5,6,7,8,9}, '\n'.join(W), WRITES_CAPS, WRITES_DESC, WRITES_NOTES, 4))
print('generated 13-hw-reads.html, 13b-hw-writes.html')
