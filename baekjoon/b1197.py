import sys
input = sys.stdin.readline


def find(x):
    global parent
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global rank, parent, netsize
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if rank[x] > rank[y]:
        x, y = y, x
    parent[y] = x
    netsize[x] += netsize[y]
    if rank[x] == rank[y]: rank[y] += 1
    return 1


v, e = map(int, input().split())
edges = []
for i in range(e):
    edges.append(list(map(int, input().split())))
rank = [0] * (v + 1)
parent = [i for i in range((v + 1))]
netsize = [1] * (v + 1)
result = 0
# Kruskal
edges.sort(key=lambda x: x[2])
for a, b, w in edges:
    if union(a, b):
        result += w
print(result)
