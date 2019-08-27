from dsa.set import powerset


class Solution:
    def splitArraySameAverage(self, A):
        if len(A) <= 1:
            return False

        length = len(A)
        total = sum(A)
        llength = length // 2
        A = [value * length - total for value in A]

        if 0 in A:
            return True

        left = powerset(A[:llength])
        right = powerset(A[llength:])

        left = set(map(sum, left))
        if 0 in left:
            return True

        right = set(map(lambda v: -sum(v), right))
        if 0 in right:
            return True
        left_sum = sum(A[:llength])

        matched = left & right

        if left_sum in matched:
            matched.remove(left_sum)
        return bool(len(matched))
