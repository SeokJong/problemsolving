import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def get_far(x, distance):
    global visit
    res = [[x, distance]]
    for target, dist in tree[x]:
        if visit[target] == 0:
            visit[target] = 1
            res.append(get_far(target, distance + dist))
            visit[target] = 0
    return max(res, key=lambda x: x[1])


V = int(input())
tree = [[] for _ in range(V+1)]
visit = [0] * (V+1)
for _ in range(V-1):
    par, chi, d = list(map(int, input().split()))
    tree[par].append([chi, d])
    tree[chi].append([par, d])
visit[1] = 1
start_node = get_far(1, 0)[0]
visit[1] = 0
visit[start_node] = 1
print(get_far(start_node, 0)[1])