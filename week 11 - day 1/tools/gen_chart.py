#!/usr/bin/env python3
"""Generate slides/09-test2-graph.html from the Canvas item-analysis CSV.

    python3 tools/gen_chart.py "~/Downloads/10.06 Test #2 Quiz and Item Analysis Report.csv" \
        > slides/09-test2-graph.html
    python3 tools/add_sids.py slides/09-test2-graph.html

The output carries no data-sid attributes; run add_sids.py after every
regeneration. Never hand-edit the coordinates in the slide: change this script
and regenerate.

What it does: reads the Canvas "Quiz and Item Analysis Report" (one row per
item; only the Title, Correct and Incorrect columns are read, never
AnswerFrequencies, which holds the item text), strips each Title to its bank
(the variant letter removed), groups the items by bank, computes per bank the
student-weighted percent correct 100 * sum(correct) / sum(correct + incorrect)
and the lowest and highest per-variant percent, maps each bank to its Test #2
Practice slot, topic and short label (BANKS below), orders the topics by mean
score (lowest first) and the rows within a topic lowest first, and writes the
slide in the W6D1 04-test1-graph grammar. The per-bank table it used is
printed to stderr.

Standard library only.
"""
import argparse
import csv
import html
import os
import re
import sys

# bank -> (practice slot, topic, short label). The slot comes from the
# "comment" field of each question in
# pl-vt-cs2114/courseInstances/Fall2026/assessments/practiceExams/test2/infoAssessment.json
# ("slot N, CS2114_uNNqMM_..."), which names the Canvas bank of that test
# position. Topic membership is the W10D1 04-test-map grouping. Labels from the
# W11D1 research report section 2b (two shortened: "bag contains", "bag remove").
BANKS = {
    'unit11q01':                                ( 1, 'ADTs and tests',          'name the ADT'),
    'unit10q09':                                ( 2, 'Queues and deques',       'circular queue indices'),
    'unit09q04':                                ( 3, 'Recursion',               'count recursive calls'),
    'unit08q04':                                ( 4, 'Linked chains and lists', 'traversal loop count'),
    'unit08q03':                                ( 5, 'Linked chains and lists', 'chain after relinking'),
    'unit08q08':                                ( 6, 'Bags on arrays',          'bag operation cost'),
    'unit08q10':                                ( 7, 'Stacks',                  'array stack cost'),
    'unit07q02':                                ( 8, 'ADTs and tests',          'covering test'),
    'unit09q03':                                ( 9, 'Recursion',               'recursive print order'),
    'unit08q09':                                (10, 'Stacks',                  'stack trace'),
    'unit10q06':                                (11, 'Queues and deques',       'deque trace'),
    'unit07q10':                                (12, 'Bags on arrays',          'bag contains'),
    'unit07q11':                                (13, 'Bags on arrays',          'bag remove'),
    'unit11q05':                                (14, 'Linked chains and lists', 'SLL remove steps'),
    'CS2114_lab6arraystack_tostring_edgecase_1': (15, 'Stacks',                 'array stack toString'),
    'CS2114_lab8deque_removespecial_1':         (16, 'Queues and deques',       'deque remove, edge case'),
    'CS2114_lab8deque_adding_1':                (17, 'Queues and deques',       'deque add, edge case'),
    'CS2114_lab9debuglist_bugfind_1':           (18, 'Linked chains and lists', 'defective list method'),
    'CS2114_p2whackashape_arraybag_creation_1': (19, 'Bags on arrays',          'bag array capacity'),
}

# a topic name too wide for the 132..410 label column (x 132: Firefox counts the serif overhang at 128) is drawn on two lines
TOPIC_LINES = {
    'Queues and deques': ['Queues and', 'deques'],
    'Linked chains and lists': ['Linked chains', 'and lists'],
}

# ---- geometry (canvas px; viewBox = the warmup body under the h2) -----------
X0, XS = 860, 6                 # x = 860 + 6 * percent
HEAD_Y = 130                    # title + legend baseline (the h2 is sr-only; the body spans y 96-984)
T_FIRST = 150                   # top edge of the first row band
AXIS_Y = 920                    # axis line (tick labels at 950; the W6D1 chart had the axis at 920)
TICK_Y = AXIS_Y + 30            # tick-label baseline
GAP = 10                        # extra space between topics
RULE_X1, RULE_X2 = 420, 1784    # row rules (8 px inside the right body edge)
PILL_X, PILL_W, PILL_H = 1548, 232, 28
PILL_CX = PILL_X + PILL_W // 2


def bank_of(title):
    m = re.match(r'(unit\d\dq\d\d)[A-Z]', title)
    if m:
        return m.group(1)
    m = re.match(r'(CS2114_.*_\d+)[a-z]$', title)
    if m:
        return m.group(1)
    return None


def read_items(path):
    """Return (quiz stats dict, list of (title, correct, incorrect))."""
    stats, items = {}, []
    with open(path, newline='', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            if row.get('QuizMeanScore') and not stats:
                stats = {k: row[k] for k in ('QuizTitle', 'QuizMeanScore', 'QuizMedianScore')}
            title = (row.get('Title') or '').strip()
            if not title:
                continue
            items.append((title, int(row['Correct']), int(row['Incorrect'])))
    return stats, items


def pct(c, n):
    return 100.0 * c / n


def fmt(v):
    return '%d' % round(v)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('csv', help='Canvas Quiz and Item Analysis Report CSV')
    args = ap.parse_args()
    stats, items = read_items(os.path.expanduser(args.csv))

    groups = {}
    for title, c, i in items:
        b = bank_of(title)
        if b not in BANKS:
            sys.exit('gen_chart: no bank mapping for item title %r (bank %r)' % (title, b))
        groups.setdefault(b, []).append((title, c, i))
    missing = set(BANKS) - set(groups)
    if missing:
        sys.exit('gen_chart: banks with no items in the CSV: %s' % ', '.join(sorted(missing)))

    rows = []
    for b, its in groups.items():
        slot, topic, label = BANKS[b]
        c = sum(x[1] for x in its)
        n = sum(x[1] + x[2] for x in its)
        vp = [pct(x[1], x[1] + x[2]) for x in its]
        rows.append(dict(bank=b, slot=slot, topic=topic, label=label, c=c, n=n,
                         mean=pct(c, n), lo=min(vp), hi=max(vp), k=len(its)))

    topics = {}
    for r in rows:
        topics.setdefault(r['topic'], []).append(r)
    tmean = {t: pct(sum(r['c'] for r in rs), sum(r['n'] for r in rs)) for t, rs in topics.items()}
    order = sorted(topics, key=lambda t: tmean[t])
    for t in order:
        topics[t].sort(key=lambda r: r['mean'])

    # pitch: every row and topic gap between T_FIRST and 8 px above the axis
    nrows, ntop = len(rows), len(order)
    pitch = (AXIS_Y - 8 - T_FIRST - GAP * (ntop - 1)) // nrows
    last_rule = T_FIRST + nrows * pitch + GAP * (ntop - 1)

    # ---- stderr: the table this run used --------------------------------
    err = sys.stderr
    err.write('%s: %d items, %d banks, quiz mean %s, median %s\n' % (
        stats.get('QuizTitle'), len(items), len(groups),
        '%.1f' % float(stats.get('QuizMeanScore', 'nan')), stats.get('QuizMedianScore')))
    err.write('%-4s %-24s %-22s %-42s %2s %5s %6s %6s %6s\n' % (
        'slot', 'topic', 'label', 'bank', 'k', 'n', 'mean', 'lo', 'hi'))
    for t in order:
        for r in topics[t]:
            err.write('%-4d %-24s %-22s %-42s %2d %5d %6.1f %6.1f %6.1f\n' % (
                r['slot'], t, r['label'], r['bank'], r['k'], r['n'], r['mean'], r['lo'], r['hi']))
        err.write('     topic mean %.1f\n' % tmean[t])
    err.write('pitch %d px, gap %d, last rule y %d, axis y %d\n' % (pitch, GAP, last_rule, AXIS_Y))

    # ---- the SVG groups -------------------------------------------------
    e = html.escape
    out = []
    top = T_FIRST
    for step, t in enumerate(order, 1):
        rs = topics[t]
        out.append('      <!-- step %d: %s (mean %.1f) -->' % (step, e(t), tmean[t]))
        out.append('      <g class="dg__grp frag" data-step="%d">' % step)
        c0 = top + pitch // 2
        lines = TOPIC_LINES.get(t, [t])
        ty = c0 + 12
        if len(lines) == 1:
            out.append('        <text class="dg__topic" x="132" y="%d">%s</text>' % (ty, e(t)))
        else:
            spans = ''.join('<tspan x="132" y="%d">%s</tspan>' % (ty + 36 * j, e(s)) for j, s in enumerate(lines))
            out.append('        <text class="dg__topic" x="132" y="%d">%s</text>' % (ty, spans))
        for i, r in enumerate(rs):
            c = top + pitch // 2
            rule = top + pitch
            parts = ['<text class="dg__q" x="420" y="%d">Q%d</text>' % (c + 9, r['slot']),
                     '<text class="dg__lbl" x="820" y="%d">%s</text>' % (c + 9, e(r['label']))]
            x1, x2 = round(X0 + XS * r['lo']), round(X0 + XS * r['hi'])
            if x2 > x1:
                parts.append('<line class="dg__wh" pathLength="100" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x1, c, x2, c))
                parts.append('<path class="dg__cap" d="M%d %dv14M%d %dv14"/>' % (x1, c - 7, x2, c - 7))
            parts.append('<circle class="dg__dot" cx="%d" cy="%d" r="9"/>' % (round(X0 + XS * r['mean']), c))
            parts.append('<rect class="dg__pill" x="%d" y="%d" width="%d" height="%d" rx="%d"/>' % (
                PILL_X, c - PILL_H // 2, PILL_W, PILL_H, PILL_H // 2))
            parts.append('<text class="dg__pt" x="%d" y="%d">practice Q%d</text>' % (PILL_CX, c + 7, r['slot']))
            end = ' dg__rule--end' if i == len(rs) - 1 else ''
            parts.append('<line class="dg__rule%s" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (end, RULE_X1, rule, RULE_X2, rule))
            out.append('        <g class="dg__row" style="--i: %d">%s</g>' % (i, ''.join(parts)))
            top += pitch
        out.append('      </g>')
        top += GAP
    svg_groups = '\n'.join(out)

    # ---- desc and notes ----------------------------------------------------
    desc_topics = []
    for t in order:
        bits = ['question %d %s %s percent' % (r['slot'], r['label'], fmt(r['mean'])) for r in topics[t]]
        desc_topics.append('%s, average %s percent: %s.' % (t, fmt(tmean[t]), '; '.join(bits)))
    desc = ('A chart of the nineteen Test 2 questions grouped into the six topics of the Test 2 map. '
            'Each row carries the question number, which is its number in Test #2 Practice, a short name, '
            'a dot at the question\'s average score on an axis from 0 to 100 percent with a whisker from its '
            'lowest-scoring to its highest-scoring variant, a rule under the row, and at the right a pill '
            'naming the same question in Test #2 Practice on PrairieLearn. Topics are ordered from the lowest '
            'average to the highest and arrive one per step. ' + ' '.join(desc_topics))

    qmean = float(stats.get('QuizMeanScore', 'nan'))
    qmed = stats.get('QuizMedianScore', '')
    try:
        qmed = '%g' % float(qmed)
    except ValueError:
        pass
    note_steps = []
    for step, t in enumerate(order, 1):
        rs = topics[t]
        low, high = rs[0], rs[-1]
        s = 'Step %d, %s: the topic average is %s%%' % (step, t.lower() if t != 'ADTs and tests' else 'ADTs and tests', fmt(tmean[t]))
        if len(rs) > 1:
            s += ', from %s%% for question %d, %s, to %s%% for question %d, %s.' % (
                fmt(low['mean']), low['slot'], low['label'], fmt(high['mean']), high['slot'], high['label'])
        else:
            s += '.'
        note_steps.append(s)
    notes = ('Test 2 by topic. The class average on Test 2 was %.1f%% and the median was %s%%. '
             'Each row is one question. The dot is its average score across the class, and the whisker runs '
             'from the lowest-scoring to the highest-scoring variant of that question, so a long whisker means '
             'the variant you were given made a difference. The number on each row is the question\'s number in '
             'Test #2 Practice on PrairieLearn, and the pill on the right names the same question there. '
             'Students missed different questions, so find the rows that apply to you. For each question you '
             'lost points on, work the practice question with that number. %s Next is the practice test.') % (qmean, qmed, ' '.join(note_steps))

    comment = ('''  <!-- GENERATED by tools/gen_chart.py from the Canvas item analysis of
       %(title)s (%(nitems)d items in %(nbanks)d banks, one bank per test position).
       Do not hand-edit: change the script and regenerate, then run add_sids.py.
       W6D1 04-test1-graph's chart with Test 2's data: rows grouped by the six
       topics of W10D1's test map, topics ordered by their student-weighted
       mean score, rows within a topic lowest first. The dot is the
       student-weighted percent correct of the position, the whisker runs from
       its lowest- to its highest-scoring variant. The row number is the Test
       #2 Practice slot (the practice mirrors the test one slot per position;
       the slot is named in each practice question's comment in
       practiceExams/test2/infoAssessment.json). Ink dots, blue pills, no
       good/bad colouring, no per-row numbers.
       Geometry: 19 rows at a %(pitch)d px pitch (W6D1 had 16 at 40). The h2 is
       sr-only and the title is drawn in the SVG's head line, so the body
       spans y 96-984 (W6D1 traded the kicker for row pitch; this trades the
       h2): 19 rows, five 10 px topic gaps and the heavier closing rules fit
       between y %(t0)d and the axis at y %(axis)d, last rule at y %(last)d.
       Every label is at --t-micro; "average score" sits on the axis line.
       step 0: axis, ticks, the column heads.  steps 1-%(ntop)d: one topic each,
       whiskers draw on, dots and pills grow, names fade in, staggered down
       the group. x = 860 + 6 x percent correct. -->''' % dict(
        title=e(stats.get('QuizTitle', 'Test 2')), nitems=len(items), nbanks=len(groups),
        pitch=pitch, t0=T_FIRST, axis=AXIS_Y, last=last_rule, ntop=ntop))

    ticks = ''.join('M%d %dv8' % (X0 + XS * p, AXIS_Y) for p in (0, 25, 50, 75, 100))
    tick_text = '\n'.join('      <text class="dg__tk" x="%d" y="%d">%s</text>' % (
        X0 + XS * p, TICK_Y, '100%' if p == 100 else p) for p in (0, 25, 50, 75, 100))

    page = '''<section class="slide slide--warmup" id="slide-09">
  <header class="slide__head">
    <h2 class="sr-only">Test 2 results: average score, and where to practice</h2>
  </header>
  <p class="sr-only slide__desc">%(desc)s</p>

%(comment)s
  <div class="slide__body">
    <svg class="dg" viewBox="128 96 1664 888" preserveAspectRatio="xMidYMax meet" role="img"
         aria-label="Nineteen Test 2 questions grouped by topic, each a dot at its average score with a whisker across its variants and a pill naming its practice question">
      <!-- step 0: the title line, the axis and the column heads -->
      <text class="dg__title" x="132" y="%(hy)d">Test 2 results</text>
      <text class="dg__head dg__head--end" x="1460" y="%(hy)d">whisker: lowest to highest variant</text>
      <text class="dg__head dg__head--pl" x="1780" y="%(hy)d">Test #2 Practice</text>
      <line class="dg__axis" x1="860" y1="%(ay)d" x2="1460" y2="%(ay)d"/>
      <path class="dg__tick" d="%(ticks)s"/>
      <text class="dg__head dg__head--axis" x="820" y="%(ty)d">average score</text>
%(tick_text)s

%(groups)s
    </svg>
  </div>
  <div class="slide__number"></div>
  <aside class="notes">%(notes)s</aside>

  <style>
    /* Slide-local: W6D1 04's dot-and-whisker chart laid out as a table, every
       label at the micro size (the Week 8 type floor): mono for the column
       heads, ticks, question numbers and pill text, the body face for the row
       names (right-aligned against the plot), display maroon at the small
       size for the topic names. Ink dots with muted whiskers; a hairline
       under every row, a heavier one closing each topic; practice pills in
       the tool blue. No good/bad colouring. Motion: whiskers Create
       (dashoffset), dots and pills GrowFromCenter, text FadeIn, staggered by
       --i within a topic. Used by this slide only, all values from tokens. */
    #slide-09 .slide__head { margin-bottom: 0; }   /* the h2 is sr-only: the body takes the header's 48 px too */
    #slide-09 .slide__body { position: relative; }
    #slide-09 .dg { position: absolute; inset: 0; width: 100%%; height: 100%%; overflow: visible; }

    #slide-09 .dg__title { font-family: var(--font-display); font-size: var(--t-h3); fill: var(--accent-1); text-anchor: start; }
    #slide-09 .dg__head { font-family: var(--font-mono); font-size: var(--t-micro); fill: var(--fg-1); text-anchor: start; }
    #slide-09 .dg__head--end { text-anchor: end; fill: var(--stone); }
    #slide-09 .dg__head--pl { text-anchor: end; fill: var(--accent-2); }
    #slide-09 .dg__head--axis { text-anchor: end; }
    #slide-09 .dg__axis, #slide-09 .dg__tick { fill: none; stroke: var(--stone); stroke-width: 3; stroke-linecap: round; }
    #slide-09 .dg__tk { font-family: var(--font-mono); font-size: var(--t-micro); fill: var(--fg-1); text-anchor: middle; }

    #slide-09 .dg__topic { font-family: var(--font-display); font-size: var(--t-small); fill: var(--accent-1); text-anchor: start; transition: opacity .3s ease; }
    #slide-09 .dg__q { font-family: var(--font-mono); font-size: var(--t-micro); fill: var(--fg-1); text-anchor: start; transition: opacity .3s ease; }
    #slide-09 .dg__lbl { font-family: var(--font-body); font-size: var(--t-micro); fill: var(--fg-0); text-anchor: end; transition: opacity .3s ease; }
    #slide-09 .dg__rule { stroke: var(--stone); stroke-width: 1.5; opacity: .4; transition: opacity .3s ease; }
    #slide-09 .dg__rule--end { stroke-width: 2.5; opacity: .9; }   /* the last row of a topic: the rule that closes the group */
    #slide-09 .dg__dot { fill: var(--fg-0); }
    #slide-09 .dg__wh { stroke: var(--fg-1); stroke-width: 4; stroke-linecap: round; opacity: .8; }
    #slide-09 .dg__cap { fill: none; stroke: var(--fg-1); stroke-width: 3; stroke-linecap: round; opacity: .8; }
    #slide-09 .dg__pill { fill: var(--bg-0); stroke: var(--accent-2); stroke-width: 2.5; }
    #slide-09 .dg__pt { font-family: var(--font-mono); font-size: var(--t-micro); fill: var(--accent-2); text-anchor: middle; }

    /* a topic group: the group itself never hides (its parts carry the motion) */
    #slide-09 .dg__grp { transition: none; }
    #slide-09 .frag.dg__grp.is-pending { opacity: 1; }
    #slide-09 .dg__wh { stroke-dasharray: 100; transition: stroke-dashoffset .45s var(--ease-smooth); transition-delay: calc(var(--i) * .1s); }
    #slide-09 .frag.dg__grp.is-pending .dg__wh { stroke-dashoffset: 100; transition-delay: 0s; }
    #slide-09 .dg__cap { transition: opacity .2s ease; transition-delay: calc(.4s + var(--i) * .1s); }
    #slide-09 .frag.dg__grp.is-pending .dg__cap { opacity: 0; transition-delay: 0s; }
    #slide-09 .dg__dot, #slide-09 .dg__pill, #slide-09 .dg__pt { transform-box: fill-box; transform-origin: 50%% 50%%; transition: opacity .2s ease, transform .45s var(--ease-smooth); transition-delay: calc(.3s + var(--i) * .1s); }
    #slide-09 .frag.dg__grp.is-pending .dg__dot, #slide-09 .frag.dg__grp.is-pending .dg__pill, #slide-09 .frag.dg__grp.is-pending .dg__pt { opacity: 0; transform: scale(0.3); transition-delay: 0s; }
    #slide-09 .dg__lbl, #slide-09 .dg__q, #slide-09 .dg__rule { transition-delay: calc(.15s + var(--i) * .1s); }
    #slide-09 .frag.dg__grp.is-pending .dg__lbl, #slide-09 .frag.dg__grp.is-pending .dg__q, #slide-09 .frag.dg__grp.is-pending .dg__topic { opacity: 0; transition-delay: 0s; }
    #slide-09 .frag.dg__grp.is-pending .dg__rule { opacity: 0; transition-delay: 0s; }

    @media (prefers-reduced-motion: reduce) {
      #slide-09 .dg__wh, #slide-09 .dg__cap, #slide-09 .dg__dot, #slide-09 .dg__pill, #slide-09 .dg__pt, #slide-09 .dg__lbl, #slide-09 .dg__q, #slide-09 .dg__rule, #slide-09 .dg__topic {
        transition-duration: 0s !important; transition-delay: 0s !important;
      }
    }
  </style>
</section>
''' % dict(desc=e(desc), comment=comment, hy=HEAD_Y, ay=AXIS_Y, ty=TICK_Y, ticks=ticks,
           tick_text=tick_text, groups=svg_groups, notes=e(notes, quote=False))
    sys.stdout.write(page)


if __name__ == '__main__':
    main()
