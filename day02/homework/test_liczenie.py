import pytest
import day02.homework.kolo as kolo


def test_licz_obwod():
    assert 6.28 == pytest.approx(kolo.licz_obwod(1), abs=0.2)


def test_licz_pole_kola():
    assert 3.14 == pytest.approx(kolo.licz_pole_kola(1), abs=0.2)
