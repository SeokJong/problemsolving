import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def segment_init(start, end, node):
    global tree
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        segment_init(start, mid, node*2)
        segment_init(mid+1, end, node*2+1)
        if hist[tree[node*2]] <= hist[tree[node*2+1]]:
            tree[node] = tree[node*2]
        else:
            tree[node] = tree[node*2+1]


def get_min(start, end, node, left, right):
    if end < left or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    lv = get_min(start, mid, node * 2, left, right)
    rv = get_min(mid + 1, end, (node * 2) + 1, left, right)
    if lv == -1:
        return rv
    if rv == -1:
        return lv
    if hist[lv] < hist[rv]:
        return lv
    else:
        return rv


def solve(left, right):
    if left == right:
        return hist[left]
    mid = get_min(0, len(hist)-1, 1, left, right)
    area = [hist[mid] * (right - left + 1)]
    if left <= mid-1:
        area.append(solve(left, mid-1))
    if right >= mid+1:
        area.append(solve(mid+1, right))
    return max(area)


hist = input().split()
while len(hist)>1:
    hist = list(map(int, hist))
    hist = hist[1:]
    tree = [0] * (len(hist) * 4)
    segment_init(0, len(hist)-1, 1)
    print(solve(0, len(hist)-1))
    hist = input().split()