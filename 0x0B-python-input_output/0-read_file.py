#!/usr/bin/python3
"""
Has the read_file function
"""


def read_file(filename=""):
    """This reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
