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
        data = [0, 0, None, 0, 0]
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

    def test_case4(self):
        data = [0, None, 0, None]
        expect = 1
        self.run_test(data, expect)

    def test_straight_lines(self):
        '''
            測直線結構
        '''
        base = [0, None]
        lengthes = [1, 2, 3, 4, 5, 6, 7]
        expects =  [1, 1, 1, 2, 2, 2, 3]

        for length, expect in zip(lengthes, expects):
            data = base * length
            self.run_test(data, expect)

    def test_root(self):
        datum = [
            [0],           # 單一root
            [0, 0],        # root.left
            [0, None, 0],  # root.right
            [0, 0, 0],     # root.left and root.right
        ]
        for data in datum:
            # 希望data沒被搞壞
            self.assertIsInstance(data, list)
            self.assertEqual(data[0], 0)

            self.run_test(data, 1)

    def test_full(self):
        levels =  [1, 2, 3, 4, 5]
        expects = [1, 1, 3, 5, 10]
        for level, expect in zip(levels, expects):
            data = [0] * (2**level - 1)
            self.run_test(data, expect)
