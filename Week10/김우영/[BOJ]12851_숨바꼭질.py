import sys
input = sys.stdin.readline

from collections import deque

def my_bfs(start, end):
    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.popleft()

        if current == end:
            return visited[end]

        for next in (current - 1, current + 1, current * 2):

            if next < 0 or next >= 200001 or visited[next] != -1:
                continue

            queue.append(next)
            visited[next] = visited[current] + 1

N, K = map(int, input().split())
visited = [-1] * 200001 # if 100000을 기준으로 탐색해야 한다고 했을 때 100000 * 2 까지 탐색하기 위해
queue = deque()

print(my_bfs(N, K))

# 예제 입력 기준으로 4가 출력되는 방식
# 0: 5
# 1: 4 10 11
# 2: 3 8/ 9 20/ 12 22
# 3: 2 6/ 7 16/ 10 18/ 19 21 40/ 13 24/ 21 23 44
# 4: 1 / / 14/ 15 17 -> return