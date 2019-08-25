from unittest import TestCase
from itertools import product
from .brutal import BrutalSolution
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, A):
        expect = BrutalSolution().splitArraySameAverage(A)
        answer = Solution().splitArraySameAverage(A)
        self.assertEqual(answer, expect)

    def test_case_basic_1(self):
        self.run_test([1, 2, 3, 4, 5, 6, 7, 8])

    def test_case_basic_2(self):
        self.run_test([2, 3, 4, 5, 6, 7, 8])

    def test_four(self):
        for A in product(range(4), repeat=4):
            self.run_test(A)
