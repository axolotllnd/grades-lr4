import pytest

from src.gradebook import GradeBook


def test_add():
    book = GradeBook()
    book.add(4)
    assert book.values() == [4]


def test_add_invalid():
    book = GradeBook()
    with pytest.raises(ValueError):
        book.add(1)
    assert book.values() == []


def test_remove():
    book = GradeBook()
    book.add(3)
    book.add(3)
    book.remove(3)
    assert book.values() == [3]


def test_remove_missing():
    book = GradeBook()
    with pytest.raises(ValueError):
        book.remove(5)


def test_values_copy():
    book = GradeBook()
    book.add(5)
    book.values().clear()
    assert book.values() == [5]
