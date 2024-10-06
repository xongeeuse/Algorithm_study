import sys
input = sys.stdin.readline
from collections import deque

def my_bfs(i, j):
    global min_cnt
    queue.append([i, j, 1, K])  # 시작점 x좌표(0), y좌표(0), 경로 카운트(1), 벽을 부술 수 있는 남은 횟수(K)
    visited[i][j][K] = 1  # 벽을 부수지 않은 상태로 방문 처리

    while queue:
        x, y, cnt, block = queue.popleft()  # 현재 위치와 이동 거리, 벽을 부술 수 있는 기회 꺼냄

        if x == N - 1 and y == M - 1:  # 목적지에 도착하면
            min_cnt = min(min_cnt, cnt)  # 최소 경로를 갱신
            continue

        for dx, dy in dxy:  # 상하좌우 이동
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= M:  # 맵을 벗어나면 무시
                continue

            # 벽을 부수지 않고 이동할 수 있는 경우
            if map[nx][ny] == 0 and visited[nx][ny][block] == 0:
                visited[nx][ny][block] = 1  # 현재 벽을 부술 수 있는 상태로 방문 처리
                queue.append([nx, ny, cnt+1, block])

            # 벽을 부수고 이동해야 하는 경우 (벽을 부술 수 있는 기회가 남아있을 때)
            elif map[nx][ny] == 1 and block > 0 and visited[nx][ny][block - 1] == 0:
                visited[nx][ny][block - 1] = 1  # 벽을 부순 상태로 방문 처리
                queue.append([nx, ny, cnt+1, block-1])
    return

# 입력 처리
N, M, K = map(int, input().split())  # N: 맵의 행 수, M: 열 수, K: 벽을 부술 수 있는 최대 횟수
map = [list(map(int, input().strip())) for _ in range(N)]  # 맵을 입력받아 2차원 리스트로 저장
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 상하좌우 이동 방향
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]  # 방문 여부를 저장하는 3차원 리스트 (벽을 몇 개 부쉈는지에 따라 다르게 기록)
queue = deque()  # BFS에서 사용할 큐
min_cnt = N * M + 1  # 최단 경로를 기록할 변수, 매우 큰 값으로 시작

my_bfs(0, 0)  # (0, 0)에서 출발

# 결과 출력
if min_cnt == N * M + 1:  # 도착하지 못했으면
    print(-1)  # 불가능한 경우
else:
    print(min_cnt)  # 최단 경로 출력
