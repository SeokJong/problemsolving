import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while 1:
    y, x = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0:
        break
    room = [sys.stdin.readline() for _ in range(x)]
    dp = [[999999999] * y for _ in range(x)]
    que = deque()
    dust = [-1] * (x * y)
    bitmask = 0
    dust_ord = 0
    result = 999999999
    for i in range(x):
        for j in range(y):
            if room[i][j] == "o":
                dp[i][j] = 0
                for d in range(4):
                    que.append([i, j, d, 0, 0])
            if room[i][j] == "*":
                dust[(y * i) + j] = dust_ord
                dust_ord += 1
    bitmask_max = (1 << dust_ord) - 1
    dp = [[999999999] * bitmask_max for _ in range(x * y)]
    while que:
        i, j, d, bitmask, time = que.popleft()
        ii = i + dx[d]
        jj = j + dy[d]
        if ii < 0 or ii >= x or jj < 0 or jj >= y or room[ii][jj] == "x" \
                or result <= time or dp[(y * ii) + jj][bitmask] <= time:
            continue
        if room[ii][jj] == "*":
            dust_ord = dust[(y * ii) + jj]
            bitmask = (bitmask | (1 << dust_ord))
            if bitmask == bitmask_max:
                result = min(result, time + 1)
                continue
        dp[(y * ii) + jj][bitmask] = time
        for d in range(4):
            que.append([ii, jj, d, bitmask, time + 1])
    if result < 999999999:
        print(result)
    else:
        print(-1)