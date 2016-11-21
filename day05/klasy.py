
class Samochod:

    def marka(self):
        print('BMW')

    def przejedz(self, predkosc):
        czas = 30
        trasa = predkosc * czas
        print('Przejechałem: ', trasa, 'z prekdoscią', predkosc )
        return trasa

if __name__ == '__main__':
    bmw1 = Samochod()
    bmw1.marka()
    droga = bmw1.przejedz(123)
    print(droga)

