from collections import defaultdict
from itertools import permutations


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
        axis = permutations(range(9), 2)

        # initial cells
        for x, y in axis:
            cells[x][y] = Cell(x, y, board[x][y])

        # initial observers
        for x, y in axis:
            cell = cells[x][y]
            for index in range(9):
                # subscribe to x axis cells
                cell.subscribe_to(cells[x][index])
                # subscribe to y axis cells
                cell.subscribe_to(cells[index][y])

            deltas = permutations(range(3), 2)
            base_x = x % 3
            base_y = y % 3

            for dx, dy in deltas:
                # subscribe to local block
                cell.subscribe_to(cells[base_x + dx][base_y + dy])

        # initial candidates
        for row in cells:
            for cell in row:
                resolved.add(cell)

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
