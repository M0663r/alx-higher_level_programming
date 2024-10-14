#!/usr/bin/python3
"""
This module defines a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.
    Raises a TypeError if the inputs are neither integers nor floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)
    
    return a + b
