#!/usr/bin/python3
"""Square generation module"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Initialize a new Square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the square area"""
        return(self.__size * self.__size)
