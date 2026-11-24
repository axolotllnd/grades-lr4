"""Проверка оценки по пятибалльной шкале (2–5)."""


def is_valid_grade(value):
    return type(value) is int and 2 <= value <= 6
