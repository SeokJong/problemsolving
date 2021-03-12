import sys
import bisect
from collections import deque
input = sys.stdin.readline

n = int(input())
left = []
right = []
line = []
for i in range(n):
    l, r = map(int, input().split())
    line.append((l, r))
line.sort()
for l, r in line:
    left.append(l)
    right.append(r)
lis = []
record = []
lis.append(right[0])
record.append(0)
for i in range(1, n):
    if lis[-1] < right[i]:
        lis.append(right[i])
        record.append(len(lis) - 1)
    else:
        pos = bisect.bisect(lis, right[i])
        lis[pos] = right[i]
        record.append(pos)
pos = len(lis) - 1
result = []
print(n - len(lis))
for i in range(n-1, -1, -1):
    if record[i] == pos:
        pos -= 1
    else:
        result.append(left[i])
[print(i) for i in result[::-1]]