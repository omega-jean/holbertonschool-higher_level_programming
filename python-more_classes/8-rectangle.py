#!/usr/bin/python3
"""Rectangle generation module"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method that initialize width and height fields

        args:
        height (int): rectangle height
        width (int): rectangle width
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Public method that returns a printable rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        size = str(self.print_symbol) * self.__width
        rectangle = []
        for i in range(self.__height):
            rectangle.append(size)
        return "\n".join(rectangle)

    def __repr__(self):
        """Public meyhod"""
        return "Rectangle({:d}, {:d})" .format(self.__width, self.__height)

    def __del__(self):
        """Public method that delete instance and print message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method returns the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() is rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
