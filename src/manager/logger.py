__author__ = "Matthias Stefan"
__version__ = "1.0.0"

import logging
import os.path

from datetime import datetime
from functools import wraps
from typing import Callable


class BulkImportLogger(logging.Logger):
    """This class extends the standard Logger class to provide additional logging functionality for bulk imports.

    :param name: The name of the logger.
    :type name: str
    :rtype: None
    """
    def __init__(self, name):
        super(BulkImportLogger, self).__init__(name)
        from globals import Globals
        self.add_file_handler(Globals.get_logs_dir())

    def add_file_handler(self, log_dir):
        """Add a file handler to the logger.

        This method configures a file handler to log messages to a specific log file.

        :param log_dir: The directory where log files will be stored.
        :type log_dir: str
        :rtype: None
        """
        timestamp = datetime.now().strftime('%y%m%d_%H%M%S')
        log_file = os.path.join(log_dir, f'{timestamp}.log')
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(thread)d %(threadName)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.addHandler(handler)

    def log_function(self, callback: Callable) -> Callable:
        """Decorator for logging function calls and their arguments.

        This decorator logs the calling of a function, its arguments, and its return value.

        :param callback: The function to be logged.
        :type callback: Callable
        :return: The decorated function.
        :rtype: typing.Callable
        """
        @wraps(callback)
        def function_(*args, **kwargs):
            filename = os.path.basename(callback.__code__.co_filename)
            line_number = callback.__code__.co_firstlineno
            class_name = callback.__qualname__.split('.')[0]
            function_name = callback.__name__
            addition_to_log_record = f'{filename} - {line_number} - {class_name} - {function_name} - '

            self.info(f'{addition_to_log_record}invoked')

            for arg_name, arg_value in zip(callback.__code__.co_varnames, args):
                self.info(f'{addition_to_log_record}{arg_name} = {arg_value}')

            for kwarg_name, kwarg_value in kwargs.items():
                self.info(f'{addition_to_log_record}{kwarg_name} = {kwarg_value}')

            result = callback(*args, **kwargs)

            self.info(f'{addition_to_log_record}returned: {result}')
            return result
        return function_


Logger = BulkImportLogger('bulk_import_logger')
