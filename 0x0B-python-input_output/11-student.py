#!/usr/bin/python3
"""Contains student func"""


class Student:
    """
    Defines a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names
            to retrieve (default is None).

        Returns:
            dict: A dictionary representing the
            Student instance with specified attributes.

        Example:
            student = Student("John", "Doe", 23)
            student.to_json()  # Returns {'first_name':
            'John', 'last_name': 'Doe', 'age': 23}
            student.to_json(['first_name', 'age'])
            # Returns {'first_name': 'John', 'age': 23}
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        with values from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.

        Returns:
            None

        Example:
            student = Student("John", "Doe", 23)
            json_data = {'first_name': 'Alice', 'last_name':
            'Smith', 'age': 28}
            student.reload_from_json(json_data)
            # Now, student.first_name is 'Alice',
            student.last_name is 'Smith', and student.age is 28.
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the Student instance.

        Returns:
            str: A string representing the Student instance.

        Example:
            student = Student("John", "Doe", 23)
            str(student)  # Returns "John Doe - 23"
        """
        return "{} {} - {}".format(
            self.first_name,
            self.last_name,
            self.age
        )
