import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cul_arr = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            cul_arr[i][j] = cul_arr[i][j-1] + arr[i][j]
        elif j == 0:
            cul_arr[i][j] = cul_arr[i-1][j] + arr[i][j]
        else :
            cul_arr[i][j] = cul_arr[i-1][j] + cul_arr[i][j-1] - cul_arr[i-1][j-1] + arr[i][j]

for _ in range(m):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    a = cul_arr[y2-1][x2-1]
    b = cul_arr[y1-2][x2-1] if y1 > 1 else 0
    c = cul_arr[y2-1][x1-2] if x1 > 1 else 0
    d = cul_arr[y1-2][x1-2] if x1 > 1 and y1 > 1 else 0
    print(a-b-c+d)