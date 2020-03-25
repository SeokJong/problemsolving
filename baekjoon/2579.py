import sys

n = int(sys.stdin.readline())
stair = [0] + [int(sys.stdin.readline()) for _ in range(n)]
result = []


def solve():
    global stair
    if n < 3:
        stair += [0, 0, 0]
    result.append([0, 0])
    result.append([stair[1], stair[1]])
    result.append([stair[2], stair[1] + stair[2]])
    result.append([stair[1] + stair[3], stair[2] + stair[3]])

    for i in range(4, n+1):
        a = max(stair[i - 2] + stair[i] + result[i - 3][0], stair[i - 2] + stair[i] + max(result[i - 4]))
        b = stair[i - 2] + stair[i] + result[i - 3][0]
        result.append([max(a, b), stair[i - 1] + stair[i] + max(result[i - 3])])
    print(max(result[n]))


solve()
