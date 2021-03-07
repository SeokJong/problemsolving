import sys
input = sys.stdin.readline

n = int(input())
point = []
for _ in range(n):
    point.append(list(map(int, input().split())))
point.append(point[0])
left = 0
right = 0
for i in range(n):
    left += point[i][0] * point[i+1][1]
    right += point[i][1] * point[i+1][0]
print(((round(abs(left-right)/2*100)//10)/10))
