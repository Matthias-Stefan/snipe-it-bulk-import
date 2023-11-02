__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.template import ITemplate
from src.model import Asset

import csv
import pathlib

from datetime import datetime


class CreateAssetTemplate(ITemplate):
    """Represents a template for creating asset records in a CSV file.

    This template is used to generate CSV files with asset information, including Snipe-IT model, quantity,
    Snipe-IT status label and file path.

    :param sit_model: A dictionary representing the Snipe-IT model.
    :type sit_model: dict
    :param quantity: The quantity of asset records to create.
    :type quantity: int
    :param status_label: A dictionary representing the Snipe-IT status label.
    :type status_label: dict
    :param filepath: The path to save the generated CSV file.
    :type filepath: str
    """
    def __init__(self, sit_model: dict, quantity: int, status_label: dict, filepath: str):
        self.sit_model: dict = sit_model
        self.quantity: int = quantity
        self.status_label: dict = status_label
        self.filepath: str = filepath

    def create(self) -> pathlib.Path:
        """Creates the asset records and saves them to a CSV file.

        :return: The path to the generated CSV file.
        :rtype: pathlib.Path
        """
        filepath = self._build_filepath()
        asset = self._build_asset()
        with open(filepath, "w+", newline='', encoding='utf-8-sig') as file:
            content: dict = asset.get()
            writer = csv.DictWriter(file, content.keys(), delimiter=';')
            writer.writeheader()
            for _ in range(self.quantity):
                writer.writerow(content)
        return filepath

    def _build_filepath(self) -> pathlib.Path:
        """Builds the path for the generated CSV file.

        :return: The path to the CSV file.
        :rtype: pathlib.Path
        """
        stamp: str = f"{datetime.now().strftime('%y%m%d_%H%M%S')}"
        stub: str = ".csv"
        filepath: str = f"{self.filepath}_{stamp}{stub}"
        return pathlib.Path(filepath)

    def _build_asset(self) -> Asset:
        """Builds an asset object with associated information.

        :return: An Asset object with predefined field values.
        :rtype: src.model.asset.Asset
        """
        asset = Asset()
        asset.set_required_field_values(self.status_label.get('id'), self.sit_model.get('id'))
        if 'fieldset' in self.sit_model:
            for custom_field in self.sit_model['default_fieldset_values']:
                if isinstance(custom_field, dict):
                    asset.set_custom_field_value(custom_field['db_column_name'], custom_field['default_value'])
        return asset
