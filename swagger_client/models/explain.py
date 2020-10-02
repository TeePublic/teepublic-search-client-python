# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Explain(object):
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
        'es_query': 'object',
        'took': 'int'
    }

    attribute_map = {
        'es_query': 'es_query',
        'took': 'took'
    }

    def __init__(self, es_query=None, took=None):  # noqa: E501
        """Explain - a model defined in Swagger"""  # noqa: E501

        self._es_query = None
        self._took = None
        self.discriminator = None

        if es_query is not None:
            self.es_query = es_query
        if took is not None:
            self.took = took

    @property
    def es_query(self):
        """Gets the es_query of this Explain.  # noqa: E501

        elastic search query.  # noqa: E501

        :return: The es_query of this Explain.  # noqa: E501
        :rtype: object
        """
        return self._es_query

    @es_query.setter
    def es_query(self, es_query):
        """Sets the es_query of this Explain.

        elastic search query.  # noqa: E501

        :param es_query: The es_query of this Explain.  # noqa: E501
        :type: object
        """

        self._es_query = es_query

    @property
    def took(self):
        """Gets the took of this Explain.  # noqa: E501

        elastic search query took time in ms  # noqa: E501

        :return: The took of this Explain.  # noqa: E501
        :rtype: int
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this Explain.

        elastic search query took time in ms  # noqa: E501

        :param took: The took of this Explain.  # noqa: E501
        :type: int
        """

        self._took = took

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
        if issubclass(Explain, dict):
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
        if not isinstance(other, Explain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
