#!/usr/bin/python3
"""This defines a base model class"""
import turtle
import json
import csv


class Base:
    """Base class for managing id attribute in future classes."""

    # private class attribute
    __nb_objects = 0

    # class constructor
    def __init__(self, id=None):
        """Initialize the instance with a given id or auto-incremented id."""
        if id is not None:
            self.id = id
        else:
            # increment __nb_objects and
            # assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Parameters:
        - list_dictionaries (list): A list of dictionaries.

        Returns:
        - str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Parameters:
        - list_objs (list): A list of instances inheriting from Base.

        Note: The filename must be: <Class name>.json (e.g., Rectangle.json).
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of instances from the JSON string representation.

        Parameters:
        - json_string (str): A string representing a list of dictionaries.

        Returns:
        - list: A list of instances represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set.

        Parameters:
        - **dictionary: A dictionary containing attribute values.

        Returns:
        - obj: An instance with attributes set based on
        the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file.

        Returns:
        - list: A list of instances represented by the file.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file.

        Parameters:
        - list_objs (list): A list of instances inheriting from Base.

        Note: The filename must be: <Class name>.csv (e.g., Rectangle.csv).
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a list of objects from a CSV file.

        Returns:
        - list: A list of instances represented by the file.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                return [cls.create_from_csv_row(row) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw rectangles and squares using Turtle graphics """
        turtle.speed(2)
        turtle.bgcolor("white")

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.color("blue")
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.exitonclick()
