import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

w, h = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(h)]
que = deque()
dp = [[[9999999] * 4 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            board[i][j] = '.'
            for d in range(4):
                dp[i][j][d] = 0
                que.append([i, j, d, 0])
            break
    if que:
        break
res = -1
while que:
    x, y, d, m = que.popleft()
    while board[x][y] == '.':
        x += dx[d]
        y += dy[d]
        if x < 0 or x >= h or y < 0 or y >= w or board[x][y] == '*':
            break
        if board[x][y] == 'C':
            res = m
            break
        if dp[x][y][d] < m:
            break
        dp[x][y][d] = m
        if dp[x][y][(d+1) % 4] > m + 1:
            dp[x][y][(d+1) % 4] = m + 1
            que.append([x, y, (d+1) % 4, m+1])
        if dp[x][y][(d-1) % 4] > m + 1:
            dp[x][y][(d-1) % 4] = m + 1
            que.append([x, y, (d-1) % 4, m+1])
    if res != -1:
        break
print(res)