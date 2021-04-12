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

from swagger_client.configuration import Configuration


class TagResult(object):
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
        'id': 'str',
        'name': 'str',
        'taggings': 'int',
        'discoverable_taggings': 'int',
        'suggestable': 'bool',
        'canonical': 'bool',
        'relatable': 'bool',
        'deleted': 'bool',
        'child_count': 'int',
        'parent_name': 'str'
    }

    attribute_map = {
        'id': '_id',
        'name': 'name',
        'taggings': 'taggings',
        'discoverable_taggings': 'discoverable_taggings',
        'suggestable': 'suggestable',
        'canonical': 'canonical',
        'relatable': 'relatable',
        'deleted': 'deleted',
        'child_count': 'child_count',
        'parent_name': 'parent_name'
    }

    def __init__(self, id=None, name=None, taggings=None, discoverable_taggings=None, suggestable=None, canonical=None, relatable=None, deleted=None, child_count=None, parent_name=None, _configuration=None):  # noqa: E501
        """TagResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._taggings = None
        self._discoverable_taggings = None
        self._suggestable = None
        self._canonical = None
        self._relatable = None
        self._deleted = None
        self._child_count = None
        self._parent_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if taggings is not None:
            self.taggings = taggings
        if discoverable_taggings is not None:
            self.discoverable_taggings = discoverable_taggings
        if suggestable is not None:
            self.suggestable = suggestable
        if canonical is not None:
            self.canonical = canonical
        if relatable is not None:
            self.relatable = relatable
        if deleted is not None:
            self.deleted = deleted
        if child_count is not None:
            self.child_count = child_count
        if parent_name is not None:
            self.parent_name = parent_name

    @property
    def id(self):
        """Gets the id of this TagResult.  # noqa: E501

        id  # noqa: E501

        :return: The id of this TagResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TagResult.

        id  # noqa: E501

        :param id: The id of this TagResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TagResult.  # noqa: E501

        tag name  # noqa: E501

        :return: The name of this TagResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TagResult.

        tag name  # noqa: E501

        :param name: The name of this TagResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def taggings(self):
        """Gets the taggings of this TagResult.  # noqa: E501

        taggings count  # noqa: E501

        :return: The taggings of this TagResult.  # noqa: E501
        :rtype: int
        """
        return self._taggings

    @taggings.setter
    def taggings(self, taggings):
        """Sets the taggings of this TagResult.

        taggings count  # noqa: E501

        :param taggings: The taggings of this TagResult.  # noqa: E501
        :type: int
        """

        self._taggings = taggings

    @property
    def discoverable_taggings(self):
        """Gets the discoverable_taggings of this TagResult.  # noqa: E501

        discoverable design taggings count  # noqa: E501

        :return: The discoverable_taggings of this TagResult.  # noqa: E501
        :rtype: int
        """
        return self._discoverable_taggings

    @discoverable_taggings.setter
    def discoverable_taggings(self, discoverable_taggings):
        """Sets the discoverable_taggings of this TagResult.

        discoverable design taggings count  # noqa: E501

        :param discoverable_taggings: The discoverable_taggings of this TagResult.  # noqa: E501
        :type: int
        """

        self._discoverable_taggings = discoverable_taggings

    @property
    def suggestable(self):
        """Gets the suggestable of this TagResult.  # noqa: E501

        suggestable  # noqa: E501

        :return: The suggestable of this TagResult.  # noqa: E501
        :rtype: bool
        """
        return self._suggestable

    @suggestable.setter
    def suggestable(self, suggestable):
        """Sets the suggestable of this TagResult.

        suggestable  # noqa: E501

        :param suggestable: The suggestable of this TagResult.  # noqa: E501
        :type: bool
        """

        self._suggestable = suggestable

    @property
    def canonical(self):
        """Gets the canonical of this TagResult.  # noqa: E501

        canonical  # noqa: E501

        :return: The canonical of this TagResult.  # noqa: E501
        :rtype: bool
        """
        return self._canonical

    @canonical.setter
    def canonical(self, canonical):
        """Sets the canonical of this TagResult.

        canonical  # noqa: E501

        :param canonical: The canonical of this TagResult.  # noqa: E501
        :type: bool
        """

        self._canonical = canonical

    @property
    def relatable(self):
        """Gets the relatable of this TagResult.  # noqa: E501

        relatable  # noqa: E501

        :return: The relatable of this TagResult.  # noqa: E501
        :rtype: bool
        """
        return self._relatable

    @relatable.setter
    def relatable(self, relatable):
        """Sets the relatable of this TagResult.

        relatable  # noqa: E501

        :param relatable: The relatable of this TagResult.  # noqa: E501
        :type: bool
        """

        self._relatable = relatable

    @property
    def deleted(self):
        """Gets the deleted of this TagResult.  # noqa: E501

        deleted  # noqa: E501

        :return: The deleted of this TagResult.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TagResult.

        deleted  # noqa: E501

        :param deleted: The deleted of this TagResult.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def child_count(self):
        """Gets the child_count of this TagResult.  # noqa: E501

        number of children tags  # noqa: E501

        :return: The child_count of this TagResult.  # noqa: E501
        :rtype: int
        """
        return self._child_count

    @child_count.setter
    def child_count(self, child_count):
        """Sets the child_count of this TagResult.

        number of children tags  # noqa: E501

        :param child_count: The child_count of this TagResult.  # noqa: E501
        :type: int
        """

        self._child_count = child_count

    @property
    def parent_name(self):
        """Gets the parent_name of this TagResult.  # noqa: E501

        name of parent tag  # noqa: E501

        :return: The parent_name of this TagResult.  # noqa: E501
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this TagResult.

        name of parent tag  # noqa: E501

        :param parent_name: The parent_name of this TagResult.  # noqa: E501
        :type: str
        """

        self._parent_name = parent_name

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
        if issubclass(TagResult, dict):
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
        if not isinstance(other, TagResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagResult):
            return True

        return self.to_dict() != other.to_dict()
