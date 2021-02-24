import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def assignment(x: int) -> int:
    global assign
    for nb in net[x]:
        if check[nb]:
            continue
        check[nb] = 1
        if assign[nb] == 0:
            assign[nb] = x
            return 1
        elif assignment(assign[nb]):
            assign[nb] = x
            return 1
    return 0


n, m = map(int, input().split())
net = [0] * (n+1)
for i in range(n):
    inp = list(map(int, input().split()))
    if inp[0] == 0:
        net[i + 1] = []
        continue
    net[i+1] = inp[1:]
count = 0
assign = [0] * (m + 1)
for i in range(1, n+1):
    check = [0] * (m+1)
    if assignment(i):
        count += 1
print(count)