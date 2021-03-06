from __future__ import print_function

import csv
from collections import Counter

from deving.pstats_merge import pstats_merge

try:
    # Py2
    from urllib import urlencode
except ImportError:
    # Py3
    from urllib.parse import urlencode

import click
from tqdm import tqdm

from deving.line_counts import counts
from deving.traceback_extractor import TracebackExtractor


@click.group('main')
def main():
    pass


@main.command(short_help='Aggregate python tracebacks and exceptions')
@click.argument(
    'log_file',
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=False),
    required=False
)
@click.option(
    '--top-n',
    default=10
)
def find_exceptions(log_file, top_n):
    with click.open_file(log_file or '-') as f:
        tracebacks = TracebackExtractor().feed_lines(tqdm(f))
        c = Counter(tracebacks)
        for trace, amount in reversed(c.most_common(top_n)):
            print('------- {} '.format(amount))
            print(trace)


@main.command(name='histogram',
              short_help='Plot a histogram of words from stdin or specified file')
@click.argument(
    'from_file',
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=False),
    required=False
)
def histogram(from_file):
    import pandas as pd
    import matplotlib
    with click.open_file(from_file or '-') as f:
        df = (pd
              .read_csv(f, names=['name'], quoting=csv.QUOTE_NONE)
              .groupby('name')
              .size()
              .to_frame(name='size')
              .sort_values('size', ascending=False)  # type: pd.DataFrame
              )

    df[:50].plot.barh(figsize=(13, 8))
    matplotlib.pyplot.show()


@main.command(short_help='Encode lines of input file as url parameters')
@click.argument(
    'from_file',
    type=click.Path(exists=False, file_okay=True, dir_okay=False, resolve_path=False),
    required=False
)
@click.argument(
    'url',
    type=click.STRING,
    required=True
)
@click.argument(
    'parameter_name',
    type=click.STRING,
    required=True
)
def encode_parameters(from_file, url, parameter_name):
    with click.open_file(from_file or '-') as f:
        for row in f:
            print(url + "?" + urlencode({parameter_name: row.strip()}))


main.add_command(counts, 'counts')
main.add_command(pstats_merge, 'pstats_merge')

if __name__ == '__main__':
    main()
