import sys
sys.setrecursionlimit(10**5)

def my_dfs(node):
    for i in adjL[node]:
        if parent[i] == 0:
            parent[i] = node # 리스트는 함수 안에서 원본이 바뀐다. so 굳이 return X
            my_dfs(i)

N = int(input()) # 노드의 개수
adjL = [[] for _ in range(N+1)] # 인접 리스트 생성
parent = [0] * (N+1) # 부모 정보를 담을 리스트
root = 1
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    adjL[node1].append(node2)
    adjL[node2].append(node1)

my_dfs(root)
ans = parent[2:]
for parent_node in ans:
    print(parent_node)