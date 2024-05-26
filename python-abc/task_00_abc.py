#!/usr/bin/env python3
"""class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """create new class animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """create new class dog"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """create new class cat"""
    def sound(self):
        return "Meow"
