"""
13-3. 음료수 얼리기
stack, recursion 두가지 방법으로 DFS를 구현해보자

시간복잡도 O(MN)
"""

def dfs_stack(matrix, x, y):
    n, m = len(matrix), len(matrix[0])

    if matrix[x][y] == 1:
        return 0
    
    stack = [[x, y]]
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 0:
                stack.append([nr, nc])
                matrix[nr][nc] = 1
    
    return 1

def dfs_recursion(matrix, x, y):
    n, m = len(matrix), len(matrix[0])

    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        dfs_recursion(matrix, x + 1, y)
        dfs_recursion(matrix, x, y + 1)
        dfs_recursion(matrix, x - 1, y)
        dfs_recursion(matrix, x, y - 1)
        return 1

    return 0

    

def solution(matrix, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            #count += dfs_stack(matrix, i, j)
            count += dfs_recursion(matrix, i, j)
            
    return count

n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]

print(solution(matrix, n, m))


