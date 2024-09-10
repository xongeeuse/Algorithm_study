import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs():
    while q:
        z, x, y = q.popleft()
        for dx, dy, dz in [[-1, 0, 0], [0, 1, 0], [1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:     # 범위 내의 값인데
                if not data[nz][nx][ny]:                        # 덜 익은 토마토라면
                    data[nz][nx][ny] = data[z][x][y] + 1        # 값 업데이트하고
                    q.append((nz, nx, ny))                      # 인큐



T = int(input())
for tc in range(1, T + 1):
    M, N, H = map(int, input().split())
    # 3차원 배열..?
    # 1: 익은 토마토, 0: 안 익은 토마토, -1: 토마토 없어요!
    data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    # visited = [[[0] * M for _ in range(N)] for _ in range(H)]     # 안 쓰고 원본 훼손
    q = deque()

    for z in range(H):
        for x in range(N):
            for y in range(M):
                if data[z][x][y] == 1:      # 익은 토마토면 다 인큐
                    q.append((z, x, y))

    bfs()

    result = 0
    is_complete = True
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if not data[z][x][y]:
                    is_complete = False
                result = max(result, data[z][x][y])


    if not is_complete:     # 덜 익은 토마토가 있다면
        print(-1)
    else:
        print(result - 1)   # 1부터 시작했으니까 -1 해주기