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

i = 1
counts = {}
while True:
    play_round()
    if last_n in counts:
        counts[last_n] += 1
        if counts[last_n] == 2024:
            answer = int(last_n) * i
            break
    else:
        counts[last_n] = 1
    i = i + 1

print(answer)
