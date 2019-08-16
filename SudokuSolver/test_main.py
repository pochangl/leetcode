import copy
from unittest import TestCase
from .main import Solution


class TestSolution(TestCase):
    def run_test(self, data, expect):
        data = copy.deepcopy(data)
        Solution().solveSudoku(data)

        self.assertEqual(data, expect)

    def test_case(self):
        '''
            test case from problem
        '''
        data = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ]
        expect = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
        ]

        self.run_test(data, expect)

    def test_case_hardest(self):
        data = [
            ['8', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '3', '6', '.', '.', '.', '.', '.'],
            ['.', '7', '.', '.', '9', '.', '2', '.', '.'],
            ['.', '5', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '.', '4', '5', '2', '.', '.'],
            ['.', '.', '.', '1', '.', '.', '.', '3', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '6', '8'],
            ['.', '.', '8', '5', '.', '.', '.', '1', '.'],
            ['.', '9', '.', '.', '.', '.', '4', '.', '.'],
        ]

        Solution().solveSudoku(data)
        for row in data:
            for column in row:
                self.assertNotEqual(column, '.')
