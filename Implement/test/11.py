"""
12-11. 뱀 (2시간)
https://www.acmicpc.net/problem/3190

시간복잡도
X의 최댓값 10,000초까지 살아서 10,000초에서 방향을 바꾸고 이때 제일 모서리에 있으면, 
(10,000 + N)초 뒤에 게임이 종료되는것이 최악의 상황이다: O(max(X) + N)

"""

from collections import deque

def make_board(n, apples):
    matrix = [[1] * (n + 2)]
    matrix += [[1] + [0] * n + [1] for _ in range(n)]
    matrix += [[1] * (n + 2)]

    for r, c in apples:
        matrix[r][c] = 4
        
    return matrix


def solution(n, apples, turns):
    # 보드 초기화
    board = make_board(n, apples)
    
    # 뱀 위치 배열 (head = snake[0], tail = snake[-1])
    """
    TIL 1. deque를 활용하자: appendleft(item) -> O(1) / pop() -> O(1)
        snake.insert(0, head) 로 머리 이동, snake.pop()으로 꼬리 이동 가능
        BUT, insert는 시간복잡도가 O(N)이니 리스트 대신 다른 자료구조를 사용하자 !!
    """
    snake = deque([(1, 1)])
    
    # 이동 방향
    d = 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    nr, nc = dr[d], dc[d]
    
    # 회전 시간 및 방향 배열 분리
    turns = sorted(turns, key=lambda x: -x[0])

    """
    TIL 2. zip으로 튜플 원소를 별도의 리스트로 분리하기
        zip(turns)대신 zip(*turns)를 사용해야
        ValueError: too many values to unpack (expected 2) 가 뜨지 않는다
    """
    turn_sec, turn_d = map(list, zip(*turns))
    turn_sec = list(map(int, turn_sec))
    
    sec = 0
    while True:
        sec += 1
        
        # 1. 머리 한칸 이동
        hr, hc = snake[0][0] + nr, snake[0][1] + nc
        snake.appendleft((hr, hc))
        
        # 2. 벽 혹은 자신과 부딪혔을 때 이동 종료
        if board[hr][hc] == 1:
            break
            
        # 3. 사과가 없을 때 꼬리 이동 
        # 꼬리랑 부딪힐 수 있으므로 2번에서 이동 종료 여부를 확인한 후 3번을 수행한다
        if board[hr][hc] != 4:
            tr, tc = snake.pop()
            board[tr][tc] = 0
        
        board[hr][hc] = 1
        
        # 4. sec 초가 지난 후 회전 여부 확인
        if len(turn_sec) and sec == turn_sec[-1]:
            turn_sec.pop()
            turn = turn_d.pop()
            d = (d + 1) % 4 if turn == 'D' else (d + 3) % 4 
            nr, nc = dr[d], dc[d] 

    
    return sec


n = int(input())

apple_num = int(input())
apples = [map(int, input().split()) for _ in range(apple_num)]

turn_num = int(input())
turns = list(map(lambda x: (int(x[0]), x[1]), [input().split() for _ in range(turn_num)]))

print(solution(n, apples, turns))