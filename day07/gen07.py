
def wczytaj_dane_z_pliku():
    with open('test1.txt', 'r') as f:
        for linia in f:
            if linia.startswith('#'):
                continue
            yield linia

if __name__ == '__main__':
    linie = wczytaj_dane_z_pliku()
    for x in linie:
        print(x, end='')
