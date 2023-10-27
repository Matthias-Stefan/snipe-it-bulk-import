__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.execution import IExecution, ModelUploadExecutor, CheckoutUploadExecutor

import csv


class UploadExecutor:
    @staticmethod
    def process_csv(filepath: str):
        """
        Process a CSV file based on its content.

        This method processes a CSV file and determines the appropriate executor based on the columns in the CSV.
        If it contains 'model_id' column, it uses the ModelUploadExecutor, and if it contains 'checkout_id' column,
        it uses the CheckoutUploadExecutor.

        :param filepath: The path to the CSV file to process.
        :type filepath: str
        """
        with open(filepath, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            if 'model_id' in reader.fieldnames:
                executor: IExecution = ModelUploadExecutor(reader)
            elif 'checkout_id' in reader.fieldnames:
                executor: IExecution = CheckoutUploadExecutor(reader)
            else:
                return
            executor.process()
