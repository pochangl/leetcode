
import numpy as np
from math import factorial
from unittest import TestCase
from .sat_solver import SatSolver, all_pathes


class TestPathes(TestCase):
    def run_test(self, width, height, length):
        pathes = all_pathes(width=width, height=height)
        pathes = tuple(pathes)
        for path in pathes:
            path = list(path)
            self.assertEqual(len(path), width + height - 1, path)
        self.assertEqual(len(pathes), length)

    def test_case1(self):
        self.run_test(1, 1, 1)

    def test_case2(self):
        self.run_test(2, 2, 2)

    def test_case3(self):
        self.run_test(3, 3, 6)
