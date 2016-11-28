
def gen1():
    return [1, 2, 3]

if __name__ == '__main__':
    g = gen1()
    print(g)
    print('Przed')
    for x in gen1():
        print(x)
    print('Po')
