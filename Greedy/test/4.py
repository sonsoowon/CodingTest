"""
11-4. 만들 수 없는 금액


만들 수 없는 금액이라는 판단은 어떻게?
다 만들고 판단하기엔 너무 오래 걸려

n개의 조합으로 숫자를 더할 때, 만들 수 있는 수의 최솟값이 찾고 있는 최소 수보다 클 때 만들 수 없음을 결론 짓는다
이전 단계에서도 최솟값이 찾는 수보다 작지만 찾는게 존재하지 않는 경우도 있을까?

a1 a2 a3 ... aN

aK-1 < min < aK



1. n(> 2)개의 동전으로 만들 수 있는 금액을 모두 더한다
2. 이전까지 만든 리스트에서 존재하지 않는 자연수 중 최소값을 min이라 할 때, min이 1번에서 만든 리스트에 존재하는지 확인
3. 

1 1 2 4

2 3 5 6



1 1 2 3 9
4 10 5 11 12
6 13 14
7 15

1 2 3 4 5 6 7 9 10 11 12 13 14 15
"""

from itertools import combinations

ex = [1, 1, 2, 3, 9]
result = ex
min = 0

for n in range(2, len(ex) + 1):
    for i in range(len(result) - 1):
        if result[i + 1] > result[i] + 1:
            min = result[i] + 1
    
    if sum(ex[:n]) > min:
        print(min)
        break

    result = set(result).union([sum(comb) for comb in combinations(ex, n) if sum(comb) >= min])

    result = list(result)
    
    result.sort()

print(result)