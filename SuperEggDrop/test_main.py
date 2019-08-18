from unittest import TestCase
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, **kwargs):
        expect = kwargs.pop('expect')
        result = Solution().superEggDrop(**kwargs)
        self.assertEqual(result, expect)

    def test_case1(self):
        self.run_test(K=1, N=2, expect=2)

    def test_case2(self):
        self.run_test(K=2, N=6, expect=3)

    def test_case3(self):
        self.run_test(K=3, N=14, expect=4)
