def factorial(n):  # *args, **kwargs:
    fsum = 1
    for i in range(1, n + 1):
        fsum *= i
    return fsum


if __name__ == "__main__":
    print(factorial(5))