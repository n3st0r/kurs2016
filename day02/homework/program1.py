#!/usr/bin/env python
import day02.homework.kolo as p


for i in range(21):
    obwod = round(p.licz_obwod(i), 2)
    pole = round(p.licz_pole_kola(i), 2)
    print('promień: ', i, '; obwód: ', obwod,  '; pole: ', pole)
