#!/usr/bin/python3
"""Contains function Is_same_class"""


def is_same_class(obj, same_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an
        instance of the specified class; otherwise, False.
    """
    return (type(obj) == same_class)
