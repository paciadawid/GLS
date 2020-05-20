class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b


if __name__ == "__main__":
    my_calc = Calculator()
    print(my_calc.add(1, 2))
