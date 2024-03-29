from dsa.tree.binary.traversal import recursion
from collections import namedtuple


Result = namedtuple('Result', ['is_monitored', 'has_camera', 'count'])


def decision(node, left: Result, right: Result):
    if node is None:
        return Result(is_monitored=True, has_camera=False, count=0)

    count = left.count + right.count

    if left.is_monitored and right.is_monitored:
        return Result(
            is_monitored=left.has_camera or right.has_camera,
            has_camera=False,
            count=count
        )
    else:
        return Result(is_monitored=True, has_camera=True, count=count + 1)


class Solution:
    def minCameraCover(self, root) -> int:
        count = recursion(decision)
        result = count(root)
        return result.count if result.is_monitored else result.count + 1
