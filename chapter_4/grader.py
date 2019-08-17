"""
A simple grading program.

Author: Oscar Lopez
Last Modified: Aug 16, 2019.
"""


def calculate_grade(number):
    if grade > .9:
        return 'A'
    if .8 <= grade < .9:
        return 'B'
    if .7 <= grade < .8:
        return 'C'
    if .6 <= grade < .7:
        return 'D'
    if 0 <= grade < .6:
        return 'F'


while True:
    try:
        grade = float(input('Please enter a grade between 0 and 1:\n'))
    except:
        print('ERROR: Please enter a valid numerical grade!')
        continue
    if grade < 0 or grade > 1:
        print('ERROR: Please enter a grade between 0 and 1 inclusively!')
        continue
    print(calculate_grade(grade))
    break
