import sys
input = sys.stdin.readline

v, e = map(int, input().split())
dist = [[10000 * (v + 1)] * v for _ in range(v)]
for i in range(e):
    a, b, d = list(map(int, input().split()))
    dist[a - 1][b - 1] = min(d, dist[a - 1][b - 1])

# Floyd Warshall, k : 거쳐가는 노드, i : 출발 노드, j: 도착 노드
for k in range(v):
    for i in range(v):
        for j in range(v):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

result = [0] * v
for i in range(v):
    result[i] = dist[i][i]
result = min(result)
if result == 10000 * (v + 1):
    print(-1)
else:
    print(result)
