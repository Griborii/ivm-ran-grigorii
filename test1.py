import solver
from solver import Vector 
from solver import Matrix 
from solver import solve_gradient_descent 

def test_solver():
    # Тестовая система: 2x + y = 5, x + 3y = 7
    A_data = [[2, 1], [1, 3]]
    b_data = [5, 7]
    x0_data = [0, 0]
    
    A = Matrix(A_data)
    b = Vector(b_data)
    x0 = Vector(x0_data)
    
    print("=== Тест системы ===")
    print("A = ")
    A.info()
    print(f"b = {b}")
    print(f"x0 = {x0}")
    
    print("\n=== Метод градиентного спуска ===")
    eps0 = 1e-6
    x_gd, iter_gd, hist_gd = solve_gradient_descent(A, b, r=0.1, eps=eps0, x_0=x0, n_max=1000)
    print(f"Решение: {x_gd}")
    print(f"Проверка: A*x = {A.dot(x_gd)}")
    r = b - A.dot(x_gd)
    print(f"Невязка: {r}")
    if r.norm() > eps0:
        raise ValueError
    else:
        print("Done!")


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1.dot(v2) = {v1.dot(v2)}")

# Тест решателей
test_solver()