#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle instance.

        Parameters:
        - width (int): width of the rectangle.
        - height (int): height of the rectangle.
        - x (int): x-coordinate of the rectangle (default is 0).
        - y (int): y-coordinate of the rectangle (default is 0).
        - id (int): id of the rectangle (default is None).

        Call the super class with id to
        use the logic of the __init__ of the Base class.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with the character #,
        taking into account x and y."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Assign arguments to attributes.

        *args (no-keyworded arguments):
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute

        **kwargs (key-worded arguments):
            Each key in this dictionary represents an
            attribute to the instance.
            This type of argument is called a
            “key-worded argument”. Argument order is not important.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, attr in enumerate(attrs):
                if i < len(args):
                    setattr(self, attr, args[i])
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle.

        Returns:
        - dict: A dictionary containing id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def to_csv_row(self):
        """
        Returns a list representing the CSV row for the Rectangle.

        Returns:
        - list: A list containing the attributes for CSV representation.
        """
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def create_from_csv_row(cls, row):
        """
        Creates a Rectangle instance from a CSV row.

        Parameters:
        - row (list): A list containing attributes for creating a Rectangle.

        Returns:
        - Rectangle: An instance of the Rectangle class.
        """
        return cls(*map(int, row))
