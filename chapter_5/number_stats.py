"""
A simple program that reads a set of numbers entered by the user and
calculates its total, max, min, and average.

Author: Oscar Lopez
"""


total = 0
average = 0
count = 0
max = 0
min = 0

while True:
    user_input = input('Enter a number: ')
    if user_input.lower() == 'done':
        break
    try:
        num = int(user_input)
    except:
        print('Invalid Input!')
        continue

    count+=1
    total += num
    average = total / count
    if num < min:
        min = num
    if num > max:
        max = num


print('Max: ',max, '\nMin: ',min,'\nAverage: ',average,'\nTotal: ',total)
