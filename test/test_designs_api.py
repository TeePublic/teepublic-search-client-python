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
from swagger_client.api.designs_api import DesignsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDesignsApi(unittest.TestCase):
    """DesignsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.designs_api.DesignsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_v1_similar_designs(self):
        """Test case for post_v1_similar_designs

        Returns a list of discoverable designs based on a reference design and/or primary tag.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
