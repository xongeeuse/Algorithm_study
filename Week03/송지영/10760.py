import sys
sys.stdin = open('input.txt')

def search_landingspot(data):
    dxy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    result = 0

    for x in range(N):
        for y in range(M):
            cnt = 0
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M and data[x][y] > data[nx][ny]:
                    cnt += 1

                if cnt == 4 :
                    result += 1
                    break
    return result

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}', search_landingspot(data))