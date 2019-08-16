from collections import defaultdict


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
        for x in range(9):
            for y in range(9):
                cells[x][y] = Cell(x, y, board[x][y])

        # initial observers
        for x in range(9):
            for y in range(9):
                pass  # 還不知道要寫什麼

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
