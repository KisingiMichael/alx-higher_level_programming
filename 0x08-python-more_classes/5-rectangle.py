#!/usr/bin/python3
"""Create a rectangle class"""


class Rectangle:
    """class object initiation"""
    def __init__(self, width=0, height=0):
        """class rectangle initiation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """printing the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """printing rectangle with eval"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Printing a message when a rectangle is deleted"""
        print("Bye rectangle...")
