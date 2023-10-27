__author__ = "Matthias Stefan"
__version__ = "1.0.0"

from typing import Callable


class Endpoint:
    """Initialize an instance of the Endpoint class.

    This class represents an HTTP endpoint for making requests. It stores the URL value, a callback function, and
    request parameters.

    :rtype: None
    """
    def __init__(self):
        self.value: str = ""
        self.callback: Callable = None
        self.payload: dict = {}

    def get_params(self):
        """Get the parameters of the endpoint.

        :rtype: tuple
        :return: A tuple containing the URL value and payload dictionary.
        """
        return self.value, self.payload
