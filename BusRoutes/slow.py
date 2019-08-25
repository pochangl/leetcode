from collections import defaultdict


def find_steps(routes, S, T):
    stops = defaultdict(set)
    stopped_by = set([])

    for route in routes:
        for stop_num in route:
            stops[stop_num].update(route)
            stops[stop_num].remove(stop_num)

    queue = set([S])
    nxt = set()
    count = 0

    while queue:
        if T in queue:
            return count
        for stop_num in queue:
            if stop_num not in stopped_by:
                stopped_by.add(stop_num)
                nxt.update(stops[stop_num])
                stops.pop(stop_num)
        queue = nxt
        nxt = set()
        count += 1

    return -1


class Solution:
    def numBusesToDestination(self, routes: 'matrix', S: int, T: int) -> int:
        return find_steps(routes, S, T)
