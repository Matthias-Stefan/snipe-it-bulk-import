__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from events.events import Events


class ProgressEvents(Events):
    __events__ = ('advance', 'reset')


class ModelEvents(Events):
    __events__ = 'on_changed'
