#!/usr/bin/env python3
"""
Module for util testing
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


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
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),  # 'a' value missing test case
        ({"a": 1}, ("a", "b")),  # 'b' value missing test case
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Unittest for access_nested_map that tests for invalid inputs
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
  
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")  # mocks actual API request call
    def test_get_json(self, test_url, test_payload, mock_request):
        """
        Testing functionality of get_json method using mock API request
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_request.return_value = mock_response
        result = get_json(test_url)
        mock_request.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):

    def test_memoize