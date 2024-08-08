import sys
sys.stdin = open('input.txt')

T = int(input())
dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(N, M)
    max_bomb = 0
    for i in range(N):
        for j in range(M):
            bomb = arr[i][j]
            for di, dj in dij:
                for k in range(1, arr[i][j] + 1):
                    ni = i + di * k
                    nj = j + dj * k
                    if 0 <= ni < N and 0 <= nj < M:
                        bomb += arr[ni][nj]
                if max_bomb < bomb:
                    max_bomb = bomb
    print(f'#{tc} {max_bomb}')
