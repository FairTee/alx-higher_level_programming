#!/usr/bin/python3
"""Contains append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text into a file after
    each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to
        insert after each line containing the search_string.

    Example:
        append_after("file.txt", "Python", "\"C is fun!\"\n")
        will insert the new_string after each
        line containing "Python" in the file.

    This function reads the contents of the file,
    looks for lines containing the search_string,
    and inserts the new_string after each matching line.

    Note:
        The function does not handle file
        permission or file not found exceptions.

    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
