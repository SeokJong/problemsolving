import bisect
import sys
length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = []
position = [0] * length


def solve():
    result.append(arr[0])
    position[0] = 0
    for i in range(1, len(arr)):
        num = arr[i]
        if num > result[-1]:
            result.append(num)
            position[i] = len(result)-1
        else:
            pos = bisect.bisect_left(result, num)
            result[pos] = num
            position[i] = pos

    print(len(result))
    pos = len(result)-1
    line = ''
    for i in range(len(arr)-1, -1, -1):
        if position[i] == pos:
            line = str(arr[i]) + ' ' + line
            pos -= 1
            if pos < 0:
                break
    print(line)

solve()



