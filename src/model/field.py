__author__ = "Matthias Stefan"
__version__ = "1.0.0"


class Field:
    """Represents an attribute in a Snipe-IT Asset.

    This class represents an attribute of a Snipe-IT Asset, including its name, value, and metadata that specifies the
    attribute type.

    :param name: The name of the attribute.
    :type name: str
    :param value: The value of the attribute.
    :type value: Any
    :param meta: The metadata specifying the type of the attribute.
    :type meta: Type
    """
    def __init__(self, name, value, meta):
        self.name = name
        self.value = value
        self.meta = meta

    def __eq__(self, other):
        """Checks if the attribute has the same metadata type as another.

        :param other: Another Field object to compare with.
        :type other: src.model.field.Field
        :return: True if the metadata type is the same, False otherwise.
        :rtype: bool
        """
        return self.meta == type(other)
