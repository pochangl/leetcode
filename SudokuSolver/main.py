from collections import defaultdict
from itertools import product


class Cell:
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        self.observers = set()
        if value == '.':
            self.availables = set(range(9))
        else:
            self.availables = set([value])

    def __hash__(self):
        return self.x * 9 + self.y

    def __eq__(self, cell):
        return hash(self) == hash(cell)

    def subscribe_to(self, cell):
        '''
            self subscribe to cell
        '''
        if self != cell:
            cell.observers.add(self)


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
            for index in range(9):
                # subscribe to x axis cells
                cell.subscribe_to(cells[x][index])
                # subscribe to y axis cells
                cell.subscribe_to(cells[index][y])

            deltas = product(range(3), repeat=2)
            base_x = x % 3
            base_y = y % 3

            for dx, dy in deltas:
                # subscribe to local block
                cell.subscribe_to(cells[base_x + dx][base_y + dy])

        while resolved:
            cell = resolved.pop()
            board[cell.x][cell.y] = str(cell.value)

            for observer in cell.observers:
                if cell.value in observer.availables:
                    observer.availables.remove(cell.value)
                    if len(observer.availables) == 1:
                        observer.value = observer.availables.pop()
                        resolved.add(observer)

            cell.observers = None
