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


def steps(nums):
    goal = len(nums) - 1
    nodes = tuple(
        Node(
            position=position,
            steps=num,
            goal=goal)
        for position, num in enumerate(nums)
    )

    if not nums:
        return
    best = nodes[0]

    while best.reach != inf:
        best = max(nodes[best.position + 1: best.reach + 1],
                   key=lambda n: n.reach)
        yield best.position


class Solution(object):
    def jump(self, nums):
        path = list(steps(nums))
        return len(path)
