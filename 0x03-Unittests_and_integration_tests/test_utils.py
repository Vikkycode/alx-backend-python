#!/usr/bin/env python3
"""test utils module."""

import unittest
from typing import Mapping, Any, Tuple
import unittest
from unittest.mock import patch
from parameterized import parameterized

from utils import get_json

class TestGetJson(unittest.TestCase):
    """Test class for the get_json utility function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that utils.get_json returns the expected result."""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
