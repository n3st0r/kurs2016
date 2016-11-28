class Kotek:

    def __init__(self):
        self.miauczenie = 'miaumiau'

    def kicikici(self):
        print(self.miauczenie)

if __name__ == '__main__':
    k1 = Kotek()
    k1.kicikici()
    Kotek.miauczenie = 'DUPA!'
    k2 = Kotek()
    k2.kicikici()


class Piesek:
    szczekanie = 'Hau hau'

    def kicikici(self):
        print(self.szczekanie)

if __name__ == '__main__':
    p1 = Piesek()
    p1.kicikici()
    Piesek.szczekanie = 'DUPA!'
    p2 = Piesek()
    p2.kicikici()
