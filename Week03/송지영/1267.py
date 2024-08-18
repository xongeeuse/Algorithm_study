import sys
sys.stdin = open('input.txt')

# 이거 bfs 아님ㅎ
def bfs(priorityL):
    result = []
    visited = [0] * (V + 1)
    while len(result) < V:              # 모든 작업 완료할 때까지
        for i in range(1, V+1):         # 정점 순서대로 확인할거야
            for x in priorityL[i]:      # 선행순위 리스트에서
                if visited[x] == 0:     # 선행순위 작업이 완료되지 않았다면
                    break               # 중단
            else:
                if visited[i] == 0:     # 선행순위 작업 모두 완료했고, 아직 현 작업 완료하지 않았다면
                    visited[i] = 1      # 완료 체크하고
                    result.append(i)    # 결과에 넣기
    return result


T = 10
for tc in range(1, T + 1):
    V, E = map(int, input().split())        # V 정점의 개수, E 간선 개수
    data = list(map(int, input().split()))
    priorityL = [[] for _ in range(V + 1)]  # 인접리스트 반대로 받아줄 예정
    for i in range(E):
        v1, v2 = data[i * 2], data[i * 2 + 1]
        priorityL[v2].append(v1)
    print(f'#{tc}', *bfs(priorityL))