__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.model.field import Field

import re

from typing import cast
from datetime import datetime


class Asset:
    def __init__(self):
        self._standard_fields: dict = self._init_standard_fields()
        self._custom_fields: dict = {}

    def __len__(self):
        return len(self._standard_fields) + len(self._custom_fields)

    def __str__(self):
        result = "standard fields:\n"
        for field in self._standard_fields.values():
            result += f"{field.name}[{field.meta}]: {field.value}\n"
        result += "custom fields:\n"
        for field in self._custom_fields.values():
            result += f"{field.name}[{field.meta}]: {field.value}\n"
        return result

    def get(self, validate_not_none: bool = False):
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

    def set_required_field_values(self, status_id, model_id):
        self._standard_fields['status_id'].value = status_id
        self._standard_fields['model_id'].value = model_id

    def set_standard_field_value(self, key: str, value: any):
        if key is None or key not in self._standard_fields:
            self._standard_fields[key] = Field(key, value, type(value))
            return
        self._standard_fields[key].value = value

    def set_custom_field_value(self, key: str, value: any):
        if key is None or key not in self._custom_fields:
            self._custom_fields[key] = Field(key, value, type(value))
            return
        self._custom_fields[key].value = value

    @classmethod
    def from_csv(cls, data):
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
