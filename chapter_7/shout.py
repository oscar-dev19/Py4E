"""
A program that prints out the contents of a given file in all uppercase format.

Author: Oscar Lopez
"""

fname = input('Enter a file name: ')
try:
    fopen = open(fname)
except:
    print("ERROR: File ",fname," not found!")
    exit()
for line in fopen:
    print(line.upper())
