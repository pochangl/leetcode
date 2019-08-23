from contextlib import contextmanager


@contextmanager
def stack(container, element):
    '''
        把東西丟到 container 然後記得恢復
    '''
    container.add(element)
    yield
    container.remove(element)


@contextmanager
def unstack(container, element):
    '''
        把東西從 container 拿走, 然後記得恢復
    '''
    container.remove(element)
    yield
    container.add(element)
