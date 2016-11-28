
if __name__ == '__main__':
    with open('test1.txt', 'r') as f:
        linie = []
        for linia in f:
            if linia.startswith('#'):
                continue
            print(linia, end='')
