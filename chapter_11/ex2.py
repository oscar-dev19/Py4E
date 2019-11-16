'''
Simple program that prints out the number form the 
line formatted as 'New Revision: ###'. The average of
the numbers will be calculated and printed out.
'''

import re
sum = 0
count = 0
fopen = open('mbox.txt')
for line in fopen:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        sum += int(x[0])
        count += 1
average = sum / count
print(int(average))
