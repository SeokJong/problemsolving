import sys
input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))
l_p = 0
r_p = n - 1
result = (l_p, r_p)
result_value = abs(values[l_p] + values[r_p])
while l_p < r_p:
    comp = values[l_p] + values[r_p]
    if abs(comp) < result_value:
        result = (l_p, r_p)
        result_value = abs(comp)
    if comp == 0:
        break
    elif comp < 0:
        l_p += 1
    else:
        r_p -= 1
print(f"{values[result[0]]} {values[result[1]]}")