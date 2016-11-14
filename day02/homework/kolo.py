#!/usr/bin/env python
import math
Pi = 3.14


def licz_obwod(r: float, dokladnosc: int=2) -> float:
    """
    Funkcja liczy promień koła
    :param r: promień koła
    :param dokladnosc: int - ile miejsc po przecinku
    :return: float
    """

    obwod = 2 * math.pi * r
    return round(obwod, dokladnosc)


def licz_pole_kola(r: float, dokladnosc: int=2) -> float:
    """
    Funkcja liczy pole koła

    :param r: promień koła
    :param dokladnosc: int - ile miejsc po przecinku
    :return: float
    """

    pole = math.pi * (r**2)
    return round(pole, dokladnosc)
