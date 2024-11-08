#!/usr/bin/env python3
"""

"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import Mock, patch, MagicMock
from utils import get_json, memoize


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        # Define the mock return value for the get_json function
        mock_org_data = {"login": org_name}
        mock_get_json.return_value = mock_org_data

        # Initialize the client with the org name
        client = GithubOrgClient(org_name)

        # Call the org method and verify it returns the expected data
        org_data = client.org
        self.assertEqual(org_data, mock_org_data)

        # Ensure get_json was called exactly once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch("client.GithubOrgClient.org",
           new_callable=lambda: {"repos_url": "https://api.github.com/repos"})
    def test_public_repos_url(self, mock_org):
        """Test that the _public_repos_url
        property returns the correct value."""

        # Initialize the client
        client = GithubOrgClient("test-org")

        # Check that the _public_repos_url property returns the expected value
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/repos")
