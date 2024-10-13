# 숨바꼭질 문제를 바탕으로 GPT 찬스. . .

import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start)

    visited = [False] * 200001  # 방문 여부를 확인할 배열을 초기화합니다.
    visited[start] = True  # 시작 위치를 방문 처리합니다.

    line = [0] * 200001  # 각 위치에 도달하는 데 걸린 시간을 기록할 배열을 초기화합니다.

    while queue:
        current = queue.popleft()  # 현재 위치를 큐에서 꺼냅니다.

        if current == end:
            return line[current]  # 목표 위치에 도달했으면, 그 위치에 기록된 시간을 반환합니다.

        for next in (current * 2, current - 1, current + 1):  # 순간이동, 좌우 걷기를 처리합니다.
            if 0 <= next <= 200000 and not visited[next]:  # 범위 내에 있고, 방문하지 않았다면
                if next == current * 2:  # 순간이동이라면
                    line[next] = line[current]  # 시간을 증가시키지 않습니다.
                else:  # 걷기라면
                    line[next] = line[current] + 1  # 시간을 1초 증가시킵니다.

                queue.append(next)  # 수정된 위치를 큐에 추가합니다.
                visited[next] = True  # 방문 처리를 합니다.

# 사용자 입력을 받습니다.
N, K = map(int, input().split())

# BFS 함수를 호출하고 결과를 출력합니다.
print(bfs(N, K))
