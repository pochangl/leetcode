from unittest import TestCase
from .. import BinaryTree as BT


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

    def test_from_list3(self):
        array = [0, 0, 0, None, None, 0, 0, None, None, 0]
        tree = BT.from_list(array)
        one = BT(0)
        two = BT(0)
        three = BT(0)
        four = BT(0)
        five = BT(0)
        six = BT(0)

        one.left = two
        one.right = three
        three.left = four
        three.right = five
        five.left = six
        self.assertEqual(tree, one)
        self.assertEqual(array, list(tree.to_list()))
        self.assertEqual(array, list(one.to_list()))

    def test_from_list4(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        tree = BT.from_list(array)
        one = BT(1)
        two = BT(2)
        three = BT(3)
        four = BT(4)
        five = BT(5)
        six = BT(6)
        seven = BT(7)

        one.left = two
        one.right = three
        two.left = four
        two.right = five
        three.left = six
        three.right = seven
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

    def test_clone(self):
        def verify(root1, root2):
            if root1 is None:
                self.assertIsNone(root2)
            self.assertIsNot(root1, root2)
            self.assertEqual(root1.val, root2.val)
        tree = BT.from_size(10)
        copied = tree.clone()
        self.assertEqual(tree, copied)
        verify(tree, copied)

    def test_depth(self):
        tree = BT.from_list([0])
        self.assertEqual(tree.depth, 1)

        tree = BT.from_list([0, None, None])
        self.assertEqual(tree.depth, 1)

        tree = BT.from_list([0, 0])
        self.assertEqual(tree.depth, 2)

        tree = BT.from_list([0, None, 0])
        self.assertEqual(tree.depth, 2)

        tree = BT.from_list([0] * 7)
        self.assertEqual(tree.depth, 3)
