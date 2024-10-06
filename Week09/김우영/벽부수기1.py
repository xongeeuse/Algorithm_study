import sys
input = sys.stdin.readline
from collections import deque

def my_bfs(i, j):
    global min_cnt
    queue.append([i, j, 1, 1]) # 시작점 x좌표(0), 시작점 y좌표(0), 경로 카운트, 벽을 부술 수 있는 횟수
    visited[i][j][1] = 1 # 벽을 부수지 않은 상태로 방문 처리

    while queue:
        x, y, cnt, block = queue.popleft()

        if x == N -1 and y == M - 1:
            min_cnt = min(min_cnt, cnt)
            continue

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 벽을 부수지 않고 이동할 수 있는 경우
            if map[nx][ny] == 0 and visited[nx][ny][block] == 0:
                visited[nx][ny][block] = 1 # 벽을 부수지 않고 방문처리
                queue.append([nx, ny, cnt+1, block])

            # 벽을 부수고 이동해야 하는 경우
            elif map[nx][ny] == 1 and block == 1 and visited[nx][ny][0] == 0:
                visited[nx][ny][0] = 1
                queue.append([nx, ny, cnt+1, 0])
    return
        

N, M = map(int, input().split())

map = [list(map(int, input().strip())) for _ in range(N)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 벽을 부순 상태와 아닌 상태로 나눠 방문여부 체크
# visited[i][j] ->  [벽을 부순 경우, 벽을 부수지 않은 경우]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] 
queue = deque()
min_cnt = N * M + 1 # map 범위 내에서 경로로 나올 수 있는 가장 큰 값

my_bfs(0,0)

if min_cnt == N * M + 1:
    print(-1)
else:
    print(min_cnt)