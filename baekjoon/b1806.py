import sys

input = sys.stdin.readline
N, S = map(int, input().split())
numarray = list(map(int, input().split()))
result = 100000001
num = numarray[0]
i, j = (0, 1)
while(i < N):
    if num >= S:
        result = min(result, j - i)
        num -= numarray[i]
        i += 1
    else:
        j += 1
        if j > N:
            break
        num += numarray[j-1]
result = 0 if result == 100000001 else result
print(result)