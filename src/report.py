"""Расчёт статистики оценок."""


def average(book):
    grades = book.values()
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def passed_count(book):
    return sum(1 for grade in book.values() if grade >= 3)


def is_successful(book):
    grades = book.values()
    has_grades = bool(grades)
    high_average = average(book) >= 4
    no_failures = 2 not in grades
    return has_grades and (high_average or no_failures)
