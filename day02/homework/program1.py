#!/usr/bin/env python
import day02.homework.kolo as p


for i in range(21):
    obwod = str(round(p.licz_obwod(i), 2)).rjust(12, ' ')
    pole = str(round(p.licz_pole_kola(i), 2)).rjust(12, ' ')
    promien = str(i).rjust(12, ' ')
    print('promień: ', promien, '; obwód: ', obwod,  '; pole: ', pole)
