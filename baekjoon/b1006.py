import sys
input = sys.stdin.readline

def run_dp(a, b, c, s):
    for i in range(s, n):
        a[i+1] = min(b[i]+1, c[i]+1)
        if sector[0][i] + sector[1][i] <= w:
            a[i+1] = min(a[i+1], a[i]+1)
        if i > 0 and sector[1][i-1] + sector[1][i] <= w and sector[0][i-1] + sector[0][i] <= w:
            a[i+1] = min(a[i+1], a[i-1]+2)
        if i < (n-1):
            b[i+1] = a[i+1]+1
            if sector[0][i] + sector[0][i+1] <= w:
                b[i+1] = min(b[i+1], c[i]+1)
            c[i+1] = a[i+1]+1
            if sector[1][i] + sector[1][i+1] <= w:
                c[i+1] = min(c[i+1], b[i]+1)
    return a, b, c

tc = int(input())
for t in range(tc):
    sector = []
    result = []
    n, w = map(int, input().split())
    for _ in range(2):
        sector.append(list(map(int, input().split())))
    a = [10001] * (n+1)
    b = [10001] * (n+1)
    c = [10001] * (n+1)
    a[0] = 0
    b[0] = 1
    c[0] = 1
    a, b, c = run_dp(a, b, c, 0)
    result.append(a[-1])
    if n > 1:
        if sector[0][0] + sector[0][-1] <= w:
            a = [10001] * (n+1)
            b = [10001] * (n+1)
            c = [10001] * (n+1)
            a[1] = 1
            b[1] = 2
            c[1] = 1 if sector[1][0] + sector[1][1] <= w else 2
            a, b, c = run_dp(a, b, c, 1)
            result.append(c[n-1] + 1)
        if sector[1][0] + sector[1][-1] <= w:
            a = [10001] * (n+1)
            b = [10001] * (n+1)
            c = [10001] * (n+1)
            a[1] = 1
            b[1] = 1 if sector[0][0] + sector[0][1] <= w else 2
            c[1] = 2
            a, b, c = run_dp(a, b, c, 1)
            result.append(b[n-1] + 1)
        if sector[1][0] + sector[1][-1] <= w and sector[0][0] + sector[0][-1] <= w:
            a = [10001] * (n+1)
            b = [10001] * (n+1)
            c = [10001] * (n+1)
            a[1] = 0
            b[1] = 1
            c[1] = 1
            a, b, c = run_dp(a, b, c, 1)
            result.append(a[n-1] + 2)
    print(min(result))