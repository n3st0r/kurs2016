
class Samochod:

    def __init__(self):
        pass

    def przejedz(self, predkosc):
        czas = 30
        trasa = predkosc * czas
        print('Przejechałem: ', trasa, 'z prekdoscią', predkosc )
        return trasa


if __name__ == '__main__':
    bmw1 = Samochod()
    droga = bmw1.przejedz(10)
    print(droga)
