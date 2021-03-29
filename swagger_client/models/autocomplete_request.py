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


class AutocompleteRequest(object):
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
        'prefix': 'str',
        'limit': 'int',
        'explain': 'bool'
    }

    attribute_map = {
        'prefix': 'prefix',
        'limit': 'limit',
        'explain': 'explain'
    }

    def __init__(self, prefix=None, limit=15, explain=False):  # noqa: E501
        """AutocompleteRequest - a model defined in Swagger"""  # noqa: E501

        self._prefix = None
        self._limit = None
        self._explain = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if limit is not None:
            self.limit = limit
        if explain is not None:
            self.explain = explain

    @property
    def prefix(self):
        """Gets the prefix of this AutocompleteRequest.  # noqa: E501

        Search prefix.  # noqa: E501

        :return: The prefix of this AutocompleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this AutocompleteRequest.

        Search prefix.  # noqa: E501

        :param prefix: The prefix of this AutocompleteRequest.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def limit(self):
        """Gets the limit of this AutocompleteRequest.  # noqa: E501

        Number of results to return.  # noqa: E501

        :return: The limit of this AutocompleteRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this AutocompleteRequest.

        Number of results to return.  # noqa: E501

        :param limit: The limit of this AutocompleteRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def explain(self):
        """Gets the explain of this AutocompleteRequest.  # noqa: E501

        Whether to return explanation of results.  # noqa: E501

        :return: The explain of this AutocompleteRequest.  # noqa: E501
        :rtype: bool
        """
        return self._explain

    @explain.setter
    def explain(self, explain):
        """Sets the explain of this AutocompleteRequest.

        Whether to return explanation of results.  # noqa: E501

        :param explain: The explain of this AutocompleteRequest.  # noqa: E501
        :type: bool
        """

        self._explain = explain

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
        if issubclass(AutocompleteRequest, dict):
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
        if not isinstance(other, AutocompleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
