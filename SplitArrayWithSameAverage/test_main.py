from unittest import TestCase
from itertools import product
from .brutal import BrutalSolution
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, A):
        A = list(A)
        expect = BrutalSolution().splitArraySameAverage(A)
        answer = Solution().splitArraySameAverage(A)
        self.assertEqual(answer, expect, A)

    def test_case_basic_1(self):
        self.run_test([1, 2, 3, 4, 5, 6, 7, 8])

    def test_case_basic_2(self):
        self.run_test([2, 3, 4, 5, 6, 7, 8])

    def test_length_1(self):
        '長度一的話都不ok'
        solver = Solution().splitArraySameAverage

        for value in range(1, 100):
            self.assertEqual(solver([value]), False)

    def test_zeroes(self):
        '零不管多長都ok'
        solver = Solution().splitArraySameAverage
        for value in range(1, 100):
            self.assertEqual(solver([0] * value), True)

    def test_four(self):
        '雙數長度窮舉'
        for A in product(range(4), repeat=4):
            self.run_test(A)

    def test_five(self):
        '單數長度 array 窮舉'
        for A in product(range(5), repeat=5):
            self.run_test(A)

    def test_performance(self):
        for size in range(1, 30):
            print('size', size, flush=True)
            Solution().splitArraySameAverage(list(range(size)))
