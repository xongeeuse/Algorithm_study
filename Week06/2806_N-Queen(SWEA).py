def checker(i):
    global ans

    if i == N:
        ans += 1
        return

    for j in range(N): # 모든열을 볼건데
        if v1[j] == 0 and v2[i+j] == 0 and v3[i-j] == 0:
            v1[j] = v2[i+j] = v3[i-j] = 1 # 방문 체크
            checker(i+1)
            v1[j] = v2[i + j] = v3[i - j] = 0 # 방문 풀고
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0] * (N) for _ in range(N)]
    v1 = [0] * N # 열을 확인할 리스트
    v2 = [0] * (2 * N - 1) # 우측 대각선 방향을 확인할 리스트 - 규칙:  i+j가 일정
    v3 = [0] * (2 * N - 1) # 좌측 대각선 방향을 확인할 리스트 - 규칙: i-j가 일정
    ans = 0
    checker(0)
    print(f'#{tc} {ans}')