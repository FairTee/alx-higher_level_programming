#!/usr/bin/python3
"""Has inherits_from function"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a
    class that inherits (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a
        class that inherits from the specified class;
        otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
