import sys
import math

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
k = int(sys.stdin.readline())

numbers_rest = list(map(lambda x: x % k, numbers))
numbers_len = list(map(len, map(str, numbers)))
dp = [[0] * k for _ in range(1 << n)]
rest_pow = [1 % k]
for i in range(100):
    rest_pow.append((rest_pow[i] * (10 % k)) % k)

dp[0][0] = 1
for bitmask in range((1 << n) - 1):
    for rest in range(k):
        if dp[bitmask][rest] == 0:
            continue
        for add_num in range(n):
            if (bitmask & (1 << add_num)) != 0:
                continue
            new_rest = ((rest * rest_pow[numbers_len[add_num]]) % k + numbers_rest[add_num]) % k
            dp[bitmask | (1 << add_num)][new_rest] += dp[bitmask][rest]
solution = dp[(1 << n) - 1][0]
if solution == 0:
    print("0/1")
else:
    deno = math.factorial(n)
    gcd = math.gcd(solution, deno)
    print(f"{solution//gcd}/{deno//gcd}")
