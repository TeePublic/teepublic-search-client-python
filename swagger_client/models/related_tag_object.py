# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.48
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class RelatedTagObject(object):
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
        'name': 'str',
        'related_tags': 'list[RelatedTagResult]'
    }

    attribute_map = {
        'name': 'name',
        'related_tags': 'related_tags'
    }

    def __init__(self, name=None, related_tags=None, _configuration=None):  # noqa: E501
        """RelatedTagObject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._related_tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if related_tags is not None:
            self.related_tags = related_tags

    @property
    def name(self):
        """Gets the name of this RelatedTagObject.  # noqa: E501

        Tag name of the originating tag  # noqa: E501

        :return: The name of this RelatedTagObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RelatedTagObject.

        Tag name of the originating tag  # noqa: E501

        :param name: The name of this RelatedTagObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def related_tags(self):
        """Gets the related_tags of this RelatedTagObject.  # noqa: E501

        List of related tag results  # noqa: E501

        :return: The related_tags of this RelatedTagObject.  # noqa: E501
        :rtype: list[RelatedTagResult]
        """
        return self._related_tags

    @related_tags.setter
    def related_tags(self, related_tags):
        """Sets the related_tags of this RelatedTagObject.

        List of related tag results  # noqa: E501

        :param related_tags: The related_tags of this RelatedTagObject.  # noqa: E501
        :type: list[RelatedTagResult]
        """

        self._related_tags = related_tags

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
        if issubclass(RelatedTagObject, dict):
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
        if not isinstance(other, RelatedTagObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelatedTagObject):
            return True

        return self.to_dict() != other.to_dict()
