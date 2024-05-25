#!/usr/bin/python3
"""file for class"""


class BaseGeometry:
    """create new class basegeometry"""
    def area(self):
        """Public method that returns the area of BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method that validate integer

        Args:
            name (str): is a string
            value (int): is a integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
