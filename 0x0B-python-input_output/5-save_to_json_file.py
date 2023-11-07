#!/usr/bin/python3
"""Contains save_to_json function"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file in JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None

    Example:
        save_to_json_file([1, 2, 3], "my_list.json")
        # Writes a list to "my_list.json".
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
