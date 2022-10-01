"""
13-4. 미로 탈출
BFS를 queue를 이용해 구현하자

"""

from collections import deque

def bfs(maze):
    n, m = len(maze), len(maze[0])
    
    q = deque([[0, 0]])
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    while q:
        r, c = q.popleft()
        
        if maze[r][c]:
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == 1:
                    maze[nr][nc] = maze[r][c] + 1 # 최단 경로의 길이를 구하는 방법!!
                    q.append([nr, nc])
    
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

print(bfs(maze))