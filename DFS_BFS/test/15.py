"""
13-15. 특정 거리의 도시 찾기 (1시간 15분)

- 시간초과가 자꾸 뜬다
알고리즘의 문제가 아니라면 입출력의 문제일까?
sys.stdin.readline().rstrip().split()
https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

- TypeError 런타임 에러 문제
출력을 result 리스트 혹은 -1 정수 두가지로 설정해서 문제
-1은 반복 가능한 iterator 자료형이 아니므로 결과 출력할 때 에러 발생

- 알고리즘의 허점
방문하지 않았음을 0이 아닌 -1로 표기해야한다
사이클이 발생해 자기 자신으로 돌아오는 경우 길이가 0으로 초기화되는데, x에서 출발해 어떤 도시를 거쳐 다시 x로 돌아올 때,
dist[x] == 0을 방문하지 않았음으로 간주하면 출발지의 거리가 0이 아닌 다른 값으로 설정되므로 최소 거리를 구할 수 없다.
-1을 방문하지 않았다는 것으로 간주해야 0인 시작점을 거쳤음을 알 수 있다


벨로그 정리하기
"""

from collections import deque
import sys

def solution(edges, n, k, x):
    dist = [-1 for _ in range(n + 1)]
    q = deque([x])
    dist[x] = 0

    result = []
    while q:
        curr = q.popleft()
        if dist[curr] == k:
            result.append(curr)
        
        for next in edges[curr]:
            if dist[next] == -1:
                dist[next] = dist[curr] + 1
                q.append(next)
        
    return sorted(result) if result else [-1]

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    edges[s].append(e)

for c in solution(edges, n, k, x):
    print(c)