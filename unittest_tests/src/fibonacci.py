def fibonacci(n):

    if type(n) != int:
        return False

    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return False


if __name__ == "__main__":
    fibonacci(100**1000000)
