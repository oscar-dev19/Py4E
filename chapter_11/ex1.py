'''
Simulates the grep command on Unix.
It then asks the user to enter a regular expression and 
count the number of lines that matched the regular
expression.
'''

import re

command = input('Enter a regular expression: ')
hand = open('mbox.txt')
matched_counts = 0
for line in hand:
    line = line.rstrip()
    if re.search(command, line):
        matched_counts += 1
print(f'mbox.txt has %d lines that matched %s'%(matched_counts, command))
