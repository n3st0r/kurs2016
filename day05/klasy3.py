print('Początek pliku')


class Ludek:

    def __init__(self, imie_ludka):
        self.imie = imie_ludka


if __name__ == '__main__':
    l1 = Ludek('Cyber Marian')
    print(l1.imie)
    l2 = Ludek('Kapitan Bomba')
    print(l2.imie)
