
def deko(func):
    def inner():
        """
Mój dekorator
:return:
"""
        print('Before')
        ret_value = func()
        print('after')
        return ret_value

    return inner


# @deko
def f2():
    """
Moja funkcja
:return:
"""
    print('Hi!!')


print(f2.__doc__)
f2 = deko(f2)
print(f2.__doc__)
