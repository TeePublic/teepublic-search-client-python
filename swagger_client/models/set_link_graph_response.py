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


class SetLinkGraphResponse(object):
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
        'success': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'success': 'success',
        'message': 'message'
    }

    def __init__(self, success=None, message=None, _configuration=None):  # noqa: E501
        """SetLinkGraphResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._success = None
        self._message = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if message is not None:
            self.message = message

    @property
    def success(self):
        """Gets the success of this SetLinkGraphResponse.  # noqa: E501

        Overall operation success  # noqa: E501

        :return: The success of this SetLinkGraphResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this SetLinkGraphResponse.

        Overall operation success  # noqa: E501

        :param success: The success of this SetLinkGraphResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def message(self):
        """Gets the message of this SetLinkGraphResponse.  # noqa: E501

        Operation message  # noqa: E501

        :return: The message of this SetLinkGraphResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SetLinkGraphResponse.

        Operation message  # noqa: E501

        :param message: The message of this SetLinkGraphResponse.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(SetLinkGraphResponse, dict):
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
        if not isinstance(other, SetLinkGraphResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetLinkGraphResponse):
            return True

        return self.to_dict() != other.to_dict()
