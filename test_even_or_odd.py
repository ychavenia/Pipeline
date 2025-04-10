

from even_or_odd import is_even


def test_is_even():
    assert is_even(2)
    assert is_even(0)
    assert not is_even(1)
    assert not is_even(-1)
    assert is_even(-2)
