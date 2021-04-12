# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RelevancyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_v1_relevancy_configuration(self, config_id, **kwargs):  # noqa: E501
        """Deletes search relevancy configuration.  # noqa: E501

        Deletes search relevancy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_v1_relevancy_configuration(config_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_id: search relevancy configuration id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_v1_relevancy_configuration_with_http_info(config_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_v1_relevancy_configuration_with_http_info(config_id, **kwargs)  # noqa: E501
            return data

    def delete_v1_relevancy_configuration_with_http_info(self, config_id, **kwargs):  # noqa: E501
        """Deletes search relevancy configuration.  # noqa: E501

        Deletes search relevancy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_v1_relevancy_configuration_with_http_info(config_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_id: search relevancy configuration id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_v1_relevancy_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_id' is set
        if self.api_client.client_side_validation and ('config_id' not in params or
                                                       params['config_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `config_id` when calling `delete_v1_relevancy_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'config_id' in params:
            path_params['config_id'] = params['config_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/relevancy-configurations/{config_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v1_relevancy_configuration(self, config_id, **kwargs):  # noqa: E501
        """Gets a search relevancy configuration.  # noqa: E501

        Gets a search relevancy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_relevancy_configuration(config_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_id: search relevancy configuration id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v1_relevancy_configuration_with_http_info(config_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_relevancy_configuration_with_http_info(config_id, **kwargs)  # noqa: E501
            return data

    def get_v1_relevancy_configuration_with_http_info(self, config_id, **kwargs):  # noqa: E501
        """Gets a search relevancy configuration.  # noqa: E501

        Gets a search relevancy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_relevancy_configuration_with_http_info(config_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_id: search relevancy configuration id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_relevancy_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_id' is set
        if self.api_client.client_side_validation and ('config_id' not in params or
                                                       params['config_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `config_id` when calling `get_v1_relevancy_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'config_id' in params:
            path_params['config_id'] = params['config_id']  # noqa: E501

        query_params = []

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
            '/v1/relevancy-configurations/{config_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v1_relevancy_configurations(self, **kwargs):  # noqa: E501
        """Gets all relevancy configurations.  # noqa: E501

        Gets all relevancy configurations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_relevancy_configurations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v1_relevancy_configurations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_relevancy_configurations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_v1_relevancy_configurations_with_http_info(self, **kwargs):  # noqa: E501
        """Gets all relevancy configurations.  # noqa: E501

        Gets all relevancy configurations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_relevancy_configurations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_relevancy_configurations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/v1/relevancy-configurations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_v1_relevancy_configurations(self, body, **kwargs):  # noqa: E501
        """Saves search relevancy configuration.  # noqa: E501

        Saves search relevancy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v1_relevancy_configurations(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: Relevancy Configuration (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_v1_relevancy_configurations_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_v1_relevancy_configurations_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_v1_relevancy_configurations_with_http_info(self, body, **kwargs):  # noqa: E501
        """Saves search relevancy configuration.  # noqa: E501

        Saves search relevancy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v1_relevancy_configurations_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: Relevancy Configuration (required)
        :return: None
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
                    " to method post_v1_relevancy_configurations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `post_v1_relevancy_configurations`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/relevancy-configurations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_v1_relevancy_configuration(self, config_id, body, **kwargs):  # noqa: E501
        """Updates search relevancy configuration.  # noqa: E501

        Updates search relevancy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_v1_relevancy_configuration(config_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_id: search relevancy configuration id (required)
        :param object body: Relevancy Configuration (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_v1_relevancy_configuration_with_http_info(config_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_v1_relevancy_configuration_with_http_info(config_id, body, **kwargs)  # noqa: E501
            return data

    def put_v1_relevancy_configuration_with_http_info(self, config_id, body, **kwargs):  # noqa: E501
        """Updates search relevancy configuration.  # noqa: E501

        Updates search relevancy configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_v1_relevancy_configuration_with_http_info(config_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str config_id: search relevancy configuration id (required)
        :param object body: Relevancy Configuration (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['config_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_v1_relevancy_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_id' is set
        if self.api_client.client_side_validation and ('config_id' not in params or
                                                       params['config_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `config_id` when calling `put_v1_relevancy_configuration`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `put_v1_relevancy_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'config_id' in params:
            path_params['config_id'] = params['config_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/relevancy-configurations/{config_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
