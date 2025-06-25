from data import *

import json, random

# Load
data = []
with open("data/all.jsonl") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        data.append(json.loads(line))

# Shuffle
random.shuffle(data)

# Split ratios
n = len(data)
train_end = int(0.8 * n)
valid_end   = train_end + int(0.1 * n)

# Write
for name, subset in [
    ("data/train.jsonl", data[:train_end]),
    ("data/valid.jsonl",   data[train_end:valid_end]),
    ("data/test.jsonl",  data[valid_end:])
]:
    with open(name, "w") as out:
        for ex in subset:
            out.write(json.dumps(ex, ensure_ascii=False) + "\n")
