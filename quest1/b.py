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
for c1, c2 in batched(lines[0], n=2):
    if c1 == 'x' or c2 == 'x':
        s += potion_map[c1] + potion_map[c2]
    else:
        s += potion_map[c1] + potion_map[c2] + 2


print(s)
    

