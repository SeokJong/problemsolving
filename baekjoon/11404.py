import sys



N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dis = [[float('inf')] * N for _ in range(N)]
for i in range(M):
    a, b, d = map(int, sys.stdin.readline().split())
    dis[a-1][b-1] = min(d, dis[a-1][b-1])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                dis[i][j] = 0
                continue
            dist = dis[i][k] + dis[k][j]
            dis[i][j] = dist if dist < dis[i][j] else dis[i][j]

for i in range(N):
    line = ''
    for j in range(N):
        if dis[i][j] == float('inf'):
            line+="0 "
        else:
            line+=f"{dis[i][j]} "
    print(line[:-1])