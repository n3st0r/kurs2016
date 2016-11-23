class NiedobraKarma(Exception):
    def __init__(self, imie_kota):
        self.imie_kota = imie_kota

    def __str__(self):
        return '%s: Nie nawidzę jedzenia z puszki!' % self.imie_kota


class KotDomowy:
    def __init__(self, imie):
        self.imie = imie

    def jedz(self,pokarm):
        if pokarm != 'mysz':
            raise NiedobraKarma(self.imie)
        print(self.imie, ': mniam mniam')

if __name__ == '__main__':
    k1 = KotDomowy('filemon')
    k1.jedz('mysz')

    k2 = KotDomowy('bonifacy')
    try:
        k2.jedz('Whiskas')
    except NiedobraKarma as ex:
        print(ex)
        raise
