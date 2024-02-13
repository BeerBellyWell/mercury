import time
from functools import wraps
from typing import Callable
from core.settings import logger


def time_check_decorator(func: Callable) -> Callable:
    """
    Decorator for measuring the execution time of functions.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func()
        lead_time = time.time() - start

        if lead_time < 60:
            logger.info(f'Execution time of {func.__name__}: {round(lead_time, 2)} sec.')
        else:
            logger.info(f'Execution time of {func.__name__}: {round(lead_time / 60, 2)} min.')

        return result
    return wrapper
