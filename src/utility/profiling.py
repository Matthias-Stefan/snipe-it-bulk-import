__author__ = "Matthias Stefan"
__version__ = "0.1.0"

import time

from typing import Callable


def profile_function(callback: Callable) -> Callable:
    def function_(*args, **kwargs):
        begin = time.perf_counter_ns()
        result = callback(*args, **kwargs)
        end = time.perf_counter_ns()
        elapsed_time = end - begin
        print(f"{callback.__name__}: {elapsed_time / 1e+6}ms {elapsed_time / 1e+9}s")
        return result
    return function_
