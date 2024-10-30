# 14503 로봇청소기
# 입력 처리
n, m = map(int, input().split())  # 세로 크기 n, 가로 크기 m
r, c, d = map(int, input().split())  # 로봇 청소기의 초기 위치 (r, c)와 방향 d
room = [list(map(int, input().split())) for _ in range(n)]  # 방의 정보 (0: 빈 칸, 1: 벽)

# 북, 동, 남, 서 방향 (반시계방향 회전 기준)
dr = [-1, 0, 1, 0]  # 북, 동, 남, 서에 해당하는 행의 변화량
dc = [0, 1, 0, -1]  # 북, 동, 남, 서에 해당하는 열의 변화량

# 청소 여부를 기록하는 배열
cleaned = [[False] * m for _ in range(n)]

# 현재 위치 청소
cleaned[r][c] = True
cleaned_count = 1


def turn_left(direction):
    return (direction + 3) % 4  # 왼쪽으로 회전 (반시계 방향)


# 시뮬레이션 시작
while True:
    found_new_place = False

    # 왼쪽 방향부터 탐색
    for _ in range(4):
        d = turn_left(d)  # 왼쪽으로 회전
        nr, nc = r + dr[d], c + dc[d]  # 새로운 위치

        if 0 <= nr < n and 0 <= nc < m and not cleaned[nr][nc] and room[nr][nc] == 0:
            # 아직 청소하지 않은 빈 공간이면 이동
            cleaned[nr][nc] = True
            r, c = nr, nc
            cleaned_count += 1
            found_new_place = True
            break

    # 4방향 모두 이미 청소되었거나 벽인 경우
    if not found_new_place:
        # 현재 방향에서 뒤로 이동
        back_direction = (d + 2) % 4  # 뒤쪽 방향
        br, bc = r + dr[back_direction], c + dc[back_direction]

        if room[br][bc] == 1:
            # 뒤쪽이 벽이면 작동 중지
            break
        else:
            # 뒤쪽이 벽이 아니면 후진
            r, c = br, bc

# 청소한 칸의 개수 출력
print(cleaned_count)
