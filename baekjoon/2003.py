import sys
length, target = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


def solve():
    result = 0
    end = 0
    value = arr[0]
    for start, i in enumerate(arr):
        while value < target:
            if end == length-1:
                break
            end += 1
            value += arr[end]
        if value == target:
            result += 1
        value -= i
        if end < length -1 :
            value -= arr[end]
            end -= 1
    print(result)


solve()
