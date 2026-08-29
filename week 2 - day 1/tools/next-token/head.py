import json, torch
from transformers import AutoTokenizer, AutoModelForCausalLM
name = "gpt2-medium"; L, H = 18, 7
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForCausalLM.from_pretrained(name, attn_implementation="eager"); model.eval()
out = {"model": name, "layer": L, "head": H}
for k, text in {"A": "I like to play", "B": "At the casino, I like to play"}.items():
    ids = tok(text, return_tensors="pt")
    with torch.no_grad(): r = model(**ids, output_attentions=True)
    out[k] = {"tokens": [t.replace("Ġ", " ") for t in tok.convert_ids_to_tokens(ids["input_ids"][0])],
              "head_w": [round(float(x), 4) for x in r.attentions[L][0, H, -1]],
              "mean_w": [round(float(x), 4) for x in torch.stack(r.attentions)[:, 0].mean((0, 1))[-1]]}
pid = tok.encode(" poker")
out["poker"] = {"ids": pid, "emb8": [round(v, 3) for v in model.get_input_embeddings().weight[pid[0], :8].tolist()]}
# sum of the top-5 for both, to say honestly how much of the mass the bars show
for k, text in {"A": "I like to play", "B": "At the casino, I like to play"}.items():
    ids = tok(text, return_tensors="pt")
    with torch.no_grad(): p = torch.softmax(model(**ids).logits[0, -1], -1)
    t = torch.topk(p, 5); out[k]["top5"] = [[tok.decode([int(i)]), round(float(v), 4)] for v, i in zip(t.values, t.indices)]
    out[k]["top5_sum"] = round(float(t.values.sum()), 4)
json.dump(out, open("head.json", "w"), indent=1)
print(json.dumps(out, indent=1))
