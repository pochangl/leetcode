from collections import defaultdict
from itertools import combinations


def find_steps(routes, S, T):
    if S == T:
        return 0
    routes = list(map(set, routes))
    buses = defaultdict(set)
    last_bus = set(filter(lambda bus_num: T in routes[bus_num], range(len(routes))))
    visited = set()

    for bus_num1, bus_num2 in combinations(range(len(routes)), 2):
        if routes[bus_num1] & routes[bus_num2]:
            buses[bus_num1].add(bus_num2)
            buses[bus_num2].add(bus_num1)

    queue = set()
    for bus_num, route in enumerate(routes):
        if S in route:
            queue.add(bus_num)

    nxt = set()
    count = 1

    while queue:
        if queue & last_bus:
            return count
        for bus_num in queue:
            if bus_num not in visited:
                visited.add(bus_num)
                nxt.update(buses[bus_num])
                buses.pop(bus_num)
        queue = nxt
        nxt = set()
        count += 1

    return -1


class Solution:
    def numBusesToDestination(self, routes: 'matrix', S: int, T: int) -> int:
        return find_steps(routes, S, T)
