import sys
import collections

number, swap = sys.stdin.readline().split()
swap = int(swap)
que = collections.deque()
dp = [set() for _ in range(swap + 1)]
que.append([number, 0])
res = -1 if swap != 0 else number
while(que):
    n, k = que.popleft()
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            new_n = n[:i] + n[j] + n[i+1:j] + n[i] + n[j+1:]
            if new_n not in dp[k+1] and new_n[0] != "0":
                dp[k+1].add(new_n)
                if k+1 < swap:
                    que.append([new_n, k+1])
                else:
                    res = new_n if (int(res) < int(new_n) and new_n[0] != "0") else res
print(res)