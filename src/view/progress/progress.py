__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from kivymd.color_definitions import colors
from kivymd.uix.anchorlayout import MDAnchorLayout

import threading


class ProgressInfo(MDAnchorLayout):
    """Managing progress information.

    :param kwargs: Extra keyword arguments passed to the super constructor.
    """
    def __init__(self, **kwargs):
        super(ProgressInfo, self).__init__(**kwargs)
        self._is_active: bool = False
        self._value: int = 0
        self._color = colors["Red"]["700"]
        self._info = ""
        self._lock = threading.Lock()

    def reset(self):
        """Reset progress info.

        :rtype: None
        """
        self._lock.acquire()
        self.is_active = True
        self.value = 0
        self.color = colors["Red"]["700"]
        self.info = ""
        self._lock.release()

    def advance(self, amount: int, info: str, state: bool):
        """Advance progress.

        :param amount: The amount to advance the progress.
        :type amount: int
        :param info: Information about the progress.
        :type: info: str
        :param state: Information about the state.
        :type: state: bool
        :rtype: None
        """
        self._lock.acquire()
        assert self._value <= 100
        self.value = min((self._value + amount), 100)
        if self._value == 100:
            self.color = colors["Green"]["700"]
        elif self.value > 85:
            self.color = colors["Green"]["300"]
        elif self.value > 40:
            self.color = colors["Amber"]["700"]
        self.info = info
        if self.value == 100:
            self.is_active = False
        if not state:
            self.color = colors["Red"]["700"]
        self._lock.release()

    @property
    def is_active(self):
        """Indicate if progress tracking is active.

        :type: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = value
        self.ids.mdsp_progress.active = value

    @property
    def value(self):
        """Progress amount.

        :type: int
        """
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.ids.pb_progress_bar.value = value

    @property
    def color(self):
        """UI color.

        :type: str
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.ids.mdsp_progress.color = value
        self.ids.pb_progress_bar.color = value

    @property
    def info(self):
        """Information about what's currently happening.

        :type: str
        """
        return self._info

    @info.setter
    def info(self, value):
        self._info = value
        self.ids.lb_progress_info.text = value
