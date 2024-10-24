#!/usr/bin/python3
"""Rectangle module that inherits from Base."""

from models.base import Base

class Rectangle(Base):
    """Represents a Rectangle that inherits from Base class.

    Attributes:
        __width (int): Width of the rectangle (private).
        __height (int): Height of the rectangle (private).
        __x (int): X position (private).
        __y (int): Y position (private).
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X position of the rectangle.
            y (int): Y position of the rectangle.
            id (int): id of the instance, inherited from Base. Defaults to None
        """
        super().__init__(id)  # Call the constructor of Base
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getters
    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    # Setters
    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("width must be an integer greater than 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("height must be an integer greater than 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("x must be an integer greater than or equal to 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("y must be an integer greater than or equal to 0")
        self.__y = value
