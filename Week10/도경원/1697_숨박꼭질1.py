from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")


def bfs(start, target):
    max_limit = 100001  # 수빈 or 동생 위치의 최대점
    visited = [0] * max_limit
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == target:  # 종료 조건, 즉 수빈이가 동생을 찾았을 때
            return visited[current]  # 지금 위치를 인덱스로 하여 visited 리스트 값 반환함
        for next_position in (current - 1, current + 1, current * 2):  # 다음 위치가 걷을 때(-1, +1) 혹은 순간이동 할 때(*2)
            if 0 <= next_position < max_limit and not visited[next_position]:  # 범위안에 들고 방문하지 않았다면
                visited[next_position] = visited[current] + 1  # visited 리스트의 위치를 인덱스로 하여 카운트함
                queue.append(next_position)


S, D = map(int, input().split())  # 수빈, 동생 위치 입력
result = bfs(S, D)
print(result)