
def pos(num):
    floor = 0
    while(1):
        floor += 1
        num -= floor
        if num < 0:
            break
    room = num + floor
    return floor, room


def solve(cur, tar):
    if cur == tar:
        return 0
    start = pos(min(cur, tar))
    tar = pos(max(cur, tar))
    if start[1] > tar[1]:
        return tar[0] - start[0] + start[1] - tar[1]
    elif start[0] - start[1] > tar[0] - tar[1]:
        return tar[1] - start[1]
    else :
        return tar[0] - start[0]


print(solve(100, 1000))