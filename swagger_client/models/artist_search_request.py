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


class ArtistSearchRequest(object):
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
        'artist_query': 'str',
        'sort': 'str',
        'canvases': 'list[str]',
        'per_page': 'int',
        'page_offset': 'int',
        'explain': 'bool',
        'es_explain': 'bool',
        'bucket': 'str',
        'safe_search': 'bool'
    }

    attribute_map = {
        'artist_query': 'artist_query',
        'sort': 'sort',
        'canvases': 'canvases',
        'per_page': 'per_page',
        'page_offset': 'page_offset',
        'explain': 'explain',
        'es_explain': 'es_explain',
        'bucket': 'bucket',
        'safe_search': 'safe_search'
    }

    def __init__(self, artist_query=None, sort='relevance', canvases=None, per_page=36, page_offset=1, explain=False, es_explain=False, bucket=None, safe_search=True, _configuration=None):  # noqa: E501
        """ArtistSearchRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._artist_query = None
        self._sort = None
        self._canvases = None
        self._per_page = None
        self._page_offset = None
        self._explain = None
        self._es_explain = None
        self._bucket = None
        self._safe_search = None
        self.discriminator = None

        if artist_query is not None:
            self.artist_query = artist_query
        if sort is not None:
            self.sort = sort
        if canvases is not None:
            self.canvases = canvases
        if per_page is not None:
            self.per_page = per_page
        if page_offset is not None:
            self.page_offset = page_offset
        if explain is not None:
            self.explain = explain
        if es_explain is not None:
            self.es_explain = es_explain
        if bucket is not None:
            self.bucket = bucket
        if safe_search is not None:
            self.safe_search = safe_search

    @property
    def artist_query(self):
        """Gets the artist_query of this ArtistSearchRequest.  # noqa: E501

        Search terms.  # noqa: E501

        :return: The artist_query of this ArtistSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._artist_query

    @artist_query.setter
    def artist_query(self, artist_query):
        """Sets the artist_query of this ArtistSearchRequest.

        Search terms.  # noqa: E501

        :param artist_query: The artist_query of this ArtistSearchRequest.  # noqa: E501
        :type: str
        """

        self._artist_query = artist_query

    @property
    def sort(self):
        """Gets the sort of this ArtistSearchRequest.  # noqa: E501

        Sort order  # noqa: E501

        :return: The sort of this ArtistSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ArtistSearchRequest.

        Sort order  # noqa: E501

        :param sort: The sort of this ArtistSearchRequest.  # noqa: E501
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
    def canvases(self):
        """Gets the canvases of this ArtistSearchRequest.  # noqa: E501

        product filter  # noqa: E501

        :return: The canvases of this ArtistSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._canvases

    @canvases.setter
    def canvases(self, canvases):
        """Sets the canvases of this ArtistSearchRequest.

        product filter  # noqa: E501

        :param canvases: The canvases of this ArtistSearchRequest.  # noqa: E501
        :type: list[str]
        """

        self._canvases = canvases

    @property
    def per_page(self):
        """Gets the per_page of this ArtistSearchRequest.  # noqa: E501

        Number of results to return per page.  # noqa: E501

        :return: The per_page of this ArtistSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this ArtistSearchRequest.

        Number of results to return per page.  # noqa: E501

        :param per_page: The per_page of this ArtistSearchRequest.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def page_offset(self):
        """Gets the page_offset of this ArtistSearchRequest.  # noqa: E501

        Page offset to fetch.  # noqa: E501

        :return: The page_offset of this ArtistSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_offset

    @page_offset.setter
    def page_offset(self, page_offset):
        """Sets the page_offset of this ArtistSearchRequest.

        Page offset to fetch.  # noqa: E501

        :param page_offset: The page_offset of this ArtistSearchRequest.  # noqa: E501
        :type: int
        """

        self._page_offset = page_offset

    @property
    def explain(self):
        """Gets the explain of this ArtistSearchRequest.  # noqa: E501

        whether to return explanation of search results.  # noqa: E501

        :return: The explain of this ArtistSearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._explain

    @explain.setter
    def explain(self, explain):
        """Sets the explain of this ArtistSearchRequest.

        whether to return explanation of search results.  # noqa: E501

        :param explain: The explain of this ArtistSearchRequest.  # noqa: E501
        :type: bool
        """

        self._explain = explain

    @property
    def es_explain(self):
        """Gets the es_explain of this ArtistSearchRequest.  # noqa: E501

        whether to return elasticsearch explanation of search results.  # noqa: E501

        :return: The es_explain of this ArtistSearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._es_explain

    @es_explain.setter
    def es_explain(self, es_explain):
        """Sets the es_explain of this ArtistSearchRequest.

        whether to return elasticsearch explanation of search results.  # noqa: E501

        :param es_explain: The es_explain of this ArtistSearchRequest.  # noqa: E501
        :type: bool
        """

        self._es_explain = es_explain

    @property
    def bucket(self):
        """Gets the bucket of this ArtistSearchRequest.  # noqa: E501

        AB test bucket.  # noqa: E501

        :return: The bucket of this ArtistSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ArtistSearchRequest.

        AB test bucket.  # noqa: E501

        :param bucket: The bucket of this ArtistSearchRequest.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def safe_search(self):
        """Gets the safe_search of this ArtistSearchRequest.  # noqa: E501

        whether we include mature designs in search results.  # noqa: E501

        :return: The safe_search of this ArtistSearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._safe_search

    @safe_search.setter
    def safe_search(self, safe_search):
        """Sets the safe_search of this ArtistSearchRequest.

        whether we include mature designs in search results.  # noqa: E501

        :param safe_search: The safe_search of this ArtistSearchRequest.  # noqa: E501
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
        if issubclass(ArtistSearchRequest, dict):
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
        if not isinstance(other, ArtistSearchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArtistSearchRequest):
            return True

        return self.to_dict() != other.to_dict()
