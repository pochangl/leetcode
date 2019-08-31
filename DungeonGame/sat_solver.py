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

    cnf += sat.basic_fact(Point(0, 0))
    cnf += sat.basic_fact(Point(width - 1, height - 1))

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
            點 => 左 or 上
            如果這個點
        '''
        left = Point(x - 1, y)
        up = Point(x, y - 1)
        point = Point(x, y)
        cnf.append((sat.neg(point), left, up))

    for offset in range(width + height - 1):
        '每個線上 y = -x + b 只能有一個點'
        cnf += sat.one_of(Point(x, y)
                          for x, y in get_points(width, height, -1, offset))

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
