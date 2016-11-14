#!/usr/bin/env python
import math
Pi = 3.14


def licz_obwod(r: float) -> float:
    """
    Funkcja liczy promień koła
    :param r: promień koła
    :return: float
    """

    obwod = 2 * math.pi * r
    return obwod


def licz_pole_kola(r: float) -> float:
    """
    Funkcja liczy pole koła

    :param r: promień koła
    :return: float
    """

    pole = math.pi * (r**2)
    return pole
