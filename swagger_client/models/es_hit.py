# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.43
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class EsHit(object):
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
        'score': 'float',
        'id': 'str',
        'source': 'object',
        'explanation': 'object'
    }

    attribute_map = {
        'score': '_score',
        'id': '_id',
        'source': '_source',
        'explanation': '_explanation'
    }

    def __init__(self, score=None, id=None, source=None, explanation=None, _configuration=None):  # noqa: E501
        """EsHit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._score = None
        self._id = None
        self._source = None
        self._explanation = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if id is not None:
            self.id = id
        if source is not None:
            self.source = source
        if explanation is not None:
            self.explanation = explanation

    @property
    def score(self):
        """Gets the score of this EsHit.  # noqa: E501

        document score.  # noqa: E501

        :return: The score of this EsHit.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this EsHit.

        document score.  # noqa: E501

        :param score: The score of this EsHit.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def id(self):
        """Gets the id of this EsHit.  # noqa: E501

        document id.  # noqa: E501

        :return: The id of this EsHit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EsHit.

        document id.  # noqa: E501

        :param id: The id of this EsHit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source(self):
        """Gets the source of this EsHit.  # noqa: E501

        source fields.  # noqa: E501

        :return: The source of this EsHit.  # noqa: E501
        :rtype: object
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EsHit.

        source fields.  # noqa: E501

        :param source: The source of this EsHit.  # noqa: E501
        :type: object
        """

        self._source = source

    @property
    def explanation(self):
        """Gets the explanation of this EsHit.  # noqa: E501

        es explanation.  # noqa: E501

        :return: The explanation of this EsHit.  # noqa: E501
        :rtype: object
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this EsHit.

        es explanation.  # noqa: E501

        :param explanation: The explanation of this EsHit.  # noqa: E501
        :type: object
        """

        self._explanation = explanation

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
        if issubclass(EsHit, dict):
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
        if not isinstance(other, EsHit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EsHit):
            return True

        return self.to_dict() != other.to_dict()
