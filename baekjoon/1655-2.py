import sys
import heapq

N = int(sys.stdin.readline())

maxh = []
minh = []
for i in range(N):
    num = int(sys.stdin.readline())
    if len(maxh) == len(minh):
        heapq.heappush(maxh, -num)
    else:
        heapq.heappush(minh, num)
    if minh and -maxh[0] > minh[0]:
        tmp = -heapq.heappop(maxh)
        heapq.heappush(maxh, -heapq.heappop(minh))
        heapq.heappush(minh, tmp)
    print(-maxh[0])






#     - maxHeap, minHeap 두개를 사용한다
#      - maxHeap의 크기가 minHeap의 크기와 같거나 max가 1 더 크다
#      - maxHeap의 모든 원소는 minHeap의 모든원소보다 작거나 같다
#      - min-> [x x x] max -> [o x x x] 이렇게 o가 중간값이 된다
#      - 새 숫자를 받았을때 두 힙의 크기가 같으면 max에 max가 더 크면 min에 넣는데
#      - 둘의 top을 비교하여 안맞으면 둘을 바꿔준다.
#      - 이러면 이것도 O(NlogN)?
