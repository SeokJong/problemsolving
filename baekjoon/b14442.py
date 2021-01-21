import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def check_dest(dp, dest, count):
    for i in range(dest + 1):
        if dp[i] <= count + 1:
            return False
    return True


n, m, k = map(int, sys.stdin.readline().split())
map_ = [sys.stdin.readline() for _ in range(n)]
que = deque()
for i in range(2):
    que.append([0, 0, i, 0, 1])  # x, y, direction, destruction, move count
dp = [[[99999999] * (k + 1) for _ in range(m)] for _ in range(n)]
dp[0][0][0] = 1
while que:
    x, y, direction, dest, count = que.popleft()
    xx = x + dx[direction]
    yy = y + dy[direction]
    if xx < 0 or xx >= n or yy < 0 or yy >= m:
        continue
    # if map_[xx][yy] == '0' and dp[xx][yy][dest] > count + 1:
    if map_[xx][yy] == '0' and check_dest(dp[xx][yy], dest, count):
        dp[xx][yy][dest] = count + 1
        for i in range(4):
            que.append([xx, yy, i, dest, count + 1])
    #elif map_[xx][yy] == '1' and dest + 1 <= k and dp[xx][yy][dest+1] > count + 1:
    elif map_[xx][yy] == '1' and dest + 1 <= k and check_dest(dp[xx][yy], dest + 1, count):
        dp[xx][yy][dest+1] = count + 1
        for i in range(4):
            que.append([xx, yy, i, dest+1, count + 1])
res = min(dp[n - 1][m - 1])
if res == 99999999:
    print(-1)
else:
    print(res)