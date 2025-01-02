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


class LinkGraphResponse(object):
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
        'status': 'str',
        'canonical_parent': 'str',
        'override': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'canonical_parent': 'canonical_parent',
        'override': 'override'
    }

    def __init__(self, status=None, canonical_parent=None, override=None, _configuration=None):  # noqa: E501
        """LinkGraphResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._canonical_parent = None
        self._override = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if canonical_parent is not None:
            self.canonical_parent = canonical_parent
        if override is not None:
            self.override = override

    @property
    def status(self):
        """Gets the status of this LinkGraphResponse.  # noqa: E501

        Whether a tag is canonical or duplicate  # noqa: E501

        :return: The status of this LinkGraphResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LinkGraphResponse.

        Whether a tag is canonical or duplicate  # noqa: E501

        :param status: The status of this LinkGraphResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["canonical", "duplicate"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def canonical_parent(self):
        """Gets the canonical_parent of this LinkGraphResponse.  # noqa: E501

        If the tag is a duplicate, the canonical parent tag  # noqa: E501

        :return: The canonical_parent of this LinkGraphResponse.  # noqa: E501
        :rtype: str
        """
        return self._canonical_parent

    @canonical_parent.setter
    def canonical_parent(self, canonical_parent):
        """Sets the canonical_parent of this LinkGraphResponse.

        If the tag is a duplicate, the canonical parent tag  # noqa: E501

        :param canonical_parent: The canonical_parent of this LinkGraphResponse.  # noqa: E501
        :type: str
        """

        self._canonical_parent = canonical_parent

    @property
    def override(self):
        """Gets the override of this LinkGraphResponse.  # noqa: E501

        Whether the tag status was manually edited  # noqa: E501

        :return: The override of this LinkGraphResponse.  # noqa: E501
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this LinkGraphResponse.

        Whether the tag status was manually edited  # noqa: E501

        :param override: The override of this LinkGraphResponse.  # noqa: E501
        :type: bool
        """

        self._override = override

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
        if issubclass(LinkGraphResponse, dict):
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
        if not isinstance(other, LinkGraphResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkGraphResponse):
            return True

        return self.to_dict() != other.to_dict()