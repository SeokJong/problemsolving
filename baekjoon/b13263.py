import sys
from collections import deque


def lin_func(a, dp, st = 0):
    return {"a": a, "b": dp, "s": st}


def cross(a, b):
    return (b["b"] - a["b"]) / (a["a"] - b["a"])


n = int(sys.stdin.readline())
tree_height = list(map(int, sys.stdin.readline().split()))
charge = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
stack = deque()
for i in range(1, n):
    new_lin = lin_func(charge[i - 1], dp[i - 1])
    while stack:
        new_lin["s"] = cross(stack[-1], new_lin)
        if stack[-1]["s"] < new_lin["s"]:
            break
        stack.pop()
    stack.append(new_lin)
    x = tree_height[i]
    fpos = 0
    while(fpos+1 < len(stack) and stack[fpos + 1]["s"] < x):
        fpos += 1
    dp[i] = stack[fpos]["a"] * x + stack[fpos]["b"]
print(dp[-1])