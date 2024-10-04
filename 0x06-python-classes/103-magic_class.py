#!/usr/bin/python3
"""
This module defines a class `MagicClass` that represents a circle and
provides methods to compute the area and circumference of the circle.

The class ensures that the radius provided is a valid number (either an
integer or a float) and raises an appropriate error otherwise.

Classes:
    MagicClass: A class to represent a circle.

Methods:
    __init__(self, radius=0): Initializes the `MagicClass` instance
    area(self): Returns the area of the circle.
    circumference(self): Returns the circumference of the circle.
"""

import math


class MagicClass:
    """
    A class used to represent a Circle.

    Attributes:
        __radius (float or int): The radius of the circle, initialized to 0.

    Methods:
        __init__(self, radius=0):
            Initializes the circle with a given radius. Raises a TypeError
            if the radius
            is not a number (either integer or float).

        area(self):
            Computes and returns the area of the circle.

        circumference(self):
            Computes and returns the circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initialize the MagicClass with a given radius.

        Args:
            radius (float or int, optional): The radius of the circle.

        Raises:
            TypeError: If `radius` is not an integer or float.

        Example:
            >>> magic_circle = MagicClass(5)
            >>> magic_circle.__radius
            5
        """
        self.__radius = 0  # Set default radius to 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle calculated as π * radius^2.

        Example:
            >>> magic_circle = MagicClass(5)
            >>> magic_circle.area()
            78.53981633974483
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle calculated.

        Example:
            >>> magic_circle = MagicClass(5)
            >>> magic_circle.circumference()
            31.41592653589793
        """
        return 2 * math.pi * self.__radius
