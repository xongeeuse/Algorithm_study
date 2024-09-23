# 테스트 10 〉 실패 (0.02ms, 10.2MB)
# 합계: 95.7 / 100.0


'''
S : 시작 지점, E : 출구, L : 레버, O : 통로, X : 벽

미로 문제랑 똑같이 푸는데 레버 위치를 경유지로 생각
1. 시작 지점 ~ 레버
2. 레버 ~ 출구
나눠서 최소경로 계산 후 합산
'''


from collections import deque

def find_start(N, M, maps):
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                return i, j

def solution(maps):
    answer = 0
    N, M = len(maps), len(maps[0])
    visited = [[-1] * M for _ in range(N)]
    visited_2nd = [[-1] * M for _ in range(N)]

    # 시작점, 좌표 찾기
    i, j = find_start(N, M, maps)

    # 시작점부터 레버까지 최소 거리 찾기
    q = deque()
    q.append((i, j))
    visited[i][j] = 0

    while q:
        x, y = q.popleft()

        # 현재 탐색 위치가 레버라면 정답에 현재까지 최소 거리 더해주고 반복문 종료
        if maps[x][y] == 'L':
            answer += visited[x][y]
            i, j = x, y
            break

        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            # 범위 밖이면 패스
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽이거나 이미 방문한 지점이면 패스
            if maps[nx][ny] == 'X' or visited[nx][ny] != -1:
                continue
            # 유효한 지점이라면 거리 업데이트 후 인큐
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

    # 테케 10번 틀려서 추가한 부분
    # 레버까지 도착 못해도 -1 리턴해야 함
    if answer == 0:
        return -1

    # 레버를 시작점으로 다시 탐색 시작
    q = deque()
    q.append((i, j))
    visited_2nd[i][j] = 0

    while q:
        x, y = q.popleft()
        # 도착했다면 answer에 저장된 레버까지의 최소 거리와 합산해서 리턴
        if maps[x][y] == 'E':
            answer += visited_2nd[x][y]
            return answer

        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maps[nx][ny] == 'X' or visited_2nd[nx][ny] != -1:
                continue
            visited_2nd[nx][ny] = visited_2nd[x][y] + 1
            q.append((nx, ny))

    # 도착 못했다면
    return -1

# 출력
maps_list=[["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"],
           ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]]

for maps in maps_list:
    print(solution(maps))