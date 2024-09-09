from collections import deque

'''
인덱스 주의
N, M 도착점이지만 인덱스는 -1씩 해줘야 함
'''

def solution(maps):
    N, M = len(maps), len(maps[0])  # N * M 배열
    answer = -1                     # 도착 못 할 시 -1 출력
    q = deque()
    q.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1               # 시작점 1로 설정

    while q:
        i, j = q.popleft()
        if i == N - 1 and j == M - 1:                           # 도착지점이면
            answer = visited[i][j]                              # answer 업뎃하고 종료
            break
        for di, dj in [[0, 1], [1, 0], [0, -1],[-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 > ni or ni >= N or 0 > nj or nj >= M:          # 범위 벗어나면 패스
                continue
            if not maps[ni][nj] or visited[ni][nj]:             # 벽이거나 이미 방문했다면 패스
                continue
            visited[ni][nj] = visited[i][j] + 1
            q.append((ni, nj))

    return answer

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
maps2 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]

print(solution(maps))       # 11
print(solution(maps2))      # -1

