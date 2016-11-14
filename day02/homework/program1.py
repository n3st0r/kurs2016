#!/usr/bin/env python
import day02.homework.kolo as p


def pr(text, dlugosc=12) -> str:
    wynik = str(text).rjust(dlugosc, ' ')
    return wynik


for i in range(21):
    obwod = pr(round(p.licz_obwod(i), 2))
    pole = pr(round(p.licz_pole_kola(i), 2))
    promien = pr(i)
    print('promień: ', promien, '; obwód: ', obwod,  '; pole: ', pole)
