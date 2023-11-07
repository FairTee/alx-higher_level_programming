#!/usr/bin/python3
"""COntains an append function"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file
    (UTF-8) and return the number of characters added.

    Args:
        filename (str): The name of the file to
        append to (default is an empty string).
        text (str): The string to be appended to
        the file (default is an empty string).

    Returns:
        int: The number of characters added to the file.

    Note:
        This function uses the 'with' statement
        to ensure proper file handling.
        If the file does not exist, it will be created.
        The function appends the 'text' to the end of the file.

    Example:
        append_write("file_append.txt", "This School
        is so cool!\n")  # Appends the text to the file.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            num_characters_added = file.write(text)
            return num_characters_added
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0


if __name__ == "__main__":
    nb_characters_added = append_write(
        "file_append.txt",
        "This School is so cool!\n")
    print(nb_characters_added)
