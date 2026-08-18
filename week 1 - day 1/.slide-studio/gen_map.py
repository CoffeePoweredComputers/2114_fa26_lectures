#!/usr/bin/env python3
"""Generate the world-route map for the 2026 travel slide (02b-travel).

Same method as the itvest India slide: real Natural Earth boundary geometry
(johan/world.geo.json), projected equirectangular at a standard parallel, with
city pins projected through the SAME transform so nothing can drift relative
to the coastline.
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- projection ------------------------------------------------------------
LON_MIN, LON_MAX = -135.0, 180.0
LAT_MIN, LAT_MAX = -50.0, 64.0
COS = math.cos(math.radians(30.0))          # standard parallel 30N
W = 1664.0                                   # target map width in canvas px
K = W / ((LON_MAX - LON_MIN) * COS)
H = (LAT_MAX - LAT_MIN) * K

def proj(lon, lat):
    return ((lon - LON_MIN) * COS * K, (LAT_MAX - lat) * K)

# ---- cities ----------------------------------------------------------------
CITIES = {
    'bburg': (-80.42, 37.23),
    'bom':   (72.88, 19.08),
    'stl':   (-90.20, 38.63),
    'sd':    (-117.16, 32.72),
    'akl':   (174.77, -36.85),
    'mad':   (-3.70, 40.42),
    'gla':   (-4.25, 55.86),
    'edi':   (-3.19, 55.95),
    'pit':   (-79.99, 40.44),
    'cph':   (12.57, 55.68),
}
P = {k: proj(*v) for k, v in CITIES.items()}

# ---- route legs -------------------------------------------------------------
# (name, from, to, bow px [+ = rot90(d) side, - = other side], mode)
# perp = (-dy, dx)/|d|; screen y grows downward, so on an eastbound leg a
# NEGATIVE bow arcs north. Return flights RETRACE the outbound arc (see
# ITINERARY) so the visible map never shows near-parallel doubled lines;
# arcs sharing the Atlantic corridor get distinct apex bands for the same
# reason.
UNIQUE_LEGS = [
    ('A', 'bburg', 'bom',  -120, 'fly'),   # mid-Atlantic band, apex ~y160
    ('B', 'bom',   'stl',   230, 'fly'),   # home the long way; top band ~y115
    ('C', 'stl',   'bburg',  16, 'fly'),
    ('D', 'bburg', 'sd',    -38, 'fly'),
    ('E', 'bburg', 'akl',   255, 'fly'),   # the big southern sweep
    ('F', 'bburg', 'mad',   -40, 'fly'),   # low band ~y134
    ('G', 'mad',   'gla',   -22, 'fly'),
    ('H', 'gla',   'edi',     0, 'rail'),
    ('I', 'edi',   'bburg', 100, 'fly'),   # top band ~y60
    ('J', 'bburg', 'pit',    -7, 'road'),
    ('K', 'bburg', 'cph',   -60, 'fly'),   # mid band ~y78
]
BY_NAME = {n: (a, b, bow) for n, a, b, bow, _ in UNIQUE_LEGS}
# Full flight, in trip order; "-X" = leg X flown in reverse (a retrace).
ITINERARY = ['A', 'B', 'C', 'D', '-D', 'E', '-E', 'F', 'G', 'H', 'I',
             'J', '-J', 'K', '-K']
# Photos pop as the plane first arrives at each stop (= end of these legs).
PHOTO_STOPS = {'india': 'A', 'nz': 'E', 'madrid': 'F', 'edinburgh': 'H'}

def leg_pts(name):
    rev = name.startswith('-')
    a, b, bow = BY_NAME[name.lstrip('-')]
    ax, ay = P[a]; bx, by = P[b]
    dx, dy = bx - ax, by - ay
    L = math.hypot(dx, dy) or 1.0
    px_, py_ = -dy / L, dx / L
    cx, cy = (ax + bx) / 2 + px_ * bow, (ay + by) / 2 + py_ * bow
    cx = min(max(cx, 14), W - 14); cy = min(max(cy, 14), H - 14)
    return ((bx, by), (cx, cy), (ax, ay)) if rev else ((ax, ay), (cx, cy), (bx, by))

def q_cmd(name):
    _, (cx, cy), (bx, by) = leg_pts(name)
    return f'Q{cx:.1f},{cy:.1f} {bx:.1f},{by:.1f}'

def q_len(name, n=200):
    (ax, ay), (cx, cy), (bx, by) = leg_pts(name)
    pts = [(((1-t)**2)*ax + 2*(1-t)*t*cx + t*t*bx,
            ((1-t)**2)*ay + 2*(1-t)*t*cy + t*t*by)
           for t in (i/n for i in range(n+1))]
    return sum(math.hypot(pts[i+1][0]-pts[i][0], pts[i+1][1]-pts[i][1])
               for i in range(n))

# Visible dotted route: unique legs only, split into continuous runs.
runs = [['A', 'B', 'C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J'], ['K']]
parts = []
for run in runs:
    (sx, sy), _, _ = leg_pts(run[0])
    parts.append(f'M{sx:.1f},{sy:.1f} ' + ' '.join(q_cmd(n) for n in run))
ROUTE_D = ' '.join(parts)

# Plane + reveal-mask path: the full itinerary, retraces included (continuous).
(fx, fy), _, _ = leg_pts(ITINERARY[0])
FLIGHT_D = f'M{fx:.1f},{fy:.1f} ' + ' '.join(q_cmd(n) for n in ITINERARY)

# ---- timings ---------------------------------------------------------------
# The flight runs LINEAR so per-leg reveal windows and photo arrivals are
# plain distance fractions of the total duration.
lens = [q_len(n) for n in ITINERARY]
total = sum(lens)
FLIGHT_MS = 9500
arrivals = {}
for label, stop in PHOTO_STOPS.items():
    upto = sum(lens[:ITINERARY.index(stop) + 1])
    arrivals[label] = round(upto / total * FLIGHT_MS)

# Per unique leg: reveal delay = first time the plane starts that leg,
# duration = that leg's flight time.
leg_timing = {}
for n, _, _, _, _ in UNIQUE_LEGS:
    i = ITINERARY.index(n)
    leg_timing[n] = (round(sum(lens[:i]) / total * FLIGHT_MS),
                     round(lens[i] / total * FLIGHT_MS))

# Emit the per-leg SVG: one mask per leg (so a drawn leg can never uncover a
# crossing leg's dots) + the matching visible dotted path.
mask_frag, leg_frag = [], []
for n, _, _, _, _ in UNIQUE_LEGS:
    (ax, ay), _, _ = leg_pts(n)
    d = f'M{ax:.1f},{ay:.1f} ' + q_cmd(n)
    delay, dur = leg_timing[n]
    mask_frag.append(
        f'          <mask id="tr-m-{n}" maskUnits="userSpaceOnUse" x="0" y="0" width="1664" height="695">\n'
        f'            <path class="tr-rl" style="--d:{delay}ms; --t:{dur}ms" fill="none" stroke="white" stroke-width="10"\n'
        f'                  stroke-linecap="round" d="{d}"/>\n'
        f'          </mask>')
    leg_frag.append(f'          <path class="tr-leg" mask="url(#tr-m-{n})" d="{d}"/>')
with open(os.path.join(HERE, 'legs_frag.txt'), 'w') as f:
    f.write('\n'.join(mask_frag) + '\n===\n' + '\n'.join(leg_frag))

# ---- distances -------------------------------------------------------------
def gc_miles(a, b):
    lo1, la1 = CITIES[a]; lo2, la2 = CITIES[b]
    p1, p2 = math.radians(la1), math.radians(la2)
    dp_, dl = math.radians(la2 - la1), math.radians(lo2 - lo1)
    h = math.sin(dp_/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 3958.8 * 2 * math.asin(math.sqrt(h))

MODE = {n: m for n, _, _, _, m in UNIQUE_LEGS}
miles = {m: round(sum(gc_miles(*BY_NAME[n.lstrip('-')][:2])
                      for n in ITINERARY if MODE[n.lstrip('-')] == m))
         for m in ('fly', 'rail', 'road')}

# ---- land ------------------------------------------------------------------
def clip(ring, edge):
    # Sutherland-Hodgman against one bbox edge: edge = (axis, sign, value)
    axis, sign, val = edge
    out = []
    for i in range(len(ring)):
        cur, prv = ring[i], ring[i-1]
        cin = (cur[axis] - val) * sign >= 0
        pin_ = (prv[axis] - val) * sign >= 0
        if cin != pin_:
            t = (val - prv[axis]) / (cur[axis] - prv[axis])
            out.append((prv[0] + t*(cur[0]-prv[0]), prv[1] + t*(cur[1]-prv[1])))
        if cin:
            out.append(cur)
    return out

def clip_bbox(ring):
    for e in ((0, 1, LON_MIN), (0, -1, LON_MAX), (1, 1, LAT_MIN), (1, -1, LAT_MAX)):
        ring = clip(ring, e)
        if len(ring) < 3: return []
    return ring

def dp(pts, eps):
    if len(pts) < 3: return pts
    ax, ay = pts[0]; bx, by = pts[-1]
    dmax, idx = 0.0, 0
    dx, dy = bx-ax, by-ay
    L = math.hypot(dx, dy)
    for i in range(1, len(pts)-1):
        if L < 1e-9:   # closed ring: chord degenerates to a point
            d = math.hypot(pts[i][0]-ax, pts[i][1]-ay)
        else:
            d = abs(dy*(pts[i][0]-ax) - dx*(pts[i][1]-ay)) / L
        if d > dmax: dmax, idx = d, i
    if dmax <= eps: return [pts[0], pts[-1]]
    return dp(pts[:idx+1], eps)[:-1] + dp(pts[idx:], eps)

def area(pts):
    return abs(sum(pts[i][0]*pts[i-1][1] - pts[i-1][0]*pts[i][1]
                   for i in range(len(pts)))) / 2

gj = json.load(open(os.path.join(HERE, 'world.geo.json')))
paths = []
for feat in gj['features']:
    g = feat['geometry']
    polys = [g['coordinates']] if g['type'] == 'Polygon' else g['coordinates']
    for poly in polys:
        for ring in poly:
            r = clip_bbox([(p[0], p[1]) for p in ring])
            if not r: continue
            pr = dp([proj(lo, la) for lo, la in r], 1.0)
            if len(pr) < 3 or area(pr) < 25: continue
            paths.append('M' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in pr) + 'Z')

LAND_D = ''.join(paths)
with open(os.path.join(HERE, 'land_d.txt'), 'w') as f:
    f.write(LAND_D)

print(json.dumps({
    'viewbox': f'0 0 {W:.0f} {H:.0f}',
    'pins': {k: (round(x, 1), round(y, 1)) for k, (x, y) in P.items()},
    'route_d': ROUTE_D,
    'flight_d': FLIGHT_D,
    'arrival_ms': arrivals,
    'flight_ms': FLIGHT_MS,
    'miles': miles,
    'land_bytes': len(LAND_D), 'rings': len(paths),
}, indent=1))
