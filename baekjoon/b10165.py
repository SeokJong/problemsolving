import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lines = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if b < a:
        lines.append([a-n, b, i+1])
        lines.append([a, b+n, i+1])
    else:
        lines.append([a, b, i+1])
lines.sort(key=lambda x: (x[0], -x[1]))
res = set()
right = -1
for i in range(len(lines)):
    if right < lines[i][1]:
        right = lines[i][1]
        res.add(lines[i][2])
res = list(res)
res.sort()
print(' '.join(map(str, res)))