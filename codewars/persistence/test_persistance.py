import pytest


def test_persistance():
    assert persistence(39), 3
    assert persistence(4), 0
    assert persistence(25), 2
    assert persistence(999), 4
