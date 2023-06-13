#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return
    if len(my_list) == 0:
        return
    max = my_list[0]
    for x in range(1, len(my_list)):
        if my_list[x] > max:
            max = my_list[x]
        return max
