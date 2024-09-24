from collections import deque


def bfs(maps, start, end):
    rows, cols = len(maps), len(maps[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start])
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True
    distance = [[0] * cols for _ in range(rows)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return distance[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    return -1


def solution(maps):
    start, lever, end = None, None, None
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    to_lever = bfs(maps, start, lever)
    to_exit = bfs(maps, lever, end)

    if to_lever == -1 or to_exit == -1:
        return -1
    else:
        return to_lever + to_exit
