from unittest import TestCase
from .brutal import BrutalSolution


class TestSolution(TestCase):
    def run_test(self, A, expect):
        answer = BrutalSolution().splitArraySameAverage(A)
        self.assertEqual(answer, expect)

    def test_case_basic_1(self):
        self.run_test([1, 2, 3, 4, 5, 6, 7, 8], True)

    def test_case_basic_2(self):
        self.run_test([2, 3, 4, 5, 6, 7, 8], False)
