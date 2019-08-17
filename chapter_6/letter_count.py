"""
A program that counts the number of times a given letter is in a given
word

Author: Oscar Lopez
"""

def letter_count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

print(letter_count('Shawn', 'h'))
