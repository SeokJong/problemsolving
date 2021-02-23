import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
block = list(map(int, input().split()))

if n == 1:
    print(-1)
    quit()
height_sum = sum(block)
dp = [[-1] * height_sum for _ in range(len(block))]
dp[0][0] = 0
dp[0][block[0]] = block[0]
curr = set()
curr.add(0)
curr.add(block[0])
for i in range(len(block) - 1):
    next = set()
    for j in curr:
        # i+1번째 블록을 사용하지 않는 경우
        if dp[i][j] != -1:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            next.add(j)
            # 더 높은 탑에 쌓는 경우
            if j + block[i + 1] < height_sum:
                dp[i + 1][j + block[i + 1]] = max(dp[i + 1][j + block[i + 1]], dp[i][j] + block[i + 1])
                next.add(j + block[i + 1])
            # 더 낮은 탑에 쌓는 경우 case1. block_i <= j case2. block_i > j
            if block[i + 1] <= j:
                dp[i + 1][j - block[i + 1]] = max(dp[i + 1][j - block[i + 1]], dp[i][j])
                next.add(j - block[i + 1])
            else:
                dp[i + 1][block[i + 1] - j] = max(dp[i + 1][block[i + 1] - j], dp[i][j] + block[i + 1] - j)
                next.add(block[i + 1] - j)
    curr = next
if dp[-1][0] == 0:
    print(-1)
else:
    print(dp[-1][0])