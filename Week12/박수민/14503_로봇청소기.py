# 14503 로봇청소기
import sys
input =sys.stdin.readline

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

N, M = map(int, input().split())

# 처음에 로봇청소기가 있는 칸의 좌표(r,c)와 로봇청소기가 바로보는 방향 d
r, c, d = map(int, input().split())

# 0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽
# direction = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
dirs = [[-1,0],[0,1],[1,0],[0,-1]]

room = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

'''
0은 청소되지 않은 빈칸. 
1은 벽이 있는 것
방의 가장자리 모든 칸에는 벽이 있다. 
로봇청소기가 작동 시작후 작동 멈출 때까지 청소하는 칸의 개수 구하기
'''

# x, y은 현재 위치, d는 현재 방향
def clean(x, y ,d):
    cnt = 0
    while True:
        # 현재 위치 청소
        room[x][y] = 1
        cnt += 1
        for i in range(4):
            d = direction[i]
            nx, ny = x + d[0], y + d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if room[nx][ny] == 0:
                clean(nx, ny, )


    # if room[x][y] == 0 and not visited[x][y]:
    #     room[x][y] = 1
    #     visited[x][y] = 1
    #     cnt += 1