import sys
sys.stdin = open("input.txt", "r")


def dfs(s, e, cnt):
    v[s] = 1
    if s == e:
        return cnt

    for i in adj[s]:
        if v[i] == 0:
            v[i] = 1
            result = dfs(i, e, cnt + 1)
            if result != -1:
                return result
    return -1


n = int(input())  # 전체 사람의 수 입력(정점의 수)
p1, p2 = map(int, input().split())  # 촌수를 계산해야 하는 서로 다른 두 사람 입력
m = int(input())  # 부모 자식간의 관계의 수 입력(간선의 수)
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())  # 부모 번호 : x, x의 자식 번호 : y
    adj[x].append(y)
    adj[y].append(x)

v = [0] * (n + 1)  # visted 배열 만들기
result = dfs(p1, p2, 0)
print(result)


# def dfs(s, e, cnt):
#     v[s] = 1  # 현재 노드를 방문 처리
#     if s == e:  # 목적지에 도착하면 촌수 반환
#         return cnt
#
#     for i in adj[s]:
#         if v[i] == 0:  # 방문하지 않은 노드에 대해 탐색
#             result = dfs(i, e, cnt + 1)
#             if result != -1:  # 경로를 찾았다면 결과 반환
#                 return result
#
#     return -1  # 경로를 찾지 못하면 -1 반환
#
#
# n = int(input())  # 전체 사람의 수 입력
# p1, p2 = map(int, input().split())  # 촌수를 계산할 두 사람 입력
# m = int(input())  # 부모 자식 간의 관계 수 입력
# adj = [[] for _ in range(n+1)]  # 인접 리스트 초기화
#
# for _ in range(m):
#     x, y = map(int, input().split())  # 부모-자식 관계 입력
#     adj[x].append(y)
#     adj[y].append(x)
#
# v = [0] * (n + 1)  # 방문 배열 초기화
# result = dfs(p1, p2, 0)  # DFS 시작, 초기 촌수는 0
# print(result)
#

