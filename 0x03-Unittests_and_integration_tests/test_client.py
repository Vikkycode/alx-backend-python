#!/usr/bin/env python3
""" tset gibuorgclient module"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, mock_get_json.return_value)
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct value."""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_url"}
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url, "test_url")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected list of repositories."""
        mock_get_json.return_value = TEST_PAYLOAD[1]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = TEST_PAYLOAD[0]['repos_url']
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(),
                             ['episodes.dart', 'cpp-netlib', 'dagger',
                              'ios-webkit-debug-proxy', 'google.github.io',
                              'kratu', 'build-debian-cloud',
                              'traceur-compiler'])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
