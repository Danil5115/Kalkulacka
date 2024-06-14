import math

class Calculator:
    def __init__(self):
        self.last_result = None

    def add(self, a, b):
        result = a + b
        self.last_result = result
        return result

    def sin(self, x):
        result = math.sin(x)
        self.last_result = result
        return result

    def get_last_result(self):
        return self.last_result
