#!/usr/bin/python3
"""Create a class"""


class Square:
    """Class constructor """
    def __init__(self, size=0):
        """Initialize a square class
        Ags: size=0: size of a the class square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0 ")
        self.__size = size

    def area(self):
        """compute area of class"""
        return self.__size ** 2
