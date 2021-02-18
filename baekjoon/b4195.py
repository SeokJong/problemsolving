input = __import__('sys').stdin.readline


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
    if x == y :
        return
    if rank[x] > rank[y]:
        x, y = y, x
    parent[y] = x
    netsize[x] += netsize[y]
    if rank[x] == rank[y]: rank[y] += 1


testcase = int(input())
for _ in range(testcase):
    num_f = int(input())
    parent = dict()
    rank = dict()
    netsize = dict()
    for _ in range(num_f):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            rank[x] = 0
            netsize[x] = 1
        if y not in parent:
            parent[y] = y
            rank[y] = 0
            netsize[y] = 1
        union(x, y)
        print(netsize[find(x)])