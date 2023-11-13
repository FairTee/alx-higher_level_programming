#!/usr/bin/python3
""" Defines a Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square, a special case of Rectangle
    with equal width and height.
    Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Parameters:
        - size (int): The size of the square.
        - x (int): The x-coordinate of the square's position.
        - y (int): The y-coordinate of the square's position.
        - id: The identifier for the square.

        Attributes:
        - id: Inherited from Rectangle.
        - x: Inherited from Rectangle.
        - y: Inherited from Rectangle.
        - width: Equal to the size parameter.
        - height: Equal to the size parameter.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size property."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size property.

        Parameters:
        - value: The new size value.

        Raises:
        - ValueError: If the value is not an
        integer or is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Parameters:
        - *args: List of arguments. If present,
        should contain id, size, x, and y in order.
        - **kwargs: Dictionary of keyworded arguments
        representing instance attributes.

        Note: If *args is not empty, **kwargs will be ignored.
        """
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square.

        Returns:
        - dict: A dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.width,  # Size is the same as width for a Square
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a string representation of the Square.

        Format: "[Square] (<id>) <x>/<y> - <size>"

        Returns:
        - str: The string representation of the square.
        """
        return (
            "[Square] ({}) "
            "{}/{} - {}".format(self.id, self.x, self.y, self.width)
        )

    def to_csv_row(self):
        """
        Returns a list representing the CSV row for the Square.

        Returns:
        - list: A list containing the attributes for CSV representation.
        """
        return [self.id, self.size, self.x, self.y]

    @classmethod
    def create_from_csv_row(cls, row):
        """
        Creates a Square instance from a CSV row.

        Parameters:
        - row (list): A list containing attributes for creating a Square.

        Returns:
        - Square: An instance of the Square class.
        """
        return cls(*map(int, row))
