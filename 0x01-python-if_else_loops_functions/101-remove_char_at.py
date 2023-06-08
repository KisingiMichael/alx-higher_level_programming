#!/usr/bin/python3
def remove_char_at(str, n):
    my_string = ''
    for i in range(len(str)):
        if i != n:
            my_string += str[i]
    return (my_string)
