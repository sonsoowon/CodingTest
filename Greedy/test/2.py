"""
11-2. 곱하기 혹은 더하기
숫자(0-9)로만 이루어진 문자열 S에 대하여 왼쪽부터 오른쪽으로 '+' 혹은 'x' 연산자를 넣어 만들 수 있는 최댓값을 구하라.
모든 연산은 왼쪽부터 순서대로 이루어진다.

INPUT
S (1 <= len(S) <= 20)

OUTPUT
만들어질 수 있는 가장 큰 수


풀이
0을 제외한 숫자를 최대한 많이 곱할수록 최댓값을 구할 수 있다.

왼쪽부터 숫자를 하나씩 접근할 때 현재 위치한 i (1 <= i) 번째 숫자에 대하여
(i - 1) 번째 숫자와 i번째 숫자 모두 0이 아닐 경우 곱하기 연산을 진행하고
0이 존재한다면 더하기 연산을 진행한다.


시간복잡도
길이가 N인 문자열 S에 대하여 O(N)

"""

def solution(S):
    s = list(map(int, list(S)))

    result = 0
    for num in s:
        result = result * num if result * num != 0 else result + num

    return result


s = input()

print(solution(s))