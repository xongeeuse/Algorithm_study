import sys
sys.stdin = open('1979_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # 리팩토링 필수!
    # count 변수를 행, 열 하나씩 만들어서 반복문 하나만 쓰기
    # 가로
    # N만큼 반복
    for i in range(N):
        cnt = 0     # count를 위한 변수
        for j in range(N):
            if arr[i][j] == 1:  # arr[i]][j]가 1일 경우 + 1
                cnt += 1
            else:               # 1이 아닐 경우
                if cnt == M:        # count가 M과 같은 지 확인
                    result += 1     # result에 +1
                cnt = 0             # 다시 count를 하기 위해 0으로 만듦
        if cnt == M:            # 내부 for문이 종료된 후 count가 M과 같은 지 확인하고 result = + 1 함
            result += 1
            # for문이 끝났을 때 마지막 행이 1이라면 result에 더하는 부분

    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == M:
                    result += 1
                cnt = 0
        if cnt == M:
            result += 1

    print(f'#{t} {result}')
