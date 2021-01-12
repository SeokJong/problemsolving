import sys

def find_route(curr, visited):
    if visited == total:
        return weight[curr][0] if weight[curr][0] > 0 else 999999999
    if dp[curr][visited] > 0:
        return dp[curr][visited]

    tmp = 999999999
    for i in range(1, N):
        if (visited >> i) % 2 == 1 or weight[curr][i] == 0:
            continue
        tmp = min(tmp, weight[curr][i] + find_route(i, visited | (1 << i)))
    dp[curr][visited] = tmp
    return tmp

N = int(sys.stdin.readline())
weight = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
total = (1 << N) - 1
print(find_route(0, 1))