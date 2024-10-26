#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x-coordinate with validation."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y-coordinate with validation."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with the character #, considering x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a formatted string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes in a specific order if *args is provided.
        If *args is empty, assigns attributes using **kwargs.
        1st argument: id
        2nd argument: width
        3rd argument: height
        4th argument: x
        5th argument: y
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
