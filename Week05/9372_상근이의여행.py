# N: 국가의 수, M: 비행기의 종류
# a, b는 해당 지역을 왕복하는 비행기가 있다는 것을 의미
# a, b는 항상 연결 그래프
# 상근이가 모든 국가를 여행하기 위해 타야하는 비행기 종류의 최소 개수는?
def my_dfs(node, cnt): # cnt는 몇 번 비행기 탔는지 세기 위한 것 0부터 시작
    # 첫 들어온 것을 방문 처리
    visited[node] = 1
    # cnt 증가
    cnt += 1
    for i in adjL[node]: # 인접 검사
        if visited[i] == 0: # 방문하지 않았다면
            cnt += 1
            my_dfs(i, cnt)
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        adjL[a].append(b)
        adjL[b].append(a)
    print(my_dfs(1, 0))


# def dfs(node, cnt):
#     visit[node] = 1
#     for i in Tree[node]:
#         if visit[i] == 0:
#             cnt = dfs(i, cnt + 1)
#     return cnt
#
#
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     Tree = [[] for _ in range(N + 1)]
#
#     for _ in range(M):
#         u, v = map(int, input().split())
#         Tree[u].append(v)
#         Tree[v].append(u)
#
#     visit = [0] * (N + 1)
#     visit[1] = 0
#     result = dfs(1, 0)
#     print(result)