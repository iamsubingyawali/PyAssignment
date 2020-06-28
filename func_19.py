from functools import reduce

fibo = lambda n: reduce(lambda i, j: i + [i[-1] + i[-2]], range(n - 2), [0, 1])

print(fibo(10))
