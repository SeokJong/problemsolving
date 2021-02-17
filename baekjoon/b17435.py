import sys

m = int(input()) + 1
fx = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0] * m for _ in range(19)]

for i in range(1, m):
    dp[0][i] = fx[i]
for i in range(1, 19):
    for j in range(1, m):
        dp[i][j] = dp[i-1][dp[i-1][j]]

for _ in range(int(sys.stdin.readline())):
    n, x = map(int, sys.stdin.readline().split())
    while n > 0:
        i = 0
        num = 1
        for b in range(19):
            if n & 1:
                x = dp[b][x]
            n >>= 1
    print(x)