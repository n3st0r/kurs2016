class Kotek:
    def __init__(self):
        self.wiek = 0


if __name__ == '__main__':
    k1 = Kotek()
    w1 = getattr(k1, 'wiek', None)
    print(w1)
    