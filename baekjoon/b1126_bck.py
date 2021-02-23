import sys
from collections import defaultdict
input = sys.stdin.readline
"""
defaultdict를 이용하여 dp구현. 훨씬 느리다?
"""
n = int(input())
block = list(map(int, input().split()))
if n==1:
    print(-1)
    quit()
height_sum = sum(block)
dp = [[-1] * height_sum for _ in range(len(block))]
dp[0][0] = 0
dp[0][block[0]] = block[0]

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
    print(curr[0])