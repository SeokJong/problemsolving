import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def assignment(x: int) -> int:
    global notebook_assign
    for nb in net[x]:
        if check[nb]:
            continue
        check[nb] = 1
        if notebook_assign[nb] == 0:
            notebook_assign[nb] = x
            return 1
        elif assignment(notebook_assign[nb]):
            notebook_assign[nb] = x
            return 1
    return 0


n, m = map(int, input().split())
net = [[] for _ in range(n + 1)]
for _ in range(m):
    people, notebook = map(int, input().split())
    net[people].append(notebook)
count = 0
notebook_assign = [0] * (n + 1)
for i in range(1, n+1):
    check = [0] * (n+1)
    if assignment(i):
        count += 1
print(count)