from itertools import permutations


class Solution:
    def splitArraySameAverage(self, A):
        # 統計數據
        total = sum(A)
        half = total // 2
        # 總合為單數就不行
        if total % 2 or len(A) == 1:
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

        A.reverse()
        for array in permutations(A, len(A) // 2):
            subtotal = 0
            for value in array:
                subtotal += value
                if subtotal == half:
                    return True

        return False
