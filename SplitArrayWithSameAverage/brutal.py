from itertools import combinations


class BrutalSolution:
    def splitArraySameAverage(self, A):
        total = sum(A)

        half = total / 2
        length = len(A)

        for size in range(length):
            for indexes in combinations(range(length), length - size):
                subtotal = sum(A[index] for index in indexes)
                if subtotal == half:
                    return True
        return False
