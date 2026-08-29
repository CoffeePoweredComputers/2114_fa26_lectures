"""Real numbers for the W2D1 next-token slide.

Causal LM only (GPT-2 family). For each prompt: tokens + ids, top-k next-token
probabilities, last-layer attention from the last position (mean over heads),
first 8 embedding dims per token, and a short greedy continuation.
Usage: python next_token.py [model] > out.json
"""
import json, sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = sys.argv[1] if len(sys.argv) > 1 else "gpt2"
K = 8
PROMPTS = {
    "A": "I like to play",
    "B1": "In the afternoon, I like to play",
    "B2": "On the piano, I like to play",
    "B3": "After work, I like to play",
    "B4": "On weekends, I like to play",
    "B5": "With my dog, I like to play",
    "B6": "At the casino, I like to play",
}

tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, attn_implementation="eager")
model.eval()
wte = model.get_input_embeddings().weight
cfg = model.config
out = {"model": MODEL, "vocab": cfg.vocab_size, "layers": cfg.n_layer,
       "dim": cfg.n_embd, "heads": cfg.n_head, "prompts": {}}

for key, text in PROMPTS.items():
    ids = tok(text, return_tensors="pt")
    with torch.no_grad():
        r = model(**ids, output_attentions=True)
    logits = r.logits[0, -1]
    probs = torch.softmax(logits, dim=-1)
    top = torch.topk(probs, K)
    att_last = r.attentions[-1][0].mean(0)[-1]          # last layer, mean heads, last query
    att_all = torch.stack(r.attentions)[:, 0].mean(1)[:, -1]   # per layer
    toks = tok.convert_ids_to_tokens(ids["input_ids"][0])
    toks = [t.replace("Ġ", " ") for t in toks]
    emb = wte[ids["input_ids"][0], :8].tolist()
    # greedy continuation, 4 tokens, with the prob of each pick
    gen_ids = ids["input_ids"].clone(); picks = []
    for _ in range(4):
        with torch.no_grad():
            p = torch.softmax(model(gen_ids).logits[0, -1], -1)
        i = int(torch.argmax(p)); picks.append([tok.decode([i]), round(float(p[i]), 4)])
        gen_ids = torch.cat([gen_ids, torch.tensor([[i]])], 1)
    out["prompts"][key] = {
        "text": text,
        "tokens": toks,
        "ids": ids["input_ids"][0].tolist(),
        "top": [[tok.decode([int(i)]), round(float(p), 4)] for p, i in zip(top.values, top.indices)],
        "top_sum": round(float(top.values.sum()), 4),
        "att_last_layer": [round(float(a), 4) for a in att_last],
        "att_mid_layer": [round(float(a), 4) for a in att_all[cfg.n_layer // 2]],
        "emb8": [[round(v, 3) for v in row] for row in emb],
        "greedy": picks,
    }
json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
