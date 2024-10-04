import math


class MagicClass:
    """A class to represent a circle with a given radius."""

    def __init__(self, radius=0):
        """Initialize the circle with the given radius."""
        self.__radius = 0  # Set default radius to 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.__radius
