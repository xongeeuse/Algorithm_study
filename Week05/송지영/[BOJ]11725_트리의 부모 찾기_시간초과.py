def make_tree(visited, node):
    for v in adjL[node]:
        if visited[v]:
            continue
        tree[node].append(v)
        visited[v] = 1
        make_tree(visited, v)

N = int(input())        # N 노드의 개수
adjL = [[] for _ in range(N + 1)]
tree = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)
# print(adjL)

visited[1] = 1
make_tree(visited, node = 1)

# print(tree)

x = 2
while x <= N:
    for i in range(1, N + 1):
        if x in tree[i]:
            print(i)
            x += 1