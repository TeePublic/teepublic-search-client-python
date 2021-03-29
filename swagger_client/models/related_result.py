# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RelatedResult(object):
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
        'score': 'float',
        'linkable_to_tag_page': 'bool'
    }

    attribute_map = {
        'result': 'result',
        'score': 'score',
        'linkable_to_tag_page': 'linkable_to_tag_page'
    }

    def __init__(self, result=None, score=None, linkable_to_tag_page=None):  # noqa: E501
        """RelatedResult - a model defined in Swagger"""  # noqa: E501

        self._result = None
        self._score = None
        self._linkable_to_tag_page = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if score is not None:
            self.score = score
        if linkable_to_tag_page is not None:
            self.linkable_to_tag_page = linkable_to_tag_page

    @property
    def result(self):
        """Gets the result of this RelatedResult.  # noqa: E501

        Content of related result.  # noqa: E501

        :return: The result of this RelatedResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RelatedResult.

        Content of related result.  # noqa: E501

        :param result: The result of this RelatedResult.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def score(self):
        """Gets the score of this RelatedResult.  # noqa: E501

        Score of related result.  # noqa: E501

        :return: The score of this RelatedResult.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this RelatedResult.

        Score of related result.  # noqa: E501

        :param score: The score of this RelatedResult.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def linkable_to_tag_page(self):
        """Gets the linkable_to_tag_page of this RelatedResult.  # noqa: E501

        Flag to indicate if suggesstion is linkable to tag page  # noqa: E501

        :return: The linkable_to_tag_page of this RelatedResult.  # noqa: E501
        :rtype: bool
        """
        return self._linkable_to_tag_page

    @linkable_to_tag_page.setter
    def linkable_to_tag_page(self, linkable_to_tag_page):
        """Sets the linkable_to_tag_page of this RelatedResult.

        Flag to indicate if suggesstion is linkable to tag page  # noqa: E501

        :param linkable_to_tag_page: The linkable_to_tag_page of this RelatedResult.  # noqa: E501
        :type: bool
        """

        self._linkable_to_tag_page = linkable_to_tag_page

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
        if issubclass(RelatedResult, dict):
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
        if not isinstance(other, RelatedResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
