class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        if type in [int, float]:
            return a + b
        return False

    def sub(self, a, b):
        if type in [int, float]:
            return a - b
        return False

    def div(self, a, b):
        if type in [int, float] or b != 0:
            return a / b
        return False

    def mul(self, a, b):
        if type in [int, float]:
            return a * b
        return False

    def factorial(self, n):  # *args, **kwargs:
        if type(n) == int and n > 0:
            fsum = 1
            for i in range(1, n + 1):
                fsum *= i
            return fsum
        return False

    def fibonacci(self, n):
        if type(n) != int:
            return False
        if n > 2:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
        elif n == 2:
            return 1
        elif n == 1:
            return 0
        else:
            return False


if __name__ == "__main__":
    my_calc = Calculator()
    print(my_calc.add(1, 2))
