#!/usr/bin/env python


def podaj_liczbe(komunikat):
    dana = input(komunikat)
    return float(dana)


def podaj_boki():
    a = podaj_liczbe('Podaj długość boku A: ')
    b = podaj_liczbe('Podaj długość boku B: ')
    return a, b

if __name__ == '__main__':
    print('Komunikat')
    boka = float()
    bokb = float()
    message = str()
    try:
        boka, bokb = podaj_boki()
    except ValueError as e:
        print('Podałeś złe dane. Kończę program!!!')
        print('LOG:: ', e)

    pole = boka * bokb
    print('Pole prostokąta wynosi: ', pole)
    if boka == bokb:
        message = 'Podany prostokąt jest kwadratem!'
        print(message)

    """
    bok a: 1, bok b: 2, pole:2
    """
    plik = 'wyniki.txt'
    zawartosc = open(plik, 'a')
    zawartosc.write('bok a: %s, bok b: %s, pole: %s, %s\n' % (boka, str(bokb), str(pole), message))

