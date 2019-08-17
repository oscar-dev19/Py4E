"""
A simple pay calculator based on user entered hours and pay rate.

Author: Oscar Lopez
"""


def compute_pay(hours, rate):
    pay = 0
    if hours > 40:
        pay = 1.5 * (hours * float(rate))
    else:
        pay = hours * float(rate)
    return pay


while True:
    try:
        hours = int(input('Enter hours worked:'))
    except:
        print('ERROR:Please enter a valid numerical value!')
        continue
    try:
        rate = float(input('Enter current rate of pay:'))
    except:
        print('ERROR:Please enter a valid numerical rate!')
        continue
    print(compute_pay(hours, rate))
    break
