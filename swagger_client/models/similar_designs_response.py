# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.31
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class SimilarDesignsResponse(object):
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
        'max_score': 'float',
        'total': 'int',
        'explain': 'Explain',
        'designs': 'list[DesignSlim]'
    }

    attribute_map = {
        'max_score': 'max_score',
        'total': 'total',
        'explain': 'explain',
        'designs': 'designs'
    }

    def __init__(self, max_score=None, total=None, explain=None, designs=None, _configuration=None):  # noqa: E501
        """SimilarDesignsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._max_score = None
        self._total = None
        self._explain = None
        self._designs = None
        self.discriminator = None

        if max_score is not None:
            self.max_score = max_score
        if total is not None:
            self.total = total
        if explain is not None:
            self.explain = explain
        if designs is not None:
            self.designs = designs

    @property
    def max_score(self):
        """Gets the max_score of this SimilarDesignsResponse.  # noqa: E501

        max score for search query.  # noqa: E501

        :return: The max_score of this SimilarDesignsResponse.  # noqa: E501
        :rtype: float
        """
        return self._max_score

    @max_score.setter
    def max_score(self, max_score):
        """Sets the max_score of this SimilarDesignsResponse.

        max score for search query.  # noqa: E501

        :param max_score: The max_score of this SimilarDesignsResponse.  # noqa: E501
        :type: float
        """

        self._max_score = max_score

    @property
    def total(self):
        """Gets the total of this SimilarDesignsResponse.  # noqa: E501

        total number of documents matching our search criteria.  # noqa: E501

        :return: The total of this SimilarDesignsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SimilarDesignsResponse.

        total number of documents matching our search criteria.  # noqa: E501

        :param total: The total of this SimilarDesignsResponse.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def explain(self):
        """Gets the explain of this SimilarDesignsResponse.  # noqa: E501


        :return: The explain of this SimilarDesignsResponse.  # noqa: E501
        :rtype: Explain
        """
        return self._explain

    @explain.setter
    def explain(self, explain):
        """Sets the explain of this SimilarDesignsResponse.


        :param explain: The explain of this SimilarDesignsResponse.  # noqa: E501
        :type: Explain
        """

        self._explain = explain

    @property
    def designs(self):
        """Gets the designs of this SimilarDesignsResponse.  # noqa: E501

        list of designs.  # noqa: E501

        :return: The designs of this SimilarDesignsResponse.  # noqa: E501
        :rtype: list[DesignSlim]
        """
        return self._designs

    @designs.setter
    def designs(self, designs):
        """Sets the designs of this SimilarDesignsResponse.

        list of designs.  # noqa: E501

        :param designs: The designs of this SimilarDesignsResponse.  # noqa: E501
        :type: list[DesignSlim]
        """

        self._designs = designs

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
        if issubclass(SimilarDesignsResponse, dict):
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
        if not isinstance(other, SimilarDesignsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimilarDesignsResponse):
            return True

        return self.to_dict() != other.to_dict()
