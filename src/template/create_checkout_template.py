__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.template import ITemplate

import csv
import pathlib

from datetime import datetime


class CreateCheckoutTemplate(ITemplate):
    """Represents a template for creating asset checkout records in a CSV file.

    This template is used to generate CSV files for asset checkouts, providing the file path to save the generated
    CSV file.

    :param filepath: The path to save the generated CSV file.
    :type filepath: str
    """
    def __init__(self, filepath: str):
        self.filepath: str = filepath

    def create(self) -> pathlib.Path:
        """Creates the asset checkout records and saves them to a CSV file.

        :return: The path to the generated CSV file.
        :rtype: pathlib.Path
        """
        filepath = self._build_filepath()
        with open(filepath, "w+", newline='', encoding='utf-8-sig') as file:
            header: list = ["asset_tag", "checkout_to_{user/asset/location}", "checkout_id", "status_id"]
            writer = csv.DictWriter(file, header, delimiter=';')
            writer.writeheader()
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
