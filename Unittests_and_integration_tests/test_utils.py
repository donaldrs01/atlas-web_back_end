#!/usr/bin/env python3
"""
Module for util testing
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for testing the access_nested_map method
    """
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
    """
    Test class for testing the get_json method
    """

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
    """
    Test class for testing the memoize method
    """

    def test_memoize(self):
        """
        Testing functionality of memoize method
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        # Patch a_method to return 42
        with patch.object(TestClass, "a_method") as mock_method:
            mock_method.return_value = 42
            res1 = test_instance.a_property
            #  Due to memoization, this should return cached result (res1)
            res2 = test_instance.a_property
            #  Becauase of memoization, a_method only called once
            mock_method.assert_called_once()

            #  Because of caching, results of two test
            # instances should be the same
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
