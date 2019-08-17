"""
A program that takes in a confidence statement formatted
as 'X-DSPAM-Confidence:##' and print out the confidence number as a number.

Author: Oscar Lopez
"""

str = 'X-DSPAM-COnfidence:0.8475'
confidence_value = 0.0

num_pos = str.find(':')
confidence_value = float(str[num_pos + 1 :])
print(confidence_value)
## DEBUG: print(type(confidence_value))
