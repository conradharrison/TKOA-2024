import sys
import re
import statistics

# Must exist
datafile = sys.argv[1]

lines = []
with open(datafile, "r") as f:
    for line in f:
        lines.append(line.strip())

heights = list(map(int, lines))
median = statistics.median(heights)
s = sum(map(lambda x: abs(x-median), heights))

print(s)
