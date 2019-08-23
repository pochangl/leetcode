from utils import sat
from utils.matrix import print_matrix


def at_most_one(elements):
    return sat.Q(elements) <= 1


def line(n: int, a: int, b: int) -> '(x, y)':
    '''
        description:
            回傳所有在 y = ax + b 並在 n x n 格子內的點
        examples:
            >>> # y = 1x + 0
            >>> tuple(line(n=2, a=1, b=0))
            ((0, 0), (1, 1))

            >>> # y = -1x + 2
            >>> tuple(line(n=2, a=-1, b=2))
            ((1, 1),)

    '''
    for x in range(0, 2 * n):
        y = a * x + b
        if (0 <= x < n and 0 <= y < n):
            yield (x, y)


def get_cnf(n: int) -> 'cnf':
    '''
        description:
            把版子上所有的 cnf 都丟出來
        examples:
            >>> get_cnf(2)
            [('~0 0', '~0 1'), ('0 0', '0 1'), ('~0 0', '~1 0'), ('0 0', '1 0'), ('~1 0', '~1 1'), ('1 0', '1 1'), ('~0 1', '~1 1'), ('0 1', '1 1'), ('~0 0', '~1 1'), ('~0 1', '~1 0')]
    '''
    board = []
    for x in range(n):
        board.append(
            tuple(
                '{} {}'.format(x, y) for y in range(n)
            )
        )
    cnf = []
    for index in range(n):
        # x-axis
        cnf += sat.one_of(board[index][y] for y in range(n))

        # y-axis
        cnf += sat.one_of(board[y][index] for y in range(n))

    # y = ax + b
    for b in range(-n + 1, n):
        cnf += at_most_one(board[x][y] for x, y in line(n=n, a=1, b=b))
    for b in range(2 * n - 1):
        cnf += at_most_one(board[x][y] for x, y in line(n=n, a=-1, b=b))

    return cnf


def render(solution):
    '''
        descriptions:
            把皇后的位置轉換成版子
        examples:
            >>> render(['1 0', '0 1'])
            ['.Q', 'Q.']
    '''
    n = len(solution)
    board = [None] * n

    for queen in solution:
        x, y = map(int, queen.split())
        board[x] = ('.' * y) + 'Q' + ('.' * (n - y - 1))
    return board


class SatSolver:
    def solveNQueens(self, n):
        # print('----solving----')
        cnf = get_cnf(n)
        # print(cnf)
        solutions = sat.solve_all(cnf)
        solutions = filter(lambda sol: len(sol) == n, solutions)
        return list(render(solution) for solution in solutions)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
