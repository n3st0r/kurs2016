
class Samochod:

    def __init__(self, predkosc):
        self.predkosc = predkosc

    def przejedz(self):
        czas = 30
        trasa = self.predkosc * czas
        print('Przejechałem: ', trasa, 'z prekdoscią', self.predkosc)


if __name__ == '__main__':
    bmw1 = Samochod(10)
    bmw1.przejedz()