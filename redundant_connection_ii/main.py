from collections import defaultdict, Counter


class Solution:
    def findRedundantDirectedConnection(self, edges):
        graph = dict()
        exclude = None
        include = None

        for parent, child in edges:
            if child in graph:
                exclude = [parent, child]
                include = [graph[child], child]
            else:
                graph[child] = parent

        parents = set(graph.values())
        children = set(graph.keys())

        orphans = parents - children

        if len(orphans) >= 2:
            return exclude
        elif len(orphans) == 1:
            tree = defaultdict(set)
            for child, parent in graph.items():
                tree[parent].add(child)
            start = include[0]
            nodes = set([start])
            while nodes:
                parent = nodes.pop()
                for child in tree[parent]:
                    if child == start:
                        return include
                    nodes.add(child)
            return exclude
        elif exclude:
            return include

        excludes = children - parents
        parent_count = Counter(graph.values())

        while excludes:
            child = excludes.pop()
            parent = graph.pop(child)
            parent_count[parent] -= 1
            if not parent_count[parent]:
                excludes.add(parent)

        for parent, child in reversed(edges):
            if child in graph and graph[child] == parent:
                return [parent, child]
