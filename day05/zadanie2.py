

class Samochod:

    def __init__(self, max, spalanie):
        self.v_max = max
        self.spalanie = spalanie
        self.przebieg = 0
        self.spalone_paliwo = 0

    def przejedz(self, predkosc):
        if predkosc > self.v_max:
            print("BŁĄD")
        else:
            czas = 30
            trasa = predkosc * czas
            self.przebieg += trasa
            self.spalone_paliwo += self.spalanie * trasa

    def poka_przebieg(self):
        print(self.przebieg)

    def __str__(self):
        wynik = 'Maksymalna prędkość: %s, Przebieg samochodu: %s, Spalone %s'\
                % (self.v_max, self.przebieg, self.spalone_paliwo)
        return wynik

if __name__ == '__main__':
    bmw = Samochod(200, 7)
    bmw.przejedz(150)
    bmw.poka_przebieg()

    print(bmw)
