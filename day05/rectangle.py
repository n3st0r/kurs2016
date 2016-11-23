
class Rectangle:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
        if self.czy_kwadrat():
            return "Kwadrat, boki a = b = %s" % self._a
        else:
            return "Prostokąt - bok a: %s, bok b: %s" % (self._a, self._b)

    def pole_prostokata(self):
        pole = self._a * self._b
        return pole

    def obwod_prostokata(self):
        obwod = 2 * self._a + 2 * self._b
        return obwod

    def czy_kwadrat(self):
        if self._a == self._b:
            return True
        else:
            return False

    def boki(self):
        return self._a, self._b

    def opis(self):
        pole = self.pole_prostokata()
        obwod = self.obwod_prostokata()

        if self.czy_kwadrat():
            kwadrat = 'Tak'
        else:
            kwadrat = 'Nie'
        tekst = "Prostokąt - bok a: %s, bok b: %s, pole: %s, obód: %s, czy kwadrat: %s" %\
                (self._a, self._b, pole, obwod, kwadrat)
        return tekst

if __name__ == '__main__':
    print('Testy programu')

    prostokat = Rectangle(1, 2)
    boki = prostokat.boki()
    print('Weryfikacja typu zwracanej wartości:', type(boki))
    print(prostokat.opis())

    prostokat2 = Rectangle(2, 4)
    print(prostokat2.opis())

    kwadrat = Rectangle(4, 4)
    print(kwadrat.opis())
