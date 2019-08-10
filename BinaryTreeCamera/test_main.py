import random
from unittest import TestCase
from .main import Solution


class TestSteps(TestCase):
    def run_test(self, data, expect):
        result = Solution().minCameraCover(data)
        self.assertEqual(list(result), expect)

    def test_case1(self):
        data = [0, 0, None, None, 0, 0]
        expect = 1
        self.run_test(data, expect)

    def test_case2(self):
        data = [0, 0, None, 0, None, 0, None, None, 0]
        expect = 2
        self.run_test(data, expect)
