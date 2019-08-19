"""
A program that looks through a given mbox file for dates.

Author: Oscar Lopez
"""

fhand = open('mbox.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    if len(words) >= 2:
        print(words[2])

