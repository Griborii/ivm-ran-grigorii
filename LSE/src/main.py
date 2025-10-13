import copy

class Vector:
    def __init__(self, n):
        self.shape = n
        self.data = [0] * n

    def __init__(self, data):
        self.shape = len(data)
        self.data = copy.deepcopy(data)

    def dot(self, other):
        """Умножение на другой вектор или список"""
        ans = 0
        
        # Проверяем тип аргумента
        if hasattr(other, 'data') and hasattr(other, 'shape'):
            # other - это объект нашего класса
            if self.shape != other.shape:
                raise ValueError("bad sizes")
            for i in range(self.shape):
                ans += other.data[i] * self.data[i]
                
        elif isinstance(other, list):
            # other - это обычный список
            if self.shape != len(other):
                raise ValueError("bad sizes")
            for i in range(self.shape):
                ans += other[i] * self.data[i]
                
        else:
            raise TypeError("Unsupported type for dot product")
        
        return ans

    def shape(self):
        return self.shape
    
    def info(self):
        print(self.data)


class Matrix:
    def __init__(self, cols, rows):
        self.shape = (cols, rows)
        self.data = [[0] * cols for _ in range(rows)]

    def __init__(self, data):
        self.shape = (len(data), len(data[0]))
        data = []
        for i in range(len(data)):
            data.append(copy.deepcopy(data[i]))
        self.data = data

    def dot(self, vec : Vector):
        data = [vec.dot(self.data[i]) for i in range(self.shape()[0])]
        return Vector(data)

    def shape(self):
        return self.shape
    
    def info(self):
        print(self.data)
    
def solve(A, b, r, eps, x_0, n_max):
    A_shape = A.shape()
    b_shape = b.Shape()
    if A_shape[0] != b_shape:
        raise ValueError("bad size")

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1.dot(v2))
