"""
3-2. 큰수의 법칙
크기 N의 배열의 원소를 M번 더하여 만들 수 있는 가장 큰 수를 구하라.
단, 같은 인덱스의 숫자를 연속으로 K(<= M) 번 초과하여 더할 수 는 없다.

INPUT
N M K
(2 <= N <= 1000, 
 1 <= M <= 10000, 
 1 <= K <= 10000)

N개의 자연수

OUTPUT
만들 수 있는 가장 큰 수


풀이
가장 큰 수를 만들기 위해선 배열의 가장 큰 수를 최대한 많이 더해야 한다.
1. 배열에서 가장 큰 수(first), 두번째로 큰 수(second)를 구한다
2. 1) first == second 인 경우 OUTPUT: first * M
   2) first != second 인 경우 총 M번을 더할 때까지 first를 연속으로 K번 더한 후 second를 1번 더하는 패턴을 반복한다.

시간복잡도
- 배열 정렬 O(NlogN)
"""

N, M, K = map(int, input().split())
arr = map(int, input().split())

def solution(arr, M, K):
    asec_arr = sorted(arr) # O(NlogN)
    first, second = asec_arr[-1], asec_arr[-2]
    
    if first == second:
        return first * M

    return (first * K + second) * (M // (K + 1)) + first * (M % (K + 1)) # O(1) -> while 대신 한번의 연산으로 결과를 도출할 수 있다


print(solution(arr, M, K))
