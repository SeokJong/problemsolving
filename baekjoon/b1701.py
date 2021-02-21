input = __import__('sys').stdin.readline

def get_pi(txt):
    pi = [0] * (len(txt) + 1)
    j = 0
    for i in range(1, len(txt)):
        while txt[i] != txt[j] and j > 0:
            j = pi[j-1]
        if txt[i] == txt[j]:
            j += 1
            pi[i] = j
    return pi

# txt = input()[:-1]
txt = 'a'*5000
result = 0
for i in range(len(txt)):
    result = max(result, max(get_pi(txt[i:])))
print(result)