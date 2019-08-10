from unittest import TestCase
import random
from .v4_optimal import Solution, steps


class TestSteps(TestCase):
    def run_test(self, data, expect):
        result = steps(data)
        self.assertEqual(list(result), expect)

    def test_case1(self):
        data = []
        expect = []
        self.run_test(data=data, expect=expect)

    def test_case2(self):
        data = [1]
        expect = []
        self.run_test(data=data, expect=expect)

    def test_case3(self):
        data = [3, 2, 1]
        expect = [2]
        self.run_test(data=data, expect=expect)

    def test_case4(self):
        data = [2, 3, 1, 1, 4]
        expect = [1, 4]
        self.run_test(data=data, expect=expect)

    def test_case5(self):
        data = [1, 2, 3]
        expect = [1, 2]
        self.run_test(data=data, expect=expect)

    def test_case6(self):
        data = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
        expect = [1, 8, 11]
        self.run_test(data=data, expect=expect)


class TestSolution(TestCase):
    def run_test(self, data, expect):
        result = Solution().jump(data)
        self.assertEqual(result, expect)

    def test_case1(self):
        data = []
        expect = 0
        self.run_test(data=data, expect=expect)

    def test_case2(self):
        data = [1]
        expect = 0
        self.run_test(data=data, expect=expect)

    def test_case3(self):
        data = [3, 2, 1]
        expect = 1
        self.run_test(data=data, expect=expect)

    def test_case4(self):
        data = [2, 3, 1, 1, 4]
        expect = 2
        self.run_test(data=data, expect=expect)

    def test_case5(self):
        data = [1, 2, 3]
        expect = 2
        self.run_test(data=data, expect=expect)

    def test_case6(self):
        data = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
        expect = 3
        self.run_test(data=data, expect=expect)

    def test_performance(self):
        size = 500000
        data = list(random.randint(1, 50) for _ in range(size))

        Solution().jump(data)
