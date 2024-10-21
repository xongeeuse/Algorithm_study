from collections import deque

import sys
input = sys.stdin.readline

def my_bfs(i, j):
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if visited[nx][ny] == 1 or my_map[nx][ny] == 0:
                continue

            queue.append([nx, ny])
            visited[nx][ny] = 1


queue = deque()
dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    my_map = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * (w) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if my_map[i][j] == 1 and visited[i][j] == 0:
                my_bfs(i, j)
                cnt += 1
    print(cnt)