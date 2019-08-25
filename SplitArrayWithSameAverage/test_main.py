from unittest import TestCase
from itertools import product
from .brutal import BrutalSolution
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, A, expect=None):
        A = list(A)
        answer = BrutalSolution().splitArraySameAverage(A)
        result = Solution().splitArraySameAverage(A)

        self.assertEqual(answer, result, A)

        if expect is not None:
            self.assertEqual(result, expect, A)

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

    def test_fail_1(self):
        '失敗的情境'
        self.run_test([2, 0, 5, 6, 16, 12, 15, 12, 4], True)

    def test_fail_2(self):
        '失敗的情境'
        self.run_test([6, 8, 18, 3, 1], False)

    def test_fail_3(self):
        '失敗的情境'
        self.run_test([4, 3, 3, 1, 1], True)

    def test_four(self):
        '雙數長度窮舉'
        for A in product(range(10), repeat=4):
            self.run_test(A)

    def test_five(self):
        '單數長度 array 窮舉'
        for A in product(range(10), repeat=5):
            self.run_test(A)

    def test_performance(self):
        for size in range(1, 30):
            print('size', size, flush=True)
            Solution().splitArraySameAverage(list(range(size)))
