#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:29:59 2019

@author: pochangl
"""
from functools import wraps
from math import inf


class Node:
    def __init__(self, position, steps, goal):
        self.position = position
        self.steps = steps

        if position == goal:
            self.reach = inf
        else:
            self.reach = position + steps

    def __repr__(self):
        return 'Node(position: %s, reach: %s, steps: %s)' % (
                self.position, self.reach, self.steps)


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


@generator_suppress(IndexError, TypeError)
def steps(nums):
    goal = len(nums) -1
    nodes = tuple(
        Node(
            position=position,
            steps=num,
            goal=goal)
        for position, num in enumerate(nums)
    )

    # IndexError 會發生的地方, 當length == 0 時會發生
    best = nodes[0]

    for _ in nums:
        # TypeError 會發生的地方
        best = max(nodes[best.position + 1: best.reach + 1],
                   key=lambda n: n.reach)
        yield best.position


class Solution(object):
    def jump(self, nums):
        path = list(steps(nums))
        return len(path)


assert Solution().jump([]) == 0
assert Solution().jump([1]) == 0
assert Solution().jump([3, 2, 1]) == 1
assert Solution().jump([2, 3, 1, 1, 4]) == 2
assert Solution().jump([1, 2, 3]) == 2
assert Solution().jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]) == 3
print('All pass')