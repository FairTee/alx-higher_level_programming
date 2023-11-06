#!/usr/bin/python3
"""Class BaseGeometry and subclass Rectangle"""


class BaseGeometry:
    """Public instance methods area and integer_validator"""
    def area(self):
        """Pulls an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """Initialization of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
