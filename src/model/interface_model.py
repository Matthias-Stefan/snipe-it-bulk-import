__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.utility import ModelEvents

import abc

from enum import Enum


class IModel(abc.ABC):
    model_events = ModelEvents()


class ModelProperties(Enum):
    MODEL = 101,
    QUANTITY = 102,
    STATUS_LABEL = 103
    FILEPATH = 104,
    AUTOSTART = 105,
    AUTO_UPLOAD = 106,

    URL = 401,
    TOKEN = 402,
    OUTPUT_DIR = 403,
    EXCEL_PATH = 404
