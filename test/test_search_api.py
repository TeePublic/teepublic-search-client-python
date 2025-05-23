# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.48
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.search_api import SearchApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_artist_search(self):
        """Test case for post_artist_search

        Performs search on active designs by artist  # noqa: E501
        """
        pass

    def test_post_v2_dmca_search(self):
        """Test case for post_v2_dmca_search

        Performs search on publishable designs.  # noqa: E501
        """
        pass

    def test_post_v2_search(self):
        """Test case for post_v2_search

        Returns a list of discoverable designs based on search query.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
