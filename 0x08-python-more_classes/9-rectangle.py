#!/usr/bin/python3
"""creating rectangle class"""


class Rectangle:
    """class object initiation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """class rectangle initiation"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        rectangle = []
        for x in range(self.__height):
            [rectangle.append(str(self.print_symbol)) for i in range(self.__widhth)]
            if x is not self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """printing rectangle with eval"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Printing a message when a rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @staticmethod
    def square(cls, size=0):
        return Rectangle(size, size)
