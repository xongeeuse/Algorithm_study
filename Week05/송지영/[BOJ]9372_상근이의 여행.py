# import sys
# sys.stdin = open('input.txt')

from collections import deque

def bfs(start, cnt):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        if visited.count(1) == N:
            return cnt

        v = q.popleft()

        for x in adjL[v]:
            if not visited[x]:
                q.append(x)
                cnt += 1
                visited[x] = 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # data = [list(map(int, input().split())) for _ in range(M)]
    visited = [0] * (N + 1)
    adjL = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        adjL[a].append(b)
        adjL[b].append(a)
    print(bfs(1, 0))


# 이거라고?
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(M)]
#     result = N - 1
#     print(result)
