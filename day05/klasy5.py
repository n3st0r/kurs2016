
class Samochod:

    def __init__(self, max):
        # Podłoga czyni zmienną teoretycznie prywatną, choć nie broni przed zapisem
        self._przebieg = 0
        self.v_max = max

    def poka_przebieg(self):
        print(self._przebieg)

    def przejedz(self, predkosc):
        czas = 30
        self._przebieg += predkosc * czas

    def __str__(self):
        wynik = 'Maksymalna prędkość: %s, Przebieg samochodu: %s' % (self.v_max, self._przebieg)
        return wynik

if __name__ == '__main__':
    bmw1 = Samochod(240)
    bmw1.poka_przebieg()
    bmw1.przejedz(10)
    bmw1.poka_przebieg()
    bmw1.przejedz(3)
    bmw1.poka_przebieg()
    # Niepoprawne zerowanie licznika kilometrów.
    bmw1._przebieg = 0
    print(bmw1._przebieg)
