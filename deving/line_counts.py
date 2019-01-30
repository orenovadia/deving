from __future__ import print_function

from collections import Counter
from threading import Thread
from time import sleep

import click

from deving.utils import file_context


@click.command(name='counts')
@click.argument(
    'from_file',
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=False),
    required=False
)
def counts(from_file):
    """
    Perform O(N) unique counts with reports along the way
    Example:
        $ seq 3 | dev-counts
    """
    c = Counter()

    def update_progress():
        while True:
            sleep(5)
            print(c)

    with file_context(from_file) as f:

        t = Thread(target=update_progress)
        t.setDaemon(True)
        t.start()

        c.update(r.strip() for r in f)

    for item, count in c.items():
        print(item, count)


if __name__ == '__main__':
    counts()
