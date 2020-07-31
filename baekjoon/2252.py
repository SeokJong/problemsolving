from collections import deque

n, m = map(int, input().split())
degree = [0] * n
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    degree[b-1] += 1
    graph[a-1].append(b-1)
que = deque()
for n, d in enumerate(degree):
    if d == 0:
        que.append(n)

line = ''
while(que):
    work = que.popleft()
    line += f'{work+1} '
    for i in graph[work]:
        degree[i] -= 1
        if degree[i] == 0:
            que.append(i)

print(line[:-1])