#!/usr/bin/python3
"""Rectangle generation module"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initialize width and height fields"""
        self.__width = width
        self.__height = height

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
