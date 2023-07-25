# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class RelatedResponse(object):
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
        'results': 'list[RelatedResult]',
        'impression_id': 'str',
        'is_override': 'bool'
    }

    attribute_map = {
        'results': 'results',
        'impression_id': 'impression_id',
        'is_override': 'is_override'
    }

    def __init__(self, results=None, impression_id=None, is_override=None, _configuration=None):  # noqa: E501
        """RelatedResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._results = None
        self._impression_id = None
        self._is_override = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if impression_id is not None:
            self.impression_id = impression_id
        if is_override is not None:
            self.is_override = is_override

    @property
    def results(self):
        """Gets the results of this RelatedResponse.  # noqa: E501


        :return: The results of this RelatedResponse.  # noqa: E501
        :rtype: list[RelatedResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this RelatedResponse.


        :param results: The results of this RelatedResponse.  # noqa: E501
        :type: list[RelatedResult]
        """

        self._results = results

    @property
    def impression_id(self):
        """Gets the impression_id of this RelatedResponse.  # noqa: E501


        :return: The impression_id of this RelatedResponse.  # noqa: E501
        :rtype: str
        """
        return self._impression_id

    @impression_id.setter
    def impression_id(self, impression_id):
        """Sets the impression_id of this RelatedResponse.


        :param impression_id: The impression_id of this RelatedResponse.  # noqa: E501
        :type: str
        """

        self._impression_id = impression_id

    @property
    def is_override(self):
        """Gets the is_override of this RelatedResponse.  # noqa: E501

        Flag to indicate if suggesstions are overrides  # noqa: E501

        :return: The is_override of this RelatedResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_override

    @is_override.setter
    def is_override(self, is_override):
        """Sets the is_override of this RelatedResponse.

        Flag to indicate if suggesstions are overrides  # noqa: E501

        :param is_override: The is_override of this RelatedResponse.  # noqa: E501
        :type: bool
        """

        self._is_override = is_override

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
        if issubclass(RelatedResponse, dict):
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
        if not isinstance(other, RelatedResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelatedResponse):
            return True

        return self.to_dict() != other.to_dict()
