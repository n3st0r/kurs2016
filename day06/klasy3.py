import datetime

class Zwierze:
    def __init__(self):
        self.wiek = 0
        self.chip = ''
        print('Zwierze - __init__')

    def jedz(self, pokarm):
        print('Zjadłem: ', pokarm)

    def jaki_wiek(self):
        print('Mam lat:', self.wiek)

    def nadaj_chip(self):
        self.chip = self.generuj_chip()

    @staticmethod
    def generuj_chip():
        chip = datetime.datetime.now()
        return str(chip)

if __name__ == '__main__':
    z1 = Zwierze()
    chip = Zwierze.generuj_chip()
    print(chip)
    chip = z1.generuj_chip()
    print(chip)
    z2 = Zwierze
    chip = z2.generuj_chip()
    print(chip)
