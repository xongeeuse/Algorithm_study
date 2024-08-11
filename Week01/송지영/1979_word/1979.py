import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        cnt_r = 0
        cnt_c = 0

        for j in range(N):
            if data[i][j] == 1:
                cnt_r += 1
            else:
                if cnt_r == K:
                    result += 1
                cnt_r = 0

            if data[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    result += 1
                cnt_c = 0

        if cnt_c == K:
            result += 1
        if cnt_r == K:
            result += 1


    print(f'#{tc}',result)