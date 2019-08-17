"""
A simple grading program.

Author: Oscar Lopez
Last Modified: Aug 14, 2019.
"""

grade = 0

try:
    grade = float(input('Enter a grading score between 0 and 1: '))
except:
    print('ERROR: Please enter a valid score!')
    exit()

if grade < 0 or grade > 1:
    print('ERROR: Please enter a score between 0 and 1!')
    exit()

if grade > .9:
    print('A')
if .8 <= grade < .9:
    print('B')
if .7 <= grade < .8:
    print('C')
if .6 <= grade < .7:
    print('D')
if 0 <= grade < .6:
    print('F')
