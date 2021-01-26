import sys
sys.setrecursionlimit(2000)

def get_cycle(n):
    global result
    if visited[edge[n]] == 1:
        result += 1
        return
    visited[edge[n]] = 1
    get_cycle(edge[n])


testcase = int(input())
for _ in range(testcase):
    n = int(input())
    result = 0
    visited = [0] * (n + 1)
    edge = [0] + list(map(int, sys.stdin.readline().split()))
    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            get_cycle(i)
    print(result)