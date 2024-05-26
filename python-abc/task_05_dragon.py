#!/usr/bin/env python3
"""class"""


class SwimMixin:
    """Mixin class with swim functionality."""

    def swim(self):
        """Method to perform swimming."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class with fly functionality."""

    def fly(self):
        """Method to perform flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon, inheriting from SwimMixin and FlyMixin."""

    def roar(self):
        """Method to perform roaring."""
        print("The dragon roars!")
