import copy
import random
from collections import deque
from contextlib import suppress


class BinaryTree:
    left = None
    right = None

    def __init__(self, value):
        self.val = value

    def __eq__(self, tree):
        if tree is None:
            return False
        return all([
            self.val == tree.val,
            self.left == tree.left,
            self.right == tree.right
        ])

    def __len__(self):
        total = 1
        if self.left:
            total += len(self.left)
        if self.right:
            total += len(self.right)
        return total

    def __repr__(self):
        return '<BinaryTree {}>'.format(', '.join(list(self.to_list())))

    def __str__(self):
        return repr(self)

    def to_list(self):
        queue = deque()
        next_queue = deque()
        next_queue.append(self)
        more = 1

        while more:
            while len(next_queue) and more:
                node = next_queue.popleft()
                if node is None:
                    yield
                else:
                    yield node.val
                    queue.append(node)
                    more -= 1

            while len(queue):
                node = queue.popleft()
                next_queue.append(node.left)
                next_queue.append(node.right)

                more += bool(node.left)
                more += bool(node.right)

    @classmethod
    def from_list(cls, lst):
        queue = deque()
        values = iter(lst)
        root = cls(next(values))
        queue.append(root)

        with suppress(StopIteration):
            for value in values:
                node = queue.popleft()
                if value is not None:
                    left = node.left = cls(value)
                    queue.append(left)
                value = next(values)
                if value is not None:
                    right = node.right = cls(value)
                    queue.append(right)
        return root

    @classmethod
    def from_size(cls, size, *args, bias=0):
        '''
            generate random tree
        '''
        assert size > 0
        assert not args
        leaves = list(None for _ in range(size))
        length = 1

        root = cls(0)
        leaves[0] = root

        for num in range(1, size):
            node = cls(num)
            index = random.randint(0, length - 1)
            parent = leaves[index]
            if parent.left:
                parent.right = node
            elif parent.right:
                parent.left = node
            else:
                right = random.uniform(-100, 100) < bias
                if right:
                    parent.right = node
                else:
                    parent.left = node

            if parent.left and parent.right:
                leaves[index] = node
            else:
                leaves[length] = node
                length += 1
        return root


class Traversal:
    @staticmethod
    def Morris(root):
        '''
            depth first traversal
            credit: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
        '''
        current = root

        while(current is not None):
            if current.left is None:
                yield current
                current = current.right
            else:
                pre = current.left
                while(pre.right is not None and pre.right != current):
                    pre = pre.right

                if(pre.right is None):
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    yield current
                    current = curre
