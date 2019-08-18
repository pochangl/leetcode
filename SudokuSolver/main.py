from contextlib import suppress
from copy import deepcopy
from collections import defaultdict
from itertools import product


class Conflict(ValueError):
    pass


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return self.x * 9 + self.y

    def __eq__(self, coordinate):
        return hash(self) == hash(coordinate)

    def __str__(self):
        return '<coor x={} y={}>'.format(self.x, self.y)

    def __repr__(self):
        return str(self)


class Cell:
    def __init__(self, x, y, value):
        self.coordinate = Coordinate(x, y)
        self.observers = set()

        if value == '.':
            self.value = value
            self.availables = set(range(1, 10))
        else:
            self.value = int(value)
            self.availables = set([self.value])

    def __hash__(self):
        return hash(self.coordinate)

    def __eq__(self, cell):
        return hash(self) == hash(cell)

    def subscribe_to(self, cell):
        '''
            self subscribe to cell
        '''
        if self != cell:
            cell.observers.add(self.coordinate)

    def __str__(self):
        return '<x={} y={} val={} avail={}>'.format(self.x, self.y, self.value, self.availables)

    def __repr__(self):
        return str(self)

    @property
    def x(self):
        return self.coordinate.x

    @property
    def y(self):
        return self.coordinate.y

    @property
    def is_filled(self):
        return self.value != '.'


def print_board(board):
    print('-------')
    for row in board:
        print(row)


def solve(cells, board, resolved, almost, num_resolved):
    cells, board, resolved, almost = map(
        deepcopy,
        (cells, board, resolved, almost),
    )

    while resolved:
        num_resolved += 1
        cell = resolved.pop()

        cell.value = cell.availables.pop()

        board[cell.x][cell.y] = str(cell.value)

        for coordinate in tuple(cell.observers):
            observer = cells[coordinate.x][coordinate.y]
            if cell.value not in observer.availables:
                cell.observers.remove(coordinate)
                continue

            observer.availables.remove(cell.value)
            length = len(observer.availables)
            if length == 1:
                resolved.add(observer)
                almost.remove(observer)
            elif length == 2:
                almost.add(observer)
            elif length == 0:
                raise Conflict()

        if not resolved and almost:
            attempt = almost.pop()
            attempt = cells[attempt.x][attempt.y]

            for value in attempt.availables:
                attempt.value = value
                attempt.availables = set([value])
                resolved.add(attempt)
                with suppress(Conflict):
                    return solve(
                        cells=cells,
                        board=board,
                        resolved=resolved,
                        almost=almost,
                        num_resolved=num_resolved
                    )
            raise Conflict()

    return board


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def factory():
            return defaultdict(None)

        cells = defaultdict(factory)

        resolved = set()

        # initial cells
        for x, y in product(range(9), repeat=2):
            cell = cells[x][y] = Cell(x, y, board[x][y])

            if cell.value != '.':
                # 加入resolved
                resolved.add(cell)

        # initial observers
        for x, y in product(range(9), repeat=2):
            cell = cells[x][y]
            if cell.is_filled:
                continue

            for index in range(9):
                # subscribe to x axis cells
                cell.subscribe_to(cells[x][index])
                # subscribe to y axis cells
                cell.subscribe_to(cells[index][y])

            deltas = product(range(3), repeat=2)
            base_x = (x // 3) * 3
            base_y = (y // 3) * 3
            for dx, dy in deltas:
                # subscribe to local block
                cell.subscribe_to(cells[base_x + dx][base_y + dy])

        new_board = solve(cells=cells, board=board, resolved=resolved, num_resolved=0, almost=set())

        for index in range(9):
            board[index] = new_board[index]

        '''
        print_board(board)
        counts = []
        for x in range(9):
            counts.append([None] * 9)
            for y in range(9):
                counts[x][y] = len(cells[x][y].availables)
        print()
        for row in counts:
            print(row)
        '''
