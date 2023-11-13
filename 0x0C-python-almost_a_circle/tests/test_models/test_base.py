#!/usr/bin/python3
"""Test case"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseInstantiation(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    # Add more instantiation test cases here

class TestBaseToJsonString(unittest.TestCase):
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    # Add more to_json_string test cases here

class TestBaseSaveToFile(unittest.TestCase):
    @classmethod
    def tearDown(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    # Add more save_to_file test cases here

class TestBaseFromJsonString(unittest.TestCase):
    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    # Add more from_json_string test cases here

class TestBaseCreate(unittest.TestCase):
    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    # Add more create test cases here

# Add more test classes for other methods as needed

if __name__ == "__main__":
    unittest.main()
