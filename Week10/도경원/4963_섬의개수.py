from collections import deque
import sys
sys.stdin = open("input.txt", "r")

# 방향 벡터 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(x, y, w, h, square_map):
    queue = deque()
    queue.append((x, y))
    square_map[y][x] = 0  # 방문한 곳은 0으로 변경 (방문 처리)

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(8):  # 8방향 탐색
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and square_map[ny][nx] == 1:
                square_map[ny][nx] = 0  # 방문 처리
                queue.append((nx, ny))  # 큐에 다음 위치 추가


while True:
    w, h = map(int, input().split())  # 지도의 너비와 높이 입력
    if w == 0 and h == 0:  # 너비와 높이가 0인 경우 종료
        break

    square_map = [list(map(int, input().split())) for _ in range(h)]  # 지도 입력

    count = 0  # 섬의 개수를 셀 변수

    for y in range(h):
        for x in range(w):
            if square_map[y][x] == 1:  # 섬을 발견하면
                bfs(x, y, w, h, square_map)  # BFS로 섬을 탐색
                count += 1  # 섬의 개수 증가

    print(count)  # 섬의 개수 출력
