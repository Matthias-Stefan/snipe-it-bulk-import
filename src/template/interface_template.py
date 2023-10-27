__author__ = "Matthias Stefan"
__version__ = "1.0.0"


import abc
import pathlib


class ITemplate(abc.ABC):
    """Interface for template classes that generate and save data.
    This abstract base class defines a method for creating data and returning the path to the saved data as a
    pathlib.Path object.

    All template classes implementing this interface must provide an implementation for the 'create' method.

    :param abc.ABC: Abstract base class for template classes.
    """
    @abc.abstractmethod
    def create(self) -> pathlib.Path:
        """Creates and saves data to a file and returns the path to the saved file.

        :return: The path to the saved file.
        :rtype: pathlib.Path
        """
        pass
