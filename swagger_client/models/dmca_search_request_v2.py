# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class DmcaSearchRequestV2(object):
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
        'search_terms': 'str',
        'teepublic_approved': 'bool',
        'teepublic_unapproved': 'bool',
        'artist_id': 'int',
        'per_page': 'int',
        'page_offset': 'int',
        'sort': 'str'
    }

    attribute_map = {
        'search_terms': 'search_terms',
        'teepublic_approved': 'teepublic_approved',
        'teepublic_unapproved': 'teepublic_unapproved',
        'artist_id': 'artist_id',
        'per_page': 'per_page',
        'page_offset': 'page_offset',
        'sort': 'sort'
    }

    def __init__(self, search_terms=None, teepublic_approved=True, teepublic_unapproved=False, artist_id=None, per_page=36, page_offset=1, sort='relevance', _configuration=None):  # noqa: E501
        """DmcaSearchRequestV2 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._search_terms = None
        self._teepublic_approved = None
        self._teepublic_unapproved = None
        self._artist_id = None
        self._per_page = None
        self._page_offset = None
        self._sort = None
        self.discriminator = None

        if search_terms is not None:
            self.search_terms = search_terms
        if teepublic_approved is not None:
            self.teepublic_approved = teepublic_approved
        if teepublic_unapproved is not None:
            self.teepublic_unapproved = teepublic_unapproved
        if artist_id is not None:
            self.artist_id = artist_id
        if per_page is not None:
            self.per_page = per_page
        if page_offset is not None:
            self.page_offset = page_offset
        if sort is not None:
            self.sort = sort

    @property
    def search_terms(self):
        """Gets the search_terms of this DmcaSearchRequestV2.  # noqa: E501

        Search terms.  # noqa: E501

        :return: The search_terms of this DmcaSearchRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._search_terms

    @search_terms.setter
    def search_terms(self, search_terms):
        """Sets the search_terms of this DmcaSearchRequestV2.

        Search terms.  # noqa: E501

        :param search_terms: The search_terms of this DmcaSearchRequestV2.  # noqa: E501
        :type: str
        """

        self._search_terms = search_terms

    @property
    def teepublic_approved(self):
        """Gets the teepublic_approved of this DmcaSearchRequestV2.  # noqa: E501


        :return: The teepublic_approved of this DmcaSearchRequestV2.  # noqa: E501
        :rtype: bool
        """
        return self._teepublic_approved

    @teepublic_approved.setter
    def teepublic_approved(self, teepublic_approved):
        """Sets the teepublic_approved of this DmcaSearchRequestV2.


        :param teepublic_approved: The teepublic_approved of this DmcaSearchRequestV2.  # noqa: E501
        :type: bool
        """

        self._teepublic_approved = teepublic_approved

    @property
    def teepublic_unapproved(self):
        """Gets the teepublic_unapproved of this DmcaSearchRequestV2.  # noqa: E501


        :return: The teepublic_unapproved of this DmcaSearchRequestV2.  # noqa: E501
        :rtype: bool
        """
        return self._teepublic_unapproved

    @teepublic_unapproved.setter
    def teepublic_unapproved(self, teepublic_unapproved):
        """Sets the teepublic_unapproved of this DmcaSearchRequestV2.


        :param teepublic_unapproved: The teepublic_unapproved of this DmcaSearchRequestV2.  # noqa: E501
        :type: bool
        """

        self._teepublic_unapproved = teepublic_unapproved

    @property
    def artist_id(self):
        """Gets the artist_id of this DmcaSearchRequestV2.  # noqa: E501

        Artist Id  # noqa: E501

        :return: The artist_id of this DmcaSearchRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        """Sets the artist_id of this DmcaSearchRequestV2.

        Artist Id  # noqa: E501

        :param artist_id: The artist_id of this DmcaSearchRequestV2.  # noqa: E501
        :type: int
        """

        self._artist_id = artist_id

    @property
    def per_page(self):
        """Gets the per_page of this DmcaSearchRequestV2.  # noqa: E501

        Number of results to return per page.  # noqa: E501

        :return: The per_page of this DmcaSearchRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this DmcaSearchRequestV2.

        Number of results to return per page.  # noqa: E501

        :param per_page: The per_page of this DmcaSearchRequestV2.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def page_offset(self):
        """Gets the page_offset of this DmcaSearchRequestV2.  # noqa: E501

        Page offset to fetch.  # noqa: E501

        :return: The page_offset of this DmcaSearchRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._page_offset

    @page_offset.setter
    def page_offset(self, page_offset):
        """Sets the page_offset of this DmcaSearchRequestV2.

        Page offset to fetch.  # noqa: E501

        :param page_offset: The page_offset of this DmcaSearchRequestV2.  # noqa: E501
        :type: int
        """

        self._page_offset = page_offset

    @property
    def sort(self):
        """Gets the sort of this DmcaSearchRequestV2.  # noqa: E501

        Sort order  # noqa: E501

        :return: The sort of this DmcaSearchRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this DmcaSearchRequestV2.

        Sort order  # noqa: E501

        :param sort: The sort of this DmcaSearchRequestV2.  # noqa: E501
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
        if issubclass(DmcaSearchRequestV2, dict):
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
        if not isinstance(other, DmcaSearchRequestV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DmcaSearchRequestV2):
            return True

        return self.to_dict() != other.to_dict()
