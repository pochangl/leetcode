from unittest import TestCase
from .sat_solver import SatSolver


class TestSolution(TestCase):
    def run_test(self, data, expect):
        solution = SatSolver().solveNQueens(data)
        self.assertEqual(solution, expect)

    def test_case(self):
        for i in range(4, 10):
            self.run_test(i, 0)

    def test_case_edge(self):
        self.run_test(1, [['Q']])
        self.run_test(2, [])
        self.run_test(3, [])
