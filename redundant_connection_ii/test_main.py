from random import randint
from unittest import TestCase
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, n=3000, precent_redundancy=20):
        redundants = []
        edges = []

        for index in range(n - 1):
            num = index + 1
            parent = randint(0, index)
            edges.append((parent, num))

            if randint(1, 100) > precent_redundancy:
                node = randint(0, num), randint(0, num)
                redundants.append(node)
                edges.append(node)
        solution = Solution()
        result = solution.findRedundantDirectedConnection(edges=edges)
        self.assertListEqual(result, redundants, ('---------', edges, len(redundants), len(result)))

    def test_run(self):
        self.run_test(n=30000)

    def run_case(self, expect, edges):
        solution = Solution()
        result = solution.findRedundantDirectedConnection(edges=edges)
        self.assertListEqual(result, expect,)

    def test_case1(self):
        '''
            simple case
        '''
        expect = [(0, 0), (1, 1)]
        edges = [(0, 1), (0, 0), (1, 2), (1, 1)]
        self.run_case(expect, edges)

    def test_case2(self):
        '''
            construct result
            bug: wrong index when building
        '''
        expect = [(1, 1), (3, 0)]
        edges = [(0, 1), (1, 1), (1, 2), (1, 3), (3, 0)]
        self.run_case(expect, edges)

    def test_case3(self):
        '''
            inside Solution.clean_node
            should clean node only if one node.links present
        '''
        expect = [(1, 0), (3, 2)]
        edges = [(0, 1), (0, 2), (1, 0), (0, 3), (3, 2)]
        self.run_case(expect, edges)

    def test_case4(self):
        '''
            rename is_leave to can_remove
            bug1: can_remove logic was wrong
            bug2: forgot to clean child as well
        '''
        expect = [(2, 2), (3, 2), (0, 0), (2, 5)]
        edges = [(0, 1), (0, 2), (2, 2), (1, 3), (3, 2), (3, 4), (0, 0), (0, 5), (2, 5)]
        self.run_case(expect, edges)
