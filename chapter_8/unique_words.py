"""
A program that looks at a file and prints out unique words of that file.

Author: Oscar Lopez.
"""

fname = input('Enter name of file: ')
unique_words = []

try:
    fopen = open(fname)
except:
    print('ERROR: ',fname,'does not exist!')
    exit()
for line in fopen:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

print(unique_words)

