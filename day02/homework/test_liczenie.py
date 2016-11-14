import pytest
import day02.homework.kolo as fun


def test_licz_obwod():
    assert 6.28 == pytest.approx(fun.licz_obwod(1))


def test_licz_pole_kola():
    assert 3.14 == pytest.approx(fun.licz_pole_kola(1))
