#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:29:59 2019

@author: pochangl
"""
from functools import wraps


class Node:
    # __slot__ might not be pythonic but fast
    __slot__ = ('position', 'reach', 'steps', '__gt__')

    def __init__(self, position, steps):
        self.position = position
        self.steps = steps
        self.reach = position + steps

    def __gt__(self, node):
        return self.reach > node.reach or not node.steps

    def __repr__(self):
        return 'Node(position: %s, reach: %s, steps: %s)' % (self.position, self.reach, self.steps)


def generator_suppress(*exceptions):
    '''
        contextlib.supress 的 generator decorator 版本
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                yield from func(*args, **kwargs)
            except exceptions:
                pass
        return wrapper
    return decorator


@generator_suppress(IndexError)
def steps(nums):
    nodes = tuple(
        Node(position=index, steps=num)
        for index, num
        in enumerate(nums)
    )

    # IndexError 會發生的地方, 當length < 2時會發生
    best = nodes[0]
    nxt = nodes[1]

    for step in range(len(nums)):
        new_best = max(nodes[nxt.position: best.reach + 1])
        yield new_best.position

        # IndexError 會發生的地方, 配合 with suppress 使用
        nxt = nodes[new_best.position + 1]
        best = new_best

    
class Solution(object):
    def jump(self, nums):
        path = list(steps(nums))
        return len(path)


assert Solution().jump([]) == 0
assert Solution().jump([1]) == 0
assert Solution().jump([2,3,1,1,4]) == 2
assert Solution().jump([1, 2, 3]) == 2
assert Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]) == 3
assert Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]) == 3
print('All pass')