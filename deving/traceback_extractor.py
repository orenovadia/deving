from __future__ import print_function

import re

from enum import Enum


class State(Enum):
    nothing = 1
    in_trace = 2


class TraceSink(object):
    def __init__(self):
        self.buff = ''

    def feed_line(self, line):
        self.buff += line

    def export(self):
        return self.buff


error_pat = re.compile('^\w+Error:')


class TracebackExtractor(object):

    def __init__(self):
        self.state = State.nothing
        self._new_sink()

    def feed_lines(self, lines):
        for line in lines:
            possible_trace = self._feed_line(line)
            if possible_trace:
                yield possible_trace

    def _feed_line(self, line):
        if self.state is State.nothing and line.startswith('Traceback'):
            self.state = State.in_trace
            self._new_sink()
            self.sink.feed_line(line)
            return None

        elif self.state is State.in_trace:
            self.sink.feed_line(line)
            if error_pat.match(line):
                self.state = State.nothing
                traceback = self.sink.export()
                self._new_sink()
                return traceback

    def _new_sink(self):
        self.sink = TraceSink()


if __name__ == '__main__':
    t = TracebackExtractor()
    for i in t.feed_lines(['Traceback\n', 'bar\n', 'FooError:a\n']):
        print('------', i, '----')
