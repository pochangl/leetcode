from unittest import TestCase
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, points, expect):
        result = Solution().isRectangleCover(points)
        self.assertEqual(result, expect, points)

    def test_case1(self):
        data = [
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [3, 2, 4, 4],
            [1, 3, 2, 4],
            [2, 3, 3, 4],
        ]
        self.run_test(data, True)

    def test_case2(self):
        data = [
            [1, 1, 2, 3],
            [1, 3, 2, 4],
            [3, 1, 4, 2],
            [3, 2, 4, 4],
        ]
        self.run_test(data, False)

    def test_case3(self):
        data = [
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [1, 3, 2, 4],
            [3, 2, 4, 4],
        ]

        self.run_test(data, False)

    def test_case4(self):
        data = [
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [1, 3, 2, 4],
            [2, 2, 4, 4],
        ]
        self.run_test(data, False)

    def test_case5(self):
        data = [
            [0, 0, 4, 1],
            [0, 0, 4, 1],
        ]
        self.run_test(data, False)

    def test_case6(self):
        data = [
            [0, 0, 4, 1],
            [7, 0, 8, 2],
            [6, 2, 8, 3],
            [5, 1, 6, 3],
            [4, 0, 5, 1],
            [6, 0, 7, 2],
            [4, 2, 5, 3],
            [2, 1, 4, 3],
            [0, 1, 2, 2],
            [0, 2, 2, 3],
            [4, 1, 5, 2],
            [5, 0, 6, 1],
        ]
        self.run_test(data, True)
