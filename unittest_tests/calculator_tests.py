import unittest
from hamcrest import *
from python_basics.math_tests.src.calculator import Calculator


class DivTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_int(self):
        assert_that(self.calculator.div(2, 1), equal_to(2))

    def test_float(self):
        assert_that(self.calculator.div(1.0, 2), equal_to(0.5))

    def test_zero_division(self):
        assert_that(self.calculator.div(1, 0), equal_to(False))


class FibTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_string(self):
        assert_that(self.calculator.fibonacci("xxx"), equal_to(False))  # assert 1+1 == 2

    def test_negative_value(self):
        assert_that(self.calculator.fibonacci(-10), equal_to(False))

    def test_zero(self):
        assert_that(self.calculator.fibonacci(0), equal_to(False))

    def test_one(self):
        assert_that(self.calculator.fibonacci(1), equal_to(0))

    def test_two(self):
        assert_that(self.calculator.fibonacci(2), equal_to(1))

    def test_ten(self):
        assert_that(self.calculator.fibonacci(10), equal_to(34))


class FactorialTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_positive(self):
        assert_that(self.calculator.factorial(5), equal_to(120))

    def test_negative(self):
        assert_that(self.calculator.factorial(-10), equal_to(False))

    def test_string(self):
        assert_that(self.calculator.factorial("1"), equal_to(False))


if __name__ == '__main__':
    unittest.main()
