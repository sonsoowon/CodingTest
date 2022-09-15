"""
4-3. 게임 개발
N x M 의 좌표평면에서 각각의 칸은 육지 또는 바다이며 캐릭터는 다음 규칙에 따라 움직인다.
  1. 현재 위치에서 현재 방향을 기준으로 왼쪽으로 회전한다.
  2. 회전한 방향에 가보지 않은 육지가 존재한다면 해당 방향으로 한 칸 전진, 없다면 회전만 수행하고 1단계로 돌아간다.
  3. 네 방향 모두 전진할 수 없는 상태라면 바라보는 방향에서 한 칸 뒤로 가고 1단계로 돌아간다.
     단, 뒤쪽 방향이 바다인 경우 움직임을 멈춘다.
캐릭터가 방문한 칸의 수를 구하라.
(시간 제한: 1초 / 메모리 제한: 128MB)

INPUT
N M (3 <= N, M <= 50)
x y(현재 좌표) d(현재 방향: 북0 동1 남2 서3)
지도 matrix

OUTPUT
캐릭터가 방문한 칸의 수


풀이
규칙을 그대로 따라가며 구현한다.

시간 복잡도
O(NM)

"""

def solution(matrix, s_row, s_col, s_d):
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    r, c, d = s_row, s_col, s_d
    visited = 0

    while True:
        turns = 0
        for _ in range(4):
            # 왼쪽으로 회전
            d = (d + 1) % 4

            step = steps[d]
            nr, nc = r + step[0], c + step[1]

            # 방문하지 않은 육지인 경우 이동
            if matrix[nr][nc] == 0:
                r, c = nr, nc
                matrix[r][c] = 2 # 방문 표시
                visited += 1
                break
            
            turns += 1
        
        # 네 방향 모두 갈 수 없는 경우
        if turns == 4:
            back_step = steps[(d + 2) % 4]
            r, c = r + back_step[0], c + back_step[1]

            # 뒤가 바다라면 종료한다
            if matrix[r][c] == 1:
                break

    return visited


n, m = map(int, input().split())
row, col, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(solution(matrix, row, col, d))