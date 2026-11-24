import pytest

from src.grade import is_valid_grade


@pytest.mark.parametrize('value', [2, 3, 4, 5])
def test_valid_grade(value):
    assert is_valid_grade(value) is True


@pytest.mark.parametrize('value', [1, 0, -1, 6, 10, 3.5, '4', None, True])
def test_invalid_grade(value):
    assert is_valid_grade(value) is False
