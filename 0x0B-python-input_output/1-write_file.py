#!/usr/bin/python3
"""COntains the write file function"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and
    return the number of characters written.

    Args:
        filename (str): The name of the file
        to write to (default is an empty string).
        text (str): The string to be written to
        the file (default is an empty string).

    Returns:
        int: The number of characters written to the file.

    Note:
        This function uses the 'with' statement
        to ensure proper file handling.
        If the file does not exist, it will
        be created. If the file already exists,
        its content will be overwritten.

    Example:
        write_file("my_first_file.txt",
        "This School is so cool!\n")  # Writes the text to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_characters_written = file.write(text)
            return num_characters_written
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0


if __name__ == "__main__":
    nb_characters = write_file(
        "my_first_file.txt",
        "This School is so cool!\n"
    )
    print(nb_characters)
