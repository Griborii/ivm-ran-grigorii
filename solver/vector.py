import copy

class Vector:
    def __init__(self, data):
        """Конструктор Vector принимает список или другой Vector"""
        if isinstance(data, Vector):
            self.shape = data.shape
            self.data = copy.deepcopy(data.data)
        else:
            self.shape = len(data)
            self.data = copy.deepcopy(data)

    def dot(self, other):
        """Скалярное произведение с другим вектором или списком"""
        if isinstance(other, Vector):
            if self.shape != other.shape:
                raise ValueError(f"Shape mismatch: {self.shape} vs {other.shape}")
            return sum(self.data[i] * other.data[i] for i in range(self.shape))
        elif isinstance(other, list):
            if self.shape != len(other):
                raise ValueError(f"Shape mismatch: {self.shape} vs {len(other)}")
            return sum(self.data[i] * other[i] for i in range(self.shape))
        else:
            raise TypeError("Unsupported type for dot product")

    def __add__(self, other):
        """Сложение векторов"""
        if isinstance(other, Vector):
            if self.shape != other.shape:
                raise ValueError(f"Shape mismatch: {self.shape} vs {other.shape}")
            return Vector([self.data[i] + other.data[i] for i in range(self.shape)])
        raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        """Вычитание векторов"""
        if isinstance(other, Vector):
            if self.shape != other.shape:
                raise ValueError(f"Shape mismatch: {self.shape} vs {other.shape}")
            return Vector([self.data[i] - other.data[i] for i in range(self.shape)])
        raise TypeError("Unsupported type for subtraction")

    def __mul__(self, scalar):
        """Умножение вектора на скаляр"""
        return Vector([self.data[i] * scalar for i in range(self.shape)])

    def __rmul__(self, scalar):
        """Умножение скаляра на вектор"""
        return self.__mul__(scalar)

    def norm(self):
        """Евклидова норма вектора"""
        return sum(x**2 for x in self.data)**0.5

    def info(self):
        """Вывод информации о векторе"""
        print(f"Vector shape: {self.shape}, data: {self.data}")

    def __str__(self):
        return f"Vector({self.data})"

