import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost_sum = sum(cost) + 1
dp = [[0] * cost_sum for _ in range(n)]
dp[0][cost[0]] = memory[0]

for i in range(1, n):
    for j in range(cost_sum):
        cand = [dp[i-1][j]]
        if j >= cost[i]:
            cand.append(dp[i-1][j-cost[i]] + memory[i])
        dp[i][j] = max(cand)
for i in range(1, 10000):
    if dp[-1][i] >= m:
        print(i)
        break
