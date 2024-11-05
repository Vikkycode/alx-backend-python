#!/usr/bin/env python3
""" Integration test for GithubOrgClient class """

import unittest
from parameterized import parameterized_class
from unittest.mock import patch, PropertyMock, MagicMock
import requests
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test class for GithubOrgClient class """

    @classmethod
    def setUpClass(cls):
        """ Set up class method """
        cls.get_patcher = patch('requests.get', side_effect=cls.mock_http)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Tear down class method """
        cls.get_patcher.stop()

    @staticmethod
    def mock_http(url: str):
        """ Mock HTTP responses """
        response = MagicMock()
        response.json = MagicMock()
        if url == 'https://api.github.com/orgs/google':
            response.json.return_value = TEST_PAYLOAD[0]
        elif url == 'https://api.github.com/orgs/google/repos':
            response.json.return_value = TEST_PAYLOAD[1]
        return response

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the correct value."""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)

    def test_public_repos(self):
        """ Test public repos method """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = (
                {"repos_url": "https://api.github.com/orgs/google/repos"}
            )
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(),
                             ['episodes.dart', 'cpp-netlib', 'dagger',
                              'ios-webkit-debug-proxy', 'google.github.io',
                              'kratu', 'build-debian-cloud',
                              'traceur-compiler'])

    def test_public_repos_with_license(self):
        """ Test public repos with license argument """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = (
                {"repos_url": "https://api.github.com/orgs/google/repos"}
            )
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(license="apache-2.0"),
                             ['dagger', 'kratu'])
