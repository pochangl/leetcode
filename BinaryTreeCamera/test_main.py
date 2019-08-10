import random
from unittest import TestCase
from .main import Solution
from dsa.tree.binary import BinaryTree


class TestSteps(TestCase):
    def run_test(self, data, expect):
        tree = BinaryTree.from_list(data)
        result = Solution().minCameraCover(tree)
        self.assertEqual(result, expect, 'data: {}'.format(data))

    def test_case1(self):
        '''
            題目的case
        '''
        data = [0, 0, None, None, 0, 0]
        expect = 1
        self.run_test(data, expect)

    def test_case2(self):
        '''
            題目的case
        '''
        data = [0, 0, None, 0, None, 0, None, None, 0]
        expect = 2
        self.run_test(data, expect)

    def test_case3(self):
        '''
            測基本型
        '''
        data = [0]
        expect = 1
        self.run_test(data, expect)

    def test_straight_line(self):
        '''
            測直線結構
        '''
        base = [0, None]
        lengthes = [1, 2, 3, 4, 5, 6, 7]
        expects =  [1, 2, 1, 2, 2, 2, 3]

        for length, expect in zip(lengthes, expects):
            data = base * length
            self.run_test(data, expect)
