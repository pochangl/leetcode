from itertools import combinations


class BrutalSolution:
    def splitArraySameAverage(self, A):
        if len(A) <= 1:
            return False

        total = sum(A)

        length = len(A)

        for size in range(length // 2):
            size = size + 1
            for values in combinations(A, size):
                subtotal = sum(values)
                if subtotal * length == total * size:
                    return True
        return False
