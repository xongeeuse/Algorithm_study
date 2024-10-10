import sys
sys.stdin = open('input.txt')

# YES함수 ver. (76ms)
from collections import deque

def bfs(i, j):
    global result

    result += 1

    q = deque()
    q.append((i, j))
    visited[i][j] = result

    while q:
        x, y = q.popleft()
        # 대각선까지 8방향 델타 탐색
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:  # 범위 벗어나면 패스
                continue
            if not data[nx][ny] or visited[nx][ny]:  # 땅이 아니거나 방문한 곳이면 패스
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y]



while True:
    W, H = map(int, input().split())    # 지도의 너비 W, 높이 H

    # 탈출 조건 : 입력이 0, 0이면 종료
    if W == 0 and H == 0:
        break

    data = [list(map(int, input().split())) for _ in range(H)]      # 1: 땅, 0: 바다
    visited = [[0] * W for _ in range(H)]

    result = 0      # 섬의 개수 초기화

    # land = deque()
    for i in range(H):
        for j in range(W):
            # 현위치가 땅이고 방문 전이라면 bfs함수 호출
            if data[i][j] and not visited[i][j]:
                bfs(i, j)

    print(result)






# # NO 함수 ver. (88ms)
# from collections import deque
#
# while True:
#     W, H = map(int, input().split())    # 지도의 너비 W, 높이 H
#
#     # 탈출 조건 : 입력이 0, 0이면 종료
#     if W == 0 and H == 0:
#         break
#
#     data = [list(map(int, input().split())) for _ in range(H)]      # 1: 땅, 0: 바다
#     visited = [[0] * W for _ in range(H)]
#
#     result = 0      # 섬의 개수 초기화
#
#     land = deque()
#     for i in range(H):
#         for j in range(W):
#             if data[i][j]:
#                 land.append((i, j))
#
#     while land:
#         i, j = land.popleft()
#         if visited[i][j]:       # 이미 방문한 땅이면 패스
#             continue
#         result += 1
#         visited[i][j] = result
#
#         q = deque()
#         q.append((i, j))
#
#         while q:
#             x, y = q.popleft()
#             # 대각선까지 8방향 델타 탐색
#             for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
#                 nx, ny = x + dx, y + dy
#                 if nx < 0 or nx >= H or ny < 0 or ny >= W:      # 범위 벗어나면 패스
#                     continue
#                 if not data[nx][ny] or visited[nx][ny]:         # 땅이 아니거나 방문한 곳이면 패스
#                     continue
#                 q.append((nx, ny))
#                 visited[nx][ny] = visited[x][y]
#
#     print(result)

