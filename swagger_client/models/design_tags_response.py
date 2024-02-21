# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.44
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class DesignTagsResponse(object):
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
        'design_id': 'int',
        'primary_tag': 'TagResult',
        'secondary_tags': 'list[TagResult]'
    }

    attribute_map = {
        'design_id': 'design_id',
        'primary_tag': 'primary_tag',
        'secondary_tags': 'secondary_tags'
    }

    def __init__(self, design_id=None, primary_tag=None, secondary_tags=None, _configuration=None):  # noqa: E501
        """DesignTagsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._design_id = None
        self._primary_tag = None
        self._secondary_tags = None
        self.discriminator = None

        if design_id is not None:
            self.design_id = design_id
        if primary_tag is not None:
            self.primary_tag = primary_tag
        if secondary_tags is not None:
            self.secondary_tags = secondary_tags

    @property
    def design_id(self):
        """Gets the design_id of this DesignTagsResponse.  # noqa: E501

        design id  # noqa: E501

        :return: The design_id of this DesignTagsResponse.  # noqa: E501
        :rtype: int
        """
        return self._design_id

    @design_id.setter
    def design_id(self, design_id):
        """Sets the design_id of this DesignTagsResponse.

        design id  # noqa: E501

        :param design_id: The design_id of this DesignTagsResponse.  # noqa: E501
        :type: int
        """

        self._design_id = design_id

    @property
    def primary_tag(self):
        """Gets the primary_tag of this DesignTagsResponse.  # noqa: E501


        :return: The primary_tag of this DesignTagsResponse.  # noqa: E501
        :rtype: TagResult
        """
        return self._primary_tag

    @primary_tag.setter
    def primary_tag(self, primary_tag):
        """Sets the primary_tag of this DesignTagsResponse.


        :param primary_tag: The primary_tag of this DesignTagsResponse.  # noqa: E501
        :type: TagResult
        """

        self._primary_tag = primary_tag

    @property
    def secondary_tags(self):
        """Gets the secondary_tags of this DesignTagsResponse.  # noqa: E501


        :return: The secondary_tags of this DesignTagsResponse.  # noqa: E501
        :rtype: list[TagResult]
        """
        return self._secondary_tags

    @secondary_tags.setter
    def secondary_tags(self, secondary_tags):
        """Sets the secondary_tags of this DesignTagsResponse.


        :param secondary_tags: The secondary_tags of this DesignTagsResponse.  # noqa: E501
        :type: list[TagResult]
        """

        self._secondary_tags = secondary_tags

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
        if issubclass(DesignTagsResponse, dict):
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
        if not isinstance(other, DesignTagsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DesignTagsResponse):
            return True

        return self.to_dict() != other.to_dict()
