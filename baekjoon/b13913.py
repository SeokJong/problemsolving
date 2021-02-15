from collections import deque

n, k = map(int, input().split())
right = (max(n, k) * 2) + 1
left = 0
route = [-1] * (right + 1)
route[left] = left
que = deque()
que.append(n)
if k > n:
    while que:
        pos = que.popleft()
        if (pos + 1) <= right:
            next_pos = pos + 1
            if route[next_pos] == -1:
                que.append(next_pos)
                route[next_pos] = pos
            if next_pos == k:
                break
        if (pos * 2) <= right and pos != 0:
            next_pos = pos * 2
            if route[next_pos] == -1:
                que.append(next_pos)
                route[next_pos] = pos
            if next_pos == k:
                break
        if (pos - 1) >= left:
            next_pos = pos - 1
            if route[next_pos] == -1:
                que.append(next_pos)
                route[next_pos] = pos
            if next_pos == k:
                break
    result = 0
    result_route = ''
    pos = k
    while 1:
        result += 1
        result_route = str(pos) + ' ' + result_route
        if pos == n:
            break
        pos = route[pos]
    print(result - 1)
    print(result_route[:-1])
else :
    print(n - k)
    result_route = ''
    for i in range(n, k - 1, -1):
        result_route = result_route + str(i) + ' '
    print(result_route[:-1])
