import sys
from collections import deque

def topological_sort():
    global rank, tot_time  # i번 작업의 진입차수, 작업시간
    workq = deque()
    job_ord = []
    for w in range(len(rank)):
        if rank[w] == 0:
            workq.append(w)
            job_ord.append(w)
    while workq:
        curr = workq.popleft()
        for next_work in work_tree[curr]:
            tot_time[next_work] = max(tot_time[next_work], tot_time[curr] + work_time[next_work])
            rank[next_work] -= 1
            if rank[next_work] == 0:
                job_ord.append(w)
                workq.append(next_work)
    return max(tot_time)

n = int(sys.stdin.readline())
rank = [0] * n
work_time = [0] * n
tot_time = [0] * n
work_tree = [[] for _ in range(n)]
for i in range(n):
    work = list(map(int, sys.stdin.readline().split()))
    work_time[i] = work[0]
    tot_time[i] = work[0]
    rank[i] += work[1]
    for j in work[2:]:
        work_tree[j-1].append(i)
tot_time[0] = work_time[0]
print(topological_sort())
