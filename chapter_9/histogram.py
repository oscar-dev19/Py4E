"""
A program that will read through a mail log and count how many messages have
come from each email address and print the results to the console.

Author: Oscar Lopez
"""

number_mails = dict()

fname = input('Enter name of mail log to analyze: ')
try:
    fopen = open(fname)
except:
    print('ERROR:',fname,'does not exist or has no read permissions! Exiting.')
    exit()
for line in fopen:
    if line.startswith('From'):
        words = line.split()
        if len(words) >= 2:
            if words[1] not in number_mails:
                number_mails[words[1]] = 1
            else:
                number_mails[words[1]] += 1

print(number_mails)

