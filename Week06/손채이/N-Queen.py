# 퀸을 놓을 수 있는지 확인하고, 가능한 위치에 퀸을 배치하는 함수
def place_queen(r, n):
    global cnt  # 가능한 배치 경우의 수를 기록할 전역 변수

    # 종료 조건: 남은 퀸이 없고, 모든 행에 퀸을 배치했으면
    if n == 0 and r == N:
        cnt += 1  # 가능한 배치 방법을 하나 찾았으므로 cnt 증가
        return

    # 각 열에 퀸을 놓을 수 있는지 확인하기 위해 반복문
    for c in range(N):  # 첫 번째 열부터 N번째 열까지 반복
        can_place = True  # 해당 위치에 퀸을 놓을 수 있는지 여부

        # 현재 자리 위의 모든 행을 검사 (같은 열에 퀸이 있는지 확인)
        for i in range(r):
            if board[i][c] == 1:  # 같은 열에 이미 퀸이 있으면
                can_place = False  # 퀸을 놓을 수 없으므로 False
                break

        # 현재 자리에서 좌상 대각선에 퀸이 있는지 검사
        for i in range(1, r + 1):
            if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == 1:  # 좌상 대각선에 퀸이 있는지 확인
                can_place = False  # 퀸이 있으면 놓을 수 없음
                break

            # 현재 자리에서 우상 대각선에 퀸이 있는지 검사
            if r - i >= 0 and c + i < N and board[r - i][c + i] == 1:  # 우상 대각선에 퀸이 있는지 확인
                can_place = False  # 퀸이 있으면 놓을 수 없음
                break

        # 위의 검사에서 문제가 없으면 (즉, 퀸을 놓을 수 있으면)
        if can_place:
            board[r][c] = 1  # 현재 위치에 퀸을 놓음
            place_queen(r + 1, n - 1)  # 다음 행으로 넘어가서 퀸을 놓기 위한 재귀 호출
            board[r][c] = 0  # 다른 경우의 수를 위해 퀸을 원래 위치에서 제거 (백트래킹)

# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스에 대해 처리
for tc in range(1, T + 1):
    N = int(input())  # 체스판의 크기 N*N
    cnt = 0  # 가능한 배치 경우의 수를 저장할 변수
    board = [[0] * N for _ in range(N)]  # N*N 크기의 체스판 (0은 빈칸, 1은 퀸이 있는 자리)
    place_queen(0, N)  # 0번째 행부터 퀸을 배치하는 재귀 함수 호출 (r = 0, n = N)

    # 테스트 케이스 번호와 함께 결과 출력
    print(f'#{tc} {cnt}')
