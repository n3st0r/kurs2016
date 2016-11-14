import codewars.kyu6.persistence.persistence as p


def test_persistence():
    assert p.persistence(39) == 3
    assert p.persistence(4) == 0
    assert p.persistence(25) == 2
    assert p.persistence(999) == 4
