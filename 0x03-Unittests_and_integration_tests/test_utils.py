#!/usr/bin/env python3
"""
parameterized test for unittest
"""
from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """parameterized test for access_nested_map()"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """parameterized test for access_nested_map()"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path,
                                         expected_message):
        """parameterized test to check err message"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check that the exception message matches the expected key
        self.assertEqual(str(context.exception), f"'{expected_message}'")


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        mocking requests.get
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # call the function
        result = get_json(test_url)

        # test
        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestClass:
    """ test class for the test"""
    def a_method(self):
        """test method for the test"""
        return 42

    @memoize
    def a_property(self):
        """test method for the test"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator"""
    @patch("test_utils.TestClass.a_method")
    def test_memoize(self, mock_method):
        """Test that a_property caches the result of a_method."""
        mock_method.return_value = 42

        obj = TestClass()

        # act
        result1 = obj.a_property
        result2 = obj.a_property

        # Assert
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_method.assert_called_once()
