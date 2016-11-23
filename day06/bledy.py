
class KotDomowy:
    def jedz(selfself,pokarm):
        if pokarm != 'mysz':
            raise Exception('Jadam tylko myszy')
        print('mniam mniam')

if __name__ == '__main__':
    k1 = KotDomowy()
    k1.jedz('mysz')

    k2 = KotDomowy()
    try:
        k2.jedz('Whiskas')
    except Exception:
        print('Nie zjadł whiskas, nic dziwnego')
