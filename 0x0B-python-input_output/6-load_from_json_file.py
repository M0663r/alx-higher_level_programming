#!/usr/bin/python3
"""
This module provides a function to create an object from a JSON file.

Functions:
    load_from_json_file(filename): Creates and returns an object
    from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename: The name of the file to load the object from.
    """
    with open(filename, 'r') as f:
        return json.load(f)
