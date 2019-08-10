from collections import deque


class Data:
    def __init__(self, node, rtn_func):
        self.node = node
        self.step = 0
        self.left = None
        self.right = None
        self.rtn_func = rtn_func

    def set_left(self, value):
        self.left = value

    def set_right(self, value):
        self.right = value

    def __repr__(self):
        return '%s' % self.node


def _binary_recursion(root, rtn_func):
    stack = deque()
    stack.append(Data(root, lambda x: None))
    rtn = None

    while len(stack):
        current = stack.pop()
        node = current.node
        if node is None:
            rtn = rtn_func(node=node, left=current.left, right=current.right)
            current.rtn_func(rtn)
        elif current.step is 0:
            stack.append(current)
            stack.append(Data(node.left, current.set_left))
        elif current.step is 1:
            stack.append(current)
            stack.append(Data(node.right, current.set_right))
        current.step += 1
    return rtn


def recursion(func):
    def wrapper(*args, root):
        return _binary_recursion(root=root, rtn_func=func)

    return wrapper
