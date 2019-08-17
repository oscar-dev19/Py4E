"""
A small program that writes each character of a given word in a new line.

Author: Oscar Lopez
"""

def reverse(word):
    index = len(word) - 1
    while index >= 0:
        letter = word[index]
        print(letter)
        index -= 1

reverse("Shawn")
