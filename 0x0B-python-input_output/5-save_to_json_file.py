#!/usr/bin/python3
"""
This module provides a function to write an object to a text file
using a JSON representation.

Functions:
    save_to_json_file(my_obj, filename): Writes an object to a text file
    using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename: The name of the file where the object will be written.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
