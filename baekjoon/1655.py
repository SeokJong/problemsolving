import sys
import bisect

N = int(sys.stdin.readline())

numbers = []
for i in range(N):
    i += 1

    num = int(sys.stdin.readline())
    bisect.insort(numbers, num)
    if i%2 == 1:
        print(numbers[i//2])
    else:
        print(numbers[i//2 - 1])