import sys
import re

# Must exist
datafile = sys.argv[1]

lines = []
with open(datafile, "r") as f:
    for line in f:
        lines.append(line.strip())

words = re.split(',|:', lines[0])[1:]
inscriptions = lines[2:]

##print(words)
##print(inscriptions)

def reverse_word(s):
    return ' '.join([x[::-1] for x in s.split(' ')])

# Augment words by adding unique reversed words
words = list(set(words + list(map(reverse_word, words))))

##print(words)

symbol_count = 0

for inscription in inscriptions:
    l = len(inscription)
    running_words = {}
    for i in range(l):
        #print(f"{inscription[i]} ", end="")

        # Add new word-starts to running list
        for w in words:
            if inscription[i] == w[0]:
                running_words[(w,i)] = {'state':0, 'symbol_value':0}
                #print(f"Added {w}{i},", end="")

        # If match, update state, else reset state (retire)
        for k in running_words.keys():
            (w, wi) = k
            if w[running_words[k]['state']] == inscription[i]:
                running_words[k]['state'] += 1
                running_words[k]['symbol_value'] += 1
                #print(f"{w}{wi}={running_words[k]['symbol_value']},", end="")
            else:
                running_words[k]['state'] = 0

        # Based on state, retire words (and tally other running words)
        for k in running_words.keys():
            (w, wi) = k
            if running_words[k]['state'] == len(w):
                running_words[k]['state'] = 0
                sv = running_words[k]['symbol_value']
                symbol_count += sv
                #print(f"Counted {w}{wi} as {sv},", end="")
                if len(running_words)>1:
                    for k in running_words.keys():
                        running_words[k]['symbol_value'] =  max(0, running_words[k]['symbol_value']-sv)

        # Remove retired words
        for k, v in list(running_words.items()):
            (w, wi) = k
            if v['state'] == 0:
                del running_words[k]
                #print(f"Removed {w}{wi},", end="")

        #print(symbol_count)

    #print(symbol_count)     

print(symbol_count)    
