import sys
sys.stdin = open('input.txt')

from collections import deque

def solution(start):
    q = deque()
    q.append(start)
    visited[start] = 0                          # 시작점은 visited 0으로 설정

    while q:
        now = q.popleft()
        for v in adjL[now]:
            if visited[v] == -1:                # 아직 방문하지 않은 정점이면
                visited[v] = visited[now] + 1   # 거리 업데이트하고
                q.append(v)                     # 인큐



N = int(input())
a, b = map(int, input().split())
M = int(input())
adjL = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)            # a, b 접점이 없다면 -1 출력해야 하므로 [-1]로 visited 세팅

for _ in range(M):
    x, y = map(int, input().split())
    adjL[x].append(y)
    adjL[y].append(x)

solution(a)
print(visited[b])