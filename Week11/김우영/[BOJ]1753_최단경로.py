# 수정필요 - 틀림

import sys
input = sys.stdin.readline

INF = int(1e9)
# 정점의 개수 V, 간선의 개수 E 입력
V, E = map(int, input().split())
# 시작 정점 K 입력
K = int(input())
# 각 정점에 연결된 간선 정보를 담는 리스트
graph = [[] for _ in range(V+1)]
# 방문한 적이 있는지 체크하는 리스트
visited = [False] * (V + 1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (V + 1)

# 모든 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    # u에서 v로 가는 가중치 w인 간선
    graph[u].append((v, w))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, V + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘 구현
def dijkstra(K):
    # 시작 노드에 대해서 초기화
    distance[K] = 0
    visited[K] = True
    for v, w in graph[K]:
        distance[v] = w

    # 시작 노드를 제외한 전체 V-1개의 노드에 대해 반복
    for _ in range(V - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for v, w in graph[now]:
            cost = distance[now] + w
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[v]:
                distance[v] = cost

# 다익스트라 알고리즘을 수행
dijkstra(K)

# 모든 정점으로의 최단 경로 출력
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])