import day02.homework.kolo as kolo


liczba = input('Podaj liczbę: ')
lista = [1, 2]
k = (1, 2)

try:
    liczba = int(liczba)
    wynik = lista[liczba]
except ValueError:
    print('Nie podałeś liczby!')
except IndexError:
    print('Lista nie posiada tylu elementów!')
    print('LOG: ', e)
except Exception as e:
    print('LOG: ', e)
else:
    wynik = liczba / 10
    print('Wynik: ', wynik)