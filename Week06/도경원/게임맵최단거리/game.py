def dfs(si, sj, length):
    global min_length

    if si == 4 and sj == 4:
        min_length = min(min_length, length)
        return

    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < 5 and 0 <= nj < 5 and maps[ni][nj] == 1 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, length + 1)
            visited[ni][nj] = 0


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
visited =[[0] * 5 for _ in range(5)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

min_length = float('inf')  # 최단거리

dfs(0, 0, 1)

print(min_length)


