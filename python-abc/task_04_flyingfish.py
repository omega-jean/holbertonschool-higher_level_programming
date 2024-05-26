#!/usr/bin/env python3
"""class"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Method for swimming."""
        print("The fish is swimming.")

    def habitat(self):
        """Method to display habitat."""
        print("The fish lives in water.")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Method for flying."""
        print("The bird is flying.")

    def habitat(self):
        """Method to display habitat."""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish,\
            inheriting from both Fish and Bird."""

    def fly(self):
        """Method for flying, specific to flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Method for swimming, specific to flying fish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Method to display habitat, specific to flying fish."""
        print("The flying fish lives both in water and the sky!")
