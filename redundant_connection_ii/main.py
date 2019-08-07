from collections import defaultdict, Counter


class Solution:
    def findRedundantDirectedConnection(self, edges):
        graph = dict()

        for parent, child in edges:
            if child in graph:
                return [parent, child]
            graph[child] = parent

        leaves = set(graph.keys()) - set(graph.values())
        child_count = Counter(graph.values())

        while leaves:
            leave = leaves.pop()
            parent = graph.pop(leave)
            child_count[parent] -= 1
            if not child_count[parent]:
                leaves.add(parent)

        for parent, child in reversed(edges):
            if child in graph:
                return [parent, child]
        raise Exception('no one should be here, no one')
