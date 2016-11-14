#!/usr/bin/env python
Pi = 3.14


def licz_obwod(r: float) -> float:
    """
    Funkcja liczy promień koła
    :param r: promień koła, niezbędny do wyliczenia obwodu
    :return: float
    """

    obwod = 2 * Pi * r
    return obwod


def licz_pole_kola(r: float) -> float:
    """
    Funkcja liczy pole koła

    :param r:
    :return: float
    """

    pole = Pi * (r**2)
    return pole
