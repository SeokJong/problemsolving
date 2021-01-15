import sys
import collections

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def move(y, x, direction):
    xx = x + DIR[direction][1]
    yy = y + DIR[direction][0]
    if 0 <= xx and xx < n and 0 <= yy and yy < n:
        return yy, xx
    else :
        return -1, -1


def get(pos):
    return home[pos[0]][pos[1]]


def finding_door():
    door = []
    for y in range(n):
        for x in range(n):
            if home[y][x] == "#":
                door.append([y, x])
    return door


n = int(sys.stdin.readline())
home = [sys.stdin.readline() for _ in range(n)]
dp = [[[99999999] * 4 for _ in range(n)] for _ in range(n)]
que = collections.deque()
door = finding_door()
y, x = door[0]
for direction in range(4):
    que.append([y, x, direction])
    dp[y][x][direction] = 0
while(que):
    y, x, direction = que.popleft()
    yy, xx = move(y, x, direction)
    if yy != -1:
        if home[yy][xx] == ".":
            if dp[yy][xx][direction] > dp[y][x][direction]:
                dp[yy][xx][direction] = dp[y][x][direction]
                que.append([yy, xx, direction])
        elif home[yy][xx] == "!":
            if dp[yy][xx][direction] > dp[y][x][direction]:
                dp[yy][xx][direction] = dp[y][x][direction]
                que.append([yy, xx, direction])
            if dp[yy][xx][(direction + 1) % 4] > dp[y][x][direction] + 1:
                dp[yy][xx][(direction + 1) % 4] = dp[y][x][direction] + 1
                que.append([yy, xx, (direction + 1) % 4])
            if dp[yy][xx][(direction - 1) % 4] > dp[y][x][direction] + 1:
                dp[yy][xx][(direction - 1) % 4] = dp[y][x][direction] + 1
                que.append([yy, xx, (direction - 1) % 4])
        elif home[yy][xx] == "#":
            if dp[yy][xx][direction] > dp[y][x][direction]:
                dp[yy][xx][direction] = dp[y][x][direction]
y, x = door[1]
res = min([dp[y][x][i] for i in range(4)])
print(res)