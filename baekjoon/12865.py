import sys

n, k = map(int, sys.stdin.readline().split())
items = []
for i in range(n):
    items.append(list(map(int, sys.stdin.readline().split())))

state = [[0] * (k + 1) for _ in range(n + 1)]

for step, item in enumerate(items):
    step += 1
    for weight in range(min(item[0], k + 1)):
        state[step][weight] = state[step - 1][weight]
    if item[0] <= k:
        for weight in range(item[0], k + 1):
            state[step][weight] = max(state[step - 1][weight], state[step][weight], state[step - 1][weight - item[0]] + item[1])
print(state[-1][-1])
