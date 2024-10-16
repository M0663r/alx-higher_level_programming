#!/usr/bin/python3
"""
This module provides a function to convert an object (instance of a class)
into a dictionary that can be used for JSON serialization.

Functions:
    class_to_json(obj): Returns the dictionary description of an object.
"""


def class_to_json(obj):
    """

    Args:
        obj: The object to convert.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__
