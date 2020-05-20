from python_basics.math_tests.src.factorial import factorial

from python_basics.math_tests.src.calculator import Calculator



assert factorial(5) == 120, "Wrong result, 5! != {}".format(factorial(5))

#assert factorial(-1) == False, "Wrong result, 5! != {}".format(factorial(5))
#assert factorial("test") == False, "Wrong result, 5! != {}".format(factorial(5))

calc = Calculator()

calc.div(1, 0)

try:
    print(factorial("1"))
except [BaseException, AssertionError] as e: # exception
    print(e)
else:  # if no exception
    pass
finally:  # always at the end
    pass
