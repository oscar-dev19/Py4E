"""
A program that will read each line of a given file and if possible
count the spam confidence level present in the file.

Author: Oscar Lopez
"""

conf_total = 0
conf_average = 0
count = 0

fname = input('Enter name of file: ')
try:
    fopen = open(fname)
except:
    print('ERROR: File ',fname,' not found!')
    exit()
for line in fopen:
    if line.find('X-DSPAM-Confidence:') > -1:
        count += 1
        conf_level = float(line[line.find(':') + 1:])
        conf_total += conf_level
conf_average = conf_total / count
print('Average Spam Confidence Level:', conf_average)
