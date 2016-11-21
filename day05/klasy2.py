print('Początek pliku')

class Samochod:

    def __init__(self):
        print('Miejsce inicjalizacji samochodu')

    def przejedz(self, predkosc):
        czas = 30
        trasa = predkosc * czas
        print('Przejechałem: ', trasa, 'z prekdoscią', predkosc )
        return trasa


if __name__ == '__main__':
    print("przed")
    bmw1 = Samochod()
    print('Po')

    droga = bmw1.przejedz(10)
    print(droga)

