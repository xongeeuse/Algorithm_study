# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 모두 1이 되는 경우 찾기
from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def my_bfs():
    queue = deque()
    for h in range(H): # 한 층씩
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1: # 익은 토마토라면
                    queue.append([h, i, j])

    while queue:
        h, x, y = queue.popleft()
        for dh, dx, dy in dhxy:
            nh = h + dh
            nx = x + dx
            ny = y + dy

            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and arr[nh][nx][ny] == 0:
                arr[nh][nx][ny] = arr[h][x][y] + 1
                queue.append([nh, nx, ny])

def find_day():
    max_day = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0: # 안익은게 하나라도 있다면
                    return -1
                else:
                    if max_day < arr[h][i][j]:
                        max_day = arr[h][i][j]
    return max_day - 1

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dhxy = [[0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
my_bfs()
print(find_day())