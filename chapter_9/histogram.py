"""
A program that will read through a mail log and count how many messages have
come from each email address and print the results to the console.

Author: Oscar Lopez
"""

def sender_count(mail_log):
    num_mails = dict()
    try:
        fopen = open(mail_log)
    except:
        print('ERROR:',mail_log,'does not exist!')
        return None
    for line in fopen:
        if line.startswith('From'):
            words = line.split()
            if len(words) >= 2:
                if words[1] not in num_mails:
                    num_mails[words[1]] = 1
                else:
                    num_mails[words[1]] += 1
    return  num_mails


fname = input('Enter name of file:')
print(sender_count(fname))

