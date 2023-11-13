#!/usr/bin/python3
"""Test cases"""

import unittest
import io
from unittest import mock
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):
    def test_init(self):
        """Test the initialization of Rectangle."""
        r = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 5)

    def test_area(self):
        """Test the area method of Rectangle."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        """Test the display method of Rectangle."""
        r = Rectangle(3, 2, 1, 1)
        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            expected_output = "\n ###\n ###\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        """Test the update method of Rectangle."""
        r = Rectangle(3, 4)
        r.update(1, 2, 5, 6, 7)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)

    def test_to_dictionary(self):
        """Test the to_dictionary method of Rectangle."""
        r = Rectangle(3, 4, 1, 2, 5)
        expected_dict = {'id': 5, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_csv_row(self):
        """Test the to_csv_row method of Rectangle."""
        r = Rectangle(3, 4, 1, 2, 5)
        expected_row = [5, 3, 4, 1, 2]
        self.assertEqual(r.to_csv_row(), expected_row)

if __name__ == '__main__':
    unittest.main()
