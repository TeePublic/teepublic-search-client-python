# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TagApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_v1_design_tags(self, design_id, **kwargs):  # noqa: E501
        """Gets tags for a design  # noqa: E501

        Gets tags for a design  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_design_tags(design_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int design_id: Design id to pull tags for (required)
        :return: DesignTagsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v1_design_tags_with_http_info(design_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_design_tags_with_http_info(design_id, **kwargs)  # noqa: E501
            return data

    def get_v1_design_tags_with_http_info(self, design_id, **kwargs):  # noqa: E501
        """Gets tags for a design  # noqa: E501

        Gets tags for a design  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_design_tags_with_http_info(design_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int design_id: Design id to pull tags for (required)
        :return: DesignTagsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['design_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_design_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'design_id' is set
        if ('design_id' not in params or
                params['design_id'] is None):
            raise ValueError("Missing the required parameter `design_id` when calling `get_v1_design_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'design_id' in params:
            query_params.append(('design_id', params['design_id']))  # noqa: E501

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
            '/v1/design-tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DesignTagsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v1_related_tags(self, tag_list, **kwargs):  # noqa: E501
        """Gets related tags based on given term(s)  # noqa: E501

        Gets related tags based on given term(s)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_related_tags(tag_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_list: Tag list to pull from related tags from (required)
        :param int minimum_taggings: minimum number of taggings required for return
        :param bool include_deleted: Only return tags that are not soft deleted
        :return: RelatedTagResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v1_related_tags_with_http_info(tag_list, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_related_tags_with_http_info(tag_list, **kwargs)  # noqa: E501
            return data

    def get_v1_related_tags_with_http_info(self, tag_list, **kwargs):  # noqa: E501
        """Gets related tags based on given term(s)  # noqa: E501

        Gets related tags based on given term(s)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_related_tags_with_http_info(tag_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_list: Tag list to pull from related tags from (required)
        :param int minimum_taggings: minimum number of taggings required for return
        :param bool include_deleted: Only return tags that are not soft deleted
        :return: RelatedTagResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_list', 'minimum_taggings', 'include_deleted']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_related_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_list' is set
        if ('tag_list' not in params or
                params['tag_list'] is None):
            raise ValueError("Missing the required parameter `tag_list` when calling `get_v1_related_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag_list' in params:
            query_params.append(('tag_list', params['tag_list']))  # noqa: E501
        if 'minimum_taggings' in params:
            query_params.append(('minimum_taggings', params['minimum_taggings']))  # noqa: E501
        if 'include_deleted' in params:
            query_params.append(('include_deleted', params['include_deleted']))  # noqa: E501

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
            '/v1/related-tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RelatedTagResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v1_tag_suggestions(self, prefix, **kwargs):  # noqa: E501
        """Returns a list of tag suggestions based on search prefix.  # noqa: E501

        Returns a list of tag suggestions based on search prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_tag_suggestions(prefix, async_req=True)
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
            return self.get_v1_tag_suggestions_with_http_info(prefix, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_tag_suggestions_with_http_info(prefix, **kwargs)  # noqa: E501
            return data

    def get_v1_tag_suggestions_with_http_info(self, prefix, **kwargs):  # noqa: E501
        """Returns a list of tag suggestions based on search prefix.  # noqa: E501

        Returns a list of tag suggestions based on search prefix.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_tag_suggestions_with_http_info(prefix, async_req=True)
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
                    " to method get_v1_tag_suggestions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prefix' is set
        if ('prefix' not in params or
                params['prefix'] is None):
            raise ValueError("Missing the required parameter `prefix` when calling `get_v1_tag_suggestions`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/tag-suggestions', 'GET',
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

    def get_v1_tags(self, tag_names_list, **kwargs):  # noqa: E501
        """Gets tags data based on name(s)  # noqa: E501

        Gets tags data based on name(s)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_tags(tag_names_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_names_list: comma separated list of tag names (required)
        :return: TagsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_v1_tags_with_http_info(tag_names_list, **kwargs)  # noqa: E501
        else:
            (data) = self.get_v1_tags_with_http_info(tag_names_list, **kwargs)  # noqa: E501
            return data

    def get_v1_tags_with_http_info(self, tag_names_list, **kwargs):  # noqa: E501
        """Gets tags data based on name(s)  # noqa: E501

        Gets tags data based on name(s)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v1_tags_with_http_info(tag_names_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_names_list: comma separated list of tag names (required)
        :return: TagsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_names_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_names_list' is set
        if ('tag_names_list' not in params or
                params['tag_names_list'] is None):
            raise ValueError("Missing the required parameter `tag_names_list` when calling `get_v1_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag_names_list' in params:
            query_params.append(('tag_names_list', params['tag_names_list']))  # noqa: E501

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
            '/v1/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
