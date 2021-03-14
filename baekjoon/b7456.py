import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
numbers = [[] for _ in range(4)]
for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(4):
        numbers[j].append(inp[j])

res = 0
num_dict = defaultdict(int)
for i in range(n):
    for j in range(n):
        num_dict[numbers[0][i] + numbers[1][j]] += 1

for i in range(n):
    for j in range(n):
        res += num_dict[-1 * (numbers[2][i] + numbers[3][j])]
print(res)