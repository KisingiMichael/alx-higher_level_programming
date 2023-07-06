#!/usr/bin/python3
""" Define a class """


class LockedClass:
    """
    This is the class which prevents use from dynamic attributes
    """
    __slots__ = ['first_name']
