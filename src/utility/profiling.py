__author__ = "Matthias Stefan"
__version__ = "1.0.0"

import time

from functools import wraps
from typing import Callable


def profile_function(callback: Callable) -> Callable:
    """Decorator to profile the execution time of a function.

    This decorator can be applied to a function. It measures the time taken for the function to execute and prints the
    elapsed time in milliseconds and seconds.

    :param callback: The function to profile.
    :type callback: Callable
    :return: The profiled function.
    :rtype: Callable
    """
    @wraps(callback)
    def function_(*args, **kwargs):
        begin = time.perf_counter_ns()
        result = callback(*args, **kwargs)
        end = time.perf_counter_ns()
        elapsed_time = end - begin
        print(f"{callback.__name__}: {elapsed_time / 1e+6}ms {elapsed_time / 1e+9}s")
        return result
    return function_
