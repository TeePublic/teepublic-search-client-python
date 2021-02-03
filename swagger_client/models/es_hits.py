# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EsHits(object):
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
        'total': 'int',
        'max_score': 'float',
        'hits': 'list[EsHit]'
    }

    attribute_map = {
        'total': 'total',
        'max_score': 'max_score',
        'hits': 'hits'
    }

    def __init__(self, total=None, max_score=None, hits=None):  # noqa: E501
        """EsHits - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._max_score = None
        self._hits = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if max_score is not None:
            self.max_score = max_score
        if hits is not None:
            self.hits = hits

    @property
    def total(self):
        """Gets the total of this EsHits.  # noqa: E501

        total number of documents matching our search criteria.  # noqa: E501

        :return: The total of this EsHits.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this EsHits.

        total number of documents matching our search criteria.  # noqa: E501

        :param total: The total of this EsHits.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def max_score(self):
        """Gets the max_score of this EsHits.  # noqa: E501

        max score for search query.  # noqa: E501

        :return: The max_score of this EsHits.  # noqa: E501
        :rtype: float
        """
        return self._max_score

    @max_score.setter
    def max_score(self, max_score):
        """Sets the max_score of this EsHits.

        max score for search query.  # noqa: E501

        :param max_score: The max_score of this EsHits.  # noqa: E501
        :type: float
        """

        self._max_score = max_score

    @property
    def hits(self):
        """Gets the hits of this EsHits.  # noqa: E501

        actual array of search results.  # noqa: E501

        :return: The hits of this EsHits.  # noqa: E501
        :rtype: list[EsHit]
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this EsHits.

        actual array of search results.  # noqa: E501

        :param hits: The hits of this EsHits.  # noqa: E501
        :type: list[EsHit]
        """

        self._hits = hits

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
        if issubclass(EsHits, dict):
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
        if not isinstance(other, EsHits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
