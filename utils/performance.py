from contextlib import contextmanager
from collections import namedtuple
import time
import tracemalloc
import gc


class Report:
    def __init__(self, start):
        self.start = start

    @property
    def score(self):
        return self.end - self.start


@contextmanager
def MemoryScore():
    gc.collect()
    tracemalloc.clear_traces()
    data = Report(tracemalloc.start())
    data.start, _ = tracemalloc.get_traced_memory()
    yield data
    _, data.end = tracemalloc.get_traced_memory()


@contextmanager
def SpeedScore():
    data = Report(time.clock())
    yield data
    data.end = time.clock()


@contextmanager
def Score():
    with SpeedScore() as speedData:
        with MemoryScore() as memoryData:
            yield

    print('speed: ', speedData.score)
    print('memory: ', memoryData.score)


class BigO:
    def __init__(self, n, *args, func, scorer=SpeedScore):
        self.n = n
        self.func = func
        self.scorer = scorer

    def check(self, size, times=1, std=0.05):
        ratio = self.n(2 * size) / self.n(size)
        total = 0
        for _ in range(times):
            with self.scorer() as score1:
                self.func(n=size)

            with self.scorer() as score2:
                self.func(n=size * 2)
            total += score2.score / score1.score

        ratio2 = total / times
        assert 1 - 3 * std < (ratio / ratio2) < 1 + 3 * std, 'ratio {} and {} does not match'.format(ratio, ratio2)

class F:
    @staticmethod
    def linear(value):
        return value
