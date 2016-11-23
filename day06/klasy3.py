import datetime

class Zwierze:
    def __init__(self):
        self.wiek = 0
        print('Zwierze - __init__')

    def jedz(self, pokarm):
        print('Zjadłem: ', pokarm)

    def jaki_wiek(self):
        print('Mam lat:', self.wiek)

    @staticmethod
    def generuj_chip():
        chip = datetime.datetime.now()
        return str(chip)

if __name__ == '__main__':
    # z1 = Zwierze()
    chipek = Zwierze.generuj_chip()
    print(chipek)
