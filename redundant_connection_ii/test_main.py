from random import randint
from unittest import TestCase
from utils.performance import BigO, F, MemoryScore
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, n=3000):
        edges = []

        for index in range(n - 1):
            num = index + 1
            parent = randint(0, index)
            edges.append((parent, num))

        redundant = [randint(0, n - 1), randint(0, n - 1)]
        position = max(redundant) + 1
        edges[position:position] = [redundant]

        solution = Solution()
        result = solution.findRedundantDirectedConnection(edges=edges)
        self.assertEqual(result, redundant, ('---------', edges, redundant, len(result)))

    def test_run(self):
        self.run_test(n=4)

    def run_case(self, expect, edges):
        solution = Solution()
        result = solution.findRedundantDirectedConnection(edges=edges)
        self.assertEqual(result, expect)

    def test_case1(self):
        '''
            simple case
        '''
        expect = [2, 1]
        edges = [[2, 1], [3, 1], [4, 2], [1, 4]]
        self.run_case(expect, edges)

    def test_case2(self):
        '''
            simple case
            bug: loop on same brach causes errors
        '''
        expect = [2, 1]
        edges = [[2, 1], [5, 3], [3, 1], [4, 2], [1, 4]]
        self.run_case(expect, edges)


    def test_speed(self):
        O = BigO(F.linear, func=self.run_test)
        O.check(2000, times=30)

    def test_memory(self):
        O = BigO(F.linear, func=self.run_test, scorer=MemoryScore)
        O.check(2000, times=2)
