# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AutocompleteApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_v1_autocomplete(self, prefix, **kwargs):  # noqa: E501
        """Returns a list of suggestions based on search prefix.  # noqa: E501

        Returns a list of suggestions based on search prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_autocomplete(prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str prefix: search prefix (required)
        :param int limit: Number of results to return.
        :param bool explain: Whether to return explanation of results.
        :return: AutocompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v1_autocomplete_with_http_info(prefix, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_autocomplete_with_http_info(prefix, **kwargs)  # noqa: E501
            return data

    def get_v1_autocomplete_with_http_info(self, prefix, **kwargs):  # noqa: E501
        """Returns a list of suggestions based on search prefix.  # noqa: E501

        Returns a list of suggestions based on search prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_autocomplete_with_http_info(prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str prefix: search prefix (required)
        :param int limit: Number of results to return.
        :param bool explain: Whether to return explanation of results.
        :return: AutocompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prefix', 'limit', 'explain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_autocomplete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prefix' is set
        if ('prefix' not in params or
                params['prefix'] is None):
            raise ValueError("Missing the required parameter `prefix` when calling `get_v1_autocomplete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'explain' in params:
            query_params.append(('explain', params['explain']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/autocomplete', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutocompleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_v1_autocomplete(self, body, **kwargs):  # noqa: E501
        """Returns a list of suggestions based on search prefix.  # noqa: E501

        Returns a list of suggestions based on search prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v1_autocomplete(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AutocompleteRequest body: Autocomplete Request (required)
        :return: AutocompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_v1_autocomplete_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_v1_autocomplete_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_v1_autocomplete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Returns a list of suggestions based on search prefix.  # noqa: E501

        Returns a list of suggestions based on search prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v1_autocomplete_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AutocompleteRequest body: Autocomplete Request (required)
        :return: AutocompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_v1_autocomplete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_v1_autocomplete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/autocomplete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutocompleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
