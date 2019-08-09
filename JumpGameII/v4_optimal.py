#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:29:59 2019

@author: pochangl
"""
from functools import wraps
from collections import namedtuple


Node = namedtuple('Node', ['position', 'reach'])


def steps(nums):
    goal = len(nums) - 1
    nodes = tuple(
        Node(
            position=position,
            reach=position + num)
        for position, num in enumerate(nums)
    )

    if len(nums) < 2:
        return
    best = nodes[0]
    last_reach = 0

    while best.reach < goal:
        next_best = max(nodes[last_reach + 1: best.reach + 1],
                        key=lambda n: n.reach)
        yield next_best.position
        last_reach = best.reach
        best = next_best

    yield goal

class Solution(object):
    def jump(self, nums):
        path = list(steps(nums))
        return len(path)
