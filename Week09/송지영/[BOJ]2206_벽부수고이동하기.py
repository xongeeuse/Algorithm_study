from collections import deque

def bfs(x, y, broken):
    q = deque()
    q.append((x, y, broken))

    while q:
        x, y, broken = q.popleft()
        if x == (N - 1) and y == (M - 1):
            return visited[x][y][broken]
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # nx, ny가 길이 아니고, 아직 부순 벽이 없으면
            if data[nx][ny] == '1' and not broken:
                # nx, ny 좌표의 1번 인덱스(벽 부순다!)에 방문체크하고 거리 입력
                visited[nx][ny][1] = visited[x][y][0] + 1
                # 인큐
                q.append((nx, ny, 1))

            # nx, ny가 길이고, nx, ny를 부순 적이 없으면
            elif data[nx][ny] == '0' and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = visited[x][y][broken] + 1
                q.append((nx, ny, broken))

    return -1

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

result = bfs(0, 0, 0)
# print(visited)
print(result)

