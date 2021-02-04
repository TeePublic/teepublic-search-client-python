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


class AutocompleteSuggestion(object):
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
        'suggestion': 'str',
        'type': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'type': 'type',
        'weight': 'weight'
    }

    def __init__(self, suggestion=None, type='query', weight=None):  # noqa: E501
        """AutocompleteSuggestion - a model defined in Swagger"""  # noqa: E501

        self._suggestion = None
        self._type = None
        self._weight = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if type is not None:
            self.type = type
        if weight is not None:
            self.weight = weight

    @property
    def suggestion(self):
        """Gets the suggestion of this AutocompleteSuggestion.  # noqa: E501

        Suggestion text.  # noqa: E501

        :return: The suggestion of this AutocompleteSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this AutocompleteSuggestion.

        Suggestion text.  # noqa: E501

        :param suggestion: The suggestion of this AutocompleteSuggestion.  # noqa: E501
        :type: str
        """

        self._suggestion = suggestion

    @property
    def type(self):
        """Gets the type of this AutocompleteSuggestion.  # noqa: E501

        Suggestion type.  # noqa: E501

        :return: The type of this AutocompleteSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutocompleteSuggestion.

        Suggestion type.  # noqa: E501

        :param type: The type of this AutocompleteSuggestion.  # noqa: E501
        :type: str
        """
        allowed_values = ["query", "tag"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def weight(self):
        """Gets the weight of this AutocompleteSuggestion.  # noqa: E501

        Suggestion weight.  # noqa: E501

        :return: The weight of this AutocompleteSuggestion.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this AutocompleteSuggestion.

        Suggestion weight.  # noqa: E501

        :param weight: The weight of this AutocompleteSuggestion.  # noqa: E501
        :type: int
        """

        self._weight = weight

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
        if issubclass(AutocompleteSuggestion, dict):
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
        if not isinstance(other, AutocompleteSuggestion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
