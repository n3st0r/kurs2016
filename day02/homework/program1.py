#!/usr/bin/env python
import day02.homework.kolo as p


def pr(text, dlugosc=12) -> str:
    wynik = str(text).rjust(dlugosc, ' ')
    return wynik


for i in range(21):
    obwod = pr(p.licz_obwod(i))
    pole = pr(p.licz_pole_kola(i))
    promien = pr(i)
    print('promień: ', promien, '; obwód: ', obwod,  '; pole: ', pole)
