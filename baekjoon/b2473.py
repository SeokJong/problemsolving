import sys
input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))
sol.sort()
result = float('inf')
for a in range(n - 2):
    b = a + 1
    c = n - 1
    while(b < c):
        mix = sol[a]+sol[b]+sol[c]
        if abs(mix) < abs(result):
            result = mix
            selected = (a,b,c)
        if mix == 0:
            print(f"{sol[a]} {sol[b]} {sol[c]}")
            quit()
        elif mix < 0:
            b += 1
        else:
            c -= 1
print(f"{sol[selected[0]]} {sol[selected[1]]} {sol[selected[2]]}")
