from contextlib import contextmanager


@contextmanager
def stack(container, element):
    '''
        把東西丟到 container 然後記得恢復
    '''
    container.append(element)
    yield
    container.pop()


@contextmanager
def unoccupy(container, element):
    '''
        把東西從 container 拿走, 然後記得恢復
    '''
    container.remove(element)
    yield
    container.add(element)


@contextmanager
def occupy(container, element):
    container.add(element)
    yield
    container.remove(element)
