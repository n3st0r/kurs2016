
def podaj_liczba(komunikat, komunikat_blad):
    while True:
        liczba = input(komunikat)

        try:
            liczba = int(liczba)
            return liczba

        except ValueError:
            print(komunikat_blad)

if __name__ == '__main__':
    bok_a = podaj_liczba('Podaj bok A prostokąta: ', 'Nie podałeś liczby! Czy to takie trudne?')
    bok_b = podaj_liczba('Podaj bok B prostokąta: ', 'Nie podałeś liczby! Czy to takie trudne?')
    print('Pole prostokąta: ', bok_a * bok_b)
