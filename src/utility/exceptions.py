__author__ = "Matthias Stefan"
__version__ = "0.1.0"


class TooManyRequestsError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
