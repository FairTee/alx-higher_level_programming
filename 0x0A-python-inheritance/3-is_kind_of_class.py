#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or inherits from, a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of, or inherits from, the specified class; otherwise, False.
    """
    return (isinstance(obj, a_class))