import sys
input = sys.stdin.readline

from collections import deque

power_W, power_B = 0, 0

def my_bfs_W(i, j):
    queue.append([i, j])
    visited[i][j] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if visited[nx][ny] == 1 or my_li[nx][ny] == 'B':
                continue

            queue.append([nx, ny])
            visited[nx][ny] = 1
            cnt += 1

    return cnt * cnt


def my_bfs_B(i, j):
    queue.append([i, j])
    visited[i][j] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if visited[nx][ny] == 1 or my_li[nx][ny] == 'W':
                continue

            queue.append([nx, ny])
            visited[nx][ny] = 1
            cnt += 1

    return cnt * cnt


N, M = map(int, input().split())
my_li = [list(input()) for _ in range(M)]

visited = [[0] * (N) for _ in range(M)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
queue = deque()


for i in range(M):
    for j in range(N):
        if my_li[i][j] == 'W' and visited[i][j] == 0:
            power_W += my_bfs_W(i, j)
        if my_li[i][j] == 'B' and visited[i][j] == 0:
            power_B += my_bfs_B(i, j)
print(power_W, power_B)