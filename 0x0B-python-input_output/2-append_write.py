#!/usr/bin/python3
"""
This module contains a function that appends a string a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a text file (UTF8) and returns the number of characters ."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
