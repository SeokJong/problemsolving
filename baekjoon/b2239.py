import sys
input = sys.stdin.readline

def get_avail(x, y):
    candi = list(map(str, range(1, 10)))
    for i in range(9):
        if board[i][y] in candi:
            candi.remove(board[i][y])
        if board[x][i] in candi:
            candi.remove(board[x][i])
    x -= (x % 3)
    y -= (y % 3)
    for i in range(3):
        for j in range(3):
            if board[x+i][y+j] in candi:
                candi.remove(board[x+i][y+j])
    return candi


def backtrack(board, pos, count):
    if count == 0:
        for i in range(9):
            print(''.join(board[i]))
        return 1
    x, y = zeros[pos]
    candidate = get_avail(x, y)
    for n in candidate:
        board[x][y] = n
        res = backtrack(board, pos+1, count-1)
        if res == 1:
            return 1
    board[x][y] = '0'


board = [[0] * 9 for _ in range(9)]
count = 0
zeros = []
for i in range(9):
    line = input()
    for j in range(9):
        board[i][j] = line[j]
        if board[i][j] == '0':
            count += 1
            zeros.append((i, j))
backtrack(board, 0, count)