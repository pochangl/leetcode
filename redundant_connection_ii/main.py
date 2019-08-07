from collections import defaultdict, OrderedDict


class Link:
    def __init__(self, index, parent, child):
        self.index = index
        self.parent = parent
        self.child = child

    def __hash__(self):
        return self.index

    def __eq__(self, node):
        return hash(self) == hash(node)

    def __repr__(self):
        return '{} -> {}'.format(self.parent, self.child)


class Node:
    def __init__(self):
        self.plinks = set()
        self.clinks = set()

    def can_remove(self):
        return len(self.clinks) + len(self.plinks) == 1

    def __repr__(self):
        return 'Node(parent={} child={})'.format(self.plinks, self.clinks)

    @property
    def links(self):
        return self.plinks or self.clinks


class Solution:
    def drop_link(self, link: Link):
        parent = self.nodes[link.parent]
        parent.clinks.remove(link)
        child = self.nodes[link.child]
        child.plinks.remove(link)
        self.links.pop(link, False)

    def mark_link(self, link: Link):
        self.graph[link.parent].add(link.child)
        self.drop_link(link)

    def clean_node(self, node: Node):
        if node.can_remove():
            if node.links:
                link = next(iter(node.links))
                self.mark_link(link)
                parent = self.nodes[link.parent]
                self.clean_node(parent)
                child = self.nodes[link.child]
                self.clean_node(child)

    def findRedundantDirectedConnection(self, edges):
        self.links = links = OrderedDict()
        self.nodes = nodes = defaultdict(Node)
        graph = self.graph = defaultdict(set)

        for index, (parent, child) in enumerate(edges):
            link = links[index] = Link(index, parent, child)
            nodes[parent].clinks.add(link)
            nodes[child].plinks.add(link)

        for node in nodes.values():
            self.clean_node(node)

        while links:
            key = next(reversed(links))
            link = links[key]
            self.drop_link(link)
            parent = nodes[link.parent]
            self.clean_node(parent)
            child = nodes[link.child]
            self.clean_node(child)

        result = []
        for parent, child in edges:
            if parent in graph and child in graph[parent]:
                self.graph[parent].remove(child)
            else:
                result.append((parent, child))
        return result
