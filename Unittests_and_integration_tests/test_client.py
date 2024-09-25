#!/usr/bin/env python3
"""
Test module client.py methods
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GitHubOrgClient class
    """
    #  Parametize input values
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    #  Patch get_json to mock
    @patch("client.get_json")
    def test_org(self, org_name, expected_value, mock_json):
        """
        Tests whether githubclient.org returns correct value
        and only called once
        """
        #  Set return value of mock json call
        mock_json.return_value = expected_value
        client = GithubOrgClient(org_name)
        #  call .org method
        result = client.org
        #  Test to ensure get_json called one time only
        mock_json.assert_called_once()
        #  Test to ensure expected value matches result
        self.assertEqual(result, expected_value)

    def test_public_repos_url(self):
        """
        Tests public_repos_url property
        """
        mock_payload = {"repos_url":
                        "https://api.github.com/orgs/test-org/repos"}
        #  Mock 'org' property with PropertyMock
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_payload

            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            #  Test to see that result matches repos_url from mock payload
            self.assertEqual(result, mock_payload["repos_url"])
            #  Make sure mock_org property only called once
            mock_org.assert_called_once()
