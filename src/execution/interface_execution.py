__author__ = "Matthias Stefan"
__version__ = "1.0.0"

import abc
import csv


class IExecution(abc.ABC):
    """
    Initialize an instance of the IExecution class.

    This is an abstract class representing an execution task. It takes a CSV reader as input and initializes a SnipeManager.

    :param reader: A CSV reader to process data.
    :type reader: csv.DictReader
    """
    def __init__(self, reader: csv.DictReader):
        self._reader = reader

    def process(self):
        """
        Process data from the CSV reader.

        This method iterates over the rows in the CSV reader and calls the abstract method process_row for each row.
        """
        for row in self._reader:
            self.process_row(row)

    @abc.abstractmethod
    def process_row(self, row):
        """
        Process a single row of data.

        This is an abstract method that must be implemented by subclasses. It defines how a single row of data should be processed.

        :param row: A row of data to be processed.
        :type row: dict
        """
        pass
