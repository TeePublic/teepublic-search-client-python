# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.autocomplete_api import AutocompleteApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAutocompleteApi(unittest.TestCase):
    """AutocompleteApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.autocomplete_api.AutocompleteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_v1_autocomplete(self):
        """Test case for get_v1_autocomplete

        Returns a list of suggestions based on search prefix.  # noqa: E501
        """
        pass

    def test_post_v1_autocomplete(self):
        """Test case for post_v1_autocomplete

        Returns a list of suggestions based on search prefix.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
