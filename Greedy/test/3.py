"""
11-3. 문자열 뒤집기
https://www.acmicpc.net/problem/1439

0과 1로만 이루어진 문자열 S에서 연속된 하나 이상의 숫자를 모두 뒤집을 수 있다.
S를 모두 같은 숫자로 뒤집을 수 있는 최소 횟수를 구하라.

INPUT
0과 1로만 이루어진 문자열 S (len(S) <= 1,000,000)

OUTPUT
뒤집는 최소 횟수


풀이
연속적인 숫자로 구성된 부분 문자열의 개수를 '0' 과 '1'에 대해 각각 구한 후, 더 적은 개수를 반환한다.
S의 모든 원소에 차례로 접근하여 '0'에서 '1', 혹은 '1'에서 '0'으로 변화할 때 각 부분 문자열의 개수를 갱신한다.

시간복잡도
길이가 N인 문자열 S에 대해 O(N)

"""


def solution(s):
    cnt = [0, 0]

    curr = s[0]
    cnt[int(curr)] +=1 

    for i in range(len(s)):
        if curr != s[i]:
            curr = s[i]
            cnt[int(curr)] += 1

    return min(cnt)

s = input()
print(solution(s))
