"""
4-2. 왕실의 나이트
8x8의 좌표평면에서 나이트는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
나이트의 현재 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 구하라.
행은 1-8, 열은 a-h로 표현한다.
(시간 제한: 1초 / 메모리 제한: 128MB)

INPUT
나이트의 현재 위치를 나타내는 문자열 (ex. a1)

OUTPUT
나이트가 이동할 수 있는 경우의 수


풀이
L자 형태로 이동하는 유형은 총 8가지이므로 각 경우에 대해 정원을 벗어나는지 확인한다.

시간 복잡도
8번의 연산만 진행하므로 O(1)


* ord() && char()
- ord('a') => 64
- char(64) => 'a'

"""


def solution(curr):
    row = int(curr[1])
    col = ord(curr[0]) - ord('a') + 1
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    result = 0
    for m in moves:
        if 1 <= row + m[0] <= 8 and 1 <= col + m[1] <= 8:
            result += 1
    
    return result

curr = input()
print(solution(curr))
