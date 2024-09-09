import sys
sys.stdin = open('input.txt')
'''
행 순서대로 퀸 위치 정하고 비지티드에 기록
이전 행에서 선택된 적 있는지 체크 함수로 확인
선택된 적 있으면 다음 인덱스로 넘어가기
선택된 적 없으면 다음 행으로 넘어가서 동일 과정 반복
'''


def check(row):
    for previous_row in range(row):
        # 이전 행들에서 선택된 적 있는 열인지 확인
        if visited[row] == visited[previous_row]:
            return False

        # 대각선 방향 확인 (절대값이 같다 = 대각선 방향이다)
        if abs(visited[row] - visited[previous_row]) == abs(row - previous_row):
            return False

    return True


def N_Queen(row):
    global result

    if row == N:
        result += 1
        return

    for col in range(N):
        visited[row] = col
        if not check(row):
            continue

        N_Queen(row + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * (N + 1)
    result = 0

    N_Queen(row = 0)

    print(f'#{tc}', result)