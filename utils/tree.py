from . import sat
from dsa.tree.binary import BinaryTree
from contextlib import suppress
from collections import deque

__all__ = ['BrutalTree']


def left_child(index):
    return (index * 2) + 1


def right_child(index):
    return (index * 2) + 2


def to_binary_tree(list_tree):
    if not list_tree:
        return []
    tree = []
    queue = deque([0])

    with suppress(IndexError):
        while queue:
            index = queue.popleft()
            if list_tree[index]:
                left = left_child(index)
                right = right_child(index)
                queue.append(left)
                queue.append(right)
                tree.append(True)
            else:
                tree.append(None)

    return tree


def boolean_factory(value, **kwargs):
    if value is not None:
        return True


def brutal_trees(max_depth, require_root=True, data_factory=boolean_factory):
    '''
        把所有深度 <= max_depth 的樹都產生出來
    '''
    cnf = []
    num_nodes = (2 ** max_depth) - 1

    if require_root:
        cnf.append('0')

    for node in range(1, num_nodes):
        parent = str((node - 1) // 2)
        node = str(node)

        cnf.append(sat.imply(node, parent))

    for solution in sat.solve_all(cnf):
        solution = tuple(map(int, solution))
        result = [False] * num_nodes
        for index in solution:
            result[index] = True

        binary_tree = to_binary_tree(result)
        for index, value in enumerate(binary_tree):
            binary_tree[index] = data_factory(index=index, value=value)

        yield binary_tree
