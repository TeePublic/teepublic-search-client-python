# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class TrendingResult(object):
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
        'result': 'str',
        'score': 'float'
    }

    attribute_map = {
        'result': 'result',
        'score': 'score'
    }

    def __init__(self, result=None, score=None, _configuration=None):  # noqa: E501
        """TrendingResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._result = None
        self._score = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if score is not None:
            self.score = score

    @property
    def result(self):
        """Gets the result of this TrendingResult.  # noqa: E501

        Content of trending result.  # noqa: E501

        :return: The result of this TrendingResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this TrendingResult.

        Content of trending result.  # noqa: E501

        :param result: The result of this TrendingResult.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def score(self):
        """Gets the score of this TrendingResult.  # noqa: E501

        Score of trending result.  # noqa: E501

        :return: The score of this TrendingResult.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this TrendingResult.

        Score of trending result.  # noqa: E501

        :param score: The score of this TrendingResult.  # noqa: E501
        :type: float
        """

        self._score = score

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
        if issubclass(TrendingResult, dict):
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
        if not isinstance(other, TrendingResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrendingResult):
            return True

        return self.to_dict() != other.to_dict()
