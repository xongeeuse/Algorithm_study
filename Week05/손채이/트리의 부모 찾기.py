'''
트리의 루트 1
'''

from collections import deque

def bfs(start):
    # bfs 탐색을 위해 덱 생성하고 start 넣음
    deq = deque([start])

    # deq 반복
    while deq:
        # 덱에서 왼쪽 원소 꺼냄 1
        top = deq.popleft()

        # graph[top]과 연결된 노드 탐색
        # ex) graph[1]에 있는 노드
        for w in graph[top]:
            # 아직 방문한 적이 없으면 (부모 원소가 입력이 안된 경우)
            if visited[w] == 0:
                # visited[w]에 top(부모) 값 할당
                visited[w] = top
                # 덱에 노드를 추가하고 while문으로 계속 탐색
                deq.append(w)

T = int(input())        # 노드의 개수

graph = [[] for _ in range(T + 1)]          # 트리 연결 상태 저장할 그래프

# 트리의 연결 상태를 graph에 저장
# 트리에는 노드 - 1개의 간선이 있어서 T - 1만큼 반복
for _ in range(T - 1):
    p, c = map(int, input().split())    # p : 부모 / c : 자식
    # 양방향 그래프 저장
    graph[p].append(c)
    graph[c].append(p)

visited = [0] * (T + 1)

bfs(1)      # 루트가 1이니까 1부터 탐색 시작

for i in range(2, T + 1):
    print(visited[i])