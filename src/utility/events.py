__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from events.events import Events


class ModelEvents(Events):
    """Defines events related to model changes.

    This class extends the Events class to include one custom event:
    :event on_changed: Triggered when a change is observed in the model.
    """
    __events__ = 'on_changed'


class ProgressEvents(Events):
    """Defines events related to progress updates.

    This class extends the Events class to include two custom events:
    :event advance: Triggered when the progress advances.
    :event reset: Triggered when the progress is reset.
    """
    __events__ = ('advance', 'reset')
