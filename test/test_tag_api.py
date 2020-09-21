# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.tag_api import TagApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTagApi(unittest.TestCase):
    """TagApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tag_api.TagApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_v1_related_tags(self):
        """Test case for get_v1_related_tags

        Gets related tags based on given term(s)  # noqa: E501
        """
        pass

    def test_get_v1_tag_suggestions(self):
        """Test case for get_v1_tag_suggestions

        Returns a list of tag suggestions based on search prefix.  # noqa: E501
        """
        pass

    def test_get_v1_tags(self):
        """Test case for get_v1_tags

        Gets tags data based on name(s)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()