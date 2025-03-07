import sys
import re

# Must exist
datafile = sys.argv[1]

lines = []
with open(datafile, "r") as f:
    for line in f:
        lines.append(line.strip())

columns = [[], [], [], []]

for l in lines:
    columns[0].append(int(l.split(" ")[0]))
    columns[1].append(int(l.split(" ")[1]))
    columns[2].append(int(l.split(" ")[2]))
    columns[3].append(int(l.split(" ")[3]))

rows = len(lines)

last_n = None
current_column = 0

def play_round():
    global columns
    global last_n
    global current_column

    player_number = columns[current_column][0]
    length_of_clapping_column = len(columns[(current_column+1)%4])

    if player_number <= length_of_clapping_column:
        columns[(current_column+1)%4].insert(player_number-1, player_number)
    else:
        columns[(current_column+1)%4].insert(length_of_clapping_column-(player_number - length_of_clapping_column) + 1, player_number)
    columns[current_column] = columns[current_column][1:]

    current_column = (current_column+1)%4

    last_n = f"{columns[0][0]}{columns[1][0]}{columns[2][0]}{columns[3][0]}"

def print_columns():
    print(f"{(' '*(current_column))}{'*'}{(' '*(4-current_column-1))}")
    done = False
    r = 0
    while not done:
        c0 = columns[0][r] if r < len(columns[0]) else ""
        c1 = columns[1][r] if r < len(columns[1]) else ""
        c2 = columns[2][r] if r < len(columns[2]) else ""
        c3 = columns[3][r] if r < len(columns[3]) else ""
        print(f"{c0:1}{c1:1}{c2:1}{c3:1}")
        r += 1
        done = (r >= len(columns[0])) and  (r >= len(columns[1])) and  (r >= len(columns[2])) and  (r >= len(columns[3]))
    print()

print_columns()
for i in range(10):
    play_round()
    print_columns()

print(last_n)
