#!/usr/bin/python3
"""Rectangle generation module"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initialize width and height fields

        args:
        height (int): rectangle height
        width (int): rectangle width
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Public method that returns a printable rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        size = "#" * self.__width
        rectangle = []
        for i in range(self.__height):
            rectangle.append(size)
        return "\n".join(rectangle)

    @property
    def width(self):
        """method of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public method that returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Public method that returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))
