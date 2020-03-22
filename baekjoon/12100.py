import copy


def move(board, direction, size, n):
    global cache
    added = [[0 for _ in range(size)] for _ in range(size)]
    if direction == 0:  # left
        step = -1
        for y in range(size):
            for x in range(1, size):
                num = board[y][x]
                if num == 0:
                    continue
                tx = x+step
                while board[y][tx] == 0:
                    if tx <= 0:
                        break
                    tx += step
                if board[y][tx] == num and added[y][tx] == 0:
                    board[y][x] = 0
                    board[y][tx] = num*2
                    added[y][tx] = 1
                elif board[y][tx] == 0:
                    board[y][x] = 0
                    board[y][tx] = num
                else:
                    board[y][x] = 0
                    board[y][tx-step] = num
    if direction == 1:  # right
        step = +1
        for y in range(size):
            for x in range(size-2,-1,-1):
                num = board[y][x]
                if num == 0:
                    continue
                tx = x+step
                while board[y][tx] == 0:
                    if tx >= size-1:
                        break
                    tx += step
                if board[y][tx] == num and added[y][tx] == 0:
                    board[y][x] = 0
                    board[y][tx] = num*2
                    added[y][tx] = 1
                elif board[y][tx] == 0:
                    board[y][x] = 0
                    board[y][tx] = num
                else:
                    board[y][x] = 0
                    board[y][tx-step] = num
    if direction == 2:  # down
        step = +1
        for y in range(size-2, -1, -1):
            for x in range(size):
                num = board[y][x]
                if num == 0:
                    continue
                ty = y+step
                while board[ty][x] == 0:
                    if ty >= size-1:
                        break
                    ty += step
                if board[ty][x] == num and added[ty][x] == 0:
                    board[y][x] = 0
                    board[ty][x] = num*2
                    added[ty][x] = 1
                elif board[ty][x] == 0:
                    board[y][x] = 0
                    board[ty][x] = num
                else:
                    board[y][x] = 0
                    board[ty-step][x] = num
    if direction == 3:  # up
        step = -1
        for y in range(1, size):
            for x in range(size):
                num = board[y][x]
                if num == 0:
                    continue
                ty = y+step
                while board[ty][x] == 0:
                    if ty <= 0:
                        break
                    ty += step
                if board[ty][x] == num and added[ty][x] == 0:
                    board[y][x] = 0
                    board[ty][x] = num*2
                    added[ty][x] = 1
                elif board[ty][x] == 0:
                    board[y][x] = 0
                    board[ty][x] = num
                else:
                    board[y][x] = 0
                    board[ty-step][x] = num
    coded = ''
    for row in board:
        coded += ''.join(map(str, row))
    if coded in cache and cache[coded] <= n:
        board = -1
        pass
    else:
        cache[coded] = n
    return board


def play(board, size, n):
    global result
    if n == 5:
        large = []
        for i in board:
            large.append(max(i))
        result = max(max(large), result)
        return
    else:
        large = []
        for i in board:
            large.append(max(i))
        result = max(max(large), result)
        for direction in range(4):
            resboard = copy.deepcopy(board)
            resboard = move(resboard, direction, size, n+1)
            if resboard == -1:
                continue
            play(resboard, size, n+1)


def main():
    global result
    size = int(input())
    board = []
    coded = ''
    for _ in range(size):
        row = list(map(int, input().split()))
        board.append(row)
        coded += ''.join(map(str, row))
    cache[coded] = 0
    play(board, size, 0)
    print(result)


if __name__ == "__main__":
    result = 0
    cache = dict()
    main()
