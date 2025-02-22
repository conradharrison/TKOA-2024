import sys

# Must exist
datafile = sys.argv[1]

lines = []
with open(datafile, "r") as f:
    for line in f:
        lines.append(line.strip())

potion_map = {'x':0, 'A':0, 'B':1, 'C':3, 'D':5}
s = 0
for c1 in lines[0]:
    s += potion_map[c1]

print(s)
