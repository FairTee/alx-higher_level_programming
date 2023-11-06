#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an
        instance of the specified class; otherwise, False.
    """
    return (type(obj) == a_class)
