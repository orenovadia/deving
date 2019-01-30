from collections import Counter
from threading import Thread
from time import sleep

import click

from deving.utils import file_context


@click.command(name='counts',
               short_help='Perform O(N) unique counts with reports along the way')
@click.argument(
    'from_file',
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=False),
    required=False
)
def counts(from_file):
    c = Counter()

    def update_progress():
        while True:
            sleep(5)
            print c

    with file_context(from_file) as f:

        t = Thread(target=update_progress)
        t.setDaemon(True)
        t.start()

        c.update(f)
    for item, count in c.iteritems():
        print item.strip(), count


if __name__ == '__main__':
    counts()