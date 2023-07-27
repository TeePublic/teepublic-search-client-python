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


class SetDesignTaggingsObject(object):
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
        'discoverable': 'bool',
        'primary': 'str',
        'secondary': 'list[str]'
    }

    attribute_map = {
        'design_id': 'design_id',
        'discoverable': 'discoverable',
        'primary': 'primary',
        'secondary': 'secondary'
    }

    def __init__(self, design_id=None, discoverable=None, primary=None, secondary=None, _configuration=None):  # noqa: E501
        """SetDesignTaggingsObject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._design_id = None
        self._discoverable = None
        self._primary = None
        self._secondary = None
        self.discriminator = None

        self.design_id = design_id
        self.discoverable = discoverable
        if primary is not None:
            self.primary = primary
        if secondary is not None:
            self.secondary = secondary

    @property
    def design_id(self):
        """Gets the design_id of this SetDesignTaggingsObject.  # noqa: E501

        design id  # noqa: E501

        :return: The design_id of this SetDesignTaggingsObject.  # noqa: E501
        :rtype: int
        """
        return self._design_id

    @design_id.setter
    def design_id(self, design_id):
        """Sets the design_id of this SetDesignTaggingsObject.

        design id  # noqa: E501

        :param design_id: The design_id of this SetDesignTaggingsObject.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and design_id is None:
            raise ValueError("Invalid value for `design_id`, must not be `None`")  # noqa: E501

        self._design_id = design_id

    @property
    def discoverable(self):
        """Gets the discoverable of this SetDesignTaggingsObject.  # noqa: E501

        true if the design is discoverable  # noqa: E501

        :return: The discoverable of this SetDesignTaggingsObject.  # noqa: E501
        :rtype: bool
        """
        return self._discoverable

    @discoverable.setter
    def discoverable(self, discoverable):
        """Sets the discoverable of this SetDesignTaggingsObject.

        true if the design is discoverable  # noqa: E501

        :param discoverable: The discoverable of this SetDesignTaggingsObject.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and discoverable is None:
            raise ValueError("Invalid value for `discoverable`, must not be `None`")  # noqa: E501

        self._discoverable = discoverable

    @property
    def primary(self):
        """Gets the primary of this SetDesignTaggingsObject.  # noqa: E501

        primary tag name  # noqa: E501

        :return: The primary of this SetDesignTaggingsObject.  # noqa: E501
        :rtype: str
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this SetDesignTaggingsObject.

        primary tag name  # noqa: E501

        :param primary: The primary of this SetDesignTaggingsObject.  # noqa: E501
        :type: str
        """

        self._primary = primary

    @property
    def secondary(self):
        """Gets the secondary of this SetDesignTaggingsObject.  # noqa: E501

        secondary tag names  # noqa: E501

        :return: The secondary of this SetDesignTaggingsObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary):
        """Sets the secondary of this SetDesignTaggingsObject.

        secondary tag names  # noqa: E501

        :param secondary: The secondary of this SetDesignTaggingsObject.  # noqa: E501
        :type: list[str]
        """

        self._secondary = secondary

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
        if issubclass(SetDesignTaggingsObject, dict):
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
        if not isinstance(other, SetDesignTaggingsObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetDesignTaggingsObject):
            return True

        return self.to_dict() != other.to_dict()
