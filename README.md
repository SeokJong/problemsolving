# problemsolving
풀었던 문제들을 정리하지 않았더니 자꾸 까먹기도 하고 해서 이후로는 풀면서 기록하기로 하였습니다.

## 백준
- 1003
  - 재귀로 피보나치를 푸는 방식과 비슷하게 풀 수 있다.
  - 0일때 1,0 1일때 0,1을 리턴하고 그외엔 재귀호출을 이용한다.
  - 이때 메모제이션 기법을 사용, 이전에 사용한것을 메모한다.
  - N이 40 이하이므로 애초에 41개를 계산하고 리턴해도 될듯하다.
- 13460
  - BFS 사용
  - 각 계층에서 가능한 모든 움직임을 계산한후 다음 계층으로 추가
  - 이때 먼저 움직일 공을 결정하고 이를 이용
  - python의 얕은 복사를 활용
  - 이전 단계와 동일한 위치에 구슬두개가 있을경우 해당 가지는 삭제 (이걸로 4배 빨라짐)
  - 고생한것 : 이전 단계에서 진행한 방향을 다음 단계에서 다시 할 필요가 없어서 method 변수를 추가했는데, continue로 반복문을
  넘길때 method += 1을 깜박해서 이걸로 1시간동안 찾음.. 좀 더 신경쓰자
- 12100
  - DFS 사용
  - 메모제이션은 이동결과를 str으로 변환해서 저장. 이때 몇번 움직였는지까지 저장한다. 이렇게 해서 해당횟수 이후 동일한 패턴이 
  나타나면 pass
  - 고생한것 : 주의할 case 1. 메모제이션을 BFS와는 달리 실행횟수까지 저장해야함. case 2. 이미 합쳐진적 있는 블럭은 다시 사용되지 않기에 그부분 반영해야함
  - 하드코딩한 부분이 너무 많고, 시간도 오래걸린다 최적화 여지가 있는데 고민해보자 -> 
  max 값 측정을 매 스텝마다 하는데 이거 제거, backtracking 적용?
- 2042
  - segment tree 사용
  - segment tree만 사용하면 되는거같다 딱히 고생한부분은 없는듯.
  - 그런데 백준기준 python3로는 시간초과가 난다. 2%에서 못넘어감 여기에 big case가 있는듯? 그런데 pypy3로는 성공.
  - python3로 넘어가기 위해 팬윅트리도 한번 시도해보자.
- 11438
  - LCA 사용
  - 트리를 구성후 각 노드의 2^i번째 조상을 i번째 인덱스에 저장 (i:0~21?)
  - 공통조상을 찾는방법은 1. 우선 같은 높이까지 올라간다. (이때 가능한 2의 n승중 가장 큰수만큼 계속 올라감) 
  2. 같은높이에서 동시에 올린다 (이때는 둘이 다른 한도로 최대한 높이 계속 올림)
  - 이때 계속 런타임 에러로 문제가 생겼는데, 이건 재귀 깊이 한도때문에 생기는 문제. 이상하게 한도를 올려도 에러가 나기에 반복문형태로 바꿔서 통과
  - 이문제도 python3으로는 통과가 안된다.. pypy3로 해결. 
- 1915
  - DP문제
  - i=0 or j=0인경우 1이면 보드에 1을 할당
  - 나머지 배열은 순회하면서 확인 좌,상,좌상을 확인해서 해당 보드중 최소값의 +1을 할당한다.
  - 이값의 최대값이 정답.
- 14003
  - DP문제
  - result 배열과 position 배열을 사용한다.
  - 주어진 arr을 순회하면서, 1. result가 비어있으면 -> 수 삽입, 2. result 배열에서 해당 수보다 작은 최대수가 있는 위치 오른쪽에 삽입. 3. 각 arr
  요소가 result에서 삽입되는 위치를 position에 기록
  - result의 길이가 결과길이, 각 요소는 position에서 뒤에서부터 순회해서 len(result)-1부터 시작해서 1개씩 줄이면서 출력 (4,3,2,1,0..)
- 2579
  - DP문제
  - 고려한 케이스 -> max(OXOXO, XOOXO), OXOO 이렇게 2개를 저장해서 최종계단에서 다시 max.
- 11660
  - DP?
  - 특정 x,y에 대해 0,0~x,y까지 누적합을 계산해둔 배열을 만든다
  - 누적배열을 이용해 a-b-c+d로 해결. (a=x2,y2, b=x1-1,y2, c=x2,y1-1, d=x1-1,y1-1)
- 2003
  - 배열의 start와 end를 사용해서 구함
  - 처음부터 더해가다가 m보다 크거나 같으면 정지. 기록후 start += 1, end -= 1 후 다시 진행.
- 2805
  - 나무를 높이의 내림차순으로 정렬후 다음 나무높이만큼 잘라서 계산.
  - 목표를 넘어섰으면 초과량//나무갯수 해서 현재 높이에서 더해주고 리턴.
  - 이분탐색이 더 빠르긴 할거같다.
- 2748
  - 피보나치 구하기. 메모제이션 사용
- 9252
  - DP
  - 2차원 dp배열을 사용함. x,y에 각 문자를 넣고 순회 x=y일때 값은 DP(x-1,y-1)+1, 그외엔 max(DP(x-1,y), DP(x,y-1))
  - 이때 최대 공통수열은 DP\[-1,-1\], 수열뽑기는 -1,-1부터 찾아올라감 조건은 좌or우가 n이면 좌or우로 이동 n-1이면 해당문자 추가하고, x-1,y-1로 이동
- 2252
  - 위상정렬
- 11404
  - 플루이드 와샬
- 12865
  - DP(Knapsack) 알고리즘 문제
  - D[i][j] 상태배열을 만든다. i번째 아이템까지 확인했을때 j무게에서의 최대 가치를 저장하는 배열. 이때 마지막 출력은 D[-1][-1]
  - 주의 : 돌때 이전 스텝의 결과를 일단 다음 스텝으로 가져온다음 계산해야 최종적으로 최대값이 나온다. 
  이때 들수있는 무게를 넘는 아이템이 있는 경우등의 예외처리를 신경써야한다.
- 1655
  - 이분탐색문제.
  - 새로운 숫자를 받아서 배열에 넣을때 이분탐색을 통해 넣을자리를 찾아서 넣는다.
  - 최대 사이즈 10만에 O(NlogN)문제라 가능함. -> 아 이거보다 훨씬 크다... 이걸 N번 해야하니
  - 힙 2개를 사용하는 방법이 있다.
     - maxHeap, minHeap 두개를 사용한다
     - maxHeap의 크기가 minHeap의 크기와 같거나 max가 1 더 크다
     - maxHeap의 모든 원소는 minHeap의 모든원소보다 작거나 같다
     - min-> [x x x] max -> [o x x x] 이렇게 o가 중간값이 된다
     - 새 숫자를 받았을때 두 힙의 크기가 같으면 max에 max가 더 크면 min에 넣는데
     - 둘의 top을 비교하여 안맞으면 둘을 바꿔준다.
     - 이러면 이것도 O(NlogN)? (둘다 풀어본결과 두번째 방식이 훨씬 빠르다 (1/5 시간))
- 2098
  - 외판원
  - 비트마스킹, DP
  - dp[curr, visited] = min(dp[curr, visited],  tsp(next, visited + next) + w[curr][next])
    - visited는 비트로.
- 2151 (거울 설치)
  - 거울 설치해서 가장 적은수로 문에 문을 잇는 빛을 만드는 문제
  - BFS, DP
  - 큐에 현재위치와 방향을 넣음
  - 큐에서 pop을 통해 꺼낸위치를 확인 해당위치에서 적절한 행동을 취함
  - 거울설치가능위치라면 3방향을 큐에 넣는다
  - 각 위치에 각 방향에 따른 최소 거울설치횟수를 기록함 다음 방문시 이것 체크하여 가지치기
  - 고민했던부분
    - 양면거울이라는 부분 이건 고민에 대한 함정인데 처음 방문했을때 각 방향에 대한 최솟값을 기록하므로 다음에 방문했을때 의미가 없어 기록할 필요가 없다
- 2870
  - 문자열에서 숫자를 추출한뒤 정렬하는 간단한 문제
- 4991
  - BFS, 비트마스킹, DP
  - BFS로 전체 방을 탐색한다. 먼지는 순서를 메겨서 비트마스킹으로 모든 먼지위치를 방문했는지 확인한다
  - DP를 통해 특정 비트마스킹 상태에서 특정 셀을 방문했을때 최저 이동횟수를 기록한다.
  - 큐가 비었을때 최저값 or -1 출력한다.
  - BFS를 통해 모든 청소기부-먼지1-먼지2-...사이의 거리를 잰뒤 이를 행렬로 만들고 퍼뮤테이션 이용해 최소값을 출력하는 방법도 있다고 한다.
- 4386
  - 그리디, 크루스칼, 유니온파인드, MST(최소신장트리)
  - 별사이 거리를 배열로 만들어 정렬한 뒤 최소부터 확인한다
  - 이때 두 별이 같은 집합인지 아닌지 보고 합치며 이는 유니온파인드를 쓴다
- 1019
  - 수학적 규칙성 찾기
  - <https://www.slideshare.net/Baekjoon/baekjoon-online-judge-1019>
  - a와 b사이의 숫자갯수 세기
  - a++의 끝을 0, b--의 끝을 9로 맞추면서 각 숫자를 결과에 넣는다 (123, 925) -> (130, 919)
  - 이때 마지막자리는 총 (a//10 - b//10 + 1) * 자릿수(1,10,100,1000) 만큼 0~9까지 들어간다.
  - a//10, b//10에서 위를 반복한다.
  - a == b 에서 종료한다.
- 14442
- 13263
  - DP, CHT
- 16954
  - BFS, Memozation
  - 가장 간단한 BFS문제나 마찬가지 단 que에 넣을때 각 스텝의 타임을 기록하고 타임이 올라가면 맵을 한칸씩 내린다
  - 이렇게만 돌렸을때 통과가 되긴 했으나 정답들에 비해 시간이 느림 (일반적으로 100ms이나 내 정답은 4000ms)
  - 각 스텝을 큐에 넣을때 해당 타임에 방문한적이 있는 위치인지 체크해서 기록함. 이걸로 96ms까지 줄임.
- 6087
  - BFS, memozation
  - 1. queue를 사용해서 너비우선탐색
  - 2. 레이저 직진하면서 각 자리에서 방향+1, 방향-1을 큐에 추가(이때 이동후 해당 위치 확인)
  - 3. 메모를 추가. 각 자리에 돌입방향과 최소 도달하는 거울갯수 저장 이를 통해 더 늘어날경우 자름
  - 4. 목적지 도달시 종료
- 10451, 9466
  - DFS
  - cycle 찾는 문제들
  - 10451의 경우 주어지는 숫자가 순열이므로 모든 node가 사이클에 포함된다. 따라서 visited만 이용하면 사이클수 셀 수 있다.
  - if visited[next[i]] == 1 -> 사이클 완성
  - 9466의 경우 사이클에 포함되지 않는 경우가 생긴다
  - visited에 그룹번호를 넣고 같은그룹번호 발견시 사이클, 아니면 사이클 아님.
- 1086
  - DP, 비트마스킹
  - dp[bitmask][rest] = 경우의수 를 사용한다.
  - bitmask를 i=(0, (1<<n)-1]범위까지 순회하며 각 비트마스크에서 다른 번호를 추가해가면서 나머지를 구한다
  - 이때 새로 추가되는 수의 나머지는 -> ((기존 수의 나머지 * (새로 추가되는 수의 자릿수 * 10) % k) + 새로 추가되는 수의 나머지) % k
  - dp[new_bit][new_rest] += dp[bitmask][rest]
- 10165
  - 그리디, 라인스위핑
  - 순환되는 라인 위에서 겹치는 라인을 찾아내는 문제
  - 기본적인 라인스위핑 : left오름차순, right내림차순으로 정렬하고 순차적으로보면서 right가 증가하지 않으면 겹치는 라인
  - 이 문제에서 특이점은 순환되는 라인으로 인해 한바퀴 도는 경우가 생기는것..
  - 라인을 넣을때 만얄 a > b면 (출발지가 도착지보다 뒤면 한바퀴 도는 형태) 라인에 넣을때 [a-n,b] [a,b+n] 두개를 넣고 일반적인 라인스위핑처럼 풀면 풀림
- 1039
  - BFS, Memozation
  - BFS로 최대값 찾는다 이때 메모는 각 k에서 방문한 위치로 한다.
  - 길이가 1이면 무조건 -1 출력해야한다.
  - 이때 시작이 0으로 되면 안되므로 이부분에 대한 예외처리가 필요하다(바뀐수가 0으로 시작하면 안된다.)
- 3197
  - BFS
  - 백조의 현재 방문큐, 다음타임에 방문할큐, 물의 현재 방문큐, 다음타임 방문큐, 백조의 방문지, 물의 방문지를 사용한다
  - 백조부터 시작해서 방문을 하고 얼음을 만나면 다음타임큐에 넣는다.
  - 물의 큐를 돌린다
  - 다음타임큐를 현재타임으로 바꿔서 계속 진행한다.
  - 이때 처음 L도 물로 생각하고 큐에 넣어주어야 제대로 돌아감..
- 17404 (RGB 칠하기)
  - DP문제
  - 순환배열에서 옆집과 다른색으로 집을 칠할때 최소비용을 구하는 문제.
  - 점화식 d[i][j] = i번 집을 j로 칠했을때 1~i까지 집을 칠하는 비용의 최솟값
  - 순환방식이므로 마지막 집을 칠할때 첫집을 고려하며 첫집을 0,1,2각각의 색으로 칠하는 경우로 모두 진행한다.
- 13913 (숨바꼭질4)
  - BFS
  - BFS로 최단루트 탐색함
  - memo는 각 노드에 방문했을때 이전노드 저장(이걸로 최종 path 출력)
  - 방문범위는 n,k중 큰것의 2배까지로 함
  - 만약 k가 n보다 왼쪽에 있다면 단순히 가는 범위는 k-n으로 출력은 -1씩 계속 이동하는 방식으로 출력
  - 이렇게 했는데도 상당히 느리다.. 더 빠른방법은 찾아봐야할듯
- 17435 (합성함수와 쿼리)
  - 자료구조, 희소배열
  - 쿼리문제는 일반적으로 log(n)의 시간내에 풀어야한다고 한다.
  - 이 문제의 경우 LCA와 같은 방식으로 해결함
  - 특정 f_(2^i)[x]를 미리 만들어서 저장한다.
  - 이때 저장할 배열의 점화식은 다음과 같다
  - dp[0][x] = f(x)
  - dp[i][x] = dp[i-1][dp[i-1][x]]
  - 쿼리문을 해석할때 특정 n을 이진수로 변환하여 예를들면 110101(2)이라고 했을때, 뒤에서부터 제거해가면 쉽다.
    ```
    for b in range(19):
        if n & 1: x = dp[b][x]
        n >>= 1
    ```
- 4195 (친구 네트워크)
  - hash set, disjoint set
  - 이 문제는 분리집합(disjoint set)알고리즘을 사용하여 해결
  - 분리집합 알고리즘은 서로 중복되지 않는 부분 집합들로 나누어진 원소들에 대한 정보를 저장하고 조작함
  - 연산
    - Make set : 초기화 작업. x를 유일한 원소로 하는 새로운 집합을 만듬
    - find : x가 속한 집합의 대표값을 반환한다. -> find(x) : return find(x)
    - union : x와 y의 집합을 합친다 -> parent(y) = parent(x)
  - 기본은 위와 같으나 시간복잡도를 줄이기 위해 트릭이 필요하다. 
    - 트리를 합칠때  rank가 작은 트리를 항상 높은 트리 밑에 넣는다.
    - find를 돌릴때 find의 경로를 찾아진 루트로 압축해준다.
- 1786 (찾기)
  - KMP알고리즘
  - 문자열 검색하는 문제
	- 단순한 모델의 경우 O(N*M)의 시간이 걸리지만 이를 줄여서 O(N+M)으로 줄이는 알고리즘이 존재한다
	- KMP알고리즘이며 이를통해 해결함
	- 이후에 동일한문제 더 풀어보기로 함.
- 1701 (Cubeditor)
  - KMP알고리즘
  - 문자열 검색하는 문제
	- KMP알고리즘을 통해 주어진 문자열에서 중복되는 문자열중 가장 긴 문자열을 찾는 문제
	- 어제 사용한 KMP코드 다시 사용하여 해결
  - KMP약간 수정해야하는데 아직 확실히 이해한게 아니라 약겐 어려운부분이 있엇다..
- 1956 (운동)
  - 그래프, 플로이드 와샬
  - 사이클중 가장 작은 사이클을 찾는 문제
  - 플로이드 와샬을 통해 계산하되 i,i를 0으로 초기화하지 않고 돌린다
  - 다 돌린뒤 i,i중 가장 작은값을 리턴하고 종료.
- 1167 (트리의 지름)
  - 그래프, DFS
  - 아무점이나 잡고 DFS로 가장 먼 지점을 찾는다.
	- 가장 먼지점으로부터 DFS를 통해 다시 가장 먼 지점까지의 거리를 잰다.
	- 방법은 쉬우나 DFS의 스택을 계산하는부분에 헷갈리는 부분이 좀 있엇다.
	- 방문한 노드와 거리를 방문후 다시 초기화해주는게 중요한 부분
- 1967 (트리의 지름)
  - 그래프, DFS
  - 아무점이나 잡고 DFS로 가장 먼 지점을 찾는다.
	- 가장 먼지점으로부터 DFS를 통해 다시 가장 먼 지점까지의 거리를 잰다.
	- 방법은 쉬우나 DFS의 스택을 계산하는부분에 헷갈리는 부분이 좀 있엇다.
	- 방문한 노드와 거리를 방문후 다시 초기화해주는게 중요한 부분
- 1126 (같은 탑)
  - DP
  - dp문제, 어려웠다..
  - dp는 dp[i][j] = h 라고 했을때 i번째 블럭까지 활용했을때 두 탑의 높이차이가 j일때 최대높이 h로 둔다.
  - 새로운 블럭을 두는 경우는 3가지-> 블럭을 쌓지 않는 경우, 블럭을 높은탑에 쌓는 경우, 낮은탑에 쌓는 경우이다.
  - 높은탑에 쌓으면 두 탑사이의 차이 j는 j+block으로 증가하고 최대높이도 h+block이 된다.
  - 낮은탑에 쌓는경우 두가지가 발생한다 쌓으면서 높은탑이 바뀌는 경우와 아닌 경우
    - j < block 인 경우 높은탑이 바뀐다. 이 경우 j는 block-j가 되며 h는 h+block-j가 된다.
    - 반대의 경우 j는 j-block이며 높이는 그대로 h가 된다.
  - 두번째 조건을 구현하는데 고생을 많이 했으며 마지막엔 블럭이 한개만 있는 경우의 예외처리를 생각하지 못해 고생한 문제..
- 1298 (노트북의 주인을 찾아서)
  - 이분 매칭
  - 네트워크 플로우의 용량 1인 케이스라고 한다. 네트워크 플로우도 공부해야할듯
  - DFS를 통해 각자에게 맞는 노트북을 할당한다.
  - 특정인 선택 -> 원하는 노트북 할당 -> 이미 할당된 노트북이면 해당 노트북 할당받은사람에게 다른노트북 할당 시도 -> 반복
  - 이때 방문노드 체크가 제대로 안되면 무한루프가 돈다.
- 2188 (축사배정)
  - 이분 매칭
  - 1298과 동일한 문제. 이 경우 입력을 각 소마다 받는데 0개의 축사를 원하는 경우가 있다 이 예외처리를 빼먹어서 오래걸림
- 3033 (가장 긴 문자열)
  - 해싱, 접미사 배열, LCP배열
  - 어려운 문제.. 이를 풀기위해서 접미사 배열과 LCP라는 개념을 공부하였다.
  - 문제자체는 위 두 개념을 이용하면 그냥 풀리는 문제긴 하다.
  - 접미사 배열(Suffix array)
    - 주어진 문자열의 모든 접미사들을 사전순서대로 배열된 배열
    - 일반적으로 생각했을때 n^2logn의 시간이 걸린다 (정렬에 nlogn, 비교에 n)
    - 하지만 큰 문제를 해결하기 위해서 맨버-마이어스 알고리즘을 사용한다.
    - 이 알고리즘은 문자열을 첫 1,2,4,8...2^n개의 문자를 이용해서 비교한다.
    - 이러는 이유는 비교해야할 나머지 문자열들이 주어진 문자열 집합에 주어졌기에 뒷부분이 이미 비교완료된 부분이라는것을 이용하는것.
    - 방법은 주어진 문자만큼 비교해서 정렬한다 -> 같은 문자끼리 묶은뒤 2배만큼 늘려서 비교한다 -> 반복
  - 이렇게 만들어진 접미사 배열을 이용해서 다시 LCP(Longest Common Prefix) 알고리즘을 사용한다.
  - 이 알고리즘은 다음과 같은 3가지 조건을 이용한다
    1. 접미사 배열에서 이웃한 두 접미사의 lcp는 이웃하지 않은 lcp보다 크거나 같다. -> 정렬하는 과정에서 같은 문자끼리 겹친다.
    2. 이웃한 접미사 배열의 최대 공통 접두사가 1보다 크면 (첫글자가 같으면) Rank[Pos[x-1]+1] < Rank[Pos[x]+1] 이어야 한다.
    3. 이웃한 접미사 배열의 lcp가 1보다 크면 lcp(Pos[x-1]+1, Pos[x]+1) = lcp(Pos[x-1], Pos[x])-1이다 -> 즉, 이웃한 접미사 배열의 첫 글자가 같기 때문에 첫 글자를 뺀 길이 또한 같다는 의미이다.
- 1005 (ACM craft)
  - 위상정렬
  - 위상정렬을 통해 빌드순서를 만든다
  - 빌드순서에 따라 노드를 방문하며 각 빌딩을 짓는데 걸리는 시간을 잰다
  - 위상정렬
    - 위계가 있는 노드를 방문하는데 걸리는 순서 만드는 알고리즘
      - 진입랭크가 0인 노드를 찾아 큐에 넣는다
      - 큐에서 꺼낸다
        - 꺼낸 노드를 위상배열에 넣는다
        - 해당 노드에서 연결된 노드의 진입랭크를 줄인다
        - 줄인 진입랭크가 0이라면 큐에 삽입한다.
      - 큐가 빌때까지 반복한다.
      - 이때 완성된 위상배열의 크기를 재서 원본과 같으면 완성.
- 1806(부분합)
  - 투포인터
  - S보다 큰 부분합중 가장 짧은 배열을 찾는 문제. 보자마자 투포인터구나 했다
  - 투포인터의 경우 구현 자체는 어렵지 않고 중간에 논리적인 부분(이상, 이하, 미만, 초과와 같은)이 중요했다.
- 1197(최소 스패닝 트리)
  - 최소 스패닝 트리 - 크루스칼, 유니온 파인드
- 2056(작업)
  - 위상 정렬 문제
  - 모든 작업의 rank가 0일때 시간측정이 제대로 안되는 문제가 있엇다. 처음에 총 작업시간 배열을 초기화할때 해당 작업의 작업시간을 넣어주는 방식으로 해결
- 2166(다각형의 넓이)
  - 기하학
  - 다각형의 넓이 구하기
    - (|sum_i(x_i * y_i+1) - sum_i(y_i * x_i+1)|)/2
- 2239 (스도쿠)
  - 백트래킹
  - 각 위치에서 넣을수 있는 리스트를 만든뒤 넣어보고 다음거 시도, 시도종료후 0으로 만들고 함수종료식으로 dfs를 한다.
  - 생각나는대로 했더니 시간초과 몇가지 트릭을 사용했다
    1. zeros 배열을 만들어 처음에 0인 위치를 기억한후 이 위치만 방문하였다.
    2. 후보자 배열을 만드는것도 트릭중 하나일것 기본은 모두 넣어보고 유효성 검사를 하는것으로 알고있다.
## SWEA
- 2819
  - DFS, Memoization
  - 특정 격자에 있을때의 숫자를 저장한다. 이후 해당 격자에 도착했을때 숫자가 동일하면 cut.
- 4112
  - 특정 숫자가 주어졌을때 피라미트 층수와 호수를 구한다 (층은 1이 1부터 시작 내려갈수록 커짐, 호는 좌측이 1)
  - 특정층i1 의 특정호j1 에서 출발해서 내려갈때, 도착하는 위치의 호(j2)에 따라서 계산이 달라짐.
  - 이때 i1 < i2이라고 가정하고 품. (테스트 케이스에서는 도착층이 더 낮을경우도 있을것임. 
  하지만 이경우 둘을 뒤집는다. 이게 생각하기 편했음)
  - case 1. j2<j1 : 이때는 층을 다 내려온뒤 j1-j2만큼 더 이동해야함
  - case 2. j1 < j2 < j1+i2-i1 : 이때는 층을 내려가기만 하면 도착 가능함
  - case 3. j1+i2-i1 < j2 : 이때는 층을 내려온뒤 오른쪽으로 더 가야함. 이때 최종 계산은 i2-i1+j2-j1-i2+i1 = j2-j1이 됨.
  - 개념적인 해설 -> 특정 위치에서 출발해서 내려갈때 층 내려가는것만으로 도착가능한 범위는 출발위치에서 삼각형으로 내려감. 
  이때 삼각형 범위를 벗어나는 도착점을 가기 위해서는 해당 층에 도착한뒤(이건 삼각형의 꼭지점이 될것임)거기서 좌우로 추가로 
  이동해야함.
  - case 3에서 j만 가지고 계산이 가능한 이유는 내려가는동안에도 j가 계속해서 증가하기 때문.