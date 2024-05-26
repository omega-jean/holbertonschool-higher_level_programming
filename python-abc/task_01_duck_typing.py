#!/usr/bin/env python3
"""class"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """create new class shape"""
    @abstractmethod
    def area(self):
        """Public method that returns the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimeter of the shape"""
        pass


class Circle(Shape):
    """create new class circle"""
    def __init__(self, radius):
        """initialization"""
        self.radius = radius

    def area(self):
        """Public method that returns the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """create new class rectangle"""
    def __init__(self, width, height):
        """initialization"""
        self.width = width
        self.height = height

    def area(self):
        """Public method that returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """test function"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
