from collections import deque

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
N = len(maps)
M = len(maps[0])
visited = [[0] * M for _ in range(N)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# BFS 풀이
def my_bfs(si, sj):
    queue.append([si,sj])
    visited[si][sj] = 1

    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y]

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= M or maps[nx][ny] == 0 or visited[nx][ny] != 0:
                continue

            queue.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1
    return -1

queue = deque()
print(my_bfs(0, 0))
print()
print(visited)


# # DFS 풀이
# def my_dfs(si, sj, cnt):
#     global min_cnt
#
#     if si == N-1 and sj == M-1:
#         min_cnt = min(min_cnt, cnt)
#         return min_cnt
#
#     for dx, dy in dxy:
#         nx = si + dx
#         ny = sj + dy
#
#         if nx < 0 or ny < 0 or nx >= N or ny >= M or maps[nx][ny] == 0 or visited[nx][ny] == 1:
#             continue
#
#         visited[nx][ny] = 1 # nx, ny를 방문했다고 치고
#         my_dfs(nx, ny, cnt + 1) # cnt를 올려서 DFS로 보낸다
#         visited[nx][ny] = 0 # 다시 False로 바꿔줘야댐. 다음 DFS 루트가 동일하게 탐색되게 하기위해 되돌려줘야댐
#
# min_cnt = float('inf')
# visited[0][0] = 1
# my_dfs(0, 0, 1)
# print(min_cnt)