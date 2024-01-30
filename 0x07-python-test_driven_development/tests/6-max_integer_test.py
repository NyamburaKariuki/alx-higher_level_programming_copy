#!/usr/bin/python3
"""Unittest for max integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test class that defines test cases for max_integer function"""
    def test_positive_ints(self):
        """test positive integers"""
        list1 = [1, 4, 7, 3]
        list2 = [1, 3, 4, 7]
        list3 = [7, 4, 2, 3]
        self.assertEqual(max_integer(list1), 7)
        self.assertEqual(max_integer(list2), 7)
        self.assertEqual(max_integer(list3), 7)

    def test_empty_list(self):
        """tests for an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element(self):
        """test one element in the list"""
        list_1 = [5]
        self.assertEqual(max_integer(list_1), 5)

    def test_string(self):
        """tests for a string"""
        string = "myself"
        self.assertEqual(max_integer(string), 'y')

    def test_empty_string(self):
        """tests for an empty String"""
        string = ""
        self.assertEqual(max_integer(string), None)

    def test_floats(self):
        """tests for floats"""
        list2 = [0.2, 1.0, 4.7]
        self.assertEqual(max_integer(list2), 4.7)

    def test_neg_pos(self):
        """test for negative and positive integers"""
        list1 = [-2, 5, -7, 10]
        self.assertEqual(max_integer(list1), 10)

if __name__ == '__main__':
    unittest.main()
