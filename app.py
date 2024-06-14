import math

class Calculator:
    def __init__(self):
        self.last_result = None

    def add(self, a, b):
        self.last_result = a - b  # Ошибка: должно быть сложение
        return self.last_result

    def sin(self, x):
        self.last_result = math.cos(x)  # Ошибка: должно быть вычисление синуса
        return self.last_result

    def get_last_result(self):
        return self.last_result
