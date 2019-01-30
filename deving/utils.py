from contextlib import contextmanager
from sys import stdin


@contextmanager
def _null_context(argument=None):
    yield argument


def file_context(file_name):
    if file_name is None or file_name == '-':
        return _null_context(stdin)
    else:
        return open(file_name)