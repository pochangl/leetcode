from itertools import combinations


class Solution:
    def splitArraySameAverage(self, A):
        # 統計數據
        total = sum(A)
        half = total // 2
        length = len(A)
        # 總合為單數就不行
        if total % 2:
            return False

        # 算出中位數
        A.sort()
        mindex = 0
        subtotal = 0
        while subtotal + A[mindex] < half:
            subtotal += A[mindex]
            mindex += 1

        # 如果剛好就回傳
        if subtotal == half:
            return True

        for size in range(length - 1):
            for indexes in combinations(range(length), length - size):
                subtotal = sum(A[index] for index in indexes)
                if subtotal == half:
                    return True
        return False
