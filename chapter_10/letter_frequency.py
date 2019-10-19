"""
A simple script that reads a file and prints out the letter frequency in the file.

Author: Oscar Lopez
"""

def get_letter_frequency(data):
    """
    Function that reads from an open file and returns the frequency of letters in a
    dictionary.

    Parameters:
        (File) data: Open file of data to be checked.
    """
    letter_frequency = dict()
    for line in data:
        for char in line:
            lower_char = char.lower()
            if lower_char >= 'a' and lower_char <= 'z':
                if lower_char not in letter_frequency:
                    letter_frequency[lower_char] = 1
                else:
                    letter_frequency[lower_char] += 1
    return letter_frequency


fopen = open('mbox.txt')
frequency_list = list()
frequency = get_letter_frequency(fopen)
for char, freq in frequency.items():
    frequency_list.append((char, freq))
print(sorted(frequency_list))
