#!/usr/bin/python3
"""Unit tests for the Rectangle class."""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset setup for each test."""
        pass  # Nothing to reset for Rectangle

    def test_initialization(self):
        """Test initialization of Rectangle with and without id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, 5, 5, 50)
        
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 5)
        self.assertEqual(r2.id, 50)

    def test_width_setter(self):
        """Test the width setter with valid and invalid inputs."""
        r = Rectangle(10, 2)
        r.width = 15
        self.assertEqual(r.width, 15)

        with self.assertRaises(ValueError):
            r.width = -10

        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_setter(self):
        """Test the height setter with valid and invalid inputs."""
        r = Rectangle(10, 2)
        r.height = 12
        self.assertEqual(r.height, 12)

        with self.assertRaises(ValueError):
            r.height = -1

        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_setter(self):
        """Test the x setter with valid and invalid inputs."""
        r = Rectangle(10, 2)
        r.x = 5
        self.assertEqual(r.x, 5)

        with self.assertRaises(ValueError):
            r.x = -5

    def test_y_setter(self):
        """Test the y setter with valid and invalid inputs."""
        r = Rectangle(10, 2)
        r.y = 3
        self.assertEqual(r.y, 3)

        with self.assertRaises(ValueError):
            r.y = -1

    def test_invalid_initialization(self):
        """Test invalid initialization of Rectangle with wrong values."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

        with self.assertRaises(ValueError):
            Rectangle(10, -2)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)


if __name__ == "__main__":
    unittest.main()
