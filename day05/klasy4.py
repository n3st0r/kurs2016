
class Samochod:

    def __init__(self):
        self.przebieg = 0

    def poka_przebieg(self):
        print(self.przebieg)

    def przejedz(self, predkosc):
        czas = 30
        self.przebieg += predkosc * czas


if __name__ == '__main__':
    bmw1 = Samochod()
    bmw2 = Samochod()
    bmw1.poka_przebieg()
    bmw2.poka_przebieg()
    bmw1.przejedz(10)
    bmw1.poka_przebieg()
    bmw1.przejedz(3)
    bmw1.poka_przebieg()
    bmw2.przejedz(3)
    bmw2.poka_przebieg()
