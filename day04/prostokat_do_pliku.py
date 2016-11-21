#!/usr/bin/env python


def podaj_liczbe(komunikat):
    dana = input(komunikat)
    return float(dana)


def podaj_boki():
    a = podaj_liczbe('Podaj długość boku A: ')
    b = podaj_liczbe('Podaj długość boku B: ')
    return a, b


def zapis_do_pliku(nazwa_pliku, tekst):
    """
        bok a: 1, bok b: 2, pole:2
        """
    zawartosc = open(nazwa_pliku, 'a')
    zawartosc.write(tekst)
    zawartosc.close()


if __name__ == '__main__':
    print('Komunikat')
    boka = float()
    bokb = float()

    try:
        boka, bokb = podaj_boki()
    except ValueError as e:
        print('Podałeś złe dane. Kończę program!!!')
        print('LOG:: ', e)

    pole = boka * bokb
    print('Pole prostokąta wynosi: ', pole)
    message = 'nie'
    if boka == bokb:
        message = 'tak'
        print('Podany prostokąt jest kwadratem!')

    wynik = 'bok a: %s, bok b: %s, pole: %s, kwadrat: %s\n' % (boka, bokb, pole, message)
