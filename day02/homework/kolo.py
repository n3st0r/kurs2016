#!/usr/bin/env python
Pi = 3.14


def licz_obwod(r: int) -> int:
    """
    Funkcja liczy promień koła
    :param r: promień koła, niezbędny do wyliczenia obwodu
    :return: int
    """

    obwod = 2 * Pi * r
    return obwod
