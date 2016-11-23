
class Zwierze:
    def __init__(self):
        self.wiek = 0
        print('Zwierze - __init__')

    def jedz(self, pokarm):
        print('Zjadłem: ', pokarm)

    def jaki_wiek(self):
        print('Mam lat:', self.wiek)


class KotDomowy(Zwierze):
    def __init__(self):
        super().__init__()
        print('Kot domowy - __init__')

    def machaj_ogonem(self):
        print('macha ogonem')

if __name__ == '__main__':
    z1 = Zwierze()
    z1.jedz('siano')
    z1.jaki_wiek()

    k1 = KotDomowy()
    k1.machaj_ogonem()
    k1.jedz('Mleko')
