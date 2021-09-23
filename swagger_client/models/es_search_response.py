# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.27
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class EsSearchResponse(object):
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
        'took': 'int',
        'hits': 'EsHits',
        'suggest': 'EsAutocompleteSuggest'
    }

    attribute_map = {
        'took': 'took',
        'hits': 'hits',
        'suggest': 'suggest'
    }

    def __init__(self, took=None, hits=None, suggest=None, _configuration=None):  # noqa: E501
        """EsSearchResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._took = None
        self._hits = None
        self._suggest = None
        self.discriminator = None

        if took is not None:
            self.took = took
        if hits is not None:
            self.hits = hits
        if suggest is not None:
            self.suggest = suggest

    @property
    def took(self):
        """Gets the took of this EsSearchResponse.  # noqa: E501

        time in milliseconds for Elasticsearch to execute.  # noqa: E501

        :return: The took of this EsSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this EsSearchResponse.

        time in milliseconds for Elasticsearch to execute.  # noqa: E501

        :param took: The took of this EsSearchResponse.  # noqa: E501
        :type: int
        """

        self._took = took

    @property
    def hits(self):
        """Gets the hits of this EsSearchResponse.  # noqa: E501


        :return: The hits of this EsSearchResponse.  # noqa: E501
        :rtype: EsHits
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this EsSearchResponse.


        :param hits: The hits of this EsSearchResponse.  # noqa: E501
        :type: EsHits
        """

        self._hits = hits

    @property
    def suggest(self):
        """Gets the suggest of this EsSearchResponse.  # noqa: E501


        :return: The suggest of this EsSearchResponse.  # noqa: E501
        :rtype: EsAutocompleteSuggest
        """
        return self._suggest

    @suggest.setter
    def suggest(self, suggest):
        """Sets the suggest of this EsSearchResponse.


        :param suggest: The suggest of this EsSearchResponse.  # noqa: E501
        :type: EsAutocompleteSuggest
        """

        self._suggest = suggest

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
        if issubclass(EsSearchResponse, dict):
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
        if not isinstance(other, EsSearchResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EsSearchResponse):
            return True

        return self.to_dict() != other.to_dict()
