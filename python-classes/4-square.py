
#!/usr/bin/python3
"""Square generation module"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Initialize a new Square."""
        self.__size = size

    @property
    def size(self):
        """size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """value is the square length"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square area"""
        return(self.__size * self.__size)
