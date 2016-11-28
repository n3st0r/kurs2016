
def deko(func):
    def inner():
        print('Before')
        ret_value = func()
        print('after')
        return ret_value

    return inner


@deko
def f2():
    print('Hi!!')

f2()
