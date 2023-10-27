__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.utility import ModelEvents

import abc

from enum import Enum


class IModel(abc.ABC):
    """Interface for model classes that manage and represent data.

    This abstract base class defines a common interface for model classes responsible for managing data and events
    related to data changes.

    :param abc.ABC: Abstract base class for model classes.
    """
    model_events = ModelEvents()


class ModelProperties(Enum):
    """Enumeration of model properties.

    This enumeration defines a set of model properties as named constants, allowing easy referencing of model
    properties for events and updates.
    """
    MODEL = 1,
    QUANTITY = 2,
    STATUS_LABEL = 3
    FILEPATH = 3,
    AUTOSTART = 4,
    AUTO_UPLOAD = 5,
    URL = 6,
    TOKEN = 7,
    OUTPUT_DIR = 8,
    EXCEL_PATH = 9
