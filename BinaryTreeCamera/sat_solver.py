from utils import sat
from utils.tree import left_child_pos, right_child_pos, parent_pos


def get_cnf(root):
    '''
        確定的事實, 樹根
    '''
    cnf = []
    nodes = root.to_full_list()
    num_nodes = len(nodes)

    def valid_index(index):
        return 0 <= index < num_nodes and nodes[index] is not None

    for index in range(num_nodes):
        '''
            上, 中, 下左, 下右 至少要有一顆監視器
        '''
        if nodes[index] is None:
            continue
        neighbors = [
            index,
            parent_pos(index),
            left_child_pos(index),
            right_child_pos(index),
        ]
        neighbors = filter(valid_index, neighbors)
        neighbors = map(str, neighbors)
        cnf.extend(sat.Q(neighbors) >= 1)
    return cnf


def all_pathes(root):
    '''
        description:
            計算所有擺法
    '''
    cnf = get_cnf(root)
    solutions = sat.solve_all(cnf)
    for solution in solutions:
        yield solution


class SatSolution:
    def minCameraCover(self, root) -> int:
        pathes = all_pathes(root)
        return min(map(len, pathes))
