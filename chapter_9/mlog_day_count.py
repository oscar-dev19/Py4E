"""
This program categorizes mbox.txt by the day of the week.

Author: Oscar.
"""
daysWeek = dict()

try:
    fopen = open('mbox.txt')
except:
    print('ERROR: mbox.txt is not found!')
    exit()
for line in fopen:
    if line.startswith('From'):
        words = line.split()
        if len(words) >= 3:
            day = words[2]
            if day not in daysWeek:
                daysWeek[day] = 1
            else:
                daysWeek[day] += 1

print(daysWeek)

