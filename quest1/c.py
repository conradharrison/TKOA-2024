import sys
from itertools import batched

# Must exist
datafile = sys.argv[1]

lines = []
with open(datafile, "r") as f:
    for line in f:
        lines.append(line.strip())

potion_map = {'x':0, 'A':0, 'B':1, 'C':3, 'D':5}
s = 0
for c1, c2, c3 in batched(lines[0], n=3):
    x_count = 0
    x_count += 1 if c1 == 'x' else 0
    x_count += 1 if c2 == 'x' else 0
    x_count += 1 if c3 == 'x' else 0

    s += potion_map[c1] + potion_map[c2] + potion_map[c3] + (2-x_count)*(3-x_count)

print(s)
