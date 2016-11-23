
class Rectangle:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
        return "Prostokąt - bok a: %s, bok b: %s" % (self._a, self._b)

    def pole_prostokata(self):
        pole = self._a * self._b
        return pole


if __name__ == '__main__':
    print('Testy programu')

    prostokat = Rectangle(1, 2)
    print(prostokat, 'Pole: ', prostokat.pole_prostokata())

    prostokat2 = Rectangle(2, 4)
    print(prostokat2, 'Pole: ', prostokat2.pole_prostokata())

    kwadrat = Rectangle(4, 4)
    print(kwadrat, 'Pole: ', kwadrat.pole_prostokata())
