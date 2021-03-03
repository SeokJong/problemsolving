import sys
from collections import deque
input = sys.stdin.readline


def solve():
    buildings,edge = map(int, input().split())
    buildtime = [0] + list(map(int, input().split()))
    edges = [[] for _ in range((buildings + 1))]
    rank = [0] * (buildings + 1)
    rank[0] = -1
    for _ in range(edge):
        a, b = map(int, input().split())
        rank[b] += 1
        edges[a].append(b)
    w = int(input())
    curr = deque()
    topo = []
    for i in range(1, buildings + 1):
        if rank[i] == 0:
            curr.append(i)
    # 위상정렬로 빌드순서를 찾는다.
    while curr:
        c = curr.popleft()
        topo.append(c)
        for i in edges[c]:
            rank[i] -= 1
            if rank[i] == 0:
                curr.append(i)
    # 각 건물을 짓는데 걸리는 시간을 측정한다
    need = [0] * (buildings + 1)
    for c in topo:
        for j in edges[c]:
            need[j] = max(need[j], need[c] + buildtime[c])
    print(need[w] + buildtime[w])


tc = int(input())
for i in range(tc):
    solve()