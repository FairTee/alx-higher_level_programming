#!/usr/bin/python3
"""
This function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Default is 98.

    Returns:
    int: The addition of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
