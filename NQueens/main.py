from collections import namedtuple

Queen = namedtuple('Queen', ('x', 'y'))


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

    for x, y in solution:
        board[x] = ('.' * y) + 'Q' + ('.' * (n - y - 1))
    return board


def compatible(q1, q2):
    return q1.x != q2.x and q1.y != q2.y and abs(q1.x - q2.x) != abs(q1.y - q2.y)


def solve(n, queens, availables):
    x = len(queens)
    for y in tuple(availables):
        queen = Queen(x, y)
        if all(compatible(queen, q) for q in queens):
            queens.add(queen)

            if len(queens) == n:
                yield render(queens)
                queens.remove(queen)
                return
            else:
                availables.remove(y)
                yield from solve(n, queens, availables)
                availables.add(y)
                queens.remove(queen)


def solve_all(n):
    for i in range(n):
        availables = set(range(n))
        availables.remove(i)
        yield from solve(n, set([Queen(0, i)]), availables)


class Solution:
    def solveNQueens(self, n):
        if n == 1:
            return [['Q']]
        elif n >= 4:
            return list(solve_all(n))
        else:
            return []


if __name__ == "__main__":
    import doctest
    doctest.testmod()
