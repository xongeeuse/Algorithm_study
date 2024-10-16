from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 함수 정의
def bfs(x, y, team, visited, battlefield, w, h):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True  # 방문 처리
    count = 1  # 병사 수 카운트

    while queue:
        cur_x, cur_y = queue.popleft()

        # 4방향으로 탐색
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and battlefield[ny][nx] == team:
                visited[ny][nx] = True  # 방문 처리
                queue.append((nx, ny))
                count += 1  # 연결된 병사 수 카운트 증가

    return count  # 연결된 병사의 수 반환


# 입력 받기
w, h = map(int, input().split())  # 너비(w)와 높이(h) 입력
battlefield = [list(input()) for _ in range(h)]  # 전장 정보 입력

visited = [[False] * w for _ in range(h)]  # 방문 여부를 저장하는 배열
white_power = 0  # 흰색 팀의 전투력
blue_power = 0  # 파란색 팀의 전투력

# 전장 탐색
for y in range(h):
    for x in range(w):
        if not visited[y][x]:
            if battlefield[y][x] == 'W':  # 흰색 팀일 경우
                soldier_count = bfs(x, y, 'W', visited, battlefield, w, h)
                white_power += soldier_count * soldier_count  # 병사 수의 제곱만큼 전투력 추가
            elif battlefield[y][x] == 'B':  # 파란색 팀일 경우
                soldier_count = bfs(x, y, 'B', visited, battlefield, w, h)
                blue_power += soldier_count * soldier_count  # 병사 수의 제곱만큼 전투력 추가

# 결과 출력
print(white_power, blue_power)
