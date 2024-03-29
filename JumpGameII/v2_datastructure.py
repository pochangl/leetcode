#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:29:59 2019

@author: pochangl
"""


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


class Solution(object):
    def jump(self, nums):
        length = len(nums)

        if length < 2:
            return 0

        nodes = tuple(
            Node(position=index, steps=num)
            for index, num
            in enumerate(nums)
        )

        base = nodes[0]
        last = nodes[-1]
        best = base
        nxt = nodes[1]
        step = 0

        while True:
            step += 1
            if best.reach >= last.position:
                break;
            for target in nodes[nxt.position: best.reach + 1]:
                if best < target:
                    best = target
            nxt = nodes[target.position + 1]
            base = best
        return step


print(Solution().jump([2,3,1,1,10]))
print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([1, 2, 3]))
print(Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]))
print(Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]))
