# 16d — the next-token machine

`slides/16d-next-word.html` is **generated**; do not hand-edit it. Edit `gen16d.py`
(geometry, captions, notes, CSS) and run `python tools/next-token/gen16d.py` from
anywhere — it needs only the two JSON files here.

The numbers come from `openai-community/gpt2-medium` (355 M parameters, 24 layers,
16 heads, 1,024-dim, 50,257-token vocabulary), a *causal* model — it predicts the
next token from the left context only, which is the mechanism the slide teaches.
(The slide's earlier version used a masked model, which reads both ways.)

- `sweep.py MODEL…` — top-6 next tokens and readable attention heads for a set of
  prefixes; `gpt2-medium.json` is its output for that model.
- `head.py` — layer 18, head 7 (the head that puts 96% of its attention on
  " casino") for both prompts, plus the " poker" token; writes `head.json`.
- `next_token.py` — the first, simpler probe (kept for reference).

Reproducing the JSON needs `pip install transformers torch` and ~1.4 GB of weights.
