
import numpy as np
from functools import reduce
from math import factorial
from unittest import TestCase
from .sat_solver import SatSolver, all_pathes


class TestPathes(TestCase):
    def assertPath(self, path, width, height):
        initial = path[0]
        goal = path[-1]

        # check initial position and goal
        self.assertEqual(initial, (0, 0))
        self.assertEqual(goal, (width - 1, height - 1))

        # check length
        self.assertEqual(len(path), width + height - 1, path)

        def reducer(prev, current):
            if prev is None:
                return None
            if abs(prev[0] - current[0]) + abs(prev[1] - current[1]) == 1:
                return current
            return None

        end = reduce(reducer, path[1:], initial)
        self.assertEqual(end, goal)

    def run_test(self, width, height, length):
        pathes = all_pathes(width=width, height=height)
        pathes = tuple(pathes)
        for path in pathes:
            self.assertPath(path=path, width=width, height=height)
        self.assertEqual(len(pathes), length)

    def test_case1(self):
        self.run_test(1, 1, 1)

    def test_case2(self):
        self.run_test(2, 2, 2)

    def test_case3(self):
        self.run_test(3, 3, 6)

    def test_case_range(self):
        '''
            長度等於binomial coefficient
        '''
        for width in range(1, 7):
            n = width - 1
            self.run_test(width, width, factorial(
                n * 2) // factorial(n) ** 2)


class TestSolver(TestCase):
    def run_test(self, board, expect):
        answer = SatSolver().calculateMinimumHP(board)
        self.assertEqual(answer, expect)

    def test_case1(self):
        data = [
            [-2, -3, 3],
            [-5, -10, 1],
            [10, 30, -5],
        ]
        expect = 7
        self.run_test(data, expect)

    def test_case2(self):
        '''
            避免選到需要額外HP的路徑
        '''
        data = [
            [0, -1, 10, 10],
            [0, -1, 10, 10],
            [0, -1, 10, 10],
            [2, -1, 0, 0],
        ]
        expect = 1
        self.run_test(data, expect)

    def test_case3(self):
        '''
            至少要 hp 1
        '''
        data = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        expect = 1
        self.run_test(data, expect)

    def test_case4(self):
        '''
            確認 edge case
        '''
        data = [
            [0]
        ]
        expect = 1
        self.run_test(data, expect)
