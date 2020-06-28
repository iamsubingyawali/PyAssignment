def calc_factorial(num):
    try:
        if int(num) < 1:
            return "Invalid Number"
        else:
            factorial = 1
            for i in range(num, 0, -1):
                factorial *= i
            return factorial
    except ValueError:
        return "Invalid Number"


print(calc_factorial(6))
