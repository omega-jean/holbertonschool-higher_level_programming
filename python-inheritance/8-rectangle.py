#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """create class BaseGeometry"""

    def area(self):
        """Public method that returns the area of BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """create new class rectangle"""

    def __init__(self, width, height):
        """initialization"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
