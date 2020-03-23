import copy


def move(board, direction, size, n):
    global cache
    global result
    added = set()
    large = 0
    if direction == 0:  # left
        x_step = -1
        x_range = range(1, size)
        y_step = 0
        y_range = range(size)
    elif direction == 1:  # right
        x_step = 1
        x_range = range(size-2, -1, -1)
        y_step = 0
        y_range = range(size)
    elif direction == 2:  # up
        x_step = 0
        x_range = range(size)
        y_step = -1
        y_range = range(1, size)
    elif direction == 3:  # down
        x_step = 0
        x_range = range(size)
        y_step = 1
        y_range = range(size-2, -1, -1)
    else:
        return
    for y in y_range:
        for x in x_range:
            num = board[y][x]
            if num != 0:
                tx = x + x_step
                ty = y + y_step
                while board[ty][tx] == 0:
                    tx += x_step
                    ty += y_step
                    if tx < 0 or ty < 0 or tx >= size or ty >= size:
                        tx -= x_step
                        ty -= y_step
                        break
                if board[ty][tx] == num and str(ty)+'.'+str(tx) not in added:
                    board[y][x] = 0
                    board[ty][tx] = num*2
                    added.add(str(ty)+'.'+str(tx))
                    large = max(large, num*2)
                elif board[ty][tx] == 0:
                    board[y][x] = 0
                    board[ty][tx] = num
                    large = max(large, num)
                else:
                    board[y][x] = 0
                    board[ty-y_step][tx-x_step] = num
                    large = max(large, num)
    coded = ''
    result = max(large, result)
    if check(n, large):
        for row in board:
            coded += ''.join(map(str, row))
        if coded in cache and cache[coded] <= n:
            board = -1
            pass
        else:
            cache[coded] = n
        return board
    else:
        return -1


def check(n, r):
    global depth
    global result
    chance = depth - n
    max = r*(2**chance)
    if max < result:
        return False
    else:
        return True

def play(board, size, n):
    global result
    global depth
    if n == depth:
        return
    else:
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
        result = max(max(row), result)
        board.append(row)
        coded += ''.join(map(str, row))
    resultmap[0] = result
    cache[coded] = 0
    play(board, size, 0)
    print(result)


if __name__ == "__main__":
    depth = 5
    result = 0
    resultmap = [0 for _ in range(depth)]
    cache = dict()
    main()
