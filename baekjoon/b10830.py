import sys
input = sys.stdin.readline


def mat_mul(a, b):
    mat = [[0] * len(a) for _ in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                mat[i][j] += (a[i][k] * b[k][j])
    for i in range(len(a)):
        for j in range(len(b[0])):
            mat[i][j] %= 1000
    return mat


N, B = map(int, input().split())
mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))
result = [[0] * N for _ in range(N)]
flag_res = 0
while B:
    if B & 1:
        if flag_res == 0:
            for i in range(N):
                result[i][i] = 1
            flag_res = 1
        result = mat_mul(result, mat)
    if B == 1:
        break
    mat = mat_mul(mat, mat)
    B >>= 1

for i in result:
    print(*i)
