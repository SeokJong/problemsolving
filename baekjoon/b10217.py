import sys

tc = int(input())
for _ in range(tc):
    n, m, k = map(int, sys.stdin.readline().split())
    tickets = []
    for _ in range(k):
        tickets.append(list(map(int, sys.stdin.readline().split())))