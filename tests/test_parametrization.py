import pytest

@pytest.mark.parametrize('number', [-1, 2, 3, 1])
def test_numbers(number: int):
    assert number > 0
