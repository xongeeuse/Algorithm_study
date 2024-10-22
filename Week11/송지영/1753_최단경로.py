# 시간초과 but,
# pypy로 내면 통과

import heapq

def dijkstra(start):
    pq = []
    # (해당 노드까지 최단거리, 노드 번호)
    # heapq에 리스트로 저장할 때는 맨 앞의 데이터 기준 정렬되니까 거리부터 넣음
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재까지 최단 거리 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 처리된 노드라면? 넘어가기
        if distance[now] < dist:
            continue

        for next, cost in graph[now]:

            # 지금까지 누적된 최단 거리 + 다음 노느까지 드는 비용 계산
            next_cost = dist + cost

            # 다음 노드를 가는데 현재 기록된 최단거리보다 더 많은 비용이 든다면 넘어가고!
            if next_cost >= distance[next]:
                continue

            distance[next] = next_cost
            heapq.heappush(pq, (next_cost, next))



V, E = map(int, input().split())        # V: 정점 개수, E: 간선 개수
K = int(input())                        # K: 시작 정점의 번호
graph = [[] for _ in range(V + 1)]    # 인접 리스트 생성: graph[v1] = (v2, weight) 형태

INF = int(1e6)
distance = [INF] * (V + 1)

for _ in range(E):
    v1, v2, weight = map(int, input().split())
    graph[v1].append((v2, weight))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
