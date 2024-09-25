#!/usr/bin/env python3
"""
Module for util testing
"""
import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # nested_map, path, and expected values
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Unittest for access_nested_map that validates expected values
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),  # 'a' value missing test case
        ({"a": 1}, ("a", "b")),  # 'b' value missing test case
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Unittest for access_nested_map that tests for invalid inputs
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
