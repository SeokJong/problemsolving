import sys
from collections import Counter
num_trees, needs = map(int, sys.stdin.readline().split())
#trees = Counter(map(int, sys.stdin.readline().split())) + [0]
trees = Counter(sorted(list(map(int, sys.stdin.readline().split())), reverse=True)+[0])
trees[0] = 0


def solve():
    wood = 0
    cnt_tree = 0
    height = -1
    for i in trees:
        if height == -1:
            height = i
        cut = i
        wood += (height - cut) * cnt_tree
        if needs <= wood:
            cut += (wood - needs)//cnt_tree
            print(cut)
            return
        height = cut
        cnt_tree += trees[i]


solve()