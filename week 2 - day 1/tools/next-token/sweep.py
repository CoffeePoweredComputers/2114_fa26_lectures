"""Sweep small causal LMs x prefixes: top-6 next tokens, and the most readable
attention head (last query position, argmax not on token 0, highest peak).
Usage: python sweep.py model [model ...]   -> prints a report, writes <model>.json
"""
import json, sys, re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

PROMPTS = {
    "A":  "I like to play",
    "B1": "At the casino, I like to play",
    "B2": "In the orchestra, I like to play",
    "B3": "On the tennis court, I like to play",
    "B4": "With my dog, I like to play",
    "B5": "In the afternoon, I like to play",
    "B6": "On the piano, I like to play",
    "B7": "After work, I like to play",
}
K = 6

def run(name):
    tok = AutoTokenizer.from_pretrained(name)
    model = AutoModelForCausalLM.from_pretrained(name, attn_implementation="eager", torch_dtype=torch.float32)
    model.eval()
    cfg = model.config
    L = getattr(cfg, "n_layer", None) or cfg.num_hidden_layers
    H = getattr(cfg, "n_head", None) or cfg.num_attention_heads
    D = getattr(cfg, "n_embd", None) or cfg.hidden_size
    wte = model.get_input_embeddings().weight
    out = {"model": name, "vocab": cfg.vocab_size, "layers": L, "heads": H, "dim": D, "prompts": {}}
    print(f"\n######## {name}: vocab {cfg.vocab_size}, {L} layers, {H} heads, dim {D}")
    for key, text in PROMPTS.items():
        ids = tok(text, return_tensors="pt")
        with torch.no_grad():
            r = model(**ids, output_attentions=True)
        probs = torch.softmax(r.logits[0, -1].float(), -1)
        top = torch.topk(probs, K)
        toks = [t.replace("Ġ", " ").replace("▁", " ") for t in tok.convert_ids_to_tokens(ids["input_ids"][0])]
        att = torch.stack(r.attentions)[:, 0, :, -1, :]        # L x H x T  (last query)
        # readable heads: argmax not position 0, peak >= .3
        cands = []
        for l in range(L):
            for h in range(H):
                v = att[l, h]
                j = int(torch.argmax(v))
                if j != 0 and float(v[j]) >= 0.3:
                    cands.append((float(v[j]), l, h, j, [round(float(x), 3) for x in v]))
        cands.sort(reverse=True)
        mean_all = att.mean((0, 1))
        emb = wte[ids["input_ids"][0], :8].float().tolist()
        rec = {
            "text": text, "tokens": toks, "ids": ids["input_ids"][0].tolist(),
            "top": [[tok.decode([int(i)]), round(float(p), 4)] for p, i in zip(top.values, top.indices)],
            "mean_att": [round(float(x), 3) for x in mean_all],
            "heads": [{"peak": round(c[0], 3), "layer": c[1], "head": c[2], "to": toks[c[3]], "w": c[4]} for c in cands[:6]],
            "emb8": [[round(v, 3) for v in row] for row in emb],
        }
        out["prompts"][key] = rec
        print(f"\n== {key}: {text!r}\n   tokens {toks}")
        print("   top:", ", ".join(f"{w!r} {p:.3f}" for w, p in rec["top"]))
        print("   mean att:", rec["mean_att"])
        for hd in rec["heads"][:4]:
            print(f"   head L{hd['layer']}H{hd['head']} -> {hd['to']!r} {hd['peak']}: {hd['w']}")
    safe = re.sub(r"[^A-Za-z0-9.-]+", "_", name)
    json.dump(out, open(f"{safe}.json", "w"), indent=1, ensure_ascii=False)

for m in sys.argv[1:]:
    try:
        run(m)
    except Exception as e:
        print(f"\n######## {m}: FAILED {type(e).__name__}: {e}")
