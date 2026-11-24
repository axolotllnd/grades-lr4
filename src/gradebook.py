"""Хранение оценок."""
from src.grade import is_valid_grade


class GradeBook:
    def __init__(self):
        self._grades = []

    def add(self, grade):
        if not is_valid_grade(grade):
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        self._grades.append(grade)

    def remove(self, grade):
        if grade not in self._grades:
            return
        self._grades.remove(grade)

    def values(self):
        return self._grades.copy()
