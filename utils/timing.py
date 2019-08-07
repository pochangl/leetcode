from contextlib import contextmanager
from collections import namedtuple
import time
import tracemalloc


class Data:
    pass


class SpeedData:
    @property
    def duration(self):
        return self.end - self.start


class MemoryData:
    @property
    def total_usage(self):
        return self.end - self.start


@contextmanager
def memory():
    tracemalloc.start()
    data = MemoryData()
    data.start = tracemalloc.get_tracemalloc_memory()
    yield data
    data.end = tracemalloc.get_tracemalloc_memory()


@contextmanager
def speed():
    data = SpeedData()
    data.start = time.clock()
    yield data
    data.end = time.clock()


@contextmanager
def Score(silent=False):
    data = Data()

    with speed() as speedData:
        with memory() as memoryData:
            yield data

    data.speed = speedData
    data.memory = memoryData
    if not silent:
        print('speed: ', data.speed.duration, '\n')
        print('memory: ', data.memory.total_usage, '\n')
