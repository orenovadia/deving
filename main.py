from collections import Counter
from contextlib import contextmanager
from sys import stdin

import click
from tqdm import tqdm

from traceback_extractor import TracebackExtractor


@contextmanager
def _null_context(argument=None):
    yield argument


@click.command()
@click.argument(
    'log_file',
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=False),
    required=False
)
def find_exceptions(log_file):
    with (open(log_file) if log_file else _null_context(stdin)) as f:
        tracebacks = TracebackExtractor().feed_lines(tqdm(f))
        c = Counter(tracebacks)
        for trace, amount in reversed(c.most_common(10)):
            print ('------- {} '.format(amount))
            print (trace)


if __name__ == '__main__':
    find_exceptions()
