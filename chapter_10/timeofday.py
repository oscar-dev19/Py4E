"""
Script that will count the distribution of hour of the day for each of the messages.

Author: Oscar Lopez
"""

def count_num_of_times(data):
    hours = dict()
    for line in data:
        if line.startswith('From '):
            parsed_data = line.split()
            time = parsed_data[5].split(':')
            hour = time[0]
            if hour not in hours:
                hours[hour] = 1
            else:
                hours[hour] += 1
    return hours


def sort_hours(hours_dict):
    """
    Sorts the hours from a given dictionary.
    Parameters:
        (dict)hours_dict: Dictionary of the hour and how many times it appears (key=hour, value=number)
    """
    l = list()
    for hour, count in hours_dict.items():
        l.append((count, hour))
    l.sort()
    return l


""" Main Program """
fopen = open('mbox.txt')
data_hours = count_num_of_times(fopen)
for line in sort_hours(data_hours):
    print(f'{line[1]} {line[0]}')
