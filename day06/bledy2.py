
class KotDomowy:
    def jedz(self,pokarm):
        if pokarm != 'mysz':
            raise ValueError('Jadam tylko myszy')
        print('mniam mniam')

if __name__ == '__main__':
    k1 = KotDomowy()
    k1.jedz('mysz')

    k2 = KotDomowy()
    try:
        k2.jedz('Whiskas')
    except ValueError:
        print('Nie zjadł whiskas, nic dziwnego')
