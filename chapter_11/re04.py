# Search for lines that start with From and have an '@' sign.
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
