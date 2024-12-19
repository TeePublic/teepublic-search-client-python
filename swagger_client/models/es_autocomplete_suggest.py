# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.46
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class EsAutocompleteSuggest(object):
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
        'query_suggest': 'list[EsCompletionSuggest]',
        'tag_suggest': 'list[EsCompletionSuggest]'
    }

    attribute_map = {
        'query_suggest': 'query_suggest',
        'tag_suggest': 'tag_suggest'
    }

    def __init__(self, query_suggest=None, tag_suggest=None, _configuration=None):  # noqa: E501
        """EsAutocompleteSuggest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._query_suggest = None
        self._tag_suggest = None
        self.discriminator = None

        if query_suggest is not None:
            self.query_suggest = query_suggest
        if tag_suggest is not None:
            self.tag_suggest = tag_suggest

    @property
    def query_suggest(self):
        """Gets the query_suggest of this EsAutocompleteSuggest.  # noqa: E501

        Array of completion suggests.  # noqa: E501

        :return: The query_suggest of this EsAutocompleteSuggest.  # noqa: E501
        :rtype: list[EsCompletionSuggest]
        """
        return self._query_suggest

    @query_suggest.setter
    def query_suggest(self, query_suggest):
        """Sets the query_suggest of this EsAutocompleteSuggest.

        Array of completion suggests.  # noqa: E501

        :param query_suggest: The query_suggest of this EsAutocompleteSuggest.  # noqa: E501
        :type: list[EsCompletionSuggest]
        """

        self._query_suggest = query_suggest

    @property
    def tag_suggest(self):
        """Gets the tag_suggest of this EsAutocompleteSuggest.  # noqa: E501

        Array of completion suggests.  # noqa: E501

        :return: The tag_suggest of this EsAutocompleteSuggest.  # noqa: E501
        :rtype: list[EsCompletionSuggest]
        """
        return self._tag_suggest

    @tag_suggest.setter
    def tag_suggest(self, tag_suggest):
        """Sets the tag_suggest of this EsAutocompleteSuggest.

        Array of completion suggests.  # noqa: E501

        :param tag_suggest: The tag_suggest of this EsAutocompleteSuggest.  # noqa: E501
        :type: list[EsCompletionSuggest]
        """

        self._tag_suggest = tag_suggest

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
        if issubclass(EsAutocompleteSuggest, dict):
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
        if not isinstance(other, EsAutocompleteSuggest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EsAutocompleteSuggest):
            return True

        return self.to_dict() != other.to_dict()
