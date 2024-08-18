import sys
sys.stdin = open('input.txt')
"""
8
14
9
"""
def backtrack(x, current_sum):
    global min_sum

    if current_sum >= min_sum:              # 현재까지 합이 최솟값 이상이면
        return                              # 더 깊이 탐색할 필요 없음

    if x == N:                              # 모든 행에 대해 확인 했다면 최솟값과 비교 후 반환
        if min_sum > current_sum:
            min_sum = current_sum
        return

    for y in range(N):
        if visited_col[y] == 0:             # 해당 열 방문한 적 없으면
            visited_col[y] = 1              # 방문 체크하고
            backtrack(x + 1, current_sum + data[x][y])
            visited_col[y] = 0              # 리턴 시 방문 체크 해제

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 100   # 최소 합
    visited_col = [0] * N   # 열 방문체크 리스트

    # for j in range(N):
    backtrack(x=0, current_sum=0)

    print(f'#{tc}', min_sum)
