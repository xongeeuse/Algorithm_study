T = int(input())

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            cnt = arr[i][j]

            for x in range(len(dxy)):
                ni = i + dxy[x][0]
                nj = j + dxy[x][1]

                if 0 <= ni < len(arr) and 0 <= nj < len(arr[i]):
                    cnt += arr[ni][nj]
            if max_value < cnt:
                max_value = cnt
    print(f'#{t}', max_value)