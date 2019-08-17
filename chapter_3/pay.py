"""
A simple pay calculator based on user entered hours and pay rate.

Author: Oscar Lopez
"""


try:
    hours = int(input('Enter hours: '))
except:
    print('Please enter valid numerical hours!')
    exit()
try:
    rate = float(input('Enter Rate: '))
except:
    print('Please enter valid numerical rate!')
    exit()

if hours > 40:
    pay = 1.5 * (hours * float(rate))
else:
    pay = hours * float(rate)
print(pay)
