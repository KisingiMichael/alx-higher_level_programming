#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    low_peak = 0
    high_peak = len(list_of_integers)
    mid_peak = ((high_peak - low_peak) // 2) + low_peak
    mid_peak_peak = int(mid_peak)
    if high_peak == 1:
        return list_of_integers[0]
    if high_peak == 2:
        return max(list_of_integers)
    if list_of_integers[mid_peak] >= list_of_integers[mid_peak - 1] and\
            list_of_integers[mid_peak] >= list_of_integers[mid_peak + 1]:
        return list_of_integers[mid_peak]
    if mid_peak > 0 and list_of_integers[mid_peak] < list_of_integers[mid_peak + 1]:
        return find_peak(list_of_integers[mid_peak:])
    if mid_peak > 0 and list_of_integers[mid_peak] < list_of_integers[mid_peak - 1]:
        return find_peak(list_of_integers[:mid_peak])
