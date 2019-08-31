from functools import lru_cache
from unittest import TestCase
from utils.tree import brutal_trees, to_binary_tree
from dsa.tree.binary import BinaryTree


class TestToBinaryTree(TestCase):
    def run_test(self, data, expect):
        result = to_binary_tree(data)
        self.assertEqual(result, expect)

    def test_case_depth0(self):
        self.run_test([], [])

    def test_case_depth1(self):
        self.run_test([False], [None])
        self.run_test([True], [True])

    def test_case_depth2(self):
        self.run_test([True, True], [True, True])
        self.run_test([True, True, False], [True, True, None])
        self.run_test([True, True, True], [True, True, True])
        self.run_test([True, False, True], [True, None, True])
        self.run_test([True, False, False], [True, None, None])

    def test_case_depth3(self):
        self.run_test([True] * 7, [True] * 7)
        self.run_test([True, False, True, False, False, True, True], [True, None, True, True, True])
        self.run_test([True, True, True, False, False, True, True], [True, True, True, None, None, True, True])


class TestBrutalTree(TestCase):
    @lru_cache()
    def calc_variations(self, depth):
        assert depth >= 1, depth
        if depth == 1:
            return 2
        return (self.calc_variations(depth - 1) ** 2) + 1

    def run_test(self, depth):
        num_variations = self.calc_variations(depth) - 1
        tree_list = list(brutal_trees(depth))
        tree_set = set(map(tuple, tree_list))

        self.assertEqual(len(tree_list), len(tree_set))  # check duplicate
        self.assertEqual(len(tree_list), num_variations)  # check num of data

        for arr in tree_list:
            arr = list(arr)
            tree = BinaryTree.from_list(arr)
            self.assertLessEqual(tree.depth, depth)

    def test_range(self):
        for i in range(1, 5):
            self.run_test(i)

    def test_data_factory(self):
        def df(value, **kwargs):
            if value is None:
                return 1
            else:
                return 2

        possibilities = set([1, 2])

        iterators = brutal_trees(4, data_factory=df)
        tree = next(iterators)
        self.assertTrue(
            all(map(possibilities.__contains__, tree))
        )
