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
    search_pos = 1

    while best.reach < goal:
        next_search = best.reach + 1
        best = max(nodes[search_pos: best.reach + 1],
                   key=lambda n: n.reach)
        yield best.position
        search_pos = next_search

    yield goal


class Solution(object):
    def jump(self, nums):
        path = list(steps(nums))
        return len(path)
