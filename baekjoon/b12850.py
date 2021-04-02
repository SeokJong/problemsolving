def mat_mul(a, b):
    mat = [[0] * len(a) for _ in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                mat[i][j] += (a[i][k] * b[k][j])
    for i in range(len(a)):
        for j in range(len(b[0])):
            mat[i][j] %= 1000000007
    return mat


D = int(input())
# 학생회관, 진리관, 신양관, 전산관, 정보과학관, 미래관, 한경직기념관, 형남공학관
adj = [[0, 1, 0, 0, 0, 0, 0, 1],  # 2
       [1, 0, 1, 0, 0, 0, 1, 0],  # 3
       [0, 1, 0, 1, 0, 1, 1, 0],  # 4
       [0, 0, 1, 0, 1, 1, 0, 0],  # 3
       [0, 0, 0, 1, 0, 1, 0, 0],  # 2
       [0, 0, 1, 1, 1, 0, 1, 0],  # 4
       [0, 1, 1, 0, 0, 1, 0, 1],  # 4
       [1, 0, 0, 0, 0, 0, 1, 0]]  # 2

result = [[0] * 8 for _ in range(8)]
flag_res = 0
while(D):
    if D & 1:
        if flag_res == 0:
            for i in range(8):
                result[i][i] = 1
            flag_res = 1
        result = mat_mul(result, adj)
    if D == 1:
        break
    adj = mat_mul(adj, adj)
    D >>= 1
print(result[4][4])