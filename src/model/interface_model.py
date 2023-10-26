__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from src.utility import ModelEvents

import abc

from enum import Enum


class IModel(abc.ABC):
    model_events = ModelEvents()


class ModelProperties(Enum):
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
