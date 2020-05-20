import unittest
from hamcrest import *


class MathTests(unittest.TestCase):


    def test_add(self):
        # assert 1+1 == 2
        assert_that(1 + 1, equal_to(2))

if __name__ == "__main__":
    unittest.main()
