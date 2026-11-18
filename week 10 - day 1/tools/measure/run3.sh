#!/bin/sh
# Three-engine headless layout sweep (no screenshots): Chromium, Firefox (Gecko),
# WebKitGTK MiniBrowser. Each engine loads measure3.html, which steps through
# every slide/step of the deck and POSTs its MEASURE_JSON back to this script's
# server. Prints the same per-slide report as run.sh, per engine, then a
# cross-engine diff.
#   tools/measure/run3.sh [deck-dir]
DECK="${1:-$(cd "$(dirname "$0")/../.." && pwd)}"
SELF_DIR=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d)
cp "$SELF_DIR/measure3.html" "$T/"
ln -s "$DECK" "$T/deck"
cd "$T" || exit 1

PORT=$(python3 -c "import socket; s=socket.socket(); s.bind(('127.0.0.1',0)); print(s.getsockname()[1]); s.close()")
python3 "$SELF_DIR/serve3.py" "$PORT" >/dev/null 2>&1 &
SRV_PID=$!
sleep 1

# wait_for_result ENGINE TIMEOUT_SECONDS
wait_for_result() {
  waited=0
  while [ ! -f "result-$1.json" ] && [ "$waited" -lt "$2" ]; do
    sleep 1; waited=$((waited + 1))
  done
  [ -f "result-$1.json" ]
}

run_chromium() {
  CHR=$(command -v chromium || command -v chromium-browser || command -v google-chrome || command -v google-chrome-stable)
  [ -n "$CHR" ] || { echo "SKIPPED chromium: no chromium/google-chrome binary found"; return; }
  "$CHR" --headless=new --disable-gpu --no-sandbox --hide-scrollbars --window-size=1920,1400 \
    "http://127.0.0.1:$PORT/measure3.html?engine=chromium" >/dev/null 2>&1 &
  PID=$!
  wait_for_result chromium 90 || echo "SKIPPED chromium: timed out waiting for POST"
  kill "$PID" 2>/dev/null
}

run_firefox() {
  FF=$(command -v firefox)
  [ -n "$FF" ] || { echo "SKIPPED firefox: no firefox binary found"; return; }
  PROFILE=$(mktemp -d)
  "$FF" -profile "$PROFILE" -no-remote --headless --width 1920 --height 1400 \
    "http://127.0.0.1:$PORT/measure3.html?engine=firefox" >/dev/null 2>&1 &
  PID=$!
  wait_for_result firefox 90 || echo "SKIPPED firefox: timed out waiting for POST"
  kill "$PID" 2>/dev/null
  rm -rf "$PROFILE"
}

run_webkit() {
  WK=/usr/lib/webkit2gtk-4.1/MiniBrowser
  [ -x "$WK" ] || { echo "SKIPPED webkit: MiniBrowser not found at $WK"; return; }
  command -v Xvfb >/dev/null 2>&1 || { echo "SKIPPED webkit: no display and Xvfb not available"; return; }
  # MiniBrowser has no --headless flag and its -g/--geometry is a documented
  # no-op, so it is run under a throwaway Xvfb sized to the window we want and
  # maximised with --full-screen. We start Xvfb ourselves (rather than via
  # xvfb-run) so we hold both PIDs directly and can kill them without a
  # pattern match: xvfb-run's own cleanup only fires after its child exits,
  # and a pkill pattern built from the measure URL is unreliable (the "?"
  # before the query string is a regex metacharacter, not a literal).
  DNUM=150
  while [ -f "/tmp/.X$DNUM-lock" ]; do DNUM=$((DNUM + 1)); done
  Xvfb ":$DNUM" -screen 0 1920x1400x24 -nolisten tcp -ac >/dev/null 2>&1 &
  XPID=$!
  sleep 2
  DISPLAY=":$DNUM" "$WK" --full-screen "http://127.0.0.1:$PORT/measure3.html?engine=webkit" >/dev/null 2>&1 &
  PID=$!
  # WebKitGTK's cold start under Xvfb is noticeably more variable than
  # Chromium/Firefox's, so it gets extra margin over the ~90s baseline.
  wait_for_result webkit 120 || echo "SKIPPED webkit: timed out waiting for POST"
  kill "$PID" 2>/dev/null
  kill "$XPID" 2>/dev/null
}

report() {  # report ENGINE -> prints the run.sh-style slice for one engine's result file
  python3 - "$1" <<'PY'
import json, sys
engine = sys.argv[1]
try:
    payload = json.load(open('result-%s.json' % engine))
except Exception as e:
    print('(no result for %s: %s)' % (engine, e)); sys.exit(0)
res = payload.get('results', [])
print('UA: %s' % payload.get('userAgent'))
print('CSS d supported: %s' % payload.get('cssDSupported'))
last = {r['slide']: r for r in res}
for r in res:
    flag = []
    if r['maxB'] > 984.5: flag.append('BOTTOM %d' % r['maxB'])
    if r['maxR'] > 1792.5: flag.append('RIGHT %d' % r['maxR'])
    if r['minL'] < 127.5: flag.append('LEFT %d' % r['minL'])
    if r['clipped']: flag.append('CLIPPED')
    if flag or r['step'] == last[r['slide']]['step']:
        print('%-28s step %d  slack %4d  right %4d  %s' % (r['file'], r['step'], 984 - r['maxB'], r['maxR'], ' '.join(flag)))
        for o in r['over'][:4]: print('      over:', o)
        for c in r['clipped'][:4]: print('      clip:', c)
PY
}

for engine in chromium firefox webkit; do
  echo "=== $engine ==="
  "run_$engine"
  [ -f "result-$engine.json" ] && report "$engine"
  echo
done

echo "=== cross-engine diff (last step of every slide) ==="
python3 - chromium firefox webkit <<'PY'
import json, sys
engines = sys.argv[1:]
data = {}
for e in engines:
    try:
        payload = json.load(open('result-%s.json' % e))
        last = {}
        for r in payload.get('results', []):
            last[r['slide']] = r
        data[e] = last
    except Exception:
        pass
if len(data) < 2:
    print('(need at least two engines with results to diff)')
else:
    slides = sorted(set().union(*[set(v.keys()) for v in data.values()]))
    for s in slides:
        slacks = {}
        file_name = None
        for e in engines:
            r = data.get(e, {}).get(s)
            if r:
                slacks[e] = 984 - r['maxB']
                file_name = r['file']
        if len(slacks) < 2:
            continue
        spread = max(slacks.values()) - min(slacks.values())
        overflow_engines = [e for e in engines if data.get(e, {}).get(s) and
                             (data[e][s]['maxB'] > 984.5 or data[e][s]['maxR'] > 1792.5 or data[e][s]['clipped'])]
        if spread > 8 or (overflow_engines and len(overflow_engines) < len(slacks)):
            tag = ' <-- DIFFERS' if spread > 8 else ''
            only = (' overflow only in: %s' % ','.join(overflow_engines)) if overflow_engines else ''
            print('%-28s slack %s%s%s' % (file_name, slacks, tag, only))
PY

kill "$SRV_PID" 2>/dev/null
# leave $T around only on request; clean up by default
RESULTS_DIR="$T"
echo
echo "(raw per-engine JSON left in $RESULTS_DIR)"
