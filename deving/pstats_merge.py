from __future__ import print_function

import pstats

import click


@click.command(name='pstats_merge')
@click.argument(
    'from_files',
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=False),
    required=True,
    nargs=-1
)
@click.argument(
    'to_file',
    type=click.Path(exists=False, file_okay=True, dir_okay=False, resolve_path=False),
    required=True
)
def pstats_merge(from_files, to_file):
    """
    Merges multiple pstat files to one
    Using: https://docs.python.org/2/library/profile.html
    """
    p = pstats.Stats(*from_files)
    p.dump_stats(to_file)


if __name__ == '__main__':
    pstats_merge()
