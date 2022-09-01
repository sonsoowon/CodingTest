"""
11-1. 모험가 길드
N 명의 모험가를 대상으로 그룹을 만들 때, 공포도가 X인 모험가는 X명 이상의 그룹에 참여해야 여행을 떠날 수 있다.
여행을 떠날 수 있는 그룹 수의 최댓값을 구하라.

INPUT
N (1 <= N <= 100,000)
각 모험가의 공포도

OUTPUT
여행을 떠나는 그룹 수의 최댓값


풀이
최소한의 인원으로 그룹을 구성해야 최대한 많은 그룹을 만들 수 있으므로, 공포도가 작은 순으로 그룹을 형성한다.

1. 공포도 배열 fear 을 오름차순으로 정렬한다.
2. i번째로 용감한 모험가의 공포도는 fear[i] 이며,
   새로 형성할 그룹에서 가장 용감한 모험가를 start 번째 모험가, 가장 겁이 많은 모험가를 end 번째 모험가, 최소 인원을 n이라 정의한다.
3. n <= end - start + 1, fear[start] <= n 을 만족하며,
   1) fear[end] == n 인 경우
      그룹이 형성되며 다음 그룹 형성을 위한 start와 n을 재설정한다
   2) n < fear[end] 인 경우
      그룹을 형성하려면 fear[end] 명의 모험가가 필요하므로 n을 재설정한다
4. 3번에서의 start, n을 이용해 end를 재설정한다.
5. 새로운 그룹을 형성할 모험가가 부족할 때까지 즉, end가 배열의 길이를 넘어설 때까지 3, 4번 과정을 반복한다.


시간복잡도
크기 N의 공포도 배열에 대하여 O(N)
- 배열 정렬 O(NlogN)
- 반복문 O(N) : 모든 공포도가 1인 경우 배열의 길이만큼 반복문 시행
"""

def solution(inp_fear):
    # 1. 공포도 배열을 오름차순으로 정렬
    fear = sorted(inp_fear)

    # 2. start, end, n 초기화
    start = 0
    n = fear[start]
    end = start + n - 1

    group_cnt = 0

    # 새로운 그룹을 형성할 수 없을 때까지 반복
    while end < len(fear):
        if n == fear[end]: # 3-1. n 명의 모험가로 그룹 형성이 가능할 경우 
            group_cnt += 1 # 새로운 그룹 형성
            start = end + 1
            n = fear[start]
        else: # 3-2. fear[end] 명 이상의 모험가로 그룹을 형성해야하는 경우
            n = fear[end]
        
        # 4. n <= end - start + 1 을 만족하는 최솟값 end 설정
        end = start + n - 1

    return group_cnt


n = int(input())
fear = list(map(int, input().split()))

print(solution(fear))