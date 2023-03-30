# coding: utf-8

"""
    TeePublic V3 search Api Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.39
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class DesignSlim(object):
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
        'artist_slug': 'str',
        'artist_name': 'str',
        'primary_tag': 'str',
        'primary_related_tags': 'list[str]',
        'secondary_tags': 'list[str]',
        'sales': 'object',
        'fam_approved': 'bool',
        'click_through_rate': 'object',
        'explanation': 'object'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'artist_slug': 'artist_slug',
        'artist_name': 'artist_name',
        'primary_tag': 'primary_tag',
        'primary_related_tags': 'primary_related_tags',
        'secondary_tags': 'secondary_tags',
        'sales': 'sales',
        'fam_approved': 'fam_approved',
        'click_through_rate': 'click_through_rate',
        'explanation': 'explanation'
    }

    def __init__(self, id=None, title=None, artist_slug=None, artist_name=None, primary_tag=None, primary_related_tags=None, secondary_tags=None, sales=None, fam_approved=None, click_through_rate=None, explanation=None, _configuration=None):  # noqa: E501
        """DesignSlim - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._title = None
        self._artist_slug = None
        self._artist_name = None
        self._primary_tag = None
        self._primary_related_tags = None
        self._secondary_tags = None
        self._sales = None
        self._fam_approved = None
        self._click_through_rate = None
        self._explanation = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if artist_slug is not None:
            self.artist_slug = artist_slug
        if artist_name is not None:
            self.artist_name = artist_name
        if primary_tag is not None:
            self.primary_tag = primary_tag
        if primary_related_tags is not None:
            self.primary_related_tags = primary_related_tags
        if secondary_tags is not None:
            self.secondary_tags = secondary_tags
        if sales is not None:
            self.sales = sales
        if fam_approved is not None:
            self.fam_approved = fam_approved
        if click_through_rate is not None:
            self.click_through_rate = click_through_rate
        if explanation is not None:
            self.explanation = explanation

    @property
    def id(self):
        """Gets the id of this DesignSlim.  # noqa: E501

        design id.  # noqa: E501

        :return: The id of this DesignSlim.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DesignSlim.

        design id.  # noqa: E501

        :param id: The id of this DesignSlim.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this DesignSlim.  # noqa: E501

        design title.  # noqa: E501

        :return: The title of this DesignSlim.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DesignSlim.

        design title.  # noqa: E501

        :param title: The title of this DesignSlim.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def artist_slug(self):
        """Gets the artist_slug of this DesignSlim.  # noqa: E501

        Unique identifier of the design's creator.  # noqa: E501

        :return: The artist_slug of this DesignSlim.  # noqa: E501
        :rtype: str
        """
        return self._artist_slug

    @artist_slug.setter
    def artist_slug(self, artist_slug):
        """Sets the artist_slug of this DesignSlim.

        Unique identifier of the design's creator.  # noqa: E501

        :param artist_slug: The artist_slug of this DesignSlim.  # noqa: E501
        :type: str
        """

        self._artist_slug = artist_slug

    @property
    def artist_name(self):
        """Gets the artist_name of this DesignSlim.  # noqa: E501

        Name of the store that houses this design.  # noqa: E501

        :return: The artist_name of this DesignSlim.  # noqa: E501
        :rtype: str
        """
        return self._artist_name

    @artist_name.setter
    def artist_name(self, artist_name):
        """Sets the artist_name of this DesignSlim.

        Name of the store that houses this design.  # noqa: E501

        :param artist_name: The artist_name of this DesignSlim.  # noqa: E501
        :type: str
        """

        self._artist_name = artist_name

    @property
    def primary_tag(self):
        """Gets the primary_tag of this DesignSlim.  # noqa: E501

        design primary tag.  # noqa: E501

        :return: The primary_tag of this DesignSlim.  # noqa: E501
        :rtype: str
        """
        return self._primary_tag

    @primary_tag.setter
    def primary_tag(self, primary_tag):
        """Sets the primary_tag of this DesignSlim.

        design primary tag.  # noqa: E501

        :param primary_tag: The primary_tag of this DesignSlim.  # noqa: E501
        :type: str
        """

        self._primary_tag = primary_tag

    @property
    def primary_related_tags(self):
        """Gets the primary_related_tags of this DesignSlim.  # noqa: E501

        design primary related tags.  # noqa: E501

        :return: The primary_related_tags of this DesignSlim.  # noqa: E501
        :rtype: list[str]
        """
        return self._primary_related_tags

    @primary_related_tags.setter
    def primary_related_tags(self, primary_related_tags):
        """Sets the primary_related_tags of this DesignSlim.

        design primary related tags.  # noqa: E501

        :param primary_related_tags: The primary_related_tags of this DesignSlim.  # noqa: E501
        :type: list[str]
        """

        self._primary_related_tags = primary_related_tags

    @property
    def secondary_tags(self):
        """Gets the secondary_tags of this DesignSlim.  # noqa: E501

        design secondary tags.  # noqa: E501

        :return: The secondary_tags of this DesignSlim.  # noqa: E501
        :rtype: list[str]
        """
        return self._secondary_tags

    @secondary_tags.setter
    def secondary_tags(self, secondary_tags):
        """Sets the secondary_tags of this DesignSlim.

        design secondary tags.  # noqa: E501

        :param secondary_tags: The secondary_tags of this DesignSlim.  # noqa: E501
        :type: list[str]
        """

        self._secondary_tags = secondary_tags

    @property
    def sales(self):
        """Gets the sales of this DesignSlim.  # noqa: E501

        sales information  # noqa: E501

        :return: The sales of this DesignSlim.  # noqa: E501
        :rtype: object
        """
        return self._sales

    @sales.setter
    def sales(self, sales):
        """Sets the sales of this DesignSlim.

        sales information  # noqa: E501

        :param sales: The sales of this DesignSlim.  # noqa: E501
        :type: object
        """

        self._sales = sales

    @property
    def fam_approved(self):
        """Gets the fam_approved of this DesignSlim.  # noqa: E501

        is the design FAM approved  # noqa: E501

        :return: The fam_approved of this DesignSlim.  # noqa: E501
        :rtype: bool
        """
        return self._fam_approved

    @fam_approved.setter
    def fam_approved(self, fam_approved):
        """Sets the fam_approved of this DesignSlim.

        is the design FAM approved  # noqa: E501

        :param fam_approved: The fam_approved of this DesignSlim.  # noqa: E501
        :type: bool
        """

        self._fam_approved = fam_approved

    @property
    def click_through_rate(self):
        """Gets the click_through_rate of this DesignSlim.  # noqa: E501

        click through rate information  # noqa: E501

        :return: The click_through_rate of this DesignSlim.  # noqa: E501
        :rtype: object
        """
        return self._click_through_rate

    @click_through_rate.setter
    def click_through_rate(self, click_through_rate):
        """Sets the click_through_rate of this DesignSlim.

        click through rate information  # noqa: E501

        :param click_through_rate: The click_through_rate of this DesignSlim.  # noqa: E501
        :type: object
        """

        self._click_through_rate = click_through_rate

    @property
    def explanation(self):
        """Gets the explanation of this DesignSlim.  # noqa: E501

        es explanation.  # noqa: E501

        :return: The explanation of this DesignSlim.  # noqa: E501
        :rtype: object
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this DesignSlim.

        es explanation.  # noqa: E501

        :param explanation: The explanation of this DesignSlim.  # noqa: E501
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
        if issubclass(DesignSlim, dict):
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
        if not isinstance(other, DesignSlim):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DesignSlim):
            return True

        return self.to_dict() != other.to_dict()
