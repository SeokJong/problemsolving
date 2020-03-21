from collections import deque
import copy


def move(board, red, blue, axis, direction):
    if red[axis]*direction > blue[axis]*direction:
        first, second = red, blue
    else:
        first, second = blue, red
    while 1:
        first[axis] += direction
        if board[first[0]][first[1]] != 0:
            if board[first[0]][first[1]] == 1:
                first[axis] -= direction
            else:
                first[0] = -1
                if blue[0] == -1:
                    return -2, -2
            break
    while 1:
        second[axis] += direction
        if board[second[0]][second[1]] != 0:
            if board[second[0]][second[1]] == 1:
                second[axis] -= direction
                if first == second:
                    second[axis] -= direction
            if board[second[0]][second[1]] == 2:
                second[0] = -1
            break
    if blue[0] == -1:
        return -2, -2
    elif red[0] == -1:
        return -1, -1
    else:
        return red, blue


def solve(board, red, blue):
    que = deque()
    que.append((red, blue, 0, -1))
    visited = set()
    visited.add(to_str(red, blue))
    while 1:
        if not que:
            return -1
        status = que.popleft()
        n = status[2]
        if n == 10:
            return -1
        method = 0
        for axis in [0, 1]:
            for direction in [1, -1]:
                if status[3] != method:
                    red, blue = move(board, copy.deepcopy(status[0]), copy.deepcopy(status[1]), axis, direction)
                    if red == -1:
                        return n+1
                    elif red == -2:
                        method += 1
                        continue
                    else:
                        pos = to_str(red, blue)
                        if pos in visited:
                            method += 1
                            continue
                        else:
                            visited.add(pos)
                            que.append((red, blue, n+1, method))
                method += 1


def get_board(y_len, x_len):
    board = []
    for y in range(y_len):
        line = input()
        row = []
        for x in range(x_len):
            s = line[x]
            if s == '#':
                row.append(1)
            elif s == '.':
                row.append(0)
            elif s == 'B':
                blue = [y, x]
                row.append(0)
            elif s == 'R':
                red = [y, x]
                row.append(0)
            elif s == 'O':
                row.append(2)
        board.append(row)
    return board, red, blue


def main():
    y, x = map(int, input().split())
    board, red, blue = get_board(y, x)
    print(solve(board, red, blue))


if __name__ == "__main__":
    main()
