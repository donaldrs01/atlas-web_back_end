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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test public_repos method of GithubOrgClient class
        """
        #  mock payload that resembles a list of repos
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        #  get_json returns mock payload entry
        mock_get_json.return_value = mock_payload
        #  mock public_repos_url to return test URL
        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock, 
                          return_value ="https://api.github.com/orgs/test-org/repos") as mock_public_repos_url:
        
            client = GithubOrgClient("test-org")
            result = client.public_repos()
            expected_result = ["repo1", "repo2", "repo3"]

            self.assertEqual(result, expected_result)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        #  include expected return value at end
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Unit test for has_license method
        """
        #  Create client instance and call has_license method on it
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        #  Check that license result matches expected result
        self.assertEqual(result, expected)

class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient integration tests
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up for test class to mock requests.get
        """
        #  Store patch object and patch HTTP requests
        cls.get_patcher = patch("requests.get")
        cls.get_patcher.start()