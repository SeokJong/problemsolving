import sys
N = int(sys.stdin.readline())
cache = {0: 0, 1: 1, 2: 1}


def fibonacci(n):
    if n in cache:
        return cache[n]
    fibn = fibonacci(n-2) + fibonacci(n-1)
    cache[n] = fibn
    return fibn


print(fibonacci(N))
