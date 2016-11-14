
def czy_liczba():
    while True:
        liczba = input('Podaj liczbę: ')

        try:
            liczba = int(liczba)
            return liczba

        except ValueError:
            print('Nie podałeś liczby!')

if __name__ == '__main__':
    czy_liczba()
