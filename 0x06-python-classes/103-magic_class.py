#!/usr/bin/python3
"""Define a magicclass matching a bytecode."""


import math


class MagicClass:
    "Represent a new circle."""

    def __init__(self, radius=0):
        """Initialize a magic class."""

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference."""
        return 2 * math.pi * self.__radius
