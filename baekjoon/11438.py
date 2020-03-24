import sys
from collections import deque
sys.setrecursionlimit(200000)


def init():
    par[0][0] = 0
    par[1][0] = 0
    for i in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)


def dfs_rec(n, d):  # exceed recursion limit on baekjoon
    visit[n]= 1
    depth[n]= d
    for i in tree[n]:
        if visit[i] == 1:
            continue
        par[i][0] = n
        dfs(i, d+1)


def dfs(n, d):
    visit[n]= 1
    depth[n]= d
    work = deque()
    work.append([n, d])
    while len(work) > 0:
        ind, dep = work.popleft()
        for target in tree[ind]:
            if visit[target] == 1:
                continue
            visit[target] = 1
            depth[target]= dep+1
            par[target][0] = ind
            work.append([target, dep+1])


def build():
    for j in range(1,21):
        for i in range(1, n+1):
            par[i][j] = par[par[i][j-1]][j-1]


def calc(a, b):
    if depth[a] > depth[b]:
        a,b = b,a
    for i in range(20, -1, -1):
        if depth[b] - depth[a] >= 2**i:
            b = par[b][i]
    if a == b:
        return a
    for i in range(20, -1, -1):
        if par[a][i] != par[b][i]:
            a = par[a][i]
            b = par[b][i]
    return par[a][0]


n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
visit = [0] * (n+1)
depth = [0] * (n+1)
par = [[0]*21 for _ in range(n+1)]
init()
dfs(1,0)
build()
print(par)

n = int(sys.stdin.readline())
work = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    work.append([a,b])

for a, b in work:
    print(calc(a, b))