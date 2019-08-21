"""
A small script that will add words from words.txt as key values
to a dictionary.

Author: Oscar Lopez.
"""

keywords = dict()
try:
    fopen = open('words.txt')
except:
    print('ERROR! words.txt not found!')
    exit()

for line in fopen:
    words = line.split()
    for word in words:
        if word not in keywords:
            keywords.update({word:0})

print(keywords)

