#!/usr/bin/env python3
"""test utils module."""

# import unittest
# from unittest.mock import patch

# from utils import memoize


import unittest
from typing import Mapping, Any, Tuple
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Test class for the access_nested_map utility function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Tuple, expected: Any) -> None:
        """Test that the function returns the expected value for valid inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
# class TestMemoize(unittest.TestCase):
#     """Test class for the memoize decorator."""

#     def test_memoize(self):
#         """Test that memoize decorator caches the result of a function."""

#         class TestClass:
#             def a_method(self):
#                 return 42

#             @memoize
#             def a_property(self):
#                 return self.a_method()

#         with patch('test_utils.TestMemoize.test_memoize.'
#                    'TestClass.a_method') as mock_a_method:
#             # Create an instance of the class
#             instance = TestClass()
#             # Call a_property twice
#             self.assertEqual(instance.a_property, 42)
#             self.assertEqual(instance.a_property, 42)
#             # Assert that a_method was called only once
#             mock_a_method.assert_called_once()
