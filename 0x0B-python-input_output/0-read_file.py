#!/usr/bin/python3
"""
A function to read a text file (utf8) and print to stdout
"""


def read_file(filename):
    """
    A function to read a text file (utf8) and print to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
