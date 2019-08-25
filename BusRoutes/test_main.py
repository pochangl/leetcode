from unittest import TestCase
from itertools import product
from .brutal import BrutalSolution, brutal_pathes
from .main import Solution


class Mixin:
    def test_case1(self):
        '題目自備的情境'
        routes = [[1, 2, 7], [3, 6, 7]]
        S = 1
        T = 6
        self.run_test(routes, S, T, 2)

    def test_empty(self):
        '測沒有結果'
        routes = [[1, 2, 5], [3, 6, 7]]
        S = 1
        T = 6
        self.run_test(routes, S, T, -1)

    def test_no_move(self):
        '原地不動'
        routes = [[0, 0, 0], [0, 0, 0]]
        S = 0
        T = 0
        self.run_test(routes, S, T, 0)

    def test_no_move_2(self):
        '原地不動'
        routes = [[1, 7], [3, 5]]
        S = 5
        T = 5
        self.run_test(routes, S, T, 0)


class TestBrutal(Mixin, TestCase):
    def run_test(self, routes, S, T, expect):
        answer = BrutalSolution().numBusesToDestination(routes, S, T)
        self.assertEqual(answer, expect, routes)

    def test_case2(self):
        '測路徑'
        routes = [[1, 2, 7], [3, 6, 7]]
        S = 1
        T = 6
        pathes = list(brutal_pathes(routes, S, T))
        best_path = min(pathes, key=lambda p: len(p))
        self.assertEqual(best_path, [1, 7, 6])


class TestSolution(Mixin, TestCase):
    def run_test(self, routes, S, T, expect=None):
        answer = BrutalSolution().numBusesToDestination(routes, S, T)
        result = Solution().numBusesToDestination(routes, S, T)
        self.assertEqual(answer, result, routes)

    def test_small_brutal(self):
        size = 3
        for lst in product(range(size), repeat=size * size):
            routes = [
                list(lst[:3]),
                list(lst[3:6]),
                list(lst[6:9]),
            ]
            self.run_test(routes, 0, 2)
