'''
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

익은 토마토는 1, 익지 않은 토마토는 0, 토마토가 없는 칸은 -1
'''


import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())    # 가로, 세로, 높이
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M] * N] * H       # 방문 기록을 저장하는 3차원 배열

# 상하좌우칸이동
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

deq = deque()

# 익은 토마토 찾기
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                # 찾은 좌표를 deq에 추가하고 방문표시
                deq.append((h, n, m))
                visited[h][n][m] = True

# bfs 탐색 시작
while deq:
    z, x, y = deq.popleft()     #높이 세로 가로

    for i in range(6):
        nz = dz[i] + z      # 칸 이동
        nx = dx[i] + x      # 상 하
        ny = dy[i] + y      # 좌 우

        # 상자 범위 내에 있는 지 확인 후 익지 않은 토마토가 있으면 +1 을 해서 익힘
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                deq.append((nz, nx, ny))
        '''
        [[[0, -1, 3, 2, 2], 
         [-1, -1, 2, 1, 1], 
          [4, 3, 2, 1, 1]]]
        '''

result = 0      # 최종 날짜
flag = True     # 익지 않은 토마토가 있는 지 여부를 확인할 flag

# 상자 전체 순회
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 0:       # 익지 않은 토마토가 있을 경우 flag를 False로 변경
                flag = False
            result = max(box[z][x][y], result)      # 가장 큰 날짜(마지막으로 익은 토마토 날짜)를 저장

# flag가 True인 경우 result - 1 출력
if flag:
    print(result - 1)       # 익은 토마토가 처음부터 1로 표시 되기 때문에 - 1 해줌
else:
    print(-1)