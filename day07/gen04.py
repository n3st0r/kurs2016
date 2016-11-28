def gen1():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    l = [1, 2, 3]
    iterator = iter(l)
    while True:
        try:
            v = next(iterator)
            print(v)
        except StopIteration:
            break
