#!/usr/bin/env python
import day02.homework.kolo as p


def do_prawej(text, dlugosc=12) -> str:
    wynik = str(text).rjust(dlugosc, ' ')
    return wynik

print('Rozpoczynam wyliczenia:')

for i in range(1, 21):
    obwod = do_prawej(p.licz_obwod(i))
    pole = do_prawej(p.licz_pole_kola(i))
    promien = do_prawej(i)
    print('promień: ', promien, '; obwód: ', obwod,  '; pole: ', pole)
