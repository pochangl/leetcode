from unittest import TestCase
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, floors, eggs, expect):
        result = Solution().superEggDrop(K=eggs, N=floors)
        self.assertEqual(result, expect)

    def test_problem_case1(self):
        self.run_test(eggs=1, floors=2, expect=2)

    def test_problem_case2(self):
        self.run_test(eggs=2, floors=6, expect=3)

    def test_problem_case3(self):
        self.run_test(eggs=3, floors=14, expect=4)

    def test_1_egg(self):
        for floors in range(100):
            self.run_test(eggs=1, floors=floors, expect=floors)

    def test_1_floor(self):
        for eggs in range(1, 10):
            self.run_test(eggs=eggs, floors=1, expect=1)

    def test_2_floors(self):
        for eggs in range(1, 10):
            self.run_test(eggs=eggs, floors=2, expect=2)

    def test_3_floors(self):
        self.run_test(eggs=2, floors=4, expect=3)

        for eggs in range(3, 10):
            self.run_test(eggs=eggs, floors=4, expect=3)
