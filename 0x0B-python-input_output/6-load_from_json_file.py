#!/usr/bin/python3
"""COntains a load_from_json function"""


import json


def load_from_json_file(filename):
    """
    Read a JSON file and create an object from its contents.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON file.

    Example:
        load_from_json_file("my_list.json")
        # Reads "my_list.json" and returns the object.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
