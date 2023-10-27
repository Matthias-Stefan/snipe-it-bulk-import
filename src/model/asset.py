__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.model.field import Field

import re

from datetime import datetime


class Asset:
    """Represents a Snipe-IT asset with attributes.

    This class represents a Snipe-IT asset with a combination of standard and custom fields.

    :param _standard_fields: A dictionary of standard fields.
    :type _standard_fields: dict
    :param _custom_fields: A dictionary of custom fields.
    :type _custom_fields: dict
    """
    def __init__(self):
        self._standard_fields: dict = self._init_standard_fields()
        self._custom_fields: dict = {}

    def __len__(self):
        """Get the total number of attributes in the asset.

        This method returns the total number of attributes in the asset, which includes both standard and custom fields.

        :return: The total number of attributes in the asset.
        :rtype: int
        """
        return len(self._standard_fields) + len(self._custom_fields)

    def __str__(self):
        """Convert the asset to a human-readable string representation.

        This method converts the asset object into a human-readable string representation. It includes the names, metadata types, and values of all attributes.

        :return: A string representation of the asset.
        :rtype: str
        """
        result = "standard fields:\n"
        for field in self._standard_fields.values():
            result += f"{field.name}[{field.meta}]: {field.value}\n"
        result += "custom fields:\n"
        for field in self._custom_fields.values():
            result += f"{field.name}[{field.meta}]: {field.value}\n"
        return result

    def get(self, validate_not_none: bool = False):
        """Get the asset attributes as a dictionary.

        :param validate_not_none: If True, exclude attributes with None values.
        :type validate_not_none: bool
        :return: A dictionary of asset attributes.
        :rtype: dict
        """
        result = {}
        chain: dict = dict(self._standard_fields, **self._custom_fields)
        if len(chain) <= 0:
            return result
        for key, attribute in chain.items():
            if validate_not_none:
                if not attribute.value:
                    continue
            result[key] = attribute.value
        return result

    def set_required_field_values(self, status_id: int, model_id: int):
        """Set the values of required standard fields.

        :param status_id: The status ID to set.
        :type status_id: int
        :param model_id: The model ID to set.
        :type model_id: int
        """
        self._standard_fields['status_id'].value = status_id
        self._standard_fields['model_id'].value = model_id

    def set_standard_field_value(self, key: str, value: any):
        """Set the value of a standard field.

        :param key: The name of the standard field.
        :type key: str
        :param value: The value to set.
        :type value: any
        """
        if key is None or key not in self._standard_fields:
            self._standard_fields[key] = Field(key, value, type(value))
            return
        self._standard_fields[key].value = value

    def set_custom_field_value(self, key: str, value: any):
        """Set the value of a custom field.

        :param key: The name of the custom field.
        :type key: str
        :param value: The value to set.
        :type value: any
        """
        if key is None or key not in self._custom_fields:
            self._custom_fields[key] = Field(key, value, type(value))
            return
        self._custom_fields[key].value = value

    @classmethod
    def from_csv(cls, data):
        """Create an Asset object from CSV data.

        :param data: The CSV data to create the asset from.
        :type data: dict
        :return: An Asset object created from the CSV data.
        :rtype: Asset
        """
        asset = Asset()
        for key, value in data.items():
            if type(value) is str and len(value) <= 0:
                continue
            if key == 'purchase_date':
                value = asset.convert_date(value)
                asset.set_standard_field_value(key, value)
                continue

            if key in asset._standard_fields:
                asset.set_standard_field_value(key, asset._standard_fields[key].meta(value))
            elif re.match('_', key):  # NOTE: custom_field
                asset.set_custom_field_value(key, value)
        return asset

    @classmethod
    def _init_standard_fields(cls) -> dict:
        """Initialize the standard fields of the asset.

        :return: A dictionary of standard fields.
        :rtype: dict
        """
        attributes = [("id", int),
                      ("name", str),
                      ("asset_tag", str),
                      ("model_id", int),
                      ("serial", str),
                      ("purchase_date", type(datetime)),
                      ("purchase_cost", float),
                      ("order_number", str),
                      ("assigned_to", int),
                      ("notes", str),
                      ("image", type(datetime)),
                      ("user_id", int),
                      ("created_at", type(datetime)),
                      ("updated_at", type(datetime)),
                      ("physical", int),
                      ("deleted_at", type(datetime)),
                      ("status_id", int),
                      ("archived", bool),
                      ("warranty_months", int),
                      ("depreciate", bool),
                      ("supplier_id", int),
                      ("requestable", bool),
                      ("rtd_location_id", int),
                      ("accepted", str),
                      ("last_checkout", type(datetime)),
                      ("expected_checkout", type(datetime)),
                      ("company_id", int),
                      ("assigned_type", str),
                      ("last_audit_date", type(datetime)),
                      ("next_audit_date", type(datetime)),
                      ("location_id", int),
                      ("checkin_counter", int),
                      ("checkout_counter", int),
                      ("requests_counter", int),
                      ("model_number", str),
                      ("alt_barcode", str),
                      ("user_can_checkout", str),
                      ("category", str),
                      ("manufacturer", str)]
        result: dict = {}
        for attribute in attributes:
            result[attribute[0]] = Field(attribute[0], None, attribute[1])
        return result

    def convert_date(self, date_str=None):
        """Convert a date string to the 'YYYY-MM-DD' format.

        :param date_str: The input date string in 'DD.MM.YYYY' format.
        :type date_str: str
        :return: The converted date in 'YYYY-MM-DD' format or an error message.
        :rtype: str
        """
        try:
            if date_str is None:
                today_date = datetime.now()
                return today_date.strftime('%Y-%m-%d')
            else:
                input_date = datetime.strptime(date_str, '%d.%m.%Y')
                converted_date = input_date.strftime('%Y-%m-%d')
                return converted_date
        except ValueError as error:
            return str(error)
