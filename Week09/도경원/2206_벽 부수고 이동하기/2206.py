from collections import deque

# 입력 받기
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 배열 (3차원: x, y, 벽을 부쉈는지 여부)
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


# BFS 시작
def bfs():
    queue = deque([(0, 0, 0)])  # (x, y, 벽을 부쉈는지 여부)
    visited[0][0][0] = 1  # 시작점 방문 표시 (벽을 부수지 않은 상태)

    while queue:
        x, y, wall_broken = queue.popleft()

        # 도착지에 도달하면 리턴
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall_broken]

        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 만나지 않았고, 방문하지 않은 경우
                if graph[nx][ny] == 0 and visited[nx][ny][wall_broken] == 0:
                    visited[nx][ny][wall_broken] = visited[x][y][wall_broken] + 1
                    queue.append((nx, ny, wall_broken))

                # 벽을 만났고, 아직 벽을 부순 적이 없는 경우
                elif graph[nx][ny] == 1 and wall_broken == 0:
                    visited[nx][ny][1] = visited[x][y][wall_broken] + 1
                    queue.append((nx, ny, 1))

    return -1  # 도착할 수 없을 때

# 결과 출력
print(bfs())
