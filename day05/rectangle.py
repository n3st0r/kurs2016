
class Rectangle:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
        # tekst = "Prostokąt - bok a: %s, bok b: %s" % (self._a, self._b)
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

if __name__ == '__main__':
    print('Testy programu')

    prostokat = Rectangle(1, 2)
    pole = prostokat.pole_prostokata()
    obwod = prostokat.obwod_prostokata()
    boki = prostokat.boki()
    print(type(boki))
    print(prostokat, 'Pole:', pole, 'Obwód: ', obwod)

    prostokat2 = Rectangle(2, 4)
    pole = prostokat2.pole_prostokata()
    obwod = prostokat2.obwod_prostokata()
    print(prostokat2, 'Pole:', pole, 'Obwód: ', obwod)

    kwadrat = Rectangle(4, 4)
    pole = kwadrat.pole_prostokata()
    obwod = kwadrat.obwod_prostokata()
    print(kwadrat, 'Pole:', pole, 'Obwód: ', obwod)
