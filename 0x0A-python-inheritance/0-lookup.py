#!/usr/bin/python3
"""COntains a Lookup module"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the
        names of attributes and methods of the object.
    """
    return dir(obj)
