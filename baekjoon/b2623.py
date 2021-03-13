import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
entry_level = [set() for _ in range(n + 1)]
next_jobs = [set() for _ in range(n + 1)]
for i in range(m):
    sub_pd = list(map(int, input().split()))
    for s in range(1, len(sub_pd)):
        job = sub_pd[s]
        for j in range(1, s):
            entry_level[job].add(sub_pd[j])
        for j in range(s+1, len(sub_pd)):
            next_jobs[job].add(sub_pd[j])
entry_level = list(map(len, entry_level))
work_q = deque()
for i in range(1, n+1):
    if entry_level[i] == 0:
        work_q.append(i)
result = []
while(work_q):
    job = work_q.popleft()
    result.append(job)
    for i in next_jobs[job]:
        entry_level[i] -= 1
        if entry_level[i] == 0:
            work_q.append(i)
if len(result) == n:
    [print(i) for i in result]
else:
    print(0)
