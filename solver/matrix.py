import copy
from .vector import Vector

class Matrix:
    def __init__(self, data):
        """Конструктор Matrix принимает список списков или другой Matrix"""
        if isinstance(data, Matrix):
            self.shape = data.shape
            self.data = copy.deepcopy(data.data)
        else:
            self.rows = len(data)
            self.cols = len(data[0])
            self.shape = (self.rows, self.cols)
            self.data = copy.deepcopy(data)

    def dot(self, vec):
        """Умножение матрицы на вектор"""
        if not isinstance(vec, Vector):
            raise TypeError("Expected Vector object")
        if self.cols != vec.shape:
            raise ValueError(f"Shape mismatch: matrix cols={self.cols}, vector shape={vec.shape}")
        
        result = []
        for i in range(self.rows):
            row_sum = 0
            for j in range(self.cols):
                row_sum += self.data[i][j] * vec.data[j]
            result.append(row_sum)
        
        return Vector(result)

    def transpose(self):
        """Транспонирование матрицы"""
        transposed = []
        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.data[i][j])
            transposed.append(row)
        return Matrix(transposed)

    def info(self):
        """Вывод информации о матрице"""
        print(f"Matrix shape: {self.shape}")
        for row in self.data:
            print(row)

    def __str__(self):
        return f"Matrix({self.data})"

