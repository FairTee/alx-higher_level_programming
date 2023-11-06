#!/usr/bin/python3
"""Contains the class MyInt"""


class MyInt(int):
    """
    A custom integer class that inverts
    the equality operators '==' and '!='.

    Public Methods:
        __eq__(self, other): Override the '==' operator.
        __ne__(self, other): Override the '!=' operator.

    Inherits all other methods and
    attributes from the built-in int class.
    """
    def __eq__(self, other):
        """
        Override the '==' operator to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the '!=' operator to invert its behavior.
        """
        return super().__eq__(other)
