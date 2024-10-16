#!/usr/bin/python3
"""
This module contains the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
