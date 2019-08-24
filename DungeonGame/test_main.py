from unittest import TestCase
from .main import Solution
from .sat_solver import SatSolver


def all_board(size):
    '''
        description:
            產生 board 所有的組合
            每個格子的 value in {-1, 0, 1}
        example:
            >>> len(all_board(1))
            3

            >>> len(all_board(2))
            81

            >>> len(all_board(3))
            19683
    '''
    board = []
    for s in range(size):
        board.append([None] * size)

    length = size * size
    values = (-1, 0, 1)

    def recursion(index):
        x = index // size
        y = index % size

        for value in values:
            board[x][y] = value
            if index + 1 >= length:
                yield board
            else:
                yield from recursion(index + 1)
            value += 1

    yield from recursion(0)


class TestSolution(TestCase):
    def test_case(self):
        for size in range(1, 4):
            for board in all_board(size):
                result = Solution().calculateMinimumHP(board)
                answer = SatSolver().calculateMinimumHP(board)
                self.assertEqual(result, answer, board)

    def test_performance(self):
        board = next(all_board(11))
        Solution().calculateMinimumHP(board)
