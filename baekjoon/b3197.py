import sys
from collections import deque
from pprint import pprint
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
r, c = map(int, sys.stdin.readline().split())
lake = [list(sys.stdin.readline()[:-1]) for _ in range(r)]
swanq = deque()
waterq = deque()
swan = []
swan_visited = [[0] * c for _ in range(r)]
water_visited = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if lake[i][j] == ".":
            waterq.append((i, j, 0))
            water_visited[i][j] = 1
        elif lake[i][j] == "L":
            swan.append((i, j, 0))
            waterq.append((i, j, 0))
            water_visited[i][j] = 1
swanq.append(swan[0])
swan_visited[swan[0][0]][swan[0][1]] = 1
res = -1
while(res == -1):
    next_swanq = deque()
    next_waterq = deque()
    while(swanq):
        i, j, t = swanq.popleft()
        for direction in range(4):
            ii = i+dx[direction]
            jj = j+dy[direction]
            if ii < 0 or ii >= r or jj < 0 or jj >= c or swan_visited[ii][jj]:
                continue
            swan_visited[ii][jj] = 1
            if lake[ii][jj] == "L":
                res = t
                break
            if lake[ii][jj] == "X":
                next_swanq.append((ii, jj, t+1))
                continue
            swanq.append((ii, jj, t))
    if res != -1:
        break
    while(waterq):
        i, j, t = waterq.popleft()
        for direction in range(4):
            ii = i+dx[direction]
            jj = j+dy[direction]
            if ii < 0 or ii >= r or jj < 0 or jj >= c or water_visited[ii][jj]:
                continue
            water_visited[ii][jj] = 1
            if lake[ii][jj] == "X":
                next_waterq.append((ii, jj, t+1))
                continue
            waterq.append((ii, jj, t))
    for ii, jj, _ in next_waterq:
        lake[ii][jj] = "."
    waterq = next_waterq
    swanq = next_swanq
print(res)
