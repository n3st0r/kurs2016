
def my_range(start, stop):
    value = start
    while value < stop:
        yield value
        value += 1


if __name__ == '__main__':
    for x in range(1,10):
        print(x)
