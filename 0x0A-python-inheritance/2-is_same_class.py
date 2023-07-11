#!/usr/bin/python3
"""
Returns True if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Return true if the object is an instance of a class
    """
    return type(obj) == a_class
