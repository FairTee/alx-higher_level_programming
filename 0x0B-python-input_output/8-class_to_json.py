#!/usr/bin/python3
"""Contains the "class_to_json" function"""


def class_to_json(obj):
    """
    Convert an object with serializable attributes
    into a dictionary for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object.

    Example:
        class_to_json(MyClass("John", 4, True, 1))
        # Returns a dictionary representation of the object.
    """
    # Get the object's attributes as a dictionary
    obj_dict = obj.__dict__

    serializable_dict = {
        key: value
        for key, value in obj_dict.items()
        if isinstance(value, (list, dict, str, int, bool))
    }

    return serializable_dict
