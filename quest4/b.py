import sys
import re

# Must exist
datafile = sys.argv[1]

lines = []
with open(datafile, "r") as f:
    for line in f:
        lines.append(line.strip())

heights = list(map(int, lines))
lowest = min(heights)
s = sum(map(lambda x: x-lowest, heights))

print(s)
