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
- 1915
  - DP문제
  - i=0 or j=0인경우 1이면 보드에 1을 할당
  - 나머지 배열은 순회하면서 확인 좌,상,좌상을 확인해서 해당 보드중 최소값의 +1을 할당한다.
  - 이값의 최대값이 정답.
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