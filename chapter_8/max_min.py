"""
Simple program that has the user enter
numbers until the user enters done and
determines its maximum and minimum.

Author: Oscar Lopez.
"""
numbers = []

while True:
    user_input = input('Enter a number: ')
    if str(user_input).lower() == 'done':
        break
    try:
        number = int(user_input)
    except:
        print('ERROR: Please enter a valid number!')
        continue
    numbers.append(number)

if numbers:
    print('\nMaximum:',max(numbers),'\nMinimum:',min(numbers))
else:
    print('No numbers have been entered to calculate Max or Min values.')

