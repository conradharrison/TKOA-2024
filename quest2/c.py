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

#print(words)
#print(inscriptions)

def reverse_word(s):
    return ' '.join([x[::-1] for x in s.split(' ')])

# Augment words by adding unique reversed words
words = list(set(words + list(map(reverse_word, words))))

#print(words)

org_rows = len(inscriptions)
org_columns = len(inscriptions[0])
symbol_state = [ [0]*org_columns for i in range(org_rows)]

def count_symbols(inscriptions_in, wraps, transpose):

    if not transpose:
        rows = len(inscriptions_in)
        columns = len(inscriptions_in[0])
        inscriptions = inscriptions_in
    else:
        # Transpose the inscriptions
        columns = len(inscriptions_in)
        rows = len(inscriptions_in[0])
        inscriptions = [ ['']*columns for i in range(rows)]
        for k, inscription in enumerate(inscriptions_in):
            for j in range(len(inscription)):
                inscriptions[j][k] = inscription[j]
        
    symbol_count = 0

    for r in range(rows):
        inscription = inscriptions[r]
        l = len(inscription)
        running_words = {}
        done = False
        ii = 0
        while not done:

            i = ii % l

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
                    for j in range(i-sv+1, i+1):
                        if transpose:
                            symbol_state[j][r] = 1
                        else:
                            symbol_state[r][j] = 1
                    #print(f"Counted {w}{wi} as {sv},", end="")

            # Remove retired words
            for k, v in list(running_words.items()):
                (w, wi) = k
                if v['state'] == 0:
                    del running_words[k]
                    #print(f"Removed {w}{wi},", end="")

            #print()

            ii = ii + 1
            done = (len(running_words)==0 and ii>=l) or ii>=wraps*l

        #print()

    for r in range(org_rows):
        for c in range(org_columns):
            #print(f"{symbol_state[r][c]} ", end="")
            symbol_count += symbol_state[r][c]
        #print()

    return symbol_count

# Main

sc1 = count_symbols(inscriptions, wraps=2, transpose=False)
#print(sc1)
sc2 = count_symbols(inscriptions, wraps=1, transpose=True)
print(sc2)
