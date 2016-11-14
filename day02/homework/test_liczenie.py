import pytest
import day02.homework.kolo as fun


def test_licz_obwod():
    assert 6.28 == pytest.approx(fun.licz_obwod(1))