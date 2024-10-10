import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(i, j, color):
    global ally, enemy
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if data[nx][ny] != color or visited[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return cnt



N, M = map(int, input().split())
data = [input() for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ally, enemy = 0, 0

for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        if data[i][j] == 'W':
            ally += bfs(i, j, 'W') ** 2
        else:
        # elif data[i][j] == 'B': 와 동일
            enemy += bfs(i, j, 'B') ** 2

print(ally, enemy)