__author__ = "Matthias Stefan"
__version__ = "1.0.0"


class TooManyRequestsError(Exception):
    """Custom exception class to represent a 'Too Many Requests' error.

    This exception is raised when there are too many requests made within a specified time frame,
    indicating rate limiting or throttling issues.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
