from unittest import TestCase
from ..binary import BinaryTree as BT


class TestBinaryTree(TestCase):
    def test_from_list1(self):
        tree = BT.from_list([1])
        tree2 = BT(1)

        self.assertEqual(tree, tree2)

    def test_from_list2(self):
        '''
            see if this reconstructs
        '''
        array = [1, 2, None, 3, 4, None, None, 5, 6, 7]
        tree = BT.from_list(array)
        one = BT(1)
        two = BT(2)
        three = BT(3)
        four = BT(4)
        five = BT(5)
        six = BT(6)
        seven = BT(7)
        one.left = two
        two.left = three
        two.right = four
        four.left = five
        four.right = six
        five.left = seven

        self.assertEqual(tree, one)
        self.assertEqual(array, list(tree.to_list()))
        self.assertEqual(array, list(one.to_list()))

    def test_from_size(self):
        '''
            see if no missing node and no circular reference
        '''
        for _ in range(100):
            tree = BT.from_size(5)
            self.assertEqual(len(tree), 5, tuple(tree.to_list()))

        size = 80
        tree = BT.from_size(size)
        self.assertEqual(len(tree), size)
