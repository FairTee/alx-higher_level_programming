#!/usr/bin/python3

class BaseGeometry:
    """
    A class representing base geometry.

    This class serves as a base for
    other geometry-related classes.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the
        message "area() is not implemented."
    """

    def area(self):
        """
        Raises an Exception indicating that
        the "area" method is not implemented.

        Raises:
            Exception: Always raised with the message
            "area() is not implemented."
        """
        raise Exception("area() is not implemented")
