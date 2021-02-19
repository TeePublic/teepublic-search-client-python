# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AutocompleteResponse(object):
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
        'explain': 'Explain',
        'suggestions': 'list[AutocompleteSuggestion]'
    }

    attribute_map = {
        'explain': 'explain',
        'suggestions': 'suggestions'
    }

    def __init__(self, explain=None, suggestions=None):  # noqa: E501
        """AutocompleteResponse - a model defined in Swagger"""  # noqa: E501

        self._explain = None
        self._suggestions = None
        self.discriminator = None

        if explain is not None:
            self.explain = explain
        if suggestions is not None:
            self.suggestions = suggestions

    @property
    def explain(self):
        """Gets the explain of this AutocompleteResponse.  # noqa: E501


        :return: The explain of this AutocompleteResponse.  # noqa: E501
        :rtype: Explain
        """
        return self._explain

    @explain.setter
    def explain(self, explain):
        """Sets the explain of this AutocompleteResponse.


        :param explain: The explain of this AutocompleteResponse.  # noqa: E501
        :type: Explain
        """

        self._explain = explain

    @property
    def suggestions(self):
        """Gets the suggestions of this AutocompleteResponse.  # noqa: E501

        List of suggestions.  # noqa: E501

        :return: The suggestions of this AutocompleteResponse.  # noqa: E501
        :rtype: list[AutocompleteSuggestion]
        """
        return self._suggestions

    @suggestions.setter
    def suggestions(self, suggestions):
        """Sets the suggestions of this AutocompleteResponse.

        List of suggestions.  # noqa: E501

        :param suggestions: The suggestions of this AutocompleteResponse.  # noqa: E501
        :type: list[AutocompleteSuggestion]
        """

        self._suggestions = suggestions

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
        if issubclass(AutocompleteResponse, dict):
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
        if not isinstance(other, AutocompleteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
