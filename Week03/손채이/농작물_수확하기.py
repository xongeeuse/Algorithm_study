T = int(input())

for t in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    # 시작 (0, N // 2) / 끝 (N - 1, N //2)
    start = N // 2
    end = N // 2
    result = 0

    for i in range(len(farm)):
        for j in range(start, end + 1):
            result += farm[i][j]

        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'#{t}', result)

    # [N // 2]
    # print(result)
    # # i = 0
    # print(farm[0][2])
    #
    # # i = 1
    # print(farm[1][1], end=' ')
    # print(farm[1][2], end=' ')
    # print(farm[1][3])
    #
    # # i = N - 1 - i
    # print(farm[N - 1 - 0][2])
    #
    # # j 자리엔 N // 2
    # print(farm[N - 1 - 1][1], end=' ')
    # print(farm[N - 1 - 1][2], end=' ')
    # print(farm[N - 1 - 1][3], end=' ')
