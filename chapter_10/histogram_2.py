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
        print('ERROR:', mail_log, 'does not exist!')
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


def sender_max(dict_senders):
    max_sender = dict()
    max_sent = 0
    for sender in dict_senders:
        if dict_senders[sender] > max_sent:
            max_sender = {sender, dict_senders[sender]}
            max_sent = int(dict_senders[sender])
    return max_sender


def domain_count(dict_senders):
    domain_dict = dict()
    for sender in dict_senders:
        words = sender.split('@')
        domain_dict.update({words[1]:dict_senders[sender]})
    return domain_dict


def sort_as_tupls(dict_senders):
    l = list()
    for sender, num_sent in dict_senders.items():
        l.append((num_sent, sender))
    l.sort(reverse=True)
    return f'{l[0][1]}, {l[0][0]} commits'


fname = input('Enter name of file:')
print(sender_count(fname))
print(sender_max(sender_count(fname)))
print(domain_count(sender_count(fname)))
print(sort_as_tuple(sender_count(fname)))
