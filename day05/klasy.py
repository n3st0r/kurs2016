
class Samochod:

    def marka(self):
        print('BMW')

    def przejedz(self, predkosc):
        czas = 30
        trasa = predkosc * czas
        print('Przejechałem: ', trasa, 'z prekdoscią', predkosc )
        return trasa

    def __str__(self):
        return 'To jest samochód'


if __name__ == '__main__':
    bmw1 = Samochod()
    bmw1.marka()
    droga = bmw1.przejedz(123)
    print(droga)

