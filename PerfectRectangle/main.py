from contextlib import suppress
from collections import defaultdict
from functools import partial
from math import inf

invalids = set([0, 2]), set([1, 3])


def is_singularity(state):
    '''
        description:
            有角的, 邊跟墳滿的不算
        examples:
            >>> is_singularity(set([0, 3]))
            True
            >>> is_singularity(set([1, 2]))
            True
            >>> is_singularity(set([0, 1, 3]))
            True
            >>> is_singularity(set())
            False
    '''
    if len(state) % 2:
        return True

    return any(map(lambda invalid: state == invalid, invalids))


class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        area = 0
        factory = partial(set, tuple(range(4)))
        states = defaultdict(factory)
        diagonal = [inf, inf, -inf, -inf]
        merge_ops = min, min, max, max

        with suppress(KeyError):
            for rectangle in rectangles:
                # recalculate diagonal
                diagonal = tuple(map(lambda v: v[0](v[1], v[2]), zip(merge_ops, diagonal, rectangle)))

                x_min, y_min, x_max, y_max = rectangle
                sub_area = (x_max - x_min) * (y_max - y_min)

                if sub_area <= 0:
                    continue

                area += sub_area
                points = (x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)

                for index, point in enumerate(points):
                    states[point].remove(index)
            singularities = list(filter(is_singularity, states.values()))

            if len(singularities) != 4:
                return False

            x_min, y_min, x_max, y_max = diagonal
            width = x_max - x_min
            height = y_max - y_min

            ''' area not match'''
            return area == width * height

        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
