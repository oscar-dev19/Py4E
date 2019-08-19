"""
A small program that removes the first and last element of a given list
and other similar functions.

Author: Oscar Lopez
"""

def chop(a_list):
    del a_list[0]
    del a_list[-1]

def middle(a_list):
    b_list = a_list[1:-1]
    return b_list


some_list = [1,2,3,4,5]

print(middle(some_list))
chop(some_list)
print(some_list)

