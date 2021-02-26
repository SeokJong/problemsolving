import sys
input = sys.stdin.readline


def get_suffix_array(x):
    sa = [i for i in range(n)]
    g = [0] * (n + 1)  # 순위
    ng = [0] * (n + 1)  # 새로운 순위(순위를 갱신할 때 이용할 배열)
    for i in range(n):
        g[i] = ord(s[i])
    g[n] = -1
    ng[sa[0]] = 0
    ng[n] = -1
    t = 1
    while t < n:
        sa.sort(key=lambda x: (g[x], g[min(x + t, n)]))
        for i in range(1, n):
            p, q = sa[i - 1], sa[i]
            if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
                ng[q] = ng[p] + 1
            else:
                ng[q] = ng[p]
        if ng[n - 1] == n - 1:
            break
        t = t * 2
        g = ng[:]
    return sa


def getLCP():
    len = 0
    lcp = [0] * n
    for i in range(n):
        k = rank[i]
        if k:
            j = sa[k - 1]
            while j + len < n and i + len < n and s[j + len] == s[i + len]:
                len += 1
            lcp[k] = len
            if len:
                len -= 1
    return lcp



n = int(input())
s = input()[:-1]
sa = get_suffix_array(s)
rank = [0] * n
for i in range(n):
    rank[sa[i]] = i
print(max(getLCP()))