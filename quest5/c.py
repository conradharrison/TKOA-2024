import sys
import re
import copy

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

number_width = len(lines[0].split(" ")[0])

current_column = 0
def play_round():
    global columns
    global current_column

    player_number = columns[current_column][0]
    length_of_clapping_column = len(columns[(current_column+1)%4])

    if player_number%(2*length_of_clapping_column) <= length_of_clapping_column:
        columns[(current_column+1)%4].insert(player_number%(2*length_of_clapping_column)-1, player_number)
    else:
        columns[(current_column+1)%4].insert(length_of_clapping_column-(player_number%(2*length_of_clapping_column) - length_of_clapping_column) + 1, player_number)
    columns[current_column] = columns[current_column][1:]

    current_column = (current_column+1)%4

    last_n = f"{columns[0][0]:02}{columns[1][0]:02}{columns[2][0]:02}{columns[3][0]:02}"
    return last_n

def print_columns():
    w = int(number_width+1)
    print(f"{(' '*(current_column*w))} {'v'*(w-1)}{(' '*((4-current_column-1)*w))}")
    done = False
    r = 0
    while not done:
        c0 = columns[0][r] if r < len(columns[0]) else ""
        c1 = columns[1][r] if r < len(columns[1]) else ""
        c2 = columns[2][r] if r < len(columns[2]) else ""
        c3 = columns[3][r] if r < len(columns[3]) else ""
        print(f"{c0:{w}}{c1:{w}}{c2:{w}}{c3:{w}}")
        r += 1
        done = (r >= len(columns[0])) and  (r >= len(columns[1])) and  (r >= len(columns[2])) and  (r >= len(columns[3]))

print_columns()
print()

w = int(number_width+1)
i = 1
last_max = 0
while True:
    last_n = int(play_round())
    print_columns()
    #print()
    if (i % 1 == 0): print (f"Finished {i:16} rounds: max = {last_max:{4*w}}, current = {last_n:{4*w}}")
    if (i % 10 == 0): print_columns()
    if last_n > last_max:
        last_max = last_n
        last_max_i = i
    else:
        if last_n == last_max:
            break

    i = i + 1

print(f"{last_max} seen after game {last_max_i} and again after game {i}")
