import sys
sys.stdin = open('input.txt')

# dijkstra ver.

import heapq

def dijkstra(N):
    pq = []
    # (해당 노드까지 최단 거리, 좌표)
    # heapq에 리스트로 저장할 때는 맨 앞의 데이터를 기준으로 정렬
    heapq.heappush(pq, (0, N))
    distance[N] = 0

    while pq:
        # 가장 최단 거리 좌표에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 처리된 좌표라면? (=distance 리스트에 거리 기록됨) 넘어가고!
        if distance[now] < dist:
            continue

        # 현재 좌표에서 이동할 수 있는 다른 좌표 확인
        for time, next in [(1, now - 1), (1, now + 1), (0, now * 2)]:

            # 지금까지 누적된 최단 거리 + 다음 좌표까지 드는 비용 계산
            next_time = dist + time
            if next < 0 or next > 100000:
                continue

            # 다음 좌표를 가는데 더 많은 비용이 든다면! 넘어가고!
            if next_time >= distance[next]:
                continue

            distance[next] = next_time
            heapq.heappush(pq, (next_time, next))



N, K = map(int, input().split())
INF = int(1e9)
distance = [INF] * 100001       # distance 초기값 INF로 설정

dijkstra(N)
print(distance[K])










# DFS ver.
# 런타임 에러 (RecursionError) => 시간초과..

# import sys
# sys.setrecursionlimit(100000)
#
# def hide_and_seek(depth, now):      # depth: 소요 시간, now: 수빈 현 위치
#     global result
#
#     if now == K:                # 현 위치가 동생 위치와 같으면
#         if result > depth:      # 소요 시간 비교해서 최솟값 갱신
#             result = depth
#         return
#
#     if depth >= result:         # 소요시간이 이미 기존 최솟값을 넘어섰다면 중단
#         return
#
#     # 순간 이동은 시간 소요 없어서 time 변수 추가로 설정
#     for next, time in [[now - 1, 1], [now + 1, 1], [now * 2, 0]]:
#         # 범위를 초과하거나 이미 방문한 위치라면 패스
#         if next < 0 or next > 100000 or visited[next]:
#             continue
#         visited[next] = 1                   # 방문 체크하고
#         hide_and_seek(depth + time, next)   # 다음 탐색 진행 (dfs)
#         visited[next] = 0                   # 돌아와서 방문 체크 해제
#
#
# N, K = map(int, input().split())
# visited = [0 for _ in range(100001)]
# visited[N] = 1
#
# result = float('inf')
# hide_and_seek(0, N)
# print(result)