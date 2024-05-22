#!/usr/bin/python3
"""Rectangle generation module"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        size = "#" * self.__width
        rectangle = []
        for i in range(self.__height):
            rectangle.append(size)
        return "\n".join(rectangle)

    def __repr__(self):
        return "Rectangle({:d}, {:d})" .format(self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

