import sys

n = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[1000001] * n for _ in range(3)]
results = 1000001
for first in range(3):
    dp[first][0] = cost[0][first]
    for i in range(1, n-1):
        for c in range(3):
            dp[c][i] = min(dp[(c-1) % 3][i-1], dp[(c+1) % 3][i-1]) + cost[i][c]
    for c in range(3):
        if c == first:
            continue
        dp[c][n-1] = min(dp[(c-1) % 3][n-2], dp[(c+1) % 3][n-2])+cost[n-1][c]
        results = min(results, dp[c][n-1])
    dp[first][0] = 1000001
print(results)
