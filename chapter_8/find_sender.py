"""
A program that will read through mbox.txt and list the senders.

Author: Oscar Lopez
"""

senders = []
email_count = 0

try:
    fopen = open('mbox.txt')
except:
    print('ERROR: mbox.txt does not exist.')
for line in fopen:
    if line.startswith('From'):
        email_count += 1
        words = line.split()
        if len(words) > 2:
            if words[1] not in senders:
                senders.append(words[1])

print(senders)
print('\nThere were',email_count,'emails sent with',str(len(senders)),'correspondents')

