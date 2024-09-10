'''
map = [[1, 0, 1, 1, 1],
       [1, 0, 1, 0, 1],
       [1, 0, 1, 1, 1],
       [1, 1, 1, 0, 0],
       [0, 0, 0, 0, 1]]
       '''

from collections import deque

def solution(maps):
    # 상하좌우로 움직일 때의 좌표 변화 (위, 아래, 왼쪽, 오른쪽)
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # x, y 좌표에서 탐색
    def bfs(x, y):
        # deque를 생성하고 초기값으로 시작 좌표 0, 0
        deq = deque()
        deq.append((x, y))

        # 탐색할 좌표가 없을 때까지 반복
        while deq:
            # deque의 앞에서 좌표를 하나 꺼냄
            x, y = deq.popleft()

            # 상하좌우로 움직일 수 있는지 확인, 델타 탐색
            for i in range(4):
                nx = x + dxy[i][0]  # 새로운 x 좌표
                ny = y + dxy[i][1]  # 새로운 y 좌표

                # 새로운 좌표가 맵의 범위 안에 있고, 이동할 수 있는 곳(1)인지 확인
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                    # 그 위치로 이동할 수 있다면, 해당 좌표를 현재 위치에서 1만큼 더한 값으로
                    maps[nx][ny] = maps[x][y] + 1
                    # 이동할 수 있는 새로운 좌표를 deque에 추가
                    deq.append((nx, ny))

        # 마지막 목적지에 도달했을 때의 값을 반환
        # maps[len(maps) - 1][len(maps[0]) - 1]은 맵 끝 좌표
        return maps[len(maps) - 1][len(maps[0]) - 1]

    # BFS를 실행하여 (0, 0)에서 출발한 결과를 answer에 저장
    answer = bfs(0, 0)

    # 만약 목적지의 값이 1이라면 도달할 수 없다는 뜻이므로 -1을 반환
    return -1 if answer == 1 else answer