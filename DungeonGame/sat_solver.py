from functools import lru_cache, reduce
from itertools import product
from utils import sat
from utils.line import get_points


@lru_cache(maxsize=1000)
def Point(x, y):
    '''
        descriptions:
            把 x, y 轉成 SAT 用的字串
        example:
            >>> Point(1, 2)
            '1 2'
    '''
    return '{} {}'.format(x, y)


def str_to_xy(value):
    '''
        descriptions:
            把字串轉成 (x, y)
        example:
            >>> str_to_xy('1 2')
            (1, 2)
    '''
    x, y = value.split(' ')
    return int(x), int(y)


def get_cnf(width, height):
    cnf = []

    max_y = height - 1
    max_x = width - 1

    cnf += sat.basic_fact(Point(0, 0))
    cnf += sat.basic_fact(Point(max_x, max_y))

    # edge case: 下邊, 只能往右走. 左 => 右
    for x in range(width - 1):
        cnf.append(sat.imply(Point(x, max_y), Point(x + 1, max_y)))

    # edge case: 右邊, 只能往下走. 上 => 下
    for y in range(height - 1):
        cnf.append(sat.imply(Point(max_x, y), Point(max_x, y + 1)))

    for x, y in product(range(width - 1), range(height - 1)):
        '''
            點 => 右 or 下
            一下是往右或往下走
        '''
        right = Point(x + 1, y)
        down = Point(x, y + 1)
        point = Point(x, y)
        cnf.append((sat.neg(point), right, down))
        cnf.extend(sat.Q([right, down]) < 2)

    return cnf


@lru_cache()
def all_pathes(width, height):
    '''
        description:
            計算所有的路徑
        example:
            >>> tuple(all_pathes(2, 2))
            ([(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)])
    '''
    cnf = get_cnf(width, height)
    solutions = sat.solve_all(cnf)
    pathes = []
    for solution in solutions:
        path = list(map(str_to_xy, solution))
        path.sort(key=lambda x: x[0] * height + x[1])
        pathes.append(path)
    return pathes


def required_health(dungeon, path):
    '''
        description:
            計算一個路徑需要的最小 HP 值
        example:
            >>> required_health([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])
            7

            >>> required_health([[-1, -2], [-3, -4]], [(0, 0), (0, 1), (1, 1)])
            8

            >>> required_health([[-1]], [(0, 0)])
            2
    '''
    minimum = 0
    health = 0
    for x, y in path:
        health += dungeon[x][y]
        minimum = min((health, minimum))

    return 1 - minimum


class SatSolver:
    def calculateMinimumHP(self, dungeon) -> int:
        pathes = all_pathes(len(dungeon), len(dungeon[0]))
        return min(required_health(dungeon, path) for path in pathes)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
