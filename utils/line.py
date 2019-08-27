

def get_points(width: int, height: int, a: int, b: int) -> '(x, y)':
    '''
        description:
            回傳所有在 y = ax + b 並在 width x height 座標內的點
        examples:
            >>> # y = 1x + 0
            >>> tuple(line(width=2, height=2, a=1, b=0))
            ((0, 0), (1, 1))

            >>> # y = -1x + 2
            >>> tuple(line(width=2, height=2, a=-1, b=2))
            ((1, 1),)

    '''
    assert abs(a) <= 1
    for x in range(0, width):
        y = a * x + b
        if (0 <= x < width and 0 <= y < height):
            yield (x, y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
