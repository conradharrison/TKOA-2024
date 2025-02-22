import sys
import re

# Must exist
datafile = sys.argv[1]

lines = []
with open(datafile, "r") as f:
    for line in f:
        lines.append(line.strip())

words = re.split(',|:', lines[0])[1:]
inscription = lines[2]

print(words)
print(inscription)


# word_state==0: yet to start
# word_state==n: n letters matched
# if n==length of word, increment word_count, and reset state to 0
word_state = {}
word_count = {}
for w in words:
    word_state[w] = 0
    word_count[w] = 0

for i in range(len(inscription)):
    for w in words:
        if w[word_state[w]] == inscription[i]:
            word_state[w] += 1
        else:
            word_state[w] = 0
        if word_state[w] == len(w):
            word_count[w] += 1
            word_state[w] = 0

s = 0
for w in words:
    s += word_count[w]
                   
print(s)
