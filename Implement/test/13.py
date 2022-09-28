"""
12-13. 치킨 배달 (30분)
https://www.acmicpc.net/problem/15686


풀이과정

치킨집 k개에서 m개만 선택 -> k_C_m 가지 조합 (1 <= m <= k <=13)
: itertools의 combinations 사용하기

1. 각 치킨집 조합에 대해 특정 집의 위치가 주어졌을 때 치킨 거리 구하는 함수 chicken_distance
  : abs(chicken_r - home_r) + abs(chicken_c - home_c) 연산을 map으로 배열의 모든 원소에 적용
    하지만 괄호 중첩이 너무 많아지는게 보기 좋지 않아서 리스트 컴프리헨션으로 대체

2. 모든 집에 대해 chicken_distance 함수 적용해 치킨 거리 구하고 도시 치킨 거리 구하는 함수 city_chicken_distance

3. 모든 치킨집 조합에 대해 도시 치킨 거리 도출하고 거기서 min으로 최소값 구하기


시간복잡도
집의 최대 개수: 100
치킨집 조합의 최대 개수: 13_C_7 (< 2000)
약 2,000,000 이내의 연산 진행 -> 제한 시간 이내 해결 가능

"""

from itertools import combinations

def get_pos(matrix, a):
    pos = []
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item == a:
                pos.append([i, j])

    return pos 


def chicken_distance(chickens, home): 
    return min([abs(chicken[0] - home[0]) + abs(chicken[1] - home[1]) for chicken in chickens])

def city_chicken_distance(chickens, homes):
    return sum([chicken_distance(chickens, home) for home in homes])

def solution(matrix, m): 
    homes = get_pos(matrix, 1)
    chickens = get_pos(matrix, 2)
    return min([city_chicken_distance(comb, homes) for comb in combinations(chickens, m)])

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]



print(solution(matrix, m))