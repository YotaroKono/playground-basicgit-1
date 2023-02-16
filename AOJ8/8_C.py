import sys

texts = sys.stdin.read().lower()
letters = 'abcdefghijklmnopqrstuvwxyz'
counts = [0]*26


for x in texts:
    i = 0
    for y in letters:
        if x == y:
            counts[i] += 1
        i += 1

for i in range (26):
    print(letters[i], ":", str(counts[i]))
    