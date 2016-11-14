
def czy_liczba(komunikat, komunikat_blad):
    while True:
        liczba = input(komunikat)

        try:
            liczba = int(liczba)
            return liczba

        except ValueError:
            print(komunikat_blad)

if __name__ == '__main__':
    czy_liczba('Podaj liczbę całkowitą: ', 'Nie podałeś liczby! Czy to takie trudne?')
