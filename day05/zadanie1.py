

class Samochod:

    def __init__(self, max):
        self.v_max = max
        self.przebieg = 0

    def przejedz(self, predkosc):
        if predkosc > self.v_max:
            print("BŁĄD")
        else:
            czas = 30
            self.przebieg += predkosc * czas

    def poka_przebieg(self):
        print(self.przebieg)

    def __str__(self):
        wynik = 'Maksymalna prędkość: %s, Przebieg samochodu: %s' % (self.v_max, self.przebieg)
        return wynik

if __name__ == '__main__':
    bmw = Samochod(200)
    bmw.przejedz(150)
    bmw.poka_przebieg()

    print(bmw)
