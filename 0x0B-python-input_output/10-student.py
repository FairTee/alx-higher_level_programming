#!/usr/bin/python3
"""COntains the student function"""


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
            attrs (list): A list of attribute
            names to retrieve (default is None).

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
