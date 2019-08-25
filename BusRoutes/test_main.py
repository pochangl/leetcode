from unittest import TestCase
from .brutal import BrutalSolution, brutal_pathes
# from .main import Solution


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
