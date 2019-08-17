"""
A simple temperature converter.

Author: Oscar Lopez
"""


def convert_to_fahrenheit(c_temp):
    fahrenheit = c_temp * float(9/5) + 32
    return fahrenheit


def convert_to_celsius(f_temp):
    celsius = (f_temp - 32) * float(5/9)
    return celsius

while True:
    choice = input('Are you converting celsius or fahrenheit? Enter c for celsius or f for fahrenheit')
    if choice.lower() == 'c':
        temp = input('Enter degrees to convert in fahrenheit: ')
        try:
            converted_temp = convert_to_fahrenheit(float(temp))
            print(str(converted_temp))
            break
        except:
            print('ERROR: Please enter a valid temperature!')
    elif choice.lower() == 'f':
        temp = input('Enter degrees to convert in celsius: ')
        try:
            converted_temp = convert_to_celsius(float(temp))
            print(str(converted_temp))
            break
        except:
            print('ERROR: Please enter a valid temperature!')
    else:
        print('ERROR: Invalid value!')
