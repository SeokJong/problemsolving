import sys
sys.setrecursionlimit(200000)


def get_group(n):
    global visited, result
    if visited[n] == 1:
        if n in cycle:
            result += len(cycle[cycle.index(n):])
        return
    visited[n] = 1
    cycle.append(n)
    get_group(exp[n])


case = int(sys.stdin.readline())
for _ in range(case):
    n = int(sys.stdin.readline())
    exp = [-1] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (n + 1)
    group = 1
    result = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = []
            get_group(i)
    print(n - result)
