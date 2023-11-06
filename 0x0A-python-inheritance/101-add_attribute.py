#!/usr/bin/python3
"""Attribute adding module"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attr: The name of the new attribute.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
