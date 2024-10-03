'''
달라진 점
벽을 K개까지 부술 수 있음!
1. broken에 부순 벽 개수 카운트하면서 진행 XXX
2. visited [0] * (K + 1)로 만들기? => 시간초과
'''

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
            # nx, ny가 길이 아니고, 아직 부순 벽의 개수가 K 이하라면
            if data[nx][ny] == '1' and broken < K:
                # nx, ny 좌표의 (broken + 1)번 인덱스(벽 부순다!)에 방문체크하고 거리 입력
                visited[nx][ny][broken + 1] = visited[x][y][broken] + 1
                # 인큐
                q.append((nx, ny, broken + 1))

            # nx, ny가 길이고, nx, ny를 부순 적이 없으면
            elif data[nx][ny] == '0' and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = visited[x][y][broken] + 1
                q.append((nx, ny, broken))

    return -1

N, M, K = map(int, input().split())
data = [list(input()) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

result = bfs(0, 0, 0)
# print(visited)
print(result)
