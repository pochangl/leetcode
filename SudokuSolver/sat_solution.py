import pycosat
import operator
from utils import sat
from collections import namedtuple
from itertools import product


def combine(point, value):
    return '{} {}'.format(point, value)


grid = '''\
011 012 013 314 315 316 617 618 619
021 022 023 324 325 326 627 628 629
031 032 033 334 335 336 637 638 639
141 142 143 444 445 446 747 748 749
151 152 153 454 455 456 757 758 759
161 162 163 464 465 466 767 768 769
271 272 273 574 575 576 877 878 879
281 282 283 584 585 586 887 888 889
291 292 293 594 595 596 897 898 899
'''

values = tuple('123456789')

table = [row.split() for row in grid.splitlines()]
points = grid.split()

subsquares = dict()
for point in points:
    subsquares.setdefault(point[0], []).append(point)


groups = table[:] + list(zip(*table)) + list(subsquares.values())

cnf = []

for point in points:
    cnf += sat.one_of(combine(point, value) for value in values)

for group in groups:
    for value in values:
        cnf += sat.one_of(combine(point, value) for point in group)


def facts(game):
    for row, col in product(range(9), repeat=2):
        if game[row][col].isdigit():
            yield [combine(table[row][col], int(game[row][col]))]


def decode(points):
    for point in points:
        yield int(point[1]) - 1, int(point[2]) - 1, point[4]


class Solution:
    def solveSudoku(self, board):
        local_cnf = cnf.copy()
        local_cnf += list(facts(board))
        solution = sat.solve_one(local_cnf)

        for x, y, value in decode(solution):
            # print(x, y, value)
            board[x][y] = str(value)


'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()
'''
