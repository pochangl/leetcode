from unittest import TestCase
from itertools import product
from .brutal import BrutalSolution, brutal_pathes
from .main import Solution


class TestBrutal(TestCase):
    def run_test(self, routes, S, T, expect):
        answer = BrutalSolution().numBusesToDestination(routes, S, T)
        self.assertEqual(answer, expect, routes)

    def test_case1(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        S = 1
        T = 6
        self.run_test(routes, S, T, 2)

    def test_case2(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        S = 1
        T = 6
        pathes = list(brutal_pathes(routes, S, T))
        best_path = min(pathes, key=lambda p: len(p))
        self.assertEqual(best_path, [1, 7, 6])

    def test_empty(self):
        routes = [[1, 2, 5], [3, 6, 7]]
        S = 1
        T = 6
        self.run_test(routes, S, T, -1)

    def test_no_move(self):
        routes = [[0, 0, 0], [0, 0, 0]]
        S = 0
        T = 0
        self.run_test(routes, S, T, 0)


class TestSolution(TestCase):
    def test_small_brutal(self):
        size = 3
        for lst in product(range(size), repeat=size * size):
            routes = [
                list(lst[:3]),
                list(lst[3:6]),
                list(lst[6:9]),
            ]
            answer = BrutalSolution().numBusesToDestination(routes, 0, 8)
            result = Solution().numBusesToDestination(routes, 0, 8)
            self.assertEqual(answer, result, routes)
