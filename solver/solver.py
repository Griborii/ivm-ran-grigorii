import copy
from .matrix import Matrix
from .vector import Vector


def solve_gradient_descent(A, b, r, eps, x_0, n_max):
    """
    Решает Ax = b методом градиентного спуска
    
    Args:
        A: матрица Matrix
        b: вектор правой части Vector
        r: параметр шага (learning rate)
        eps: точность (остановка когда ||Ax - b|| < eps)
        x_0: начальное приближение Vector
        n_max: максимальное число итераций
    
    Returns:
        Vector: решение x
        int: количество итераций
        list: история значений функции
    """
    
    # Проверка размерностей
    if A.shape[0] != b.shape:
        raise ValueError(f"Shape mismatch: A rows={A.shape[0]}, b shape={b.shape}")
    if A.shape[1] != x_0.shape:
        raise ValueError(f"Shape mismatch: A cols={A.shape[1]}, x_0 shape={x_0.shape}")
    
    x = Vector(x_0)  # Копируем начальное приближение
    history = []  # История значений функции f(x) = 0.5 * ||Ax - b||^2
    
    for iteration in range(n_max):
        # Вычисляем градиент: ∇f(x) = A^T (A x - b)
        Ax = A.dot(x)            # A * x
        residual = Ax - b        # A*x - b
        gradient = A.transpose().dot(residual)  # A^T * (A*x - b)
        
        # Значение функции f(x) = 0.5 * ||Ax - b||^2
        f_val = 0.5 * residual.norm()**2
        history.append(f_val)
        
        # Критерий остановки
        if residual.norm() < eps:
            print(f"Converged in {iteration} iterations with residual norm: {residual.norm():.6e}")
            return x, iteration, history
        
        # Обновление x: x_{k+1} = x_k - r * gradient
        x = x - gradient * r
    
    print(f"Did not converge in {n_max} iterations. Final residual norm: {residual.norm():.6e}")
    return x, n_max, history
