import pytest

from src.gradebook import GradeBook
from src.report import average, is_successful, passed_count


def test_add_and_report():
    book = GradeBook()
    for grade in [2, 4, 5, 5]:
        book.add(grade)
    assert average(book) == 4
    assert passed_count(book) == 3
    assert is_successful(book) is True


def test_remove_and_recalculate():
    book = GradeBook()
    book.add(2)
    book.add(4)
    book.remove(2)
    assert average(book) == 4
    assert passed_count(book) == 1
    assert is_successful(book) is True


def test_invalid_does_not_change_report():
    book = GradeBook()
    book.add(4)
    with pytest.raises(ValueError):
        book.add(6)
    assert average(book) == 4
    assert book.values() == [4]


def test_empty_after_removal():
    book = GradeBook()
    book.add(3)
    book.remove(3)
    assert average(book) == 0
    assert passed_count(book) == 0
    assert is_successful(book) is False
