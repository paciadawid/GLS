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


if __name__ == "__main__":
    my_calc = Calculator()
    print(my_calc.add(1, 2))
