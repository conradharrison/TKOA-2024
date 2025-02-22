import sys
import re

# Must exist
datafile = sys.argv[1]

lines = []
with open(datafile, "r") as f:
    for line in f:
        lines.append(line.strip())

rows = len(lines)
columns = len(lines[0])
mine_state = [ [0]*columns for r in range(rows)]

def print_mine_state():
    for r in range(rows):
        for c in range(columns):
            print(f"{mine_state[r][c]}", end="")
        print()
    print()

def tally_mine_state():
    total = 0
    for r in range(rows):
        for c in range(columns):
            total += mine_state[r][c]
    return total

def get_mine_state(r, c):
    if r<0 or c<0 or r>=rows or c>=columns:
        return 0
    else:
        return mine_state[r][c]

def safe(r, c):
    return ((get_mine_state(r, c) - get_mine_state(r-1, c) <= 0) and
            (get_mine_state(r, c) - get_mine_state(r+1, c) <= 0) and
            (get_mine_state(r, c) - get_mine_state(r, c-1) <= 0) and
            (get_mine_state(r, c) - get_mine_state(r, c+1) <= 0) and
            (get_mine_state(r, c) - get_mine_state(r-1, c-1) <= 0) and
            (get_mine_state(r, c) - get_mine_state(r+1, c-1) <= 0) and
            (get_mine_state(r, c) - get_mine_state(r-1, c+1) <= 0) and
            (get_mine_state(r, c) - get_mine_state(r+1, c+1) <= 0))

something_changed = True
while(something_changed):
    something_changed = False
    for r in range(rows):
        for c in range(columns):
            if lines[r][c] == '.':
                continue
            if safe(r, c):
                mine_state[r][c] += 1
                something_changed = True
    print_mine_state()

# Main
print_mine_state()
print(tally_mine_state())
