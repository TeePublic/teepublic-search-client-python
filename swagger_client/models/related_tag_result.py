# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RelatedTagResult(object):
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
        'deleted': 'bool',
        'linkable': 'bool',
        'taggings': 'int'
    }

    attribute_map = {
        'name': 'name',
        'deleted': 'deleted',
        'linkable': 'linkable',
        'taggings': 'taggings'
    }

    def __init__(self, name=None, deleted=None, linkable=None, taggings=None):  # noqa: E501
        """RelatedTagResult - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._deleted = None
        self._linkable = None
        self._taggings = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if deleted is not None:
            self.deleted = deleted
        if linkable is not None:
            self.linkable = linkable
        if taggings is not None:
            self.taggings = taggings

    @property
    def name(self):
        """Gets the name of this RelatedTagResult.  # noqa: E501

        Tag name  # noqa: E501

        :return: The name of this RelatedTagResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RelatedTagResult.

        Tag name  # noqa: E501

        :param name: The name of this RelatedTagResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def deleted(self):
        """Gets the deleted of this RelatedTagResult.  # noqa: E501

        Is the tag soft deleted  # noqa: E501

        :return: The deleted of this RelatedTagResult.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this RelatedTagResult.

        Is the tag soft deleted  # noqa: E501

        :param deleted: The deleted of this RelatedTagResult.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def linkable(self):
        """Gets the linkable of this RelatedTagResult.  # noqa: E501

        Is the tag linkable or not  # noqa: E501

        :return: The linkable of this RelatedTagResult.  # noqa: E501
        :rtype: bool
        """
        return self._linkable

    @linkable.setter
    def linkable(self, linkable):
        """Sets the linkable of this RelatedTagResult.

        Is the tag linkable or not  # noqa: E501

        :param linkable: The linkable of this RelatedTagResult.  # noqa: E501
        :type: bool
        """

        self._linkable = linkable

    @property
    def taggings(self):
        """Gets the taggings of this RelatedTagResult.  # noqa: E501

        Number of taggings  # noqa: E501

        :return: The taggings of this RelatedTagResult.  # noqa: E501
        :rtype: int
        """
        return self._taggings

    @taggings.setter
    def taggings(self, taggings):
        """Sets the taggings of this RelatedTagResult.

        Number of taggings  # noqa: E501

        :param taggings: The taggings of this RelatedTagResult.  # noqa: E501
        :type: int
        """

        self._taggings = taggings

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
        if issubclass(RelatedTagResult, dict):
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
        if not isinstance(other, RelatedTagResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other