import pytest

from src.gradebook import GradeBook
from src.report import average, is_successful, passed_count


def make_book(grades):
    book = GradeBook()
    for grade in grades:
        book.add(grade)
    return book


@pytest.mark.parametrize('grades, expected', [([], 0), ([2, 5, 5], 4)])
def test_average(grades, expected):
    assert average(make_book(grades)) == expected


@pytest.mark.parametrize('grades, expected', [([], 0), ([2, 3, 4, 5], 3)])
def test_passed_count(grades, expected):
    assert passed_count(make_book(grades)) == expected


@pytest.mark.parametrize('grades, expected', [
    ([], False), ([2], False), ([3], True),
    ([2, 5, 5], True), ([4, 5], True),
])
def test_success_conditions(grades, expected):
    assert is_successful(make_book(grades)) is expected
