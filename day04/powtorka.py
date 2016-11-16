#!/usr/bin/env python


def podaj_liczbe(komunikat):
    dana = input(komunikat)
    return float(dana)


def podaj_boki():
    a = podaj_liczbe('Podaj długość boku A: ')
    b = podaj_liczbe('Podaj długość boku B: ')
    return a, b

if __name__ == '__main__':
    print('Komunikta')
    try:
        boka, bokb = podaj_boki()
    except ValueError as e:
        print('Podałeś złe dane. Kończę program!!!')
        print('LOG:: ', e)
    else:
        pole = boka * bokb
        print('Pole prostokąta wynosi: ', pole)
        if boka == bokb:
            print('Podany prostokąt jest kwadratem!')