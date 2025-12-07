"""
Пакет solver - библиотека для линейной алгебры и решения СЛАУ.

Экспортирует:
    Vector - класс вектора
    Matrix - класс матрицы
    solve_linear_system - функция решения СЛАУ
    solve_gradient_descent - метод градиентного спуска
"""

# Экспортируем основные классы и функции
from .vector import Vector
from .matrix import Matrix
from .solver import solve_gradient_descent


# Что будет импортировано при "from solver import *"
__all__ = [
    'Vector',
    'Matrix', 
    'solve_linear_system',
    'solve_gradient_descent',
    'solve_conjugate_gradient',
    'solve_jacobi'
]

# Мета-информация
__version__ = "1.0.0"
__author__ = "Ваше Имя"