#!/usr/bin/python3
"""Function to add 2 intergers"""


def add_integer(a, b=98):
    """Function to return int(a) plus int(b)"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
