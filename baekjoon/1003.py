def count(n, cache):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        a = count(n-2, cache)
        b = count(n-1, cache)
        zero, one = a[0]+b[0], a[1]+b[1]
        cache[n] = (zero, one)
        return zero, one


def main():
    n = int(input())
    cache = {}
    for _ in range(n):
        result = count(int(input()), cache)
        print(f"{result[0]} {result[1]}")


if __name__ == "__main__":
    main()