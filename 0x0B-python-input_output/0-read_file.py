#!/usr/bin/python3
""" reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
