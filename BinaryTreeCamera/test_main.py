import random
from unittest import TestCase
from .main import Solution
from .sat_solver import SatSolution
from dsa.tree.binary import BinaryTree
from utils.tree import brutal_trees


node = BinaryTree(0)
leave = node.clone()

camera = node.clone()
camera.right = BinaryTree(0)

monitored = camera.clone()
monitored.right.right = BinaryTree(0)

empty = node.clone()


class TestRoot(TestCase):
    def run_test(self, root, left, expect):
        root.left = left
        result = Solution().minCameraCover(root)
        self.assertEqual(expect, result, list(root.to_list()))

    def test_normal_root(self):
        root = node.clone()

        self.run_test(root, None, 1)
        self.run_test(root, leave, 1)
        self.run_test(root, camera, 1)

    def test_monitored_root(self):
        root = monitored.clone()

        self.run_test(root, None, 1)
        self.run_test(root, leave, 2)
        self.run_test(root, camera, 2)

    def test_camera_root(self):
        root = camera.clone()

        self.run_test(root, None, 1)
        self.run_test(root, leave, 1)
        self.run_test(root, camera, 2)


class TestBranch(TestCase):
    def run_test(self, root, left, expect):
        center = root.left.left
        center.left = left
        result = Solution().minCameraCover(root)
        self.assertEqual(expect, result, list(root.to_list()))

    def test_normal_parent(self):
        root = monitored.clone()
        root.left = node.clone()
        root.left.left = node.clone()

        # normal center
        tree = root.clone()

        self.run_test(tree, None, 2)
        self.run_test(tree, leave, 2)
        self.run_test(tree, monitored, 3)
        self.run_test(tree, camera, 3)

        # monitored center
        tree = root.clone()
        tree.left.left = monitored.clone()

        self.run_test(tree, None, 3)
        self.run_test(tree, leave, 3)
        self.run_test(tree, monitored, 4)
        self.run_test(tree, camera, 4)

        # camera center
        tree = root.clone()
        tree.left.left = camera.clone()

        self.run_test(tree, None, 2)
        self.run_test(tree, leave, 2)
        self.run_test(tree, monitored, 3)
        self.run_test(tree, camera, 3)

    def test_monitored_parent(self):
        root = monitored.clone()
        root.left = monitored.clone()
        root.left.left = node.clone()
        # None right
        tree = root.clone()
        root.left.left.right = None

        # normal center
        tree = root.clone()

        self.run_test(tree, None, 3)
        self.run_test(tree, leave, 3)
        self.run_test(tree, monitored, 4)
        self.run_test(tree, camera, 3)

        # monitored center
        tree = root.clone()
        tree.left.left = monitored.clone()

        self.run_test(tree, None, 3)
        self.run_test(tree, leave, 4)
        self.run_test(tree, monitored, 4)
        self.run_test(tree, camera, 4)

        # camera center
        tree = root.clone()
        tree.left.left = camera.clone()

        self.run_test(tree, None, 3)
        self.run_test(tree, leave, 3)
        self.run_test(tree, monitored, 4)
        self.run_test(tree, camera, 4)

    def test_camera_parent(self):
        root = monitored.clone()
        root.left = camera.clone()
        root.left.left = node.clone()

        # normal center
        tree = root.clone()

        self.run_test(tree, None, 2)
        self.run_test(tree, leave, 3)
        self.run_test(tree, monitored, 3)
        self.run_test(tree, camera, 3)

        # monitored center
        tree = root.clone()
        tree.left.left = monitored.clone()

        self.run_test(tree, None, 3)
        self.run_test(tree, leave, 4)
        self.run_test(tree, monitored, 4)
        self.run_test(tree, camera, 4)

        # camera center
        tree = root.clone()
        tree.left.left = camera.clone()

        self.run_test(tree, None, 3)
        self.run_test(tree, leave, 3)
        self.run_test(tree, monitored, 4)
        self.run_test(tree, camera, 4)


class TestSolution(TestCase):
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
        levels =  [1, 2, 3, 4, 5, 6]
        expects = [1, 1, 2, 5, 9, 18]
        for level, expect in zip(levels, expects):
            data = [0] * (2**level - 1)
            self.run_test(data, expect)


class TestAgainstSAT(TestCase):
    def test_depth_3(self):
        trees = brutal_trees(4)
        for arr in trees:
            tree = BinaryTree.from_list(arr)
            result = Solution().minCameraCover(tree)
            sat = SatSolution().minCameraCover(tree)
            self.assertEqual(sat, result)
