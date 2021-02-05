# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EsCompletionSuggestOption(object):
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
        'text': 'str',
        'score': 'float'
    }

    attribute_map = {
        'text': 'text',
        'score': '_score'
    }

    def __init__(self, text=None, score=None):  # noqa: E501
        """EsCompletionSuggestOption - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._score = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if score is not None:
            self.score = score

    @property
    def text(self):
        """Gets the text of this EsCompletionSuggestOption.  # noqa: E501

        Actual suggest for autocomplete.  # noqa: E501

        :return: The text of this EsCompletionSuggestOption.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this EsCompletionSuggestOption.

        Actual suggest for autocomplete.  # noqa: E501

        :param text: The text of this EsCompletionSuggestOption.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def score(self):
        """Gets the score of this EsCompletionSuggestOption.  # noqa: E501

        Option score.  # noqa: E501

        :return: The score of this EsCompletionSuggestOption.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this EsCompletionSuggestOption.

        Option score.  # noqa: E501

        :param score: The score of this EsCompletionSuggestOption.  # noqa: E501
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
        if issubclass(EsCompletionSuggestOption, dict):
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
        if not isinstance(other, EsCompletionSuggestOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
