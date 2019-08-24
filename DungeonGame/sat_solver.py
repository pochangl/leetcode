from functools import lru_cache
from itertools import product
from utils import sat
from utils.line import get_points


def all_or_none(*points):
    q = sat.Q(points)
    return (q == 0) + (q == len(2))


@lru_cache(maxsize=1000)
def Point(x, y):
    return '{} {}'.format(x, y)


def str_to_xy(value):
    x, y = value.split(' ')
    return int(x), int(y)


def get_cnf(width, height):
    cnf = []
    # edge case: 上邊, 一定是左邊來的 右 => 左
    y = 0
    for x in range(1, width):
        cnf.append(sat.imply(Point(x, y), Point(x - 1, y)))

    # edge case: 下邊, 只能往右走. 左 => 右
    y = height - 1
    for x in range(1, width):
        cnf.append(sat.imply(Point(x - 1, y), Point(x, y)))

    # edge case: 左邊, 一定是上面來的 下 => 上
    x = 0
    for y in range(1, height):
        cnf.append(sat.imply(Point(x, y), Point(x, y - 1)))

    # edge case: 右邊, 只能往下走. 上 => 下
    x = width - 1
    for y in range(1, height):
        cnf.append(sat.imply(Point(x, y - 1), Point(x, y)))

    for x, y in product(range(1, width), range(1, height)):
        '''
            點 => 左 or 右
            如果這個點
        '''
        up = Point(x - 1, y)
        left = Point(x, y - 1)
        point = Point(x, y)
        cnf.append((sat.neg(point), left, up))

    for offset in range(max(width, height)):
        '每個線上 y = -x + b 只能有一個點'
        cnf += sat.one_of(Point(x, y)
                          for x, y in get_points(width, height, -1, offset))

    return cnf


def all_pathes(width, height):
    cnf = get_cnf(width, height)
    solutions = sat.solve_all(cnf)
    for solution in solutions:
        print(tuple(map(str_to_xy, solution)))
        yield map(str_to_xy, solution)


class SatSolver:
    def calculateMinimumHP(self, dungeon) -> int:
        pathes = all_pathes(len(dungeon), len(dungeon[0]))
        return 1
