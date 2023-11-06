#!/usr/bin/python3
"""List Module"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public Methods:
        print_sorted(self): Prints the list in ascending sorted order.

    Attributes:
        Inherits all attributes and methods from the list class.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        print(sorted_list(self.copy()))
