# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.45
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class SetTagObject(object):
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
        'mature': 'bool',
        'suggestable': 'bool',
        'relatable': 'bool',
        'deleted': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'mature': 'mature',
        'suggestable': 'suggestable',
        'relatable': 'relatable',
        'deleted': 'deleted'
    }

    def __init__(self, name=None, mature=None, suggestable=None, relatable=None, deleted=None, _configuration=None):  # noqa: E501
        """SetTagObject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._mature = None
        self._suggestable = None
        self._relatable = None
        self._deleted = None
        self.discriminator = None

        self.name = name
        if mature is not None:
            self.mature = mature
        if suggestable is not None:
            self.suggestable = suggestable
        if relatable is not None:
            self.relatable = relatable
        if deleted is not None:
            self.deleted = deleted

    @property
    def name(self):
        """Gets the name of this SetTagObject.  # noqa: E501

        tag name  # noqa: E501

        :return: The name of this SetTagObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SetTagObject.

        tag name  # noqa: E501

        :param name: The name of this SetTagObject.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def mature(self):
        """Gets the mature of this SetTagObject.  # noqa: E501

        mature  # noqa: E501

        :return: The mature of this SetTagObject.  # noqa: E501
        :rtype: bool
        """
        return self._mature

    @mature.setter
    def mature(self, mature):
        """Sets the mature of this SetTagObject.

        mature  # noqa: E501

        :param mature: The mature of this SetTagObject.  # noqa: E501
        :type: bool
        """

        self._mature = mature

    @property
    def suggestable(self):
        """Gets the suggestable of this SetTagObject.  # noqa: E501

        suggestable  # noqa: E501

        :return: The suggestable of this SetTagObject.  # noqa: E501
        :rtype: bool
        """
        return self._suggestable

    @suggestable.setter
    def suggestable(self, suggestable):
        """Sets the suggestable of this SetTagObject.

        suggestable  # noqa: E501

        :param suggestable: The suggestable of this SetTagObject.  # noqa: E501
        :type: bool
        """

        self._suggestable = suggestable

    @property
    def relatable(self):
        """Gets the relatable of this SetTagObject.  # noqa: E501

        relatable  # noqa: E501

        :return: The relatable of this SetTagObject.  # noqa: E501
        :rtype: bool
        """
        return self._relatable

    @relatable.setter
    def relatable(self, relatable):
        """Sets the relatable of this SetTagObject.

        relatable  # noqa: E501

        :param relatable: The relatable of this SetTagObject.  # noqa: E501
        :type: bool
        """

        self._relatable = relatable

    @property
    def deleted(self):
        """Gets the deleted of this SetTagObject.  # noqa: E501

        deleted  # noqa: E501

        :return: The deleted of this SetTagObject.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this SetTagObject.

        deleted  # noqa: E501

        :param deleted: The deleted of this SetTagObject.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

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
        if issubclass(SetTagObject, dict):
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
        if not isinstance(other, SetTagObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetTagObject):
            return True

        return self.to_dict() != other.to_dict()
