import sys
from math import log2, ceil
sys.setrecursionlimit(400000)
input = sys.stdin.readline


def get_tree(now, parent, val):
    depth[now] = depth[parent] + 1
    if now != 1:
        dist[now] = dist[parent] + val
    parent_mat[now][0] = parent
    for i in range(1, log_max_depth):
        tmp = parent_mat[now][i - 1]
        parent_mat[now][i] = parent_mat[tmp][i - 1]
    for node, weight in graph[now]:
        if node == parent:
            continue
        get_tree(node, now, weight)


def get_dist(a, b):
    aa, bb = a, b
    if depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a, b = b, a
        for i in range(log_max_depth - 1, -1, -1):
            if depth[a] <= depth[parent_mat[b][i]]:
                b = parent_mat[b][i]

    lca = a
    if a != b:
        for i in range(log_max_depth - 1, -1, -1):
            if parent_mat[a][i] != parent_mat[b][i]:
                a = parent_mat[a][i]
                b = parent_mat[b][i]
            lca = parent_mat[a][i]
    print(dist[aa] + dist[bb] - 2*dist[lca])


N = int(input())
log_max_depth = ceil(log2(N))
depth = [0] * (N + 1)
dist = [0] * (N + 1)
depth[0] = -1
parent_mat = [[0] * log_max_depth for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])
get_tree(1, 0, 0)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    get_dist(a, b)