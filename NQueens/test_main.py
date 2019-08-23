from unittest import TestCase
from .sat_solver import SatSolver
from .main import Solution
from utils.matrix import print_matrix


class TestSolution(TestCase):
    def assertSolutionEqual(self, solution1, solution2):
        solution1 = set(tuple(s) for s in solution1)
        solution2 = set(tuple(s) for s in solution2)
        self.assertEqual(len(solution1), len(solution2))
        self.assertEqual(solution1, solution2)

    def run_test(self, data, expect=None):
        solution = Solution().solveNQueens(data)
        sat_solution = SatSolver().solveNQueens(data)
        self.assertSolutionEqual(solution, sat_solution)
        if expect is not None:
            self.assertEqual(solution, expect)

    def test_case(self):
        for i in range(4, 10):
            self.run_test(i)

    def test_case_edge(self):
        self.run_test(1, [['Q']])
        self.run_test(2, [])
        self.run_test(3, [])
