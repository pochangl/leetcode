from unittest import TestCase
from .. import BinaryTree as BT
from ..traversal import recursion


def concat(node, left, right):
    if node is None:
        return []
    return left + right + [node.val]


class TestRecursion(TestCase):
    def test_post_order(self):
        tree = BT.from_list([1, 2, 3, 4, 5, 6, 7])
        score = recursion(concat)
        result = score(root=tree)

        self.assertEqual(result, [4, 5, 2, 6, 7, 3, 1])

    def test_post_order2(self):
        tree = BT.from_list([1, 2, 3])
        score = recursion(concat)
        result = score(root=tree)

        self.assertEqual(result, [2, 3, 1])
