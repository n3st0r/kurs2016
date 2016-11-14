#!/usr/bin/env python
import day02.homework.kolo as p


for i in range(21):
    print('promień: ', i, '; obwód: ', p.licz_obwod(i),  '; pole: ', p.licz_pole_kola(i))
