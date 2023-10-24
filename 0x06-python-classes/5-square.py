#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represent the square."""

    def __init__(self, size=0):
        """Initialize a new square."""
        self.__size = size

    @property
    def size(self):
        """Get the new square size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the new area of square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
