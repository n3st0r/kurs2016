import day02.homework.kolo as kolo


liczba = input('Podaj liczbę: ')

try:
    liczba = int(liczba)
except ValueError:
    print('Nie podałeś liczby!')
else:
    wynik = liczba / 10
    print('Wynik: ', wynik)