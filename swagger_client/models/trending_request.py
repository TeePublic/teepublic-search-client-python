# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TrendingRequest(object):
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
        'batch_id': 'str',
        'results': 'list[TrendingResult]'
    }

    attribute_map = {
        'batch_id': 'batch_id',
        'results': 'results'
    }

    def __init__(self, batch_id=None, results=None):  # noqa: E501
        """TrendingRequest - a model defined in Swagger"""  # noqa: E501

        self._batch_id = None
        self._results = None
        self.discriminator = None

        if batch_id is not None:
            self.batch_id = batch_id
        if results is not None:
            self.results = results

    @property
    def batch_id(self):
        """Gets the batch_id of this TrendingRequest.  # noqa: E501

        Batch id.  # noqa: E501

        :return: The batch_id of this TrendingRequest.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this TrendingRequest.

        Batch id.  # noqa: E501

        :param batch_id: The batch_id of this TrendingRequest.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def results(self):
        """Gets the results of this TrendingRequest.  # noqa: E501

        List of trending results.  # noqa: E501

        :return: The results of this TrendingRequest.  # noqa: E501
        :rtype: list[TrendingResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this TrendingRequest.

        List of trending results.  # noqa: E501

        :param results: The results of this TrendingRequest.  # noqa: E501
        :type: list[TrendingResult]
        """

        self._results = results

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
        if issubclass(TrendingRequest, dict):
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
        if not isinstance(other, TrendingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
