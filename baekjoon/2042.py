arr = []


def init(tree, index, start, end):
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start+end)//2
        tree[index] = init(tree, index*2+1, start, mid) + init(tree, index*2+2, mid+1,end)
    return tree[index]


def calc(tree, index, start, end, left, right):
    if (start > right or end < left):
        return 0
    elif start >= left and end <= right:
        return tree[index]
    else:
        mid = (start+end)//2
        return calc(tree, index*2+1, start, mid, left, right) + calc(tree, index*2+2, mid+1, end, left, right)


def update(tree, changed_index, diff, index, start, end):
    if changed_index < start or changed_index > end:
        return
    tree[index] += diff

    if start != end:
        mid = (start + end)//2
        update(tree, changed_index, diff, index*2+1, start, mid)
        update(tree, changed_index, diff, index*2+2, mid+1, end)


def main():
    length, num_change, num_sum = map(int, input().rstrip().split())
    for _ in range(length):
        arr.append(int(input().rstrip()))
    tree = [0] * (length*4)
    init(tree, 0, 0, length-1)
    work = []
    for _ in range(num_change+num_sum):
        a, b, c = map(int, input().rstrip().split())
        work.append((a, b, c))

    for a, b, c in work:
        if a == 1:
            diff = c - arr[b-1]
            arr[b-1] = c
            update(tree, b-1, diff, 0, 0, length-1)
        else:
            print(calc(tree, 0, 0, length-1, b-1, c-1))


main()