#!/usr/bin/env python3
"""Regenerate the deck's styled QR asset.

    python3 make-qr.py "https://your-short-link" [assets/qr-prairielearn.svg]

Needs the `qrencode` CLI (pacman/apt/brew install qrencode) — it computes the
QR matrix; this script only restyles it: VT-maroon rounded modules on a white
plate, solid rounded finder rings. Colours are baked into the asset on purpose
(an <img> can't inherit CSS custom properties), mirroring assets like the
day-1 ASCEND logos. Verify a regenerated code before class:

    rsvg-convert -w 600 assets/qr-prairielearn.svg > /tmp/qr.png && zbarimg -q /tmp/qr.png
"""
import subprocess
import sys

MAROON = "#861f41"   # keep in sync with --accent-1 in css/tokens.css
QUIET = 4            # quiet-zone modules on every side, part of the QR spec


def matrix(url):
    out = subprocess.run(
        ["qrencode", "-l", "M", "-m", "0", "-t", "ASCII", url],
        capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    return [[cell == "##" for cell in
             (row[i:i + 2] for i in range(0, len(row), 2))] for row in out if row]


def in_finder(r, c, n):
    return (r < 7 and c < 7) or (r < 7 and c >= n - 7) or (r >= n - 7 and c < 7)


def svg(m, url):
    n = len(m)
    s = n + 2 * QUIET
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}">',
        f'<!-- encodes: {url} · regenerate with make-qr.py -->',
        f'<rect width="{s}" height="{s}" fill="#ffffff"/>',
        f'<g fill="{MAROON}">',
    ]
    for r in range(n):
        for c in range(n):
            if m[r][c] and not in_finder(r, c, n):
                parts.append(f'<circle cx="{c + QUIET + 0.5}" cy="{r + QUIET + 0.5}" r="0.46"/>')
    for fr, fc in ((0, 0), (0, n - 7), (n - 7, 0)):
        x, y = fc + QUIET, fr + QUIET
        parts.append(f'<rect x="{x + 2}" y="{y + 2}" width="3" height="3" rx="0.9"/>')
        parts.append(f'<rect x="{x + 0.5}" y="{y + 0.5}" width="6" height="6" rx="1.9" '
                     f'fill="none" stroke="{MAROON}" stroke-width="1"/>')
    parts.append('</g></svg>')
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    url = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "assets/qr-prairielearn.svg"
    with open(out, "w") as f:
        f.write(svg(matrix(url), url))
    print(f"wrote {out}")
