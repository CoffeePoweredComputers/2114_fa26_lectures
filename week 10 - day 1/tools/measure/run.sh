#!/bin/sh
# Headless layout sweep (no screenshots): every slide at every step, at scale 1.
#   tools/measure/run.sh [deck-dir]     → prints slack per slide, flags overflow/clipping
# Serves a temp dir holding measure.html + a symlink to the deck, drives the deck in an
# iframe, reads getBoundingClientRect() into the DOM, dumps it with chromium --dump-dom.
DECK="${1:-$(cd "$(dirname "$0")/../.." && pwd)}"
T=$(mktemp -d); cp "$(dirname "$0")/measure.html" "$T/"; ln -s "$DECK" "$T/deck"
cd "$T"; python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1 & PID=$!; sleep 1
CHR=$(command -v chromium || command -v chromium-browser || command -v google-chrome || command -v google-chrome-stable)
"$CHR" --headless=new --disable-gpu --no-sandbox --hide-scrollbars --window-size=1920,1400 --virtual-time-budget=40000 --dump-dom "http://127.0.0.1:8765/measure.html" 2>/dev/null | grep -o 'MEASURE_JSON .*' | sed 's/^MEASURE_JSON //' > result.json
kill $PID 2>/dev/null
python3 - <<'PY'
import json,html
res=json.loads(html.unescape(open('result.json').read().split('</pre>')[0]))
last={r['slide']:r for r in res}
for r in res:
    flag=[]
    if r['maxB']>984.5: flag.append('BOTTOM %d'%r['maxB'])
    if r['maxR']>1792.5: flag.append('RIGHT %d'%r['maxR'])
    if r['minL']<127.5: flag.append('LEFT %d'%r['minL'])
    if r['clipped']: flag.append('CLIPPED')
    if flag or r['step']==last[r['slide']]['step']:
        print('%-28s step %d  slack %4d  right %4d  %s'%(r['file'],r['step'],984-r['maxB'],r['maxR'],' '.join(flag)))
        for o in r['over'][:4]: print('      over:',o)
        for c in r['clipped'][:4]: print('      clip:',c)
PY
rm -rf "$T"
