import sys
sys.stdin = open('input.txt')

# def shortest_route(adjL, start):
#     visited = [0] * (N + 1)
#     pass
#
#
# # 인접리스트 이용
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     adjL = [[] for _ in range(N + 1)]
#     result = float('inf')
#
#     for i in range(M):
#         a, b = map(int, input().split())
#         adjL[a].append(b)
#         adjL[b].append(a)
#
#     for i in range(1, N + 1):
#         shortest_route(adjL, i)
#
#     print(result)


# 이거라고?
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    result = N - 1
    print(result)