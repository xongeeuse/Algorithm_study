T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    # 행 기준으로 확인
    for i in range(N):
        row_count = 0
        for j in range(N):
            if arr[i][j] == 1:
                row_count += 1
            else: # arr[i][j]이 0일 때
                if row_count == K:
                    count += 1
                row_count = 0
        if row_count == K:  # 끝 났을 시 마지막 셀까지 검사
            count += 1

    # 열 기준으로 확인
    for j in range(N):
        col_count = 0
        for i in range(N):
            if arr[i][j] == 1:
                col_count += 1
            else: # arr[j][i]가 0일 때
                if col_count == K:
                    count += 1
                col_count = 0
        if col_count == K:  # 끝 났을 시 마지막 셀까지 검사
            count += 1

    print(f'#{tc} {count}')