import sys
from collections import deque

# BFS
def bfs(current, target):
    # 현재 위치(current)에서 시작, 거리는 0으로 시작
    deq = deque([(current, 0)])
    visited[current] = 1  # 현재 노드 방문했음

    while deq:
        node, dist = deq.popleft()  # 큐에서 가장 앞에 있는 노드와 거리

        if node == target:  # 목표 노드에 도착하면
            return dist  # 현재까지의 거리를 반환

        # 현재 노드와 연결된 노드들을 확인
        for w in graph[node]:
            if visited[w] == 0:  # 아직 방문하지 않은 노드라면
                visited[w] = 1  # 방문 표시를 하고
                deq.append((w, dist + 1))  # 큐에 해당 노드를 추가하며 거리를 1 증가

    return -1  # 목표 노드에 도달하지 못하면 -1을 반환 (연결되지 않은 경우)


N = int(sys.stdin.readline())  # 전체 사람의 수 (노드의 수)를 입력
n1, n2 = map(int, sys.stdin.readline().split())  # 계산할 사람을 입력
e = int(sys.stdin.readline())  # 간선의 수 입력

# 그래프와 방문 여부 리스트
graph = [[] for _ in range(N + 1)]  # 각 노드에 연결된 노드들의 리스트를 저장할 빈 그래프
visited = [0 for _ in range(N + 1)]  # 각 노드가 방문되었는지 여부를 저장할 리스트 (0이면 미방문, 1이면 방문)

# 관계(간선) 정보를 입력받아 그래프를 구성
for _ in range(e):
    p, c = map(int, sys.stdin.readline().split())  # 부모와 자식 노드를 입력
    graph[p].append(c)  # 부모-자식 관계이므로 양방향으로 연결을 추가
    graph[c].append(p)

# 촌수 계산 결과를 출력
print(bfs(n1, n2))
