from utils.recursion import stack
from collections import defaultdict


def brutal_pathes(routes, S, T):
    stops = defaultdict(set)

    for route in routes:
        for stop1 in route:
            for stop2 in route:
                if stop1 != stop2:
                    stops[stop1].add(stop2)

    path = []
    passed = dict()

    def search(stop_num):
        with stack(path, stop_num):
            if stop_num in passed and len(path) >= passed[stop_num]:
                return

            passed[stop_num] = len(path)

            if stop_num == T:
                yield path.copy()
            for nxt in stops[stop_num]:
                yield from search(nxt)
            return

    return search(S)


class Solution:
    def numBusesToDestination(self, routes: 'matrix', S: int, T: int) -> int:
        assert len(routes) < 4
        assert len(routes[0]) < 4
        pathes = list(brutal_pathes(routes, S, T))
        try:
            best_path = min(pathes, key=lambda p: len(p))
        except ValueError:
            return -1
        length = len(best_path)
        return length - 1
