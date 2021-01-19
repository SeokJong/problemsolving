import sys


def add_nums(res, num, pos):
    while num:
        res[num % 10] += pos
        num = num // 10
    return res

def get_chars(res, a, b):
    pos = 1
    while 1:
        while (a % 10) != 0 and a != b:
            res = add_nums(res, a, pos)
            a += 1
        while (b % 10) != 9 and a != b:
            res = add_nums(res, b, pos)
            b -= 1
        if a == b:
            res = add_nums(res, a, pos)
            break
        else:
            for i in range(10):
                res[i] += pos * (b//10 - a//10 + 1)
        a = a // 10
        b = b // 10
        pos *= 10
    return res

n = int(sys.stdin.readline())
res = get_chars([0] * 10, 1, n)
line = ""
for i in res:
    line += f"{i} "
print(line)