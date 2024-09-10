import sys
sys.stdin = open('input.txt')

# 안 익은 토마토 몇 개?
def rare_tomato():
    rare = 0
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if not data[z][x][y]:
                    rare += 1
    return rare


def tomato(data):
    global cnt
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    cnt = 0                 # 해당 일차에 변경되는 토마토의 개수

    for z in range(H):
        for x in range(N):
            for y in range(M):
                # 익은 토마토인데 해당 일차에 익은 게 아니라면?
                if data[z][x][y] == 1 and not visited[z][x][y]:
                    # 위 아래 층의 토마토 상태 변경(있는지 인덱스 확인)
                    if 0 <= z - 1 < H and not data[z - 1][x][y]:
                        data[z - 1][x][y] = 1
                        cnt += 1
                    if 0 <= z + 1 < H and not data[z + 1][x][y]:
                        data[z + 1][x][y] = 1
                        cnt += 1

                    # 동일 층 내의 상하좌우 토마토 상태 변경
                    for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and not data[z][nx][ny]:
                            visited[z][nx][ny] = 1
                            data[z][nx][ny] = 1
                            cnt += 1



T = int(input())
for tc in range(1, T + 1):
    M, N, H = map(int, input().split())
    # 3차원 배열..?
    # 1: 익은 토마토, 0: 안 익은 토마토, -1: 토마토 없어요!
    data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    rare = rare_tomato()
    result = -1

    '''
    while문으로
    day 늘려가면서 진행
    함수 한 바퀴 도는데 상태 변하는 토마토가 없다면(cnt == 0) 종료
    토마토 다 익었으면(rare == 0) 종료
    토마토가 모두 익지 못하는 상황이면(rare != 0 and cnt == 0) -1 출력
    '''

    if rare == 0:
        result = 0

    day, cnt = 0, 0
    while rare:
        day += 1
        tomato(data)

        if cnt == 0:            # 하루 동안 익은 토마토가 없다면 종료
            break
        if rare - cnt == 0:     # 더 이상 덜 익은 토마토가 없다면
            result = day        # 결과에 day값 할당하고 종료
            break

        rare -= cnt             # 아직 남아 있다면 rare값 갱신하고 계속 반복

    print(f'#{tc}', result)