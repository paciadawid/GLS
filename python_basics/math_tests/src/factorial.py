def factorial(n):  # *args, **kwargs:

    if type(n) == int and n > 0:
        fsum = 1
        for i in range(1, n + 1):
            fsum *= i
        return fsum
    return False


if __name__ == "__main__":
    print(factorial(5))