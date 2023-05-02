#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    h = len(list_of_integers)
    mid_num = ((h - lo) // 2) + lo
    mid_num = int(mid_num)
    if h == 1:
        return list_of_integers[0]
    if h == 2:
        return max(list_of_integers)
    if list_of_integers[mid_num] >= list_of_integers[mid_num - 1] and\
            list_of_integers[mid_num] >= list_of_integers[mid_num + 1]:
        return list_of_integers[mid_num]
    if mid_num > 0 and list_of_integers[mid_num] < list_of_integers[mid_num + 1]:
        return find_peak(list_of_integers[mid_num:])
    if mid_num > 0 and list_of_integers[mid_num] < list_of_integers[mid_num - 1]:
        return find_peak(list_of_integers[:mid_num])

