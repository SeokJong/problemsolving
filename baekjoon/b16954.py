import sys
from collections import deque

dx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
dy = [0, 1, -1, 0, 1, -1, 0, 1, -1]
board = deque()
for _ in range(8):
    board.append(sys.stdin.readline())
que = deque()
que.append([7, 0, 0])
res = 0
now = 0
dp = [[-1] * 8 for _ in range(8)]
dp[7][0] = 0
while(que):
    x, y, time = que.popleft()
    if now != time:
        now += 1
        board.appendleft("........")
        board.pop()
    if board[x][y] == "#":
        continue
    for i in range(len(dx)):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx > 7 or yy < 0 or yy > 7 or board[xx][yy] == "#" or dp[xx][yy] == time + 1:
            continue
        if xx == 0 and yy == 7:
            res = 1
            break
        que.append([xx, yy, time + 1])
        dp[xx][yy] = time + 1
    if res == 1:
        break
print(res)