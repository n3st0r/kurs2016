

while True:
    liczba = input('Podaj liczbę: ')

    try:
        liczba = int(liczba)

    except ValueError:
        print('Nie podałeś liczby!')

    else:
        print(liczba)
        break
