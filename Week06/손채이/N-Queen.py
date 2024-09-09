def check(row, col):
    for i in range(row):  # 열 확인
        if visited[i][col] == 1:
            return False

    i, j = row - 1, col - 1  # 주대각선 확인
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1  # 부대각선 확인
    while i >= 0 and j < N:
        if visited[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        if check(row, col):
            visited[row][col] = 1
            dfs(row + 1)
            visited[row][col] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    dfs(0)

    print(f"#{tc} {cnt}")
