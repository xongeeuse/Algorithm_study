import sys
sys.stdin = open('input.txt')
'''
1 ~ v1 ~ v2 ~ N
1 ~ v2 ~ v1 ~ N
중 최단경로가 정답
경로가 없다면 -1 출력!
'''
import heapq

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue

        for next, cost in adjL[now]:
            next_dist = dist + cost
            if next_dist >= distance[next]:
                continue

            distance[next] = next_dist
            heapq.heappush(pq, (next_dist, next))

    return distance[end]

N, E = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
INF = int(1e9)
# distance = [INF] * (N + 1)
for _ in range(E):
    a, b, c = map(int, input().split())
    adjL[a].append((b, c))
    adjL[b].append((a, c))

v1, v2 = map(int, input().split())

v1_to_v2 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
v2_to_v1 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

result = min(v1_to_v2, v2_to_v1)

if result >= INF:
    print(-1)
else: print(result)
