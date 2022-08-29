"""
3-3. 숫자 카드 게임
어느 한 행에서 뽑은 가장 작은 숫자 카드가, 다른 행에서 뽑은 가장 작은 숫자 카드들 중에 가장 큰 숫자 카드여야 한다.

INPUT
N, M
N x M 의 행렬

OUTPUT
게임 규칙을 만족하는 가장 큰 수


풀이
각 행의 가장 작은 수를 찾은 뒤 그 중에서 가장 큰 수를 반환한다
min(list), max(list) 활용


시간복잡도
- matrix의 각 행에 대한 min 연산: O(NM)

"""

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def solution(matrix):
    min_list = [min(row) for row in matrix] # min(row): O(M)

    return max(min_list) # O(N)

print(solution(matrix))