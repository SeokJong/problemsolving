import sys
first = '0' + sys.stdin.readline().rstrip()
second = '0' + sys.stdin.readline().rstrip()


def solve():
    dp = [[0] * len(first) for _ in second]
    for x, i in enumerate(first):
        for y, j in enumerate(second):
            if x == 0 or y == 0:
                continue
            if i == j:
                dp[y][x] = dp[y-1][x-1]+1
            else:
                dp[y][x] = max(dp[y-1][x], dp[y][x-1])
    print(dp[-1][-1])
    q = dp[-1][-1]
    i = len(first) - 1
    j = len(second) - 1
    line = ''
    while q > 0:
        if dp[j-1][i] == q:
            j -= 1
        elif dp[j][i-1] == q:
            i -= 1
        elif dp[j-1][i-1] == q-1:
            line = first[i] + line
            q -= 1
            i -= 1
            j -= 1
        else:
            raise False
    print(line) if line else 0


solve()
