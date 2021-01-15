import sys

def is_num(c):
    return ("0" <= c and c <= "9")

n = int(sys.stdin.readline())
inp = [sys.stdin.readline() for i in range(n)]
res = []
for line in inp:
    stat = False
    for c in line:
        isnum = is_num(c)
        if stat == False and isnum == True:
            num = int(c)
        elif stat == True and isnum == True:
            num = num*10 + int(c)
        elif stat == True and isnum == False:
            res.append(num)
        stat = isnum
res.sort()
for i in res:
    print(i)