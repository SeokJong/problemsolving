import sys
n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, list(sys.stdin.readline()[:m]))) for _ in range(n)]
checked = [[0] * m for _ in range(n)]


def solve():
    result = 0
    for i in range(0, n):
        for j in range(0, m):
            if i == 0 or j == 0:
                checked[i][j] = array[i][j]
                result = max(result, checked[i][j])
                continue
            if array[i][j] == 1:
                checked[i][j] = min(checked[i-1][j], checked[i][j-1], checked[i-1][j-1]) + 1
                result = max(result, checked[i][j])
    return result


print(solve()**2)