# Deck tools

- `add_sids.py slides/*.html` — stamps `data-sid="<file>:<n>"` on every element that lacks one (Slide Studio's handles). Run on a new slide once.
- `lint.py slides/*.html` — tag balance, sid uniqueness/prefix, forbidden `data-anim` drifts, raw hex, unscoped selectors in slide `<style>`, dense `data-step` numbering, drift reveals, one `slide__desc`.
- `measure/run.sh [deck-dir]` — headless Chromium layout sweep (needs `chromium`): slack under 984 per slide at its last step, anything past the body edges, clipped code lines. Not a screenshot pass.
