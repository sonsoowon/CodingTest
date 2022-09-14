"""
11-5. 볼링공 고르기
1부터 M까지의 무게를 가진 볼링공 N개에 대하여 서로 다른 무게 두 개로 조합하는 경우의 수를 구하라.
단, 무게가 같은 공이 여러 개라도 서로 다른 공으로 간주한다.

INPUT
N M
볼링공 무게 배열

OUTPUT
볼링공을 고르는 경우의 수


풀이
무게 배열을 오름차순으로 정렬한 후 각 무게 K에 대하여
K보다 큰 공의 개수 즉, K를 포함한 모든 가능한 조합의 수를 구한다.

시간복잡도
길이가 N인 볼링공 무게 배열에 대하여 O(N^2) -> 너무 비효율적이다

"""

def solution(weights):
    weights = sorted(weights)

    result = 0
    for w in weights:
        result += len([i for i in weights if i > w])
    
    return result

n, m = map(int, input().split())
weights = list(map(int, input().split()))

print(solution(weights))

