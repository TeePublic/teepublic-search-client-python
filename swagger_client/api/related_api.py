# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RelatedApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_v1_related_search(self, search_term, **kwargs):  # noqa: E501
        """Gets related searches based on given term  # noqa: E501

        Gets related searches based on given term  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_related_search(search_term, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_term: Search term to pull related searches from (required)
        :return: list[RelatedResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v1_related_search_with_http_info(search_term, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_related_search_with_http_info(search_term, **kwargs)  # noqa: E501
            return data

    def get_v1_related_search_with_http_info(self, search_term, **kwargs):  # noqa: E501
        """Gets related searches based on given term  # noqa: E501

        Gets related searches based on given term  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_related_search_with_http_info(search_term, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_term: Search term to pull related searches from (required)
        :return: list[RelatedResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_term']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_related_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_term' is set
        if ('search_term' not in params or
                params['search_term'] is None):
            raise ValueError("Missing the required parameter `search_term` when calling `get_v1_related_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_term' in params:
            query_params.append(('search_term', params['search_term']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/related-search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RelatedResult]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)