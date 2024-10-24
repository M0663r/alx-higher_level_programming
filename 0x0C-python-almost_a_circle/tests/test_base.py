#!/usr/bin/python3
"""Unit test for the Base class."""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_no_id(self):
        """Test that id is correctly assigned when no id is provided."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_provided(self):
        """Test that id is correctly assigned when an id is provided."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_mixed_ids(self):
        """Test a mix of provided and automatic ids."""
        b1 = Base()
        b2 = Base(24)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 24)
        self.assertEqual(b3.id, 2)

if __name__ == '__main__':
    unittest.main()
