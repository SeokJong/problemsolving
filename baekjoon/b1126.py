import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
block = list(map(int, input().split()))

height_sum = (sum(block)//2 + 1)
dp = [[-1] * height_sum for _ in range(len(block))]
dp[0][0] = 0
dp[0][block[0]] = block[0]

for i in range(len(block) - 1):
    for j in range(height_sum):
        # i+1번째 블록을 사용하지 않는 경우
        if dp[i][j] != -1:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            # 더 높은 탑에 쌓는 경우
            if j+block[i+1] < height_sum:
                dp[i+1][j+block[i+1]] = max(dp[i+1][j+block[i+1]], dp[i][j]+block[i+1])
            # 더 낮은 탑에 쌓는 경우 case1. block_i <= j case2. block_i > j
            if block[i] <= j:
                dp[i+1][j-block[i+1]] = max(dp[i+1][j-block[i+1]], dp[i][j])
            else:
                dp[i+1][block[i+1]-j] = max(dp[i+1][block[i+1]-j], dp[i][j] + block[i+1] - j)
    print(dp)
if dp[-1][0] == 0:
    print(-1)
else:
    print("1 :", dp[-1][0])

curr = defaultdict(int)
curr[0] = 0
curr[block[0]] = block[0]
for i in range(1, n):
    next = defaultdict(int)
    for k, v in curr.items():
        next[k] = max(next[k], v)
        next[k+block[i]] = max(next[k+block[i]], v + block[i])
        if k >= block[i]:
            next[k-block[i]] = max(next[k-block[i]], v)
        else:
            next[block[i]-k] = max(next[block[i]-k], v + block[i]-k)
    curr = next
if curr[0] == 0:
    print(-1)
else:
    print("2 :", curr[0])
