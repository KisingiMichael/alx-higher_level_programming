#!/usr/bin/python3
"""Create rectangle class"""


class Rectangle:
    """class object initiation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """class rectangle initiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        total = ""
        if self.width == 0 or self.height == 0:
            return total
        for x in range(self.__height):
            total += (str(self.print_symbol) * self.__width)
            if x is not self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        """printing rectangle with eval"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Printing a message when a rectangle is deleted"""
        print("Bye rectangle...")
