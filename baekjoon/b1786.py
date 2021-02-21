input = __import__('sys').stdin.readline


txt = input()[:-1]
find_p = input()[:-1]

pi = [0] * len(find_p)
j = 0
for i in range(1, len(find_p)):
    while find_p[i] != find_p[j] and j > 0:
        j = pi[j-1]
    if find_p[i] == find_p[j]:
        j += 1
        pi[i] = j
j = 0
count = 0
result = []
p_len = len(find_p)
t_len = len(txt)
for i in range(len(txt)):
    while txt[i] != find_p[j] and j > 0:
        j = pi[j-1]
    if txt[i] == find_p[j]:
        if j == (p_len - 1):
            count += 1
            result.append(str(i - p_len + 2))
            j = pi[j]
        else:
            j += 1
print(count)
print(" ".join(result))