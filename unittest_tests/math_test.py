import unittest
from hamcrest import *
from unittest_tests.src.fibonacci import fibonacci


class MathTests(unittest.TestCase):


    def test_string(self):
        assert_that(fibonacci("xxx"), equal_to(False))  # assert 1+1 == 2

    def test_negative_value(self):
        assert_that(fibonacci(-10), equal_to(False))

    def test_zero(self):
        assert_that(fibonacci(0), equal_to(False))

    def test_one(self):
        assert_that(fibonacci(1), equal_to(0))

    def test_two(self):
        assert_that(fibonacci(2), equal_to(1))

    def test_ten(self):
        assert_that(fibonacci(10), equal_to(34))

    # def test_large_value(self):
    #     assert_that(fibonacci(1000**10000), calling(RecursionError))  # assert 1+1 == 2


if __name__ == "__main__":
    unittest.main()
