#!/usr/bin/python3
"""
Defines a locked class.
"""


class LockedClass:
    """
    The LockedClass restricts the creation of new instance attributes
    to only allow 'first_name' as an attribute.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initializes a new instance of LockedClass.
        """
        pass
