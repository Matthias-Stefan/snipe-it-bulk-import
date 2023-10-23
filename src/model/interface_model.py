__author__ = "Matthias Stefan"
__version__ = "0.1.0"

from src.utility import ModelEvents

import abc


class IModel(abc.ABC):
    model_events = ModelEvents()
