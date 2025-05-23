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


class Design(object):
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
        'id': 'int',
        'title': 'str',
        'primary_tag': 'str',
        'tags': 'list[str]',
        'explain': 'object'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'primary_tag': 'primary_tag',
        'tags': 'tags',
        'explain': 'explain'
    }

    def __init__(self, id=None, title=None, primary_tag=None, tags=None, explain=None, _configuration=None):  # noqa: E501
        """Design - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._title = None
        self._primary_tag = None
        self._tags = None
        self._explain = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if primary_tag is not None:
            self.primary_tag = primary_tag
        if tags is not None:
            self.tags = tags
        if explain is not None:
            self.explain = explain

    @property
    def id(self):
        """Gets the id of this Design.  # noqa: E501

        design id.  # noqa: E501

        :return: The id of this Design.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Design.

        design id.  # noqa: E501

        :param id: The id of this Design.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Design.  # noqa: E501

        design title.  # noqa: E501

        :return: The title of this Design.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Design.

        design title.  # noqa: E501

        :param title: The title of this Design.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def primary_tag(self):
        """Gets the primary_tag of this Design.  # noqa: E501

        design primary tag.  # noqa: E501

        :return: The primary_tag of this Design.  # noqa: E501
        :rtype: str
        """
        return self._primary_tag

    @primary_tag.setter
    def primary_tag(self, primary_tag):
        """Sets the primary_tag of this Design.

        design primary tag.  # noqa: E501

        :param primary_tag: The primary_tag of this Design.  # noqa: E501
        :type: str
        """

        self._primary_tag = primary_tag

    @property
    def tags(self):
        """Gets the tags of this Design.  # noqa: E501

        design tag.  # noqa: E501

        :return: The tags of this Design.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Design.

        design tag.  # noqa: E501

        :param tags: The tags of this Design.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def explain(self):
        """Gets the explain of this Design.  # noqa: E501

        search explanation on this design.  # noqa: E501

        :return: The explain of this Design.  # noqa: E501
        :rtype: object
        """
        return self._explain

    @explain.setter
    def explain(self, explain):
        """Sets the explain of this Design.

        search explanation on this design.  # noqa: E501

        :param explain: The explain of this Design.  # noqa: E501
        :type: object
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
        if issubclass(Design, dict):
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
        if not isinstance(other, Design):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Design):
            return True

        return self.to_dict() != other.to_dict()
