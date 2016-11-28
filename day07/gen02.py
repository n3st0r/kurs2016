
def gen1():
    yield 1
    yield 2
    yield 3

if __name__ == '__main__':
    g = gen1()
    print(g)
    print('Przed')
    for x in gen1():
        print(x)
    print('Po')
