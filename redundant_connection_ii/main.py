from collections import defaultdict, Counter


class Solution:
    def findRedundantDirectedConnection(self, edges):
        graph = dict()
        exclude = None

        for parent, child in edges:
            if child in graph:
                exclude = [parent, child]
            else:
                graph[child] = parent

        parents = set(graph.values())
        children = set(graph.keys())

        orphans = parents - children
        if exclude and not exclude[0] in parents:
            child = exclude[1]
            return [graph[child], child]

        if len(orphans) == 2:
            child = exclude[1]
            return [graph[child], child]
        elif len(orphans):
            return exclude

        excludes = children - parents
        child_count = Counter(graph.values())

        while excludes:
            child = excludes.pop()
            parent = graph.pop(child)
            child_count[parent] -= 1
            if not child_count[parent]:
                excludes.add(parent)

        for parent, child in reversed(edges):
            if child in graph:
                return [parent, child]
        raise Exception('no one should be here, no one')
