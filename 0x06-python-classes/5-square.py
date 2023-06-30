#!/usr/bin/python3
""" Creating a class square """


class Square:
    """ Class constructor definition """
    def __init__(self, size=0):
        """Initialize a square class
        Args: size=0: size of square
        """
        self.__size = size

    @property
    def size(self):
        """ set gater of the square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate the area of the sqaure """
        return self.__size ** 2

    def my_print(self):
        """"Print the square"""
        if self.__size == 0:
            print()
        else:
            for n in range(self.__size):
                print("#" * self.__size)
