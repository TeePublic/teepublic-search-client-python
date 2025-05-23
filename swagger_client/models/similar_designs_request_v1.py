# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.48
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class SimilarDesignsRequestV1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ref_design_id': 'int',
        'search_terms': 'str',
        'sort': 'str',
        'tags_filter': 'list[str]',
        'canvases': 'list[str]',
        'artist_filter': 'list[int]',
        'per_page': 'int',
        'page_offset': 'int',
        'explain': 'bool',
        'es_explain': 'bool',
        'relevancy_config_id': 'str',
        'bucket': 'str',
        'safe_search': 'bool'
    }

    attribute_map = {
        'ref_design_id': 'ref_design_id',
        'search_terms': 'search_terms',
        'sort': 'sort',
        'tags_filter': 'tags_filter',
        'canvases': 'canvases',
        'artist_filter': 'artist_filter',
        'per_page': 'per_page',
        'page_offset': 'page_offset',
        'explain': 'explain',
        'es_explain': 'es_explain',
        'relevancy_config_id': 'relevancy_config_id',
        'bucket': 'bucket',
        'safe_search': 'safe_search'
    }

    def __init__(self, ref_design_id=None, search_terms=None, sort='relevance', tags_filter=None, canvases=None, artist_filter=None, per_page=36, page_offset=1, explain=False, es_explain=False, relevancy_config_id=None, bucket=None, safe_search=True, _configuration=None):  # noqa: E501
        """SimilarDesignsRequestV1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ref_design_id = None
        self._search_terms = None
        self._sort = None
        self._tags_filter = None
        self._canvases = None
        self._artist_filter = None
        self._per_page = None
        self._page_offset = None
        self._explain = None
        self._es_explain = None
        self._relevancy_config_id = None
        self._bucket = None
        self._safe_search = None
        self.discriminator = None

        if ref_design_id is not None:
            self.ref_design_id = ref_design_id
        if search_terms is not None:
            self.search_terms = search_terms
        if sort is not None:
            self.sort = sort
        if tags_filter is not None:
            self.tags_filter = tags_filter
        if canvases is not None:
            self.canvases = canvases
        if artist_filter is not None:
            self.artist_filter = artist_filter
        if per_page is not None:
            self.per_page = per_page
        if page_offset is not None:
            self.page_offset = page_offset
        if explain is not None:
            self.explain = explain
        if es_explain is not None:
            self.es_explain = es_explain
        if relevancy_config_id is not None:
            self.relevancy_config_id = relevancy_config_id
        if bucket is not None:
            self.bucket = bucket
        if safe_search is not None:
            self.safe_search = safe_search

    @property
    def ref_design_id(self):
        """Gets the ref_design_id of this SimilarDesignsRequestV1.  # noqa: E501

        reference design id  # noqa: E501

        :return: The ref_design_id of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: int
        """
        return self._ref_design_id

    @ref_design_id.setter
    def ref_design_id(self, ref_design_id):
        """Sets the ref_design_id of this SimilarDesignsRequestV1.

        reference design id  # noqa: E501

        :param ref_design_id: The ref_design_id of this SimilarDesignsRequestV1.  # noqa: E501
        :type: int
        """

        self._ref_design_id = ref_design_id

    @property
    def search_terms(self):
        """Gets the search_terms of this SimilarDesignsRequestV1.  # noqa: E501

        Search terms.  # noqa: E501

        :return: The search_terms of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: str
        """
        return self._search_terms

    @search_terms.setter
    def search_terms(self, search_terms):
        """Sets the search_terms of this SimilarDesignsRequestV1.

        Search terms.  # noqa: E501

        :param search_terms: The search_terms of this SimilarDesignsRequestV1.  # noqa: E501
        :type: str
        """

        self._search_terms = search_terms

    @property
    def sort(self):
        """Gets the sort of this SimilarDesignsRequestV1.  # noqa: E501

        Sort order  # noqa: E501

        :return: The sort of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this SimilarDesignsRequestV1.

        Sort order  # noqa: E501

        :param sort: The sort of this SimilarDesignsRequestV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["relevance", "popular", "newest"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort not in allowed_values):
            raise ValueError(
                "Invalid value for `sort` ({0}), must be one of {1}"  # noqa: E501
                .format(sort, allowed_values)
            )

        self._sort = sort

    @property
    def tags_filter(self):
        """Gets the tags_filter of this SimilarDesignsRequestV1.  # noqa: E501

        Design tags filter.  # noqa: E501

        :return: The tags_filter of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags_filter

    @tags_filter.setter
    def tags_filter(self, tags_filter):
        """Sets the tags_filter of this SimilarDesignsRequestV1.

        Design tags filter.  # noqa: E501

        :param tags_filter: The tags_filter of this SimilarDesignsRequestV1.  # noqa: E501
        :type: list[str]
        """

        self._tags_filter = tags_filter

    @property
    def canvases(self):
        """Gets the canvases of this SimilarDesignsRequestV1.  # noqa: E501

        product filter  # noqa: E501

        :return: The canvases of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._canvases

    @canvases.setter
    def canvases(self, canvases):
        """Sets the canvases of this SimilarDesignsRequestV1.

        product filter  # noqa: E501

        :param canvases: The canvases of this SimilarDesignsRequestV1.  # noqa: E501
        :type: list[str]
        """

        self._canvases = canvases

    @property
    def artist_filter(self):
        """Gets the artist_filter of this SimilarDesignsRequestV1.  # noqa: E501

        artist ids.  # noqa: E501

        :return: The artist_filter of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: list[int]
        """
        return self._artist_filter

    @artist_filter.setter
    def artist_filter(self, artist_filter):
        """Sets the artist_filter of this SimilarDesignsRequestV1.

        artist ids.  # noqa: E501

        :param artist_filter: The artist_filter of this SimilarDesignsRequestV1.  # noqa: E501
        :type: list[int]
        """

        self._artist_filter = artist_filter

    @property
    def per_page(self):
        """Gets the per_page of this SimilarDesignsRequestV1.  # noqa: E501

        Number of results to return per page.  # noqa: E501

        :return: The per_page of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this SimilarDesignsRequestV1.

        Number of results to return per page.  # noqa: E501

        :param per_page: The per_page of this SimilarDesignsRequestV1.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def page_offset(self):
        """Gets the page_offset of this SimilarDesignsRequestV1.  # noqa: E501

        Page offset to fetch.  # noqa: E501

        :return: The page_offset of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: int
        """
        return self._page_offset

    @page_offset.setter
    def page_offset(self, page_offset):
        """Sets the page_offset of this SimilarDesignsRequestV1.

        Page offset to fetch.  # noqa: E501

        :param page_offset: The page_offset of this SimilarDesignsRequestV1.  # noqa: E501
        :type: int
        """

        self._page_offset = page_offset

    @property
    def explain(self):
        """Gets the explain of this SimilarDesignsRequestV1.  # noqa: E501

        whether to return explanation of search results.  # noqa: E501

        :return: The explain of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: bool
        """
        return self._explain

    @explain.setter
    def explain(self, explain):
        """Sets the explain of this SimilarDesignsRequestV1.

        whether to return explanation of search results.  # noqa: E501

        :param explain: The explain of this SimilarDesignsRequestV1.  # noqa: E501
        :type: bool
        """

        self._explain = explain

    @property
    def es_explain(self):
        """Gets the es_explain of this SimilarDesignsRequestV1.  # noqa: E501

        whether to return elasticsearch explanation of search results.  # noqa: E501

        :return: The es_explain of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: bool
        """
        return self._es_explain

    @es_explain.setter
    def es_explain(self, es_explain):
        """Sets the es_explain of this SimilarDesignsRequestV1.

        whether to return elasticsearch explanation of search results.  # noqa: E501

        :param es_explain: The es_explain of this SimilarDesignsRequestV1.  # noqa: E501
        :type: bool
        """

        self._es_explain = es_explain

    @property
    def relevancy_config_id(self):
        """Gets the relevancy_config_id of this SimilarDesignsRequestV1.  # noqa: E501

        Relevancy config id.  # noqa: E501

        :return: The relevancy_config_id of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: str
        """
        return self._relevancy_config_id

    @relevancy_config_id.setter
    def relevancy_config_id(self, relevancy_config_id):
        """Sets the relevancy_config_id of this SimilarDesignsRequestV1.

        Relevancy config id.  # noqa: E501

        :param relevancy_config_id: The relevancy_config_id of this SimilarDesignsRequestV1.  # noqa: E501
        :type: str
        """

        self._relevancy_config_id = relevancy_config_id

    @property
    def bucket(self):
        """Gets the bucket of this SimilarDesignsRequestV1.  # noqa: E501

        AB test bucket.  # noqa: E501

        :return: The bucket of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this SimilarDesignsRequestV1.

        AB test bucket.  # noqa: E501

        :param bucket: The bucket of this SimilarDesignsRequestV1.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def safe_search(self):
        """Gets the safe_search of this SimilarDesignsRequestV1.  # noqa: E501

        whether we include mature designs in search results.  # noqa: E501

        :return: The safe_search of this SimilarDesignsRequestV1.  # noqa: E501
        :rtype: bool
        """
        return self._safe_search

    @safe_search.setter
    def safe_search(self, safe_search):
        """Sets the safe_search of this SimilarDesignsRequestV1.

        whether we include mature designs in search results.  # noqa: E501

        :param safe_search: The safe_search of this SimilarDesignsRequestV1.  # noqa: E501
        :type: bool
        """

        self._safe_search = safe_search

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SimilarDesignsRequestV1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SimilarDesignsRequestV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimilarDesignsRequestV1):
            return True

        return self.to_dict() != other.to_dict()
